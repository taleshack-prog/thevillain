"""Estagio 5 — Batch Ingestion & Cache (GDD 3.6).

Grava o enigma aprovado em riddle_templates + clues e pre-aquece o payload
PUBLICO (sem gabarito) no Redis para entrega instantanea.
"""
from __future__ import annotations

import json
import uuid
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.redis import get_redis
from app.db.models import Clue, RiddleTemplate
from app.engine.constants import CLUE_PENALTIES

_CACHE_TTL = 24 * 3600  # pool rotativo diario (FR-012)


def _public_payload(riddle: RiddleTemplate) -> dict[str, Any]:
    """Projecao publica — NUNCA inclui correct_answer nem symbolic_hash."""
    return {
        "riddle_id": str(riddle.riddle_id),
        "difficulty_level": riddle.difficulty_level,
        "scenario_context": riddle.scenario_context,
        "riddle_text": riddle.riddle_text,
    }


async def ingest_riddle(
    db: AsyncSession, theme_id: uuid.UUID, difficulty: int,
    payload: dict[str, Any], integrity_hash: str,
) -> RiddleTemplate:
    """Persiste o enigma homologado e suas pistas; pre-aquece cache Redis."""
    riddle = RiddleTemplate(
        theme_id=theme_id,
        difficulty_level=difficulty,
        scenario_context=payload["scenario"],
        riddle_text=payload["riddle"],
        correct_answer=payload["correct_answer"],
        distractors=payload["distractors"],
        deduction_steps=payload["deduction_steps"],
        symbolic_hash=integrity_hash,
    )
    db.add(riddle)
    await db.flush()

    for clue in payload["clues"]:
        db.add(Clue(
            riddle_id=riddle.riddle_id,
            tier_level=clue["tier"],
            clue_text=clue["text"],
            score_penalty_percent=CLUE_PENALTIES[clue["tier"]],
        ))
    await db.commit()
    await db.refresh(riddle)

    # Pre-aquece a projecao publica (sem gabarito) no Redis.
    try:
        await get_redis().set(
            f"riddle:public:{riddle.riddle_id}",
            json.dumps(_public_payload(riddle), ensure_ascii=False),
            ex=_CACHE_TTL,
        )
    except Exception:
        # Cache e otimizacao; falha aqui nao impede a ingestao.
        pass
    return riddle
