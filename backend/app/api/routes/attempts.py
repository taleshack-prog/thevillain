"""Decifracao sob pressao e revanche (FR-006/007/008/009)."""
import uuid

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas import (
    AttemptStartRequest, AttemptStartResponse, ClueOut, SubmitRequest, SubmitResponse,
    ChallengeCreateResponse,
)
from app.db.base import get_db_session
from app.services import attempt_service, challenge_service, ranking_service

router = APIRouter(tags=["decifracao"])


@router.post("/challenges/{share_token}/attempts", response_model=AttemptStartResponse, status_code=201)
async def start_attempt(
    share_token: str, req: AttemptStartRequest, db: AsyncSession = Depends(get_db_session),
) -> AttemptStartResponse:
    found = await challenge_service.get_by_share_token(db, share_token)
    if found is None:
        raise HTTPException(404, "Convite nao encontrado ou expirado.")
    challenge, riddle = found
    try:
        payload = await attempt_service.start_attempt(db, challenge, riddle, uuid.UUID(req.solver_user_id))
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
    return AttemptStartResponse(**payload)


@router.post("/attempts/{attempt_id}/clues/{tier}", response_model=ClueOut)
async def consume_clue(
    attempt_id: uuid.UUID, tier: int = Path(ge=1, le=3), db: AsyncSession = Depends(get_db_session),
) -> ClueOut:
    attempt = await attempt_service.get_attempt(db, attempt_id)
    if attempt is None:
        raise HTTPException(404, "Tentativa nao encontrada.")
    try:
        data = await attempt_service.consume_clue(db, attempt, tier)
    except ValueError as exc:
        raise HTTPException(409, str(exc)) from exc
    except LookupError as exc:
        raise HTTPException(404, str(exc)) from exc
    return ClueOut(**data)


@router.post("/attempts/{attempt_id}/submit", response_model=SubmitResponse)
async def submit(
    attempt_id: uuid.UUID, req: SubmitRequest, db: AsyncSession = Depends(get_db_session),
) -> SubmitResponse:
    attempt = await attempt_service.get_attempt(db, attempt_id)
    if attempt is None:
        raise HTTPException(404, "Tentativa nao encontrada.")
    try:
        result = await attempt_service.submit(db, attempt, req.chosen_option_id)
    except ValueError as exc:
        raise HTTPException(409, str(exc)) from exc
    except TimeoutError as exc:
        raise HTTPException(410, str(exc)) from exc

    # Atualiza ranking apenas para acertos validos (fora de quarentena).
    if result["is_correct"] and not result["quarantined"]:
        await ranking_service.apply_result(
            db, uuid.UUID(result["solver_user_id"]),
            result["score"]["final_score"], result["score"]["is_genius"],
        )
    return SubmitResponse(
        is_correct=result["is_correct"], quarantined=result["quarantined"],
        time_spent_seconds=result["time_spent_seconds"], score=result["score"],
        correct_answer=result["correct_answer"], deduction_steps=result["deduction_steps"],
    )


@router.post("/attempts/{attempt_id}/rematch", response_model=ChallengeCreateResponse, status_code=201)
async def rematch(attempt_id: uuid.UUID, db: AsyncSession = Depends(get_db_session)) -> ChallengeCreateResponse:
    """Revanche (FR-009): o Heroi vira Vilao e forja um novo desafio no mesmo tema/dificuldade."""
    attempt = await attempt_service.get_attempt(db, attempt_id)
    if attempt is None:
        raise HTTPException(404, "Tentativa nao encontrada.")
    original = await attempt_service.get_attempt(db, attempt_id)
    # Recupera desafio/enigma de origem para replicar tema+dificuldade.
    from app.db.models import Challenge, RiddleTemplate
    from sqlalchemy import select
    ch = (await db.execute(select(Challenge).where(Challenge.challenge_id == original.challenge_id))).scalars().first()
    rid = (await db.execute(select(RiddleTemplate).where(RiddleTemplate.riddle_id == ch.riddle_id))).scalars().first()
    created = await challenge_service.create_challenge(
        db, attempt.solver_user_id, rid.theme_id, rid.difficulty_level,
        provocation="A vinganca e um prato que se serve decifrado.",
    )
    if created is None:
        raise HTTPException(404, "Sem enigma disponivel para revanche.")
    challenge, _ = created
    return ChallengeCreateResponse(
        challenge_id=str(challenge.challenge_id), share_token=challenge.share_token,
        share_path=f"/c/{challenge.share_token}", expires_at=challenge.expires_at.isoformat(),
    )
