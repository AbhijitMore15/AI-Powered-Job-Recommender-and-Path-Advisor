from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.data_loader import load_careers_json
from app.utils.similarity_engine import train_similarity, get_similar_careers

router = APIRouter()
CAREERS = load_careers_json()

# Train similarity once on startup
train_similarity(CAREERS)

class SimilarRequest(BaseModel):
    career_name: str
    top_n: int = 5

@router.post("/")
def similar_careers(payload: SimilarRequest):
    results = get_similar_careers(payload.career_name, payload.top_n)

    if not results:
        raise HTTPException(status_code=404, detail="Career not found")

    return {
        "career": payload.career_name,
        "similar_careers": results
    }
