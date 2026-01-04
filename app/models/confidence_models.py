# app/models/confidence_models.py

from pydantic import BaseModel, Field
from typing import List, Optional


class ConfidenceRequest(BaseModel):
    career: str
    user_skills: List[str]

    # optional (future use / compatibility)
    interests: Optional[List[str]] = Field(
        default=None,
        alias="interest"
    )

    class Config:
        populate_by_name = True


class ConfidenceResponse(BaseModel):
    career: str
    fit_score: int
    confidence_level: str
    explanation: str
    matched_skills: List[str]
    missing_skills: List[str]
