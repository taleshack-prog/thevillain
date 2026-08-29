"""Catalogo de temas goticos (FR-001)."""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas import ThemeOut
from app.db.base import get_db_session
from app.services import challenge_service

router = APIRouter(prefix="/themes", tags=["curadoria"])


@router.get("", response_model=list[ThemeOut])
async def list_themes(db: AsyncSession = Depends(get_db_session)) -> list[ThemeOut]:
    themes = await challenge_service.list_themes(db)
    return [
        ThemeOut(
            theme_id=str(t.theme_id), slug=t.slug, title=t.title,
            description=t.description, accent_color=t.accent_color,
            is_philosophical=t.is_philosophical,
        )
        for t in themes
    ]
