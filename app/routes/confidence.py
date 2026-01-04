# app/routes/confidence.py

from fastapi import APIRouter, HTTPException
from app.models.confidence_models import (
    ConfidenceRequest,
    ConfidenceResponse
)
from app.utils.data_loader import load_careers_json
from app.utils.confidence_engine import calculate_confidence

router = APIRouter()
CAREERS = load_careers_json()


@router.post("/", response_model=ConfidenceResponse)
def confidence_check(payload: ConfidenceRequest):

    career = next(
        (
            c for c in CAREERS
            if c["career_name"].lower() == payload.career.lower()
        ),
        None
    )

    if not career:
        raise HTTPException(
            status_code=404,
            detail="Career not found"
        )

    required_skills = career.get("required_skills", [])

    result = calculate_confidence(
        payload.user_skills,
        required_skills
    )

    return {
        "career": career["career_name"],
        "fit_score": result["fit_score"],
        "confidence_level": result["confidence_level"],
        "explanation": result["confidence_explanation"],
        "matched_skills": result["matched_skills"],
        "missing_skills": result["missing_skills"]
    }
