# app/models/confidence_models.py
from pydantic import BaseModel
from typing import List

class ConfidenceRequest(BaseModel):
    career: str
    user_skills: List[str]

class ConfidenceResponse(BaseModel):
    career: str
    fit_score: int
    confidence_level: str
    explanation: str
