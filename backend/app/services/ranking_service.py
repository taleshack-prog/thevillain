"""Ranking por coorte (FR-010) e atualizacao pos-veredito (FR-013 — Bonus de Genio)."""
from __future__ import annotations

import datetime as dt
import uuid

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import RankingEntry
from app.services.cohort import current_cohort_id


async def apply_result(
    db: AsyncSession, user_id: uuid.UUID, final_score: int, is_genius: bool,
) -> None:
    """Upsert incremental da entrada de ranking do jogador na coorte corrente."""
    cohort_id = current_cohort_id()
    entry = (await db.execute(
        select(RankingEntry).where(
            RankingEntry.cohort_id == cohort_id, RankingEntry.user_id == user_id
        )
    )).scalars().first()

    if entry is None:
        db.add(RankingEntry(
            cohort_id=cohort_id, user_id=user_id,
            accumulated_score=final_score, challenges_completed=1,
            genius_awards_count=1 if is_genius else 0,
        ))
    else:
        await db.execute(
            update(RankingEntry)
            .where(RankingEntry.entry_id == entry.entry_id)
            .values(
                accumulated_score=RankingEntry.accumulated_score + final_score,
                challenges_completed=RankingEntry.challenges_completed + 1,
                genius_awards_count=RankingEntry.genius_awards_count + (1 if is_genius else 0),
                updated_at=dt.datetime.now(dt.timezone.utc),
            )
        )
    await db.commit()


async def get_cohort_ranking(db: AsyncSession, cohort_id: uuid.UUID | None = None, limit: int = 30) -> list[dict]:
    """Top da coorte (default: coorte da semana corrente), ordenado por score."""
    cohort_id = cohort_id or current_cohort_id()
    rows = (await db.execute(
        select(RankingEntry)
        .where(RankingEntry.cohort_id == cohort_id)
        .order_by(RankingEntry.accumulated_score.desc(), RankingEntry.updated_at.asc())
        .limit(limit)
    )).scalars().all()
    return [
        {
            "rank_position": i + 1,
            "user_id": str(r.user_id),
            "accumulated_score": r.accumulated_score,
            "challenges_completed": r.challenges_completed,
            "genius_awards_count": r.genius_awards_count,
        }
        for i, r in enumerate(rows)
    ]
