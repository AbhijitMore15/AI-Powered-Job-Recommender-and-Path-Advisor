from pydantic import BaseModel
from typing import List

class RecommendRequest(BaseModel):
    interest: str

class ExtraSuggestion(BaseModel):
    career: str
    confidence: float

class RecommendResponse(BaseModel):
    career: str
    confidence: float
    skills: List[str] = []
    description: str = ""
    extra: List[ExtraSuggestion] = []
