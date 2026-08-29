"""Estagio 4 — Auditoria de Pistas (GDD 3.6).

Confere a hierarquia de revelacao progressiva: exatamente 3 pistas, tiers 1,2,3
unicos, e ausencia de redundancia obvia (textos distintos). Retorna (ok, motivos).
"""
from __future__ import annotations

from typing import Any

from app.engine.constants import N_CLUES


def audit_clues(clues: list[dict[str, Any]]) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    if len(clues) != N_CLUES:
        reasons.append(f"Esperadas {N_CLUES} pistas, recebidas {len(clues)}.")
        return False, reasons

    tiers = sorted(c.get("tier") for c in clues)
    if tiers != [1, 2, 3]:
        reasons.append(f"Tiers devem ser 1,2,3 unicos; recebido {tiers}.")

    texts = [(c.get("text") or "").strip().casefold() for c in clues]
    if len(set(texts)) != len(texts):
        reasons.append("Pistas redundantes: ha textos identicos entre os tiers.")
    if any(len(t) < 10 for t in texts):
        reasons.append("Alguma pista e curta demais (< 10 caracteres).")

    return (len(reasons) == 0), reasons
