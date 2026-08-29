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
from app.ai.deps import get_provider
from app.ai.pipeline import RiddleGenerationError, generate_and_ingest
from app.ai.provider import LLMProvider
from sqlalchemy import select

router = APIRouter(prefix="/challenges", tags=["desafio"])


@router.post("", response_model=ChallengeCreateResponse, status_code=201)
async def create_challenge(
    req: ChallengeCreateRequest,
    db: AsyncSession = Depends(get_db_session),
    provider: LLMProvider = Depends(get_provider),
) -> ChallengeCreateResponse:
    try:
        theme_id = uuid.UUID(req.theme_id)
        creator_id = uuid.UUID(req.creator_user_id)
    except ValueError as exc:
        raise HTTPException(422, f"Identificador invalido: {exc}") from exc

    forged = None
    if req.generate:
        # Forja um enigma novo via pipeline de IA (FR-002) e vincula ao desafio.
        theme = (await db.execute(
            select(RiddleTheme).where(RiddleTheme.theme_id == theme_id)
        )).scalars().first()
        if theme is None:
            raise HTTPException(404, "Tema nao encontrado.")
        try:
            forged, _report = await generate_and_ingest(
                db, provider, theme_id=theme_id, theme_title=theme.title,
                difficulty=req.difficulty, category=req.category,
            )
        except RiddleGenerationError as exc:
            raise HTTPException(422, str(exc)) from exc

    created = await challenge_service.create_challenge(
        db, creator_id, theme_id, req.difficulty, req.provocation, riddle=forged,
    )
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
