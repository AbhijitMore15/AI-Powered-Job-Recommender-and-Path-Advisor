from typing import Dict, List

from app.utils.confidence_engine import calculate_confidence
from app.utils.explainability_engine import generate_explanation
from app.utils.roadmap_engine import create_full_roadmap
from app.utils.data_loader import CAREERS


def ai_advisor(
    interest: str,
    skills: List[str],
    effort: int,
    compare: bool = False
) -> Dict:

    interest = interest.lower()

    filtered = [
        c for c in CAREERS
        if interest in " ".join(c.get("keywords", [])).lower()
    ]

    if not filtered:
        return {
            "detail": "No suitable career found for the given interest."
        }

    scored = []

    for career in filtered:
        confidence = calculate_confidence(
            career=career,
            user_skills=skills
        )

        scored.append({
            "career": career,
            "confidence": confidence
        })

    scored.sort(
        key=lambda x: x["confidence"]["fit_score"],
        reverse=True
    )

    selected = scored[0]["career"]
    confidence = scored[0]["confidence"]

    roadmap = create_full_roadmap(
        career=selected,
        user_skills=skills,
        effort=effort
    )

    explanation = generate_explanation(
        career_data=selected,
        confidence=confidence,
        interest=interest,
        effort=effort
    )

    return {
        "career": selected["career_name"],
        "confidence": confidence,
        "explanation": explanation,
        "roadmap": roadmap
    }
