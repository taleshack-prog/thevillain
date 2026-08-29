"""
Decifracao sob pressao: iniciar tentativa, consumir pistas e submeter (FR-006/007/008).
Regra de ouro: o gabarito so e revelado apos a submissao final.
"""
from __future__ import annotations

import datetime as dt
import json
import uuid

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import security
from app.core.config import get_settings
from app.core.redis import get_redis
from app.db.models import Challenge, Clue, RiddleAttempt, RiddleTemplate, Result
from app.engine.constants import CLUE_PENALTIES, TOTAL_TIME_SECONDS, ANTI_CHEAT_MIN_SECONDS
from app.engine.options import build_sealed_options, is_correct_submission
from app.engine.scoring import calculate_final_score

_settings = get_settings()
_SESSION_TTL = int(TOTAL_TIME_SECONDS) + 120  # tempo total + folga de rede


def _skey(attempt_id: uuid.UUID) -> str:
    return f"attempt:{attempt_id}"


async def start_attempt(
    db: AsyncSession, challenge: Challenge, riddle: RiddleTemplate, solver_user_id: uuid.UUID,
) -> dict:
    """Cria a tentativa, sela as opcoes e retorna o payload publico (sem gabarito)."""
    now = dt.datetime.now(dt.timezone.utc)
    nonce = security.new_nonce()
    attempt = RiddleAttempt(
        challenge_id=challenge.challenge_id,
        solver_user_id=solver_user_id,
        started_at=now,
        session_hmac="",  # preenchido apos termos o attempt_id
    )
    db.add(attempt)
    await db.flush()  # gera attempt_id/created_at sem encerrar a transacao

    distractors = riddle.distractors if isinstance(riddle.distractors, list) else json.loads(riddle.distractors)
    sealed = build_sealed_options(
        _settings.session_hmac_secret, str(attempt.attempt_id), nonce,
        riddle.correct_answer, distractors,
    )
    session_sig = security.sign_session(str(attempt.attempt_id), nonce, attempt.started_at.isoformat())
    attempt.session_hmac = session_sig
    await db.commit()

    # Estado efemero da sessao no Redis (id correto retido no servidor).
    await get_redis().hset(_skey(attempt.attempt_id), mapping={
        "correct_option_id": sealed.correct_option_id,
        "nonce": nonce,
        "difficulty": str(riddle.difficulty_level),
        "riddle_id": str(riddle.riddle_id),
    })
    await get_redis().expire(_skey(attempt.attempt_id), _SESSION_TTL)

    return {
        "attempt_id": str(attempt.attempt_id),
        "riddle_id": str(riddle.riddle_id),
        "difficulty_level": riddle.difficulty_level,
        "scenario_context": riddle.scenario_context,
        "riddle_text": riddle.riddle_text,
        "options": sealed.options,          # apenas {option_id, text}
        "total_time_seconds": TOTAL_TIME_SECONDS,
        "session_signature": session_sig,
        "nonce": nonce,
        "started_at": attempt.started_at.isoformat(),
    }


async def get_attempt(db: AsyncSession, attempt_id: uuid.UUID) -> RiddleAttempt | None:
    return (await db.execute(
        select(RiddleAttempt).where(RiddleAttempt.attempt_id == attempt_id)
    )).scalars().first()


async def consume_clue(db: AsyncSession, attempt: RiddleAttempt, tier: int) -> dict:
    """Entrega uma pista e registra o uso (penalidade aplicada na pontuacao)."""
    if tier not in CLUE_PENALTIES:
        raise ValueError("Tier de pista invalido (1..3).")
    if attempt.finished_at is not None:
        raise ValueError("Tentativa ja finalizada.")

    riddle_id = uuid.UUID((await get_redis().hget(_skey(attempt.attempt_id), "riddle_id")) or str(uuid.UUID(int=0)))
    clue = (await db.execute(
        select(Clue).where(Clue.riddle_id == riddle_id, Clue.tier_level == tier)
    )).scalars().first()
    if clue is None:
        raise LookupError("Pista nao encontrada para este enigma.")

    used = list(attempt.clues_used or [])
    if tier not in used:
        used.append(tier)
        await db.execute(
            update(RiddleAttempt)
            .where(RiddleAttempt.attempt_id == attempt.attempt_id,
                   RiddleAttempt.created_at == attempt.created_at)
            .values(clues_used=sorted(used))
        )
        await db.commit()
    return {"tier": tier, "clue_text": clue.clue_text,
            "score_penalty_percent": float(clue.score_penalty_percent)}


async def submit(
    db: AsyncSession, attempt: RiddleAttempt, chosen_option_id: str,
) -> dict:
    """Apura o veredito com base no relogio do servidor e revela o gabarito."""
    if attempt.finished_at is not None:
        raise ValueError("Tentativa ja submetida.")

    state = await get_redis().hgetall(_skey(attempt.attempt_id))
    if not state:
        raise TimeoutError("Sessao expirada ou inexistente.")

    correct_option_id = state["correct_option_id"]
    difficulty = int(state["difficulty"])
    riddle_id = uuid.UUID(state["riddle_id"])

    now = dt.datetime.now(dt.timezone.utc)
    time_spent = (now - attempt.started_at).total_seconds()
    quarantine = security.is_temporal_anomaly(time_spent, ANTI_CHEAT_MIN_SECONDS)

    is_correct = is_correct_submission(chosen_option_id, correct_option_id)
    clue_tiers = list(attempt.clues_used or [])

    if is_correct and not quarantine:
        score = calculate_final_score(difficulty, time_spent, clue_tiers_used=clue_tiers)
    else:
        score = {"base_points": difficulty * 1000, "time_bonus": 0.0, "penalties": 0.0,
                 "genius_multiplier": 1.0, "is_genius": False, "final_score": 0}

    await db.execute(
        update(RiddleAttempt)
        .where(RiddleAttempt.attempt_id == attempt.attempt_id,
               RiddleAttempt.created_at == attempt.created_at)
        .values(finished_at=now, time_spent_seconds=round(time_spent, 2), is_correct=is_correct)
    )
    db.add(Result(
        attempt_id=attempt.attempt_id, attempt_created_at=attempt.created_at,
        base_points=score["base_points"], time_bonus=score["time_bonus"],
        penalties=score["penalties"], genius_multiplier=score["genius_multiplier"],
        final_score=score["final_score"],
    ))
    await db.commit()
    await get_redis().delete(_skey(attempt.attempt_id))  # sessao encerrada

    # Gabarito e trilha revelados AGORA (pos-submissao).
    riddle = (await db.execute(
        select(RiddleTemplate).where(RiddleTemplate.riddle_id == riddle_id)
    )).scalars().first()

    return {
        "is_correct": is_correct,
        "quarantined": quarantine,
        "time_spent_seconds": round(time_spent, 2),
        "score": score,
        "correct_answer": riddle.correct_answer if riddle else None,
        "deduction_steps": (riddle.deduction_steps if riddle else []),
        "solver_user_id": str(attempt.solver_user_id),
    }
