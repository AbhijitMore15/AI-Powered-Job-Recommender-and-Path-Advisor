from fastapi import APIRouter, HTTPException
from app.models.user_models import ProfileCreateRequest, ProfileUpdateRequest, RecommendPersonalRequest, PredictRequest, PersonalRecommendResponse, PredictResponse
from app.utils.user_store import create_or_get_profile, update_profile, get_profile, append_history
from app.utils.personal_matcher import build_personalized_recommendations
from app.utils.comparison import find_career_by_name
from typing import Dict

router = APIRouter()

@router.post("/create", summary="Create or get profile")
def create_profile(payload: ProfileCreateRequest):
    prof = create_or_get_profile(payload.user_id, base={"user_id": payload.user_id, "name": payload.name, "email": payload.email})
    return prof

@router.get("/{user_id}", summary="Get user profile")
def read_profile(user_id: str):
    prof = get_profile(user_id)
    if not prof:
        raise HTTPException(status_code=404, detail="Profile not found")
    return prof

@router.patch("/{user_id}", summary="Update profile")
def patch_profile(user_id: str, payload: ProfileUpdateRequest):
    try:
        updated = update_profile(user_id, payload.dict())
    except KeyError:
        raise HTTPException(status_code=404, detail="Profile not found")
    return updated

@router.post("/recommend", summary="Personalized recommendations")
def personal_recommend(payload: RecommendPersonalRequest):
    prof = get_profile(payload.user_id)
    if not prof:
        raise HTTPException(status_code=404, detail="Profile not found")
    recs = build_personalized_recommendations(prof, top_n=payload.top_n)
    # log action
    append_history(payload.user_id, {"action":"recommend", "top_n": payload.top_n})
    return {"user_id": payload.user_id, "recommendations": recs, "used_profile": prof}

@router.post("/predict", summary="Predict career path", response_model=PredictResponse)
def predict_path(payload: PredictRequest):
    prof = get_profile(payload.user_id)
    if not prof:
        raise HTTPException(status_code=404, detail="Profile not found")
    # Very simple predictor: top 3 recommended careers -> soft probabilities
    recs = build_personalized_recommendations(prof, top_n=5)
    # convert scores to probabilities
    raw_scores = [r["score"] for r in recs]
    ssum = sum(raw_scores) or 1.0
    preds = []
    for r in recs[:3]:
        prob = round((r["score"] / ssum) * 1.0, 3) if ssum else 0.0
        preds.append({"career": r["career"], "probability": prob, "rationale": r["explanation"]})
    append_history(payload.user_id, {"action":"predict", "horizon_months": payload.horizon_months})
    return {"user_id": payload.user_id, "predictions": preds}
