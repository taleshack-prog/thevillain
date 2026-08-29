"""Healthcheck e metadados de build."""
from fastapi import APIRouter
from app.core.config import get_settings

router = APIRouter(tags=["system"])


@router.get("/health")
async def health() -> dict:
    s = get_settings()
    return {"status": "ok", "app": s.app_name, "env": s.app_env}
