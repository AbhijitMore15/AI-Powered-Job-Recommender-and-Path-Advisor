from pydantic import BaseModel
from typing import List

class SkillGapItem(BaseModel):
    skill: str
    difficulty: str
    estimated_time: str

class RoadmapPhase(BaseModel):
    phase: str
    steps: List[str]

class RoadmapRequest(BaseModel):
    career: str
    current_skills: List[str]

class RoadmapResponse(BaseModel):
    career: str
    difficulty: str
    skill_gap: List[SkillGapItem]
    roadmap: List[RoadmapPhase]
