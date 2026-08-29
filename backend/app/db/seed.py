"""
Popula riddle_themes, riddle_templates e clues com os enigmas-exemplo homologados
(SSoT — Anexo F1). Cada enigma passa pelo Quality Gate antes de ser inserido.

Uso:  python -m app.db.seed
"""
from __future__ import annotations

import asyncio
import json
from pathlib import Path

import asyncpg

from app.core.config import get_settings
from app.engine.validator import SymbolicValidator

_SEED = Path(__file__).resolve().parent.parent / "data" / "seed_riddles.json"


def _asyncpg_dsn(url: str) -> str:
    # Converte o DSN do SQLAlchemy (postgresql+asyncpg://) para o formato do asyncpg.
    return url.replace("postgresql+asyncpg://", "postgresql://")


async def seed() -> None:
    data = json.loads(_SEED.read_text(encoding="utf-8"))
    dsn = _asyncpg_dsn(get_settings().database_url)
    conn = await asyncpg.connect(dsn)
    try:
        theme_ids: dict[str, str] = {}
        for t in data["themes"]:
            row = await conn.fetchrow(
                """
                INSERT INTO riddle_themes (slug, title, description, accent_color, is_philosophical)
                VALUES ($1,$2,$3,$4,$5)
                ON CONFLICT (slug) DO UPDATE SET title = EXCLUDED.title
                RETURNING theme_id
                """,
                t["slug"], t["title"], t["description"], t["accent_color"], t["is_philosophical"],
            )
            theme_ids[t["slug"]] = str(row["theme_id"])
            print(f"[tema] {t['slug']} -> {row['theme_id']}")

        for r in data["riddles"]:
            payload = {
                "scenario": r["scenario"], "riddle": r["riddle"],
                "correct_answer": r["correct_answer"], "distractors": r["distractors"],
                "deduction_steps": r["deduction_steps"], "clues": r["clues"],
            }
            ok, reasons = SymbolicValidator.full_gate(payload)
            if not ok:
                raise ValueError(f"Enigma reprovado no Quality Gate: {reasons}")
            integrity = SymbolicValidator.generate_integrity_hash(payload)

            riddle_row = await conn.fetchrow(
                """
                INSERT INTO riddle_templates
                    (theme_id, difficulty_level, scenario_context, riddle_text,
                     correct_answer, distractors, deduction_steps, symbolic_hash)
                VALUES ($1,$2,$3,$4,$5,$6,$7,$8)
                RETURNING riddle_id
                """,
                theme_ids[r["theme_slug"]], r["difficulty_level"], r["scenario"], r["riddle"],
                r["correct_answer"], json.dumps(r["distractors"], ensure_ascii=False),
                json.dumps(r["deduction_steps"], ensure_ascii=False), integrity,
            )
            riddle_id = riddle_row["riddle_id"]
            penalties = {1: 0.10, 2: 0.25, 3: 0.50}
            for c in r["clues"]:
                await conn.execute(
                    """
                    INSERT INTO clues (riddle_id, tier_level, clue_text, score_penalty_percent)
                    VALUES ($1,$2,$3,$4)
                    """,
                    riddle_id, c["tier"], c["text"], penalties[c["tier"]],
                )
            print(f"[enigma] {r['theme_slug']} dif={r['difficulty_level']} -> {riddle_id}")
        print("Seed concluido com sucesso.")
    finally:
        await conn.close()


if __name__ == "__main__":
    asyncio.run(seed())
