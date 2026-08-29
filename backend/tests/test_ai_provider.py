"""MockProvider deve produzir enigmas deterministicos e aprovados pelo Quality Gate."""
import pytest

from app.ai.provider import MockProvider, build_provider
from app.engine.validator import SymbolicValidator as SV
from app.ai.clue_audit import audit_clues


@pytest.mark.asyncio
async def test_mock_gera_payload_valido():
    payload = await MockProvider().generate_riddle("prompt", seed=42)
    ok, reasons = SV.full_gate(payload)
    assert ok, reasons
    ok_c, rc = audit_clues(payload["clues"])
    assert ok_c, rc


@pytest.mark.asyncio
async def test_mock_e_deterministico_por_seed():
    p = MockProvider()
    a = await p.generate_riddle("x", seed=7)
    b = await p.generate_riddle("y", seed=7)
    c = await p.generate_riddle("x", seed=8)
    assert a == b and a != c


@pytest.mark.asyncio
async def test_resposta_correta_nao_esta_nos_distratores():
    payload = await MockProvider().generate_riddle("x", seed=123)
    assert payload["correct_answer"] not in payload["distractors"]


def test_build_provider_default_mock():
    assert build_provider("qualquercoisa", base_url="http://x", model="m").name == "mock"
    assert build_provider("ollama", base_url="http://x", model="m").name == "ollama"
