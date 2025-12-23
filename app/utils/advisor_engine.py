# app/utils/advisor_engine.py

from typing import List
from app.utils.data_loader import load_careers_json
from app.utils.confidence_engine import calculate_confidence
from app.utils.roadmap_engine import create_full_roadmap

# ✅ LOAD DATASET ONCE
CAREERS = load_careers_json()


def ai_advisor(
    interest: str,
    skills: List[str],
    experience_level: str = "beginner",
    effort: int = 3
):
    interest = interest.lower().strip()
    skills = skills or []

    selected = None

    # 🔍 Find matching career
    for career in CAREERS:
        interests = [i.lower() for i in career.get("interests", [])]
        tags = [t.lower() for t in career.get("tags", [])]
        keywords = [k.lower() for k in career.get("keywords", [])]

        if (
            interest in interests
            or interest in tags
            or interest in keywords
        ):
            selected = career
            break

    if not selected:
        return {
            "career": None,
            "experience_level": experience_level,
            "confidence": None,
            "why_selected": "No suitable career found for the given interest.",
            "roadmap": None
        }

    # 📊 Confidence score
    confidence = calculate_confidence(
        required_skills=selected.get("required_skills", []),
        user_skills=skills
    )

    # ⚙ Adjust effort by experience level
    if experience_level == "beginner":
        effort = max(1, effort - 1)
    elif experience_level == "advanced":
        effort = min(5, effort + 1)

    # 🗺 Roadmap
    roadmap = create_full_roadmap(
        career=selected,
        user_skills=skills,
        effort=effort
    )

    why_selected = (
        f"This career was selected because your interest '{interest}' "
        f"matches its domain and aligns with the skill requirements of "
        f"{selected['career_name']}."
    )

    return {
        "career": selected["career_name"],
        "experience_level": experience_level,
        "confidence": confidence,
        "why_selected": why_selected,
        "roadmap": roadmap
    }
