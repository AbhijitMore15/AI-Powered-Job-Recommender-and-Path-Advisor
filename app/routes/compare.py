# app/routes/compare.py

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from app.data.loader import CAREERS
from app.utils.comparison_engine import compare_careers

router = APIRouter()


class CompareRequest(BaseModel):
    careers: List[str]
    user_skills: List[str]
    effort: int = 3


@router.post("/compare")
def compare_endpoint(payload: CompareRequest):
    return compare_careers(
        careers=CAREERS,
        career_names=payload.careers,
        user_skills=payload.user_skills,
        effort=payload.effort
    )
