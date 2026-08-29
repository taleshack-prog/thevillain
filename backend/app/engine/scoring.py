"""
Motor de Pontuacao e Bonus de Genio (SSoT — GDD 3.4 / TDD 4.5).

    Pontuacao = (PontosBase * TempoRestante/TempoTotal)
                * (1 - PenalidadePistas)
                * MultiplicadorGenio

- PontosBase        = 1000 * dificuldade (1..5)  -> 1000..5000
- TempoRestante     = TempoTotal - tempo_gasto (nunca negativo)
- PenalidadePistas  = soma das penalidades das pistas usadas (0.10/0.25/0.50)
- MultiplicadorGenio= 1.5 se tempo_gasto <= 30% do total E nenhuma pista; senao 1.0
"""
from __future__ import annotations
from collections.abc import Iterable

from app.engine.constants import (
    TOTAL_TIME_SECONDS,
    BASE_POINTS_PER_LEVEL,
    CLUE_PENALTIES,
    GENIUS_TIME_RATIO,
    GENIUS_MULTIPLIER,
)


def calculate_final_score(
    difficulty: int,
    time_spent: float,
    total_time: float = TOTAL_TIME_SECONDS,
    clue_tiers_used: Iterable[int] = (),
) -> dict:
    """Calcula o placar final de uma tentativa. Retorna o breakdown completo."""
    if not 1 <= difficulty <= 5:
        raise ValueError("difficulty deve estar entre 1 e 5")
    if total_time <= 0:
        raise ValueError("total_time deve ser positivo")

    tiers = list(clue_tiers_used)
    unknown = [t for t in tiers if t not in CLUE_PENALTIES]
    if unknown:
        raise ValueError(f"tiers de pista invalidos: {unknown}")

    base_points = difficulty * BASE_POINTS_PER_LEVEL
    time_ratio = max(0.0, (total_time - time_spent) / total_time)
    penalty_sum = sum(CLUE_PENALTIES[t] for t in tiers)
    time_bonus = base_points * time_ratio

    score_raw = time_bonus * max(0.0, 1.0 - penalty_sum)

    is_genius = (time_spent <= GENIUS_TIME_RATIO * total_time) and (penalty_sum == 0)
    genius_multiplier = GENIUS_MULTIPLIER if is_genius else 1.0

    final_score = max(0, int(round(score_raw * genius_multiplier)))

    return {
        "base_points": base_points,
        "time_ratio": round(time_ratio, 4),
        "time_bonus": round(time_bonus, 2),
        "penalties": round(penalty_sum, 2),
        "genius_multiplier": genius_multiplier,
        "is_genius": is_genius,
        "final_score": final_score,
    }
