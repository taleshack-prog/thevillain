"""
Endpoint de validacao de enigmas (Estagio 3-4 do pipeline de IA — TDD 4.3).
Recebe um payload gerado e retorna o veredito do Quality Gate deterministico.
"""
from fastapi import APIRouter
from pydantic import BaseModel

from app.engine.validator import SymbolicValidator

router = APIRouter(prefix="/riddles", tags=["riddles"])


class ValidationResult(BaseModel):
    valid: bool
    reasons: list[str]
    integrity_hash: str | None = None


@router.post("/validate", response_model=ValidationResult)
async def validate(payload: dict) -> ValidationResult:
    ok, reasons = SymbolicValidator.full_gate(payload)
    integrity = SymbolicValidator.generate_integrity_hash(payload) if ok else None
    return ValidationResult(valid=ok, reasons=reasons, integrity_hash=integrity)
