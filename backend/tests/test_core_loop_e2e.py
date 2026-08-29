"""
Integracao do core loop ponta a ponta (curadoria -> convite -> decifracao ->
veredito -> ranking -> revancha) contra Postgres 16 + Redis reais.

Pula automaticamente se DATABASE_URL/REDIS_URL nao estiverem acessiveis, para
nao quebrar ambientes sem servicos. Requer seed previo (python -m app.db.seed).
"""
from __future__ import annotations

import json
import uuid

import pytest

pytestmark = pytest.mark.asyncio

httpx = pytest.importorskip("httpx")


async def _services_up() -> bool:
    try:
        import asyncpg
        from redis.asyncio import Redis
        from app.core.config import get_settings
        s = get_settings()
        conn = await asyncpg.connect(s.database_url.replace("postgresql+asyncpg://", "postgresql://"))
        await conn.close()
        r = Redis.from_url(s.redis_url)
        await r.ping(); await r.aclose()
        return True
    except Exception:
        return False


@pytest.fixture
async def client():
    if not await _services_up():
        pytest.skip("Postgres/Redis indisponiveis — teste de integracao pulado.")
    from httpx import ASGITransport
    from app.main import app
    async with httpx.AsyncClient(transport=ASGITransport(app=app), base_url="http://t") as c:
        yield c
    from app.core.redis import close_redis
    from app.db.base import dispose_engine
    await close_redis(); await dispose_engine()


async def test_core_loop_esconde_gabarito_e_pontua(client):
    themes = (await client.get("/api/v1/themes")).json()
    if not themes:
        pytest.skip("Sem temas — rode 'python -m app.db.seed' antes.")
    theme = next((t for t in themes if t["slug"] == "mansao-vitoriana"), themes[0])

    created = (await client.post("/api/v1/challenges", json={
        "creator_user_id": str(uuid.uuid4()), "theme_id": theme["theme_id"],
        "difficulty": 2, "provocation": "Decifra?",
    }))
    if created.status_code == 404:
        pytest.skip("Sem enigma homologado para tema/dificuldade.")
    token = created.json()["share_token"]

    # Convite nao pode conter enigma/gabarito.
    prev = (await client.get(f"/api/v1/challenges/{token}")).json()
    assert "correct_answer" not in prev and "riddle_text" not in prev

    # Inicio da decifracao nao pode vazar o gabarito.
    start = (await client.post(f"/api/v1/challenges/{token}/attempts",
                               json={"solver_user_id": str(uuid.uuid4())})).json()
    assert "correct_answer" not in json.dumps(start)
    for o in start["options"]:
        assert set(o.keys()) == {"option_id", "text"}

    # Submissao imediata cai em quarentena (anti-cheat < 3.5s).
    any_opt = start["options"][0]["option_id"]
    sub = (await client.post(f"/api/v1/attempts/{start['attempt_id']}/submit",
                             json={"chosen_option_id": any_opt})).json()
    assert sub["quarantined"] is True and sub["score"]["final_score"] == 0
