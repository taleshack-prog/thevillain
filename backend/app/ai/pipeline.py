"""
Orquestrador do Pipeline de IA de 5 estagios (GDD 3.6), esteira serial inviolavel:

  1. Prompt Assembly      -> app.ai.prompt.assemble_prompt
  2. SLM Generation       -> LLMProvider (mock | ollama)
  3. Validacao Simbolica  -> SymbolicValidator.full_gate (Quality Gate)
  4. Auditoria de Pistas  -> app.ai.clue_audit.audit_clues
  5. Ingestion & Cache    -> app.ai.ingestion.ingest_riddle

Reexecuta a geracao ate MAX_GENERATION_ATTEMPTS caso o Quality Gate reprove,
variando a semente. Retorna o RiddleTemplate homologado ou levanta erro.
"""
from __future__ import annotations

import json
import random
import uuid
from dataclasses import dataclass, field
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.ai.clue_audit import audit_clues
from app.ai.constants import CATEGORIES, MAX_GENERATION_ATTEMPTS
from app.ai.ingestion import ingest_riddle
from app.ai.prompt import assemble_prompt
from app.ai.provider import LLMProvider
from app.db.models import RiddleTemplate
from app.engine.validator import SymbolicValidator


class RiddleGenerationError(RuntimeError):
    """Falha ao produzir um enigma aprovado dentro do teto de tentativas."""


@dataclass
class GenerationReport:
    approved: bool = False
    attempts: int = 0
    provider: str = ""
    reasons: list[str] = field(default_factory=list)  # motivos da ultima reprovacao


async def generate_and_ingest(
    db: AsyncSession,
    provider: LLMProvider,
    *,
    theme_id: uuid.UUID,
    theme_title: str,
    difficulty: int,
    category: str | None = None,
    seed: int | None = None,
) -> tuple[RiddleTemplate, GenerationReport]:
    if not 1 <= difficulty <= 5:
        raise ValueError("difficulty deve estar entre 1 e 5")
    category = category or CATEGORIES[1]  # default: logico_dedutivo
    base_seed = seed if seed is not None else random.randint(1, 2**31 - 1)

    report = GenerationReport(provider=provider.name)

    for attempt in range(MAX_GENERATION_ATTEMPTS):
        report.attempts = attempt + 1
        cur_seed = base_seed + attempt

        # Estagio 1
        prompt = assemble_prompt(
            theme_title=theme_title, category=category,
            difficulty=difficulty, seed=cur_seed,
        )
        # Estagio 2
        try:
            payload: dict[str, Any] = await provider.generate_riddle(prompt, seed=cur_seed)
        except (json.JSONDecodeError, ValueError) as exc:
            report.reasons = [f"Geracao invalida (JSON): {exc}"]
            continue

        # Estagio 3 (Quality Gate deterministico)
        ok_gate, gate_reasons = SymbolicValidator.full_gate(payload)
        if not ok_gate:
            report.reasons = gate_reasons
            continue

        # Estagio 4 (Auditoria de pistas)
        ok_clues, clue_reasons = audit_clues(payload.get("clues", []))
        if not ok_clues:
            report.reasons = clue_reasons
            continue

        # Estagio 5 (Ingestao + cache)
        integrity = SymbolicValidator.generate_integrity_hash(payload)
        riddle = await ingest_riddle(db, theme_id, difficulty, payload, integrity)
        report.approved = True
        report.reasons = []
        return riddle, report

    raise RiddleGenerationError(
        f"Nenhum enigma aprovado em {report.attempts} tentativas "
        f"(provider={provider.name}). Ultima reprovacao: {report.reasons}"
    )
