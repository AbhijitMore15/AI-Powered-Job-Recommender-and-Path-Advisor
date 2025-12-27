from fastapi import APIRouter, HTTPException
from app.utils.data_loader import load_careers_json
from app.ml.similarity import (
    build_tfidf_matrix,
    compute_similarity_matrix,
    get_similar_careers
)

# ✅ MUST be named exactly "router"
router = APIRouter()

CAREERS = load_careers_json()

# Build ML artifacts ONCE
TFIDF_MATRIX, _ = build_tfidf_matrix(CAREERS)
SIMILARITY_MATRIX = compute_similarity_matrix(TFIDF_MATRIX)


def find_career_index(name: str):
    name = name.lower().strip()
    for i, c in enumerate(CAREERS):
        if c.get("career_name", "").lower().strip() == name:
            return i
    return None


@router.get("/similar/{career_name}")
def similar_careers(career_name: str, top_k: int = 5):
    idx = find_career_index(career_name)

    if idx is None:
        raise HTTPException(status_code=404, detail="Career not found")

    results = get_similar_careers(
        career_index=idx,
        careers=CAREERS,
        similarity_matrix=SIMILARITY_MATRIX,
        top_k=top_k
    )

    return {
        "career": CAREERS[idx]["career_name"],
        "similar_careers": results
    }
