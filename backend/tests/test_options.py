"""Testes da selagem de opcoes — garantia de que o gabarito nao vaza (TDD 4.7)."""
import random
from app.engine.options import build_sealed_options, is_correct_submission, derive_option_id


SECRET = "segredo-de-teste"
CORRECT = "15:00"
DISTRACTORS = ["14:55", "15:15", "15:20"]


def _sealed(seed=1):
    return build_sealed_options(SECRET, "att-1", "nonce-1", CORRECT, DISTRACTORS, rng=random.Random(seed))


def test_quatro_opcoes_com_ids_unicos():
    s = _sealed()
    ids = [o["option_id"] for o in s.options]
    assert len(s.options) == 4
    assert len(set(ids)) == 4


def test_correct_id_esta_entre_as_opcoes_mas_nao_e_marcado():
    s = _sealed()
    ids = [o["option_id"] for o in s.options]
    assert s.correct_option_id in ids
    # Nenhum campo do payload publico indica corretude:
    assert all(set(o.keys()) == {"option_id", "text"} for o in s.options)


def test_verificacao_de_submissao():
    s = _sealed()
    correct_text_idx = [o["text"] for o in s.options].index(CORRECT)
    assert is_correct_submission(s.options[correct_text_idx]["option_id"], s.correct_option_id) is True
    wrong_idx = (correct_text_idx + 1) % 4
    assert is_correct_submission(s.options[wrong_idx]["option_id"], s.correct_option_id) is False


def test_derive_option_id_deterministico_e_dependente_do_segredo():
    a = derive_option_id(SECRET, "att-1", "nonce-1", 0)
    b = derive_option_id(SECRET, "att-1", "nonce-1", 0)
    c = derive_option_id("outro-segredo", "att-1", "nonce-1", 0)
    assert a == b and a != c and len(a) == 16


def test_exige_tres_distratores():
    import pytest
    with pytest.raises(ValueError):
        build_sealed_options(SECRET, "att-1", "n", CORRECT, ["so-um"], rng=random.Random(0))
