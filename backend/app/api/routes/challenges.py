"""Criacao de desafio e convite compartilhavel (FR-001, FR-005) + ranking (FR-010)."""
import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas import (
    ChallengeCreateRequest, ChallengeCreateResponse, ChallengePublicOut, RankingRow,
)
from app.db.base import get_db_session
from app.db.models import RiddleTheme
from app.services import challenge_service, ranking_service
from sqlalchemy import select

router = APIRouter(prefix="/challenges", tags=["desafio"])


@router.post("", response_model=ChallengeCreateResponse, status_code=201)
async def create_challenge(
    req: ChallengeCreateRequest, db: AsyncSession = Depends(get_db_session),
) -> ChallengeCreateResponse:
    try:
        created = await challenge_service.create_challenge(
            db, uuid.UUID(req.creator_user_id), uuid.UUID(req.theme_id), req.difficulty, req.provocation,
        )
    except ValueError as exc:
        raise HTTPException(422, f"Identificador invalido: {exc}") from exc
    if created is None:
        raise HTTPException(404, "Nenhum enigma homologado para este tema e dificuldade.")
    challenge, _riddle = created
    return ChallengeCreateResponse(
        challenge_id=str(challenge.challenge_id),
        share_token=challenge.share_token,
        share_path=f"/c/{challenge.share_token}",
        expires_at=challenge.expires_at.isoformat(),
    )


@router.get("/{share_token}", response_model=ChallengePublicOut)
async def get_challenge(share_token: str, db: AsyncSession = Depends(get_db_session)) -> ChallengePublicOut:
    found = await challenge_service.get_by_share_token(db, share_token)
    if found is None:
        raise HTTPException(404, "Convite nao encontrado ou expirado.")
    challenge, riddle = found
    theme = (await db.execute(
        select(RiddleTheme).where(RiddleTheme.theme_id == riddle.theme_id)
    )).scalars().first()
    return ChallengePublicOut(
        challenge_id=str(challenge.challenge_id),
        share_token=challenge.share_token,
        theme_title=theme.title if theme else "",
        accent_color=theme.accent_color if theme else "#8B5CF6",
        difficulty_level=riddle.difficulty_level,
        custom_provocation=challenge.custom_provocation,
        expires_at=challenge.expires_at.isoformat(),
    )


@router.get("/{share_token}/ranking", response_model=list[RankingRow])
async def challenge_ranking(share_token: str, db: AsyncSession = Depends(get_db_session)) -> list[RankingRow]:
    # Ranking da coorte semanal corrente (FR-010).
    rows = await ranking_service.get_cohort_ranking(db)
    return [RankingRow(**r) for r in rows]
