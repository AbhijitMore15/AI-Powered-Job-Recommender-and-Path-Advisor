from fastapi import APIRouter
from app.models.recommend_models import RecommendRequest, RecommendResponse
from app.utils.data_loader import load_careers_json
from app.utils.ml_engine import ml_match
from app.utils.memory_engine import remember_new_career
import difflib

router = APIRouter()

CAREERS = load_careers_json()

# Synonym mapper
SYNONYMS = {
    "bio": "biology",
    "biotech": "biotechnology",
    "medical": "medicine",
    "doctor": "medicine",
    "cs": "computer science",
    "it": "information technology",
    "ai": "artificial intelligence",
    "ml": "machine learning",
    "ds": "data science",
    "commerce": "finance",
    "business": "management",
}

def normalize(i: str):
    return SYNONYMS.get(i.lower(), i.lower())

def fuzzy(a, b):
    return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()

@router.post("/", response_model=RecommendResponse)
def recommend_career(payload: RecommendRequest):

    q = normalize(payload.interest)

    # ML score
    ml_score, ml_best = ml_match(q)

    # Fuzzy score fallback
    best_fuzzy_score = 0
    best_fuzzy = None
    for c in CAREERS:
        score = fuzzy(q, c["career_name"])
        if score > best_fuzzy_score:
            best_fuzzy_score = score
            best_fuzzy = c

    # Combine scores
    if ml_score >= best_fuzzy_score:
        best = ml_best
        score = ml_score
    else:
        best = best_fuzzy
        score = best_fuzzy_score

    # If still too low → store in memory
    if score < 0.25:
        remember_new_career(q, payload.interest)
        return {
            "career": f"No strong match found for '{payload.interest}'",
            "confidence": 0.0,
            "skills": [],
            "description": "Saved to memory for future learning.",
            "extra": []
        }

    return {
        "career": best["career_name"],
        "confidence": round(float(score), 3),
        "skills": best.get("required_skills", []),
        "description": best.get("career_description", ""),
        "extra": []
    }
