"""Baseline: aplica o schema PostgreSQL 16 congelado (SSoT / TDD 4.2).

Executa o schema.sql instrucao a instrucao, pois o driver asyncpg (protocolo
estendido) nao aceita multiplos comandos numa unica chamada. Idempotente
(CREATE ... IF NOT EXISTS).

Revision ID: 0001_baseline
Revises:
Create Date: 2026-08-29
"""
from pathlib import Path

from alembic import op

revision = "0001_baseline"
down_revision = None
branch_labels = None
depends_on = None

_SCHEMA_SQL = Path(__file__).resolve().parents[2] / "app" / "db" / "schema.sql"


def _split_statements(sql: str) -> list[str]:
    """Divide o SQL em comandos individuais (schema.sql nao usa dollar-quoting)."""
    statements: list[str] = []
    for raw in sql.split(";"):
        # Remove linhas que sao apenas comentario para detectar chunks vazios.
        meaningful = "\n".join(
            ln for ln in raw.splitlines() if not ln.strip().startswith("--")
        ).strip()
        if meaningful:
            statements.append(raw.strip() + ";")
    return statements


def upgrade() -> None:
    sql = _SCHEMA_SQL.read_text(encoding="utf-8")
    for stmt in _split_statements(sql):
        op.execute(stmt)


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS results CASCADE")
    op.execute("DROP TABLE IF EXISTS ranking_entries CASCADE")
    op.execute("DROP TABLE IF EXISTS telemetry_events CASCADE")
    op.execute("DROP TABLE IF EXISTS riddle_attempts CASCADE")
    op.execute("DROP TABLE IF EXISTS challenges CASCADE")
    op.execute("DROP TABLE IF EXISTS clues CASCADE")
    op.execute("DROP TABLE IF EXISTS riddle_templates CASCADE")
    op.execute("DROP TABLE IF EXISTS riddle_themes CASCADE")
    op.execute("DROP SCHEMA IF EXISTS pii_data CASCADE")
    op.execute("DROP TABLE IF EXISTS alembic_version")
