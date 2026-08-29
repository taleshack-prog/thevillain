"""Endpoint de calculo de pontuacao (motor GDD 3.4). Util para simulacao/calibracao."""
from fastapi import APIRouter, HTTPException

from app.api.schemas import ScoreRequest, ScoreResponse
from app.engine.scoring import calculate_final_score

router = APIRouter(prefix="/scoring", tags=["scoring"])


@router.post("/preview", response_model=ScoreResponse)
async def preview_score(req: ScoreRequest) -> ScoreResponse:
    try:
        result = calculate_final_score(
            difficulty=req.difficulty,
            time_spent=req.time_spent,
            clue_tiers_used=req.clue_tiers_used,
        )
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return ScoreResponse(**{k: result[k] for k in ScoreResponse.model_fields})
