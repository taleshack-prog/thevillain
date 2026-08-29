"""Estagio 1 — Prompt Assembly (GDD 3.6). Monta o prompt injetando tema,
dificuldade, categoria e semente, exigindo saida em JSON estrito conforme schema."""
from __future__ import annotations

_SYSTEM_RULES = """Voce e o Curador de "O Vilao", arquiteto de enigmas goticos.
Gere UM enigma logico fechado, em portugues, com estetica Dark Fantasy sobria.
Responda SOMENTE com um objeto JSON valido, sem markdown, seguindo EXATAMENTE:
{
  "scenario": "2-3 frases (40-300 chars) situando o contexto gotico",
  "riddle": "a charada central (30-250 chars)",
  "correct_answer": "resposta correta (1-60 chars)",
  "distractors": ["3 alternativas incorretas plausiveis, distintas entre si"],
  "deduction_steps": ["2 a 4 passos de deducao encadeados (10-150 chars cada)"],
  "clues": [
    {"tier": 1, "text": "pista sutil"},
    {"tier": 2, "text": "pista direcional"},
    {"tier": 3, "text": "pista reveladora"}
  ]
}
A resposta correta NAO pode aparecer entre os distractors. Deve haver solucao unica."""


def assemble_prompt(*, theme_title: str, category: str, difficulty: int, seed: int) -> str:
    """Monta o prompt final (Estagio 1)."""
    return (
        f"{_SYSTEM_RULES}\n\n"
        f"TEMA: {theme_title}\n"
        f"CATEGORIA LOGICA: {category}\n"
        f"DIFICULDADE (1 a 5 caveiras): {difficulty}\n"
        f"SEMENTE: {seed}\n"
        "Gere o enigma agora, apenas o JSON."
    )
