"""Schemas de entrada/saida da API. O gabarito nunca aparece nas respostas de jogo."""
from __future__ import annotations
from pydantic import BaseModel, Field


class ThemeOut(BaseModel):
    theme_id: str
    slug: str
    title: str
    description: str
    accent_color: str
    is_philosophical: bool


class OptionOut(BaseModel):
    """Opcao de resposta entregue ao cliente: apenas id efemero + texto (sem gabarito)."""
    option_id: str  # embaralhado/nonce; correto so e conhecido no servidor
    text: str


class RiddlePublicOut(BaseModel):
    """Payload de gameplay — SEM correct_answer, SEM symbolic_hash."""
    riddle_id: str
    theme: str
    difficulty_level: int = Field(ge=1, le=5)
    scenario_context: str
    riddle_text: str
    options: list[OptionOut]
    total_time_seconds: float
    session_signature: str
    nonce: str


class ScoreRequest(BaseModel):
    difficulty: int = Field(ge=1, le=5)
    time_spent: float = Field(ge=0)
    clue_tiers_used: list[int] = Field(default_factory=list)


class ScoreResponse(BaseModel):
    base_points: int
    time_bonus: float
    penalties: float
    genius_multiplier: float
    is_genius: bool
    final_score: int
