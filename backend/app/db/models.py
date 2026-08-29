"""
Modelos ORM mapeados 1:1 ao schema PostgreSQL 16 congelado (TDD 4.2).
NAO alteram DDL — apenas refletem as tabelas existentes. Migracoes via Alembic.
"""
from __future__ import annotations

import datetime as dt
import uuid

from sqlalchemy import (
    Boolean, CheckConstraint, ForeignKey, Integer, Numeric, SmallInteger,
    String, Text, text,
)
from sqlalchemy.dialects.postgresql import ARRAY, JSONB, TIMESTAMP, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

_UUID = UUID(as_uuid=True)
_TS = TIMESTAMP(timezone=True)


class RiddleTheme(Base):
    __tablename__ = "riddle_themes"
    theme_id: Mapped[uuid.UUID] = mapped_column(_UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    slug: Mapped[str] = mapped_column(String(64), unique=True)
    title: Mapped[str] = mapped_column(String(128))
    description: Mapped[str] = mapped_column(Text)
    accent_color: Mapped[str] = mapped_column(String(7), server_default=text("'#8B5CF6'"))
    is_philosophical: Mapped[bool] = mapped_column(Boolean, server_default=text("false"))
    created_at: Mapped[dt.datetime] = mapped_column(_TS, server_default=text("NOW()"))


class RiddleTemplate(Base):
    __tablename__ = "riddle_templates"
    riddle_id: Mapped[uuid.UUID] = mapped_column(_UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    theme_id: Mapped[uuid.UUID] = mapped_column(_UUID, ForeignKey("riddle_themes.theme_id"))
    difficulty_level: Mapped[int] = mapped_column(SmallInteger)
    scenario_context: Mapped[str] = mapped_column(Text)
    riddle_text: Mapped[str] = mapped_column(Text)
    correct_answer: Mapped[str] = mapped_column(String(255))       # NUNCA serializado ao cliente
    distractors: Mapped[list] = mapped_column(JSONB)
    deduction_steps: Mapped[list] = mapped_column(JSONB)
    symbolic_hash: Mapped[str] = mapped_column(String(64))
    is_active: Mapped[bool] = mapped_column(Boolean, server_default=text("true"))
    created_at: Mapped[dt.datetime] = mapped_column(_TS, server_default=text("NOW()"))
    __table_args__ = (CheckConstraint("difficulty_level BETWEEN 1 AND 5"),)


class Clue(Base):
    __tablename__ = "clues"
    clue_id: Mapped[uuid.UUID] = mapped_column(_UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    riddle_id: Mapped[uuid.UUID] = mapped_column(_UUID, ForeignKey("riddle_templates.riddle_id", ondelete="CASCADE"))
    tier_level: Mapped[int] = mapped_column(SmallInteger)
    clue_text: Mapped[str] = mapped_column(Text)
    score_penalty_percent: Mapped[float] = mapped_column(Numeric(4, 2))
    created_at: Mapped[dt.datetime] = mapped_column(_TS, server_default=text("NOW()"))
    __table_args__ = (CheckConstraint("tier_level BETWEEN 1 AND 3"),)


class Challenge(Base):
    __tablename__ = "challenges"
    challenge_id: Mapped[uuid.UUID] = mapped_column(_UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    creator_user_id: Mapped[uuid.UUID] = mapped_column(_UUID)
    riddle_id: Mapped[uuid.UUID] = mapped_column(_UUID, ForeignKey("riddle_templates.riddle_id"))
    custom_provocation: Mapped[str | None] = mapped_column(String(280), nullable=True)
    share_token: Mapped[str] = mapped_column(String(64), unique=True)
    expires_at: Mapped[dt.datetime] = mapped_column(_TS)
    created_at: Mapped[dt.datetime] = mapped_column(_TS, server_default=text("NOW()"))


class RiddleAttempt(Base):
    __tablename__ = "riddle_attempts"
    # Tabela particionada por RANGE(created_at); PK composta (attempt_id, created_at).
    attempt_id: Mapped[uuid.UUID] = mapped_column(_UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    challenge_id: Mapped[uuid.UUID] = mapped_column(_UUID, ForeignKey("challenges.challenge_id"))
    solver_user_id: Mapped[uuid.UUID] = mapped_column(_UUID)
    started_at: Mapped[dt.datetime] = mapped_column(_TS, server_default=text("NOW()"))
    finished_at: Mapped[dt.datetime | None] = mapped_column(_TS, nullable=True)
    time_spent_seconds: Mapped[float | None] = mapped_column(Numeric(6, 2), nullable=True)
    clues_used: Mapped[list[int]] = mapped_column(ARRAY(SmallInteger), server_default=text("'{}'"))
    is_correct: Mapped[bool] = mapped_column(Boolean, server_default=text("false"))
    session_hmac: Mapped[str] = mapped_column(String(64))
    created_at: Mapped[dt.datetime] = mapped_column(_TS, primary_key=True, server_default=text("NOW()"))


class Result(Base):
    __tablename__ = "results"
    result_id: Mapped[uuid.UUID] = mapped_column(_UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    attempt_id: Mapped[uuid.UUID] = mapped_column(_UUID)
    attempt_created_at: Mapped[dt.datetime] = mapped_column(_TS)
    base_points: Mapped[int] = mapped_column(Integer)
    time_bonus: Mapped[float] = mapped_column(Numeric(6, 2))
    penalties: Mapped[float] = mapped_column(Numeric(6, 2))
    genius_multiplier: Mapped[float] = mapped_column(Numeric(3, 2), server_default=text("1.0"))
    final_score: Mapped[int] = mapped_column(Integer)
    calculated_at: Mapped[dt.datetime] = mapped_column(_TS, server_default=text("NOW()"))


class RankingEntry(Base):
    __tablename__ = "ranking_entries"
    entry_id: Mapped[uuid.UUID] = mapped_column(_UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    cohort_id: Mapped[uuid.UUID] = mapped_column(_UUID)
    user_id: Mapped[uuid.UUID] = mapped_column(_UUID)
    accumulated_score: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    challenges_completed: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    genius_awards_count: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    rank_position: Mapped[int | None] = mapped_column(Integer, nullable=True)
    updated_at: Mapped[dt.datetime] = mapped_column(_TS, server_default=text("NOW()"))
