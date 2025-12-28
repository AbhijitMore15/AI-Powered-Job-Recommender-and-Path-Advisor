# app/routes/advisor.py

from fastapi import APIRouter
from app.models.advisor_models import AdvisorRequest
from app.utils.advisor_engine import ai_advisor

router = APIRouter(prefix="/advisor", tags=["Advisor"])


@router.post("/")
def advisor_endpoint(payload: AdvisorRequest):
    return ai_advisor(
        interest=payload.interest,
        skills=payload.skills,
        effort=payload.effort,
        compare=payload.compare
    )
