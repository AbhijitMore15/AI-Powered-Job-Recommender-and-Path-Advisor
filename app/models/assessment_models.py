from pydantic import BaseModel
from typing import List, Optional


class AssessmentSubmitRequest(BaseModel):
    selected_interests: List[str]
    selected_skills: List[str]
    confidence: Optional[float] = 0.7


class AssessmentScore(BaseModel):
    interest_match: float
    skill_match: float
    overall_match: float


class AssessmentResponse(BaseModel):
    score: AssessmentScore
    recommendations: dict
