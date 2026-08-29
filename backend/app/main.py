"""O Vilao — aplicacao FastAPI (Gateway & Application API, TDD 4.1)."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.api.routes import health, scoring, riddles

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Motor de curadoria procedural, validacao simbolica e pontuacao — O Vilao.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix=settings.api_v1_prefix)
app.include_router(scoring.router, prefix=settings.api_v1_prefix)
app.include_router(riddles.router, prefix=settings.api_v1_prefix)


@app.get("/")
async def root() -> dict:
    return {"product": "O Vilao", "docs": "/docs", "health": f"{settings.api_v1_prefix}/health"}
