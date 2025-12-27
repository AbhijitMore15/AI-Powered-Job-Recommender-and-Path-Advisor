# app/utils/advisor_engine.py
from typing import List, Dict
from app.utils.data_loader import load_careers_json
from app.utils.ranking_engine import rank_careers
from app.utils.confidence_engine import calculate_confidence
from app.utils.roadmap_engine import create_full_roadmap

# Load dataset ONCE
CAREERS = load_careers_json()


def ai_advisor(
    interest: str,
    skills: List[str],
    experience_level: str = "beginner",
    effort: int = 3,
    compare: bool = False
) -> Dict:
    """
    Main advisor brain.
    """

    # Rank careers based on interest + skills
    ranked = rank_careers(
        careers=CAREERS,
        interest=interest,
        user_skills=skills,
        effort=effort
    )

    if not ranked:
        return {
            "career": None,
            "why_selected": "No suitable career found for the given interest."
        }

    # Pick top career
    selected = ranked[0]

    # Confidence score
    confidence = calculate_confidence(
        career=selected,
        user_skills=skills
    )

    # Full AI roadmap (Day 12+)
    roadmap = create_full_roadmap(
        career=selected,
        user_skills=skills,
        effort=effort
    )

    response = {
        "career": selected["career_name"],
        "experience_level": experience_level,
        "why_selected": (
            f"Selected based on your interest in {interest} "
            f"and alignment with required skills."
        ),
        "confidence": confidence,
        "roadmap": roadmap
    }

    # Optional comparison (Day 13 feature)
    if compare and len(ranked) > 1:
        response["comparison"] = [
            {
                "career": c["career_name"],
                "confidence": calculate_confidence(c, skills)
            }
            for c in ranked[1:3]
        ]

    return response
