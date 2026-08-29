"""
Motor de Validacao Simbolica (SSoT — TDD 4.3 / Estagio 3 do pipeline de IA).

Quality Gate deterministico: garante unicidade da resposta, plausibilidade dos
distratores e conformidade estrutural com o JSON Schema estrito. Nenhum enigma
chega a riddle_templates sem passar por aqui.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft7Validator

from app.engine.constants import (
    N_DISTRACTORS,
    DEDUCTION_STEPS_MIN,
    DEDUCTION_STEPS_MAX,
    N_CLUES,
)

_SCHEMA_PATH = Path(__file__).with_name("riddle_schema.json")
_SCHEMA = json.loads(_SCHEMA_PATH.read_text(encoding="utf-8"))
_JSON_VALIDATOR = Draft7Validator(_SCHEMA)


class SymbolicValidator:
    """Valida o payload logico e semantico de um enigma."""

    @staticmethod
    def schema_errors(payload: dict[str, Any]) -> list[str]:
        """Erros de conformidade com o JSON Schema estrito (vazio = conforme)."""
        return [e.message for e in _JSON_VALIDATOR.iter_errors(payload)]

    @staticmethod
    def validate_riddle_payload(payload: dict[str, Any]) -> bool:
        """Regras deterministicas (TDD 4.3). True somente se TODAS passarem."""
        required = ["scenario", "riddle", "correct_answer", "distractors", "deduction_steps"]
        if not all(k in payload for k in required):
            return False

        distractors: list[str] = payload.get("distractors", [])
        correct: str = payload.get("correct_answer", "").strip()

        # Regra 1: exatamente 3 distratores.
        if len(distractors) != N_DISTRACTORS:
            return False

        # Regra 2: distratores distintos entre si e da resposta correta (4 unicos).
        all_answers = {d.strip().lower() for d in distractors} | {correct.lower()}
        if len(all_answers) != N_DISTRACTORS + 1:
            return False

        # Regra 3: trilha de deducao encadeada com 2 a 4 passos.
        steps: list[str] = payload.get("deduction_steps", [])
        if not (DEDUCTION_STEPS_MIN <= len(steps) <= DEDUCTION_STEPS_MAX):
            return False

        return True

    @staticmethod
    def validate_clue_hierarchy(clues: list[dict[str, Any]]) -> bool:
        """Estagio 4: exatamente 3 pistas, tiers 1,2,3 sem repeticao (revelacao progressiva)."""
        if len(clues) != N_CLUES:
            return False
        tiers = sorted(c.get("tier") for c in clues)
        return tiers == [1, 2, 3]

    @staticmethod
    def generate_integrity_hash(payload: dict[str, Any]) -> str:
        """Hash de integridade logica gravado em riddle_templates.symbolic_hash."""
        serialized = json.dumps(payload, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()

    @classmethod
    def full_gate(cls, payload: dict[str, Any]) -> tuple[bool, list[str]]:
        """Portao completo: schema + regras + hierarquia de pistas. (ok, motivos)."""
        reasons = cls.schema_errors(payload)
        if reasons:
            return False, reasons
        if not cls.validate_riddle_payload(payload):
            reasons.append("Falha nas regras deterministicas (distratores/unicidade/passos).")
        if not cls.validate_clue_hierarchy(payload.get("clues", [])):
            reasons.append("Hierarquia de pistas invalida (esperado tiers 1,2,3 unicos).")
        return (len(reasons) == 0), reasons
