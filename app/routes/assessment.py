from fastapi import APIRouter
from app.utils.data_loader import load_careers_json
from app.models.assessment_models import AssessmentSubmitRequest, AssessmentResponse
from app.models.recommend_models import RecommendRequest
from app.routes.recommend import recommend_career

router = APIRouter()
CAREERS = load_careers_json()


def calculate_match(user_items, career_items):
    if not user_items:
        return 0.0
    matched = len(set(user_items) & set(map(str.lower, career_items)))
    return round(matched / len(user_items), 2)


@router.post("/submit", response_model=AssessmentResponse)
def submit_assessment(payload: AssessmentSubmitRequest):
    interest_scores = []
    skill_scores = []

    for c in CAREERS:
        interest_scores.append(
            calculate_match(
                [i.lower() for i in payload.selected_interests],
                c.get("interests", [])
            )
        )
        skill_scores.append(
            calculate_match(
                [s.lower() for s in payload.selected_skills],
                c.get("required_skills", []) + c.get("optional_skills", [])
            )
        )

    interest_match = max(interest_scores)
    skill_match = max(skill_scores)

    overall_match = round(
        interest_match * 0.5 + skill_match * 0.5, 2
    )

    # 🔥 USE EXISTING RECOMMENDER
    recommend_payload = RecommendRequest(
        interests=payload.selected_interests,
        skills=payload.selected_skills,
        score=overall_match
    )

    recommendations = recommend_career(recommend_payload)

    return {
        "score": {
            "interest_match": interest_match,
            "skill_match": skill_match,
            "overall_match": overall_match
        },
        "recommendations": recommendations
    }
