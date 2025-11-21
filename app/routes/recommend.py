from fastapi import APIRouter
from app.models.recommend_models import RecommendRequest, RecommendResponse

router = APIRouter()

@router.post("/", response_model=RecommendResponse)
def recommend_career(payload: RecommendRequest):
    if payload.interest == "data":
        career = "Data Scientist"
    elif payload.interest == "software":
        career = "Software Developer"
    else:
        career = "IT Generalist"

    return {"career": career, "confidence": 0.8}
