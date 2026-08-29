"""Configuracao central (pydantic-settings).

Carrega o `.env` da RAIZ do repositorio de forma absoluta, para funcionar
independentemente do diretorio de trabalho (ex.: rodar alembic/uvicorn de
dentro de `backend/`). Variaveis de ambiente do shell tem prioridade sobre o .env.
"""
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# backend/app/core/config.py -> parents: [0]=core [1]=app [2]=backend [3]=raiz
_REPO_ROOT = Path(__file__).resolve().parents[3]
_ENV_FILES = (str(_REPO_ROOT / ".env"), ".env")  # raiz + fallback local (CWD)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=_ENV_FILES, extra="ignore")

    app_env: str = "development"
    app_name: str = "O Vilao API"
    api_v1_prefix: str = "/api/v1"

    database_url: str = "postgresql+asyncpg://vilao:vilao@localhost:5432/vilao"
    redis_url: str = "redis://localhost:6379/0"
    celery_broker_url: str = "redis://localhost:6379/1"

    # Seguranca / anti-cheat / LGPD
    session_hmac_secret: str = "dev-hmac-secret-troque-em-producao"
    telemetry_salt: str = "dev-salt-troque-em-producao"
    jwt_secret: str = "dev-jwt-secret"
    jwt_algorithm: str = "HS256"

    # Inferencia IA
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "mistral:7b-instruct-q4_0"

    cors_origins: str = "http://localhost:3000,http://localhost:19006"

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
