"""Atribuicao de coorte por safra temporal (FR-010: 30 jogadores por coorte semanal)."""
from __future__ import annotations

import datetime as dt
import uuid

# Namespace estavel para derivar UUIDs de coorte de forma deterministica.
_COHORT_NS = uuid.UUID("6a3fa000-0000-4000-8000-000000000001")


def current_cohort_id(now: dt.datetime | None = None) -> uuid.UUID:
    """Coorte = ano-semana ISO corrente (uuid5 deterministico)."""
    now = now or dt.datetime.now(dt.timezone.utc)
    iso = now.isocalendar()
    return uuid.uuid5(_COHORT_NS, f"{iso.year}-W{iso.week:02d}")
