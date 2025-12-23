# app/routes/advisor.py
from fastapi import APIRouter, HTTPException
from app.models.advisor_models import AdvisorRequest, AdvisorResponse
from app.utils.advisor_engine import ai_advisor

router = APIRouter()

@router.post("/", response_model=AdvisorResponse)
def advisor_endpoint(payload: AdvisorRequest):
    try:
        return ai_advisor(
            interest=payload.interest,
            skills=payload.skills,
            experience_level=payload.experience_level,
            effort=payload.effort
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
