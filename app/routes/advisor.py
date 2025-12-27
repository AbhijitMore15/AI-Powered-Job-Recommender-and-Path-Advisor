# app/routes/advisor.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
from app.utils.advisor_engine import ai_advisor

router = APIRouter()

class AdvisorRequest(BaseModel):
    interest: str
    skills: list[str]
    experience_level: str = "beginner"
    effort: int = 3
    compare: Optional[bool] = False


@router.post("/")
def advisor_endpoint(payload: AdvisorRequest):
    return ai_advisor(
        interest=payload.interest,
        skills=payload.skills,
        effort=payload.effort,
        compare=payload.compare
    )
