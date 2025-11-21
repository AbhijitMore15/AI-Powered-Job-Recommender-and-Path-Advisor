from pydantic import BaseModel

class RecommendRequest(BaseModel):
    interest: str

class RecommendResponse(BaseModel):
    career: str
    confidence: float
