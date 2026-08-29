"""Curadoria e convite (FR-001, FR-005). No MVP seleciona um enigma homologado
existente por tema+dificuldade; a geracao procedural via IA chega na Fatia 2."""
from __future__ import annotations

import datetime as dt
import secrets
import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Challenge, RiddleTemplate, RiddleTheme

CHALLENGE_TTL_HOURS = 72


async def list_themes(db: AsyncSession) -> list[RiddleTheme]:
    rows = await db.execute(select(RiddleTheme).order_by(RiddleTheme.title))
    return list(rows.scalars().all())


async def pick_riddle(db: AsyncSession, theme_id: uuid.UUID, difficulty: int) -> RiddleTemplate | None:
    stmt = (
        select(RiddleTemplate)
        .where(
            RiddleTemplate.theme_id == theme_id,
            RiddleTemplate.difficulty_level == difficulty,
            RiddleTemplate.is_active.is_(True),
        )
        .order_by(RiddleTemplate.created_at.desc())
        .limit(1)
    )
    return (await db.execute(stmt)).scalars().first()


async def create_challenge(
    db: AsyncSession,
    creator_user_id: uuid.UUID,
    theme_id: uuid.UUID,
    difficulty: int,
    provocation: str | None,
) -> tuple[Challenge, RiddleTemplate] | None:
    riddle = await pick_riddle(db, theme_id, difficulty)
    if riddle is None:
        return None
    challenge = Challenge(
        creator_user_id=creator_user_id,
        riddle_id=riddle.riddle_id,
        custom_provocation=provocation,
        share_token=secrets.token_urlsafe(24),
        expires_at=dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=CHALLENGE_TTL_HOURS),
    )
    db.add(challenge)
    await db.commit()
    await db.refresh(challenge)
    return challenge, riddle


async def get_by_share_token(db: AsyncSession, share_token: str) -> tuple[Challenge, RiddleTemplate] | None:
    stmt = select(Challenge).where(Challenge.share_token == share_token)
    challenge = (await db.execute(stmt)).scalars().first()
    if challenge is None:
        return None
    riddle = (await db.execute(
        select(RiddleTemplate).where(RiddleTemplate.riddle_id == challenge.riddle_id)
    )).scalars().first()
    return (challenge, riddle) if riddle else None
