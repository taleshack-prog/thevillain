"""Geracao procedural de enigmas via pipeline de IA (FR-002, GDD 3.6)."""
import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.ai.deps import get_provider
from app.ai.pipeline import RiddleGenerationError, generate_and_ingest
from app.ai.provider import LLMProvider
from app.api.schemas import GenerateRiddleRequest, GenerateRiddleResponse
from app.db.base import get_db_session
from app.db.models import RiddleTheme

router = APIRouter(prefix="/riddles", tags=["geracao"])


@router.post("/generate", response_model=GenerateRiddleResponse, status_code=201)
async def generate_riddle(
    req: GenerateRiddleRequest,
    db: AsyncSession = Depends(get_db_session),
    provider: LLMProvider = Depends(get_provider),
) -> GenerateRiddleResponse:
    try:
        theme_id = uuid.UUID(req.theme_id)
    except ValueError as exc:
        raise HTTPException(422, f"theme_id invalido: {exc}") from exc

    theme = (await db.execute(
        select(RiddleTheme).where(RiddleTheme.theme_id == theme_id)
    )).scalars().first()
    if theme is None:
        raise HTTPException(404, "Tema nao encontrado.")

    try:
        riddle, report = await generate_and_ingest(
            db, provider, theme_id=theme_id, theme_title=theme.title,
            difficulty=req.difficulty, category=req.category, seed=req.seed,
        )
    except RiddleGenerationError as exc:
        raise HTTPException(422, str(exc)) from exc

    return GenerateRiddleResponse(
        riddle_id=str(riddle.riddle_id), theme_id=str(theme_id),
        difficulty_level=riddle.difficulty_level,
        provider=report.provider, attempts=report.attempts, approved=report.approved,
    )
