"""Testes do motor de pontuacao e Bonus de Genio (GDD 3.4 / TDD 4.5)."""
import pytest
from app.engine.scoring import calculate_final_score
from app.engine.constants import TOTAL_TIME_SECONDS as T


def test_base_points_por_dificuldade():
    for diff in range(1, 6):
        r = calculate_final_score(diff, time_spent=0.0)
        assert r["base_points"] == diff * 1000


def test_bonus_genio_ativa_ate_30_porcento_sem_pistas():
    r = calculate_final_score(5, time_spent=0.30 * T)   # exatamente 54s
    assert r["is_genius"] is True
    assert r["genius_multiplier"] == 1.5


def test_bonus_genio_nao_ativa_apos_limiar():
    r = calculate_final_score(5, time_spent=0.30 * T + 0.01)
    assert r["is_genius"] is False
    assert r["genius_multiplier"] == 1.0


def test_bonus_genio_nao_ativa_com_pista():
    r = calculate_final_score(5, time_spent=10.0, clue_tiers_used=[1])
    assert r["is_genius"] is False


def test_penalidades_progressivas_somam():
    r = calculate_final_score(3, time_spent=90.0, clue_tiers_used=[1, 2])
    assert r["penalties"] == pytest.approx(0.35)


def test_placar_maximo_teorico():
    # dif 5, 0s, sem pistas => 5000 * 1.0 * 1.0 * 1.5 = 7500
    r = calculate_final_score(5, time_spent=0.0)
    assert r["final_score"] == 7500


def test_score_nunca_negativo_com_tempo_estourado():
    r = calculate_final_score(1, time_spent=10_000.0)
    assert r["final_score"] >= 0


def test_dificuldade_invalida():
    with pytest.raises(ValueError):
        calculate_final_score(6, time_spent=10.0)


def test_tier_de_pista_invalido():
    with pytest.raises(ValueError):
        calculate_final_score(3, time_spent=10.0, clue_tiers_used=[9])
