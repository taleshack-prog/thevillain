"""Schemas de entrada/saida da API. O gabarito nunca aparece nas respostas de jogo."""
from __future__ import annotations
from pydantic import BaseModel, Field


# ---- Temas ----
class ThemeOut(BaseModel):
    theme_id: str
    slug: str
    title: str
    description: str
    accent_color: str
    is_philosophical: bool


# ---- Pontuacao (preview) ----
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


# ---- Curadoria / Convite ----
class ChallengeCreateRequest(BaseModel):
    creator_user_id: str
    theme_id: str
    difficulty: int = Field(ge=1, le=5)
    provocation: str | None = Field(default=None, max_length=280)


class ChallengeCreateResponse(BaseModel):
    challenge_id: str
    share_token: str
    share_path: str
    expires_at: str


class ChallengePublicOut(BaseModel):
    """Preview publico do convite — SEM enigma e SEM gabarito."""
    challenge_id: str
    share_token: str
    theme_title: str
    accent_color: str
    difficulty_level: int
    custom_provocation: str | None
    expires_at: str


# ---- Decifracao ----
class OptionOut(BaseModel):
    option_id: str   # id opaco (HMAC) — nao indica corretude
    text: str


class AttemptStartRequest(BaseModel):
    solver_user_id: str


class AttemptStartResponse(BaseModel):
    attempt_id: str
    riddle_id: str
    difficulty_level: int
    scenario_context: str
    riddle_text: str
    options: list[OptionOut]
    total_time_seconds: float
    session_signature: str
    nonce: str
    started_at: str


class ClueOut(BaseModel):
    tier: int
    clue_text: str
    score_penalty_percent: float


class SubmitRequest(BaseModel):
    chosen_option_id: str


class SubmitResponse(BaseModel):
    is_correct: bool
    quarantined: bool
    time_spent_seconds: float
    score: ScoreResponse
    correct_answer: str | None
    deduction_steps: list[str]


# ---- Ranking ----
class RankingRow(BaseModel):
    rank_position: int
    user_id: str
    accumulated_score: int
    challenges_completed: int
    genius_awards_count: int
