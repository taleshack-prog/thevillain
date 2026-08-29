"""Constantes de balanceamento do GDD (SSoT 3.3 / 3.4). Nao alterar sem homologacao."""

TOTAL_TIME_SECONDS: float = 180.0            # GDD 3.4: TempoTotal
BASE_POINTS_PER_LEVEL: int = 1000            # PontosBase = 1000 * dificuldade (1..5)

# Penalidade progressiva por pista (GDD 3.3 — Camada 4)
CLUE_PENALTIES: dict[int, float] = {1: 0.10, 2: 0.25, 3: 0.50}

# Bonus de Genio (GDD 3.4 / TDD 4.5): resolucao em <=30% do tempo e sem pistas.
GENIUS_TIME_RATIO: float = 0.30
GENIUS_MULTIPLIER: float = 1.5

# Anti-cheat temporal (TDD 4.7): submissoes < 3.5s vao para quarentena.
ANTI_CHEAT_MIN_SECONDS: float = 3.5

# Anatomia do enigma (GDD 3.3 / JSON Schema)
N_DISTRACTORS: int = 3
DEDUCTION_STEPS_MIN: int = 2
DEDUCTION_STEPS_MAX: int = 4
N_CLUES: int = 3
