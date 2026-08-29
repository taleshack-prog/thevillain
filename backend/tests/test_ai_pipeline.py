"""Orquestrador dos 5 estagios com MockProvider, sem tocar em banco real.

A ingestao (Estagio 5) e substituida por um stub para isolar a logica de esteira.
"""
import uuid
import pytest

import app.ai.pipeline as pipeline_mod
from app.ai.pipeline import generate_and_ingest, RiddleGenerationError
from app.ai.provider import MockProvider, LLMProvider

pytestmark = pytest.mark.asyncio


class _FakeRiddle:
    def __init__(self):
        self.riddle_id = uuid.uuid4()
        self.difficulty_level = 3


async def _fake_ingest(db, theme_id, difficulty, payload, integrity_hash):
    r = _FakeRiddle(); r.difficulty_level = difficulty
    return r


async def test_pipeline_aprova_com_mock(monkeypatch):
    monkeypatch.setattr(pipeline_mod, "ingest_riddle", _fake_ingest)
    riddle, report = await generate_and_ingest(
        db=None, provider=MockProvider(),
        theme_id=uuid.uuid4(), theme_title="Criptas", difficulty=3, seed=5,
    )
    assert report.approved is True
    assert report.attempts >= 1
    assert report.provider == "mock"
    assert riddle.difficulty_level == 3


class _BadProvider(LLMProvider):
    name = "bad"
    async def generate_riddle(self, prompt, *, seed):
        return {"scenario": "curto", "riddle": "x", "correct_answer": "a",
                "distractors": ["a", "a", "a"], "deduction_steps": ["um"], "clues": []}


async def test_pipeline_falha_apos_teto(monkeypatch):
    monkeypatch.setattr(pipeline_mod, "ingest_riddle", _fake_ingest)
    with pytest.raises(RiddleGenerationError):
        await generate_and_ingest(
            db=None, provider=_BadProvider(),
            theme_id=uuid.uuid4(), theme_title="X", difficulty=2, seed=1,
        )


async def test_difficulty_invalida():
    with pytest.raises(ValueError):
        await generate_and_ingest(
            db=None, provider=MockProvider(),
            theme_id=uuid.uuid4(), theme_title="X", difficulty=9,
        )
