"""Constantes do pipeline de IA (GDD 3.6). Categorias e limites da geração."""

# Categorias logicas oficiais (GDD 3.5)
CATEGORIES = (
    "charada_gotica",      # Charada Classica Gotica
    "logico_dedutivo",     # Logico-Dedutivo
    "numerico_sequencial", # Numerico-Sequencial
    "criptografia_runica", # Criptografia Runica
)

# Teto de tentativas de geracao ate passar no Quality Gate (evita loop infinito).
MAX_GENERATION_ATTEMPTS = 5
