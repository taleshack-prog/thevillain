"""Coorte por safra semanal ISO (FR-010)."""
import datetime as dt
from app.services.cohort import current_cohort_id


def test_mesma_semana_gera_mesma_coorte():
    a = dt.datetime(2026, 8, 24, 9, 0, tzinfo=dt.timezone.utc)   # seg
    b = dt.datetime(2026, 8, 28, 22, 0, tzinfo=dt.timezone.utc)  # sex, mesma semana ISO
    assert current_cohort_id(a) == current_cohort_id(b)


def test_semanas_diferentes_geram_coortes_diferentes():
    a = dt.datetime(2026, 8, 24, tzinfo=dt.timezone.utc)
    b = dt.datetime(2026, 9, 1, tzinfo=dt.timezone.utc)
    assert current_cohort_id(a) != current_cohort_id(b)
