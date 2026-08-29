"""O Vilao — aplicacao FastAPI (Gateway & Application API, TDD 4.1)."""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.core.redis import close_redis
from app.db.base import dispose_engine
from app.api.routes import health, scoring, riddles, themes, challenges, attempts

settings = get_settings()


@asynccontextmanager
async def lifespan(_app: FastAPI):
    yield
    await close_redis()
    await dispose_engine()


app = FastAPI(
    title=settings.app_name,
    version="0.2.0",
    description="Core loop assincrono de O Vilao: curadoria, convite, decifracao e ranking.",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_p = settings.api_v1_prefix
for r in (health.router, scoring.router, riddles.router, themes.router, challenges.router, attempts.router):
    app.include_router(r, prefix=_p)


@app.get("/")
async def root() -> dict:
    return {"product": "O Vilao", "version": app.version, "docs": "/docs",
            "health": f"{_p}/health"}
