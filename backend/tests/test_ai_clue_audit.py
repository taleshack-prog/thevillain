"""Estagio 4 — auditoria de hierarquia de pistas."""
from app.ai.clue_audit import audit_clues


def _clues(tiers, texts=None):
    texts = texts or [f"pista suficientemente longa {t}" for t in tiers]
    return [{"tier": t, "text": tx} for t, tx in zip(tiers, texts)]


def test_hierarquia_valida():
    ok, reasons = audit_clues(_clues([1, 2, 3]))
    assert ok and reasons == []


def test_reprova_tier_repetido():
    ok, _ = audit_clues(_clues([1, 2, 2]))
    assert ok is False


def test_reprova_quantidade_errada():
    ok, _ = audit_clues(_clues([1, 2]))
    assert ok is False


def test_reprova_pistas_redundantes():
    ok, _ = audit_clues(_clues([1, 2, 3], ["igual identica aqui"] * 3))
    assert ok is False
