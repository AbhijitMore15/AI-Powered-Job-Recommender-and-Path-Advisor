# app/models/confidence_models.py
from pydantic import BaseModel
from typing import List, Optional

class ConfidenceRequest(BaseModel):
    career_name: str
    user_skills: List[str]
    user_interest: Optional[str] = ""

class ConfidenceResponse(BaseModel):
    career: str
    fit_score: int
    confidence_level: str
    explanation: str
