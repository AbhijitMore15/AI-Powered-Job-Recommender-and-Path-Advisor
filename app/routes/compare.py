# app/routes/compare.py
from fastapi import APIRouter, HTTPException
from app.models.compare_models import CompareRequest, CompareResponse, CareerSummary, ComparisonEntry
from app.utils.comparison import compare_careers

router = APIRouter()

@router.post("/", response_model=CompareResponse)
def compare(payload: CompareRequest):
    res = compare_careers(payload.career_1, payload.career_2, payload.prefer)
    if res.get("error"):
        raise HTTPException(status_code=404, detail="One or both careers not found in dataset")
    c1 = res["career_1"]
    c2 = res["career_2"]
    comp = res["comparison"]

    return {
        "career_1": c1,
        "career_2": c2,
        "comparison": comp
    }
