from pydantic import BaseModel
from typing import Optional, Dict, Any

class AdvisorRequest(BaseModel):
    interest: str
    skills: list[str]
    experience_level: str = "beginner"
    effort: int = 3

class AdvisorResponse(BaseModel):
    career: Optional[str]
    experience_level: str
    confidence: Optional[Dict[str, Any]]
    why_selected: str
    roadmap: Optional[Dict[str, Any]]
