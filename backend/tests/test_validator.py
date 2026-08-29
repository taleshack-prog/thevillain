"""Testes do Motor de Validacao Simbolica (TDD 4.3) e do seed homologado."""
import json
from pathlib import Path

from app.engine.validator import SymbolicValidator as SV


def _riddle_base() -> dict:
    return {
        "scenario": "Na cripta silenciosa, tres selos guardam um unico caminho verdadeiro entre sombras.",
        "riddle": "Qual selo revela a passagem sem despertar a armadilha ancestral?",
        "correct_answer": "Selo de Prata",
        "distractors": ["Selo de Bronze", "Selo de Chumbo", "Selo de Osso"],
        "deduction_steps": [
            "Apenas um selo mantem a inscricao coerente com o testamento.",
            "Os demais contradizem a regra da unica verdade permitida.",
        ],
        "clues": [
            {"tier": 1, "text": "Observe qual inscricao nao entra em contradicao com as outras."},
            {"tier": 2, "text": "Duas afirmacoes verdadeiras juntas violam o testamento antigo."},
            {"tier": 3, "text": "Procure o cenario em que so uma frase permanece verdadeira."},
        ],
    }


def test_payload_valido_passa_no_gate():
    ok, reasons = SV.full_gate(_riddle_base())
    assert ok is True and reasons == []


def test_reprova_com_menos_de_tres_distratores():
    p = _riddle_base(); p["distractors"] = ["A", "B"]
    assert SV.validate_riddle_payload(p) is False


def test_reprova_distrator_igual_a_resposta():
    p = _riddle_base(); p["distractors"] = ["Selo de Prata", "Selo de Bronze", "Selo de Osso"]
    assert SV.validate_riddle_payload(p) is False


def test_reprova_passos_fora_do_intervalo():
    p = _riddle_base(); p["deduction_steps"] = ["passo unico e curto demais aqui"]
    assert SV.validate_riddle_payload(p) is False


def test_hierarquia_de_pistas_exige_tiers_123():
    p = _riddle_base(); p["clues"][2]["tier"] = 2
    assert SV.validate_clue_hierarchy(p["clues"]) is False


def test_hash_integridade_deterministico():
    p = _riddle_base()
    assert SV.generate_integrity_hash(p) == SV.generate_integrity_hash(dict(p))


def test_seed_homologado_passa_no_gate():
    seed = json.loads((Path(__file__).resolve().parent.parent /
                       "app" / "data" / "seed_riddles.json").read_text(encoding="utf-8"))
    for r in seed["riddles"]:
        payload = {k: r[k] for k in
                   ("scenario", "riddle", "correct_answer", "distractors", "deduction_steps", "clues")}
        ok, reasons = SV.full_gate(payload)
        assert ok, reasons
