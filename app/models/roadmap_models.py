from pydantic import BaseModel
from typing import List, Optional

class RoadmapRequest(BaseModel):
    career: str
    current_skills: List[str]
    effort: Optional[int] = 3   # Optional effort level

class SkillGapItem(BaseModel):
    skill: str
    difficulty: str
    estimated_time: str

class RoadmapPhase(BaseModel):
    phase: str
    steps: List[str]
    duration: str  # NEW (AI generated duration)

class RoadmapResponse(BaseModel):
    career: str
    difficulty: str
    skill_gap: List[SkillGapItem]
    roadmap: List[RoadmapPhase]
    explanation: str   # NEW
