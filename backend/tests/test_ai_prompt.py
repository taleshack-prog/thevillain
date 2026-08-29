"""Estagio 1 — o prompt deve conter tema, categoria, dificuldade e semente."""
from app.ai.prompt import assemble_prompt


def test_prompt_contem_parametros():
    p = assemble_prompt(theme_title="Criptas dos Cruzados", category="logico_dedutivo",
                        difficulty=3, seed=99)
    assert "Criptas dos Cruzados" in p
    assert "logico_dedutivo" in p
    assert "3" in p and "99" in p
    assert "JSON" in p
