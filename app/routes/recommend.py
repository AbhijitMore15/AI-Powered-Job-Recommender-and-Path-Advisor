from fastapi import APIRouter
from app.models.recommend_models import RecommendRequest, RecommendResponse
from app.utils.data_loader import load_careers_json
from app.utils.ml_engine import ml_match
from app.utils.memory_engine import remember_new_career
import difflib

router = APIRouter()
CAREERS = load_careers_json()

# -----------------------------
# Synonym mapper
# -----------------------------
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

# -----------------------------
# Normalize interests
# -----------------------------
def normalize_interests(interests):
    if not interests:
        return ""

    normalized = []
    for i in interests:
        if isinstance(i, str):
            normalized.append(SYNONYMS.get(i.lower(), i.lower()))

    return " ".join(normalized)

# -----------------------------
# Fuzzy matcher
# -----------------------------
def fuzzy(a, b):
    return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()

# -----------------------------
# Recommendation endpoint (TOP-3)
# -----------------------------
@router.post("/", response_model=RecommendResponse)
def recommend_career(payload: RecommendRequest):
    """
    Assessment-aware career recommendation.
    EXTENSION: returns top 3 careers instead of 1.
    """

    # 1️⃣ Normalize interests
    q = normalize_interests(payload.interests)

    # 2️⃣ ML base score (query-level)
    ml_score, _ = ml_match(q)

    ranked_results = []

    # 3️⃣ Score EVERY career (do NOT remove fuzzy logic)
    for c in CAREERS:
        fuzzy_score = fuzzy(q, c["career_name"])

        # choose better of ML vs fuzzy for this career
        base_score = max(ml_score, fuzzy_score)

        # assessment-aware confidence
        assessment_score = payload.score if payload.score is not None else 0.6
        final_confidence = round(
            min(0.95, max(0.4, base_score * 0.7 + assessment_score * 0.3)),
            3,
        )

        ranked_results.append({
            "career": c["career_name"],
            "confidence": final_confidence,
            "skills": c.get("required_skills", []),
            "description": c.get("career_description", ""),
        })

    # 4️⃣ Sort by confidence
    ranked_results.sort(key=lambda x: x["confidence"], reverse=True)

    # 5️⃣ If nothing meaningful matched → memory
    if ranked_results[0]["confidence"] < 0.25:
        remember_new_career(q, payload.interests)
        return {
            "results": [],
            "note": "No strong match found. Saved to memory for future learning.",
        }

    # 6️⃣ Return TOP-3
    return {
        "results": ranked_results[:3]
    }
