from pydantic import BaseModel
from typing import List

class ConfidenceRequest(BaseModel):
    career_name: str
    user_skills: List[str]

class ConfidenceResponse(BaseModel):
    career: str
    fit_score: int
    confidence_level: str
    explanation: str
