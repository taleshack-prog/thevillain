"""Injecao do LLMProvider conforme configuracao (LLM_PROVIDER)."""
from __future__ import annotations

from functools import lru_cache

from app.ai.provider import LLMProvider, build_provider
from app.core.config import get_settings


@lru_cache
def get_provider() -> LLMProvider:
    s = get_settings()
    return build_provider(s.llm_provider, base_url=s.ollama_base_url, model=s.ollama_model)
