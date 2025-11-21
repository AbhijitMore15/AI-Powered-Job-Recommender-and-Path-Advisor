from pydantic import BaseModel
from typing import List

class RoadmapRequest(BaseModel):
    career: str

class RoadmapResponse(BaseModel):
    career: str
    steps: List[str]
