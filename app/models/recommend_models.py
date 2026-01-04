from pydantic import BaseModel
from typing import List, Optional


class CareerResult(BaseModel):
    career: str
    confidence: float
    skills: List[str]
    description: str


class RecommendRequest(BaseModel):
    score: Optional[float] = 0.6
    category: Optional[str] = None
    interests: List[str]
    skills: Optional[List[str]] = []


class RecommendResponse(BaseModel):
    results: List[CareerResult]
