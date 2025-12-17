# app/utils/confidence_engine.py
from typing import List, Dict

def calculate_fit_score(
    career: Dict,
    user_skills: List[str],
    user_interest: str = ""
):
    # --- Skill match ---
    required = career.get("required_skills", [])
    if required:
        matched = [s for s in required if any(us.lower() in s.lower() for us in user_skills)]
        skill_score = (len(matched) / len(required)) * 50
    else:
        skill_score = 20  # neutral fallback

    # --- Interest relevance ---
    interest_text = (
        career.get("career_name", "") +
        career.get("category", "") +
        career.get("sub_category", "")
    ).lower()

    interest_score = 30 if user_interest and user_interest.lower() in interest_text else 10

    # --- Difficulty adjustment ---
    difficulty = career.get("difficulty_level", "Medium")
    difficulty_score = {
        "Easy": 20,
        "Medium": 15,
        "Hard": 10
    }.get(difficulty, 12)

    total_score = min(int(skill_score + interest_score + difficulty_score), 100)

    # Confidence label
    if total_score >= 75:
        level = "High"
    elif total_score >= 50:
        level = "Medium"
    else:
        level = "Low"

    explanation = (
        f"Skill match contributed {int(skill_score)}%, "
        f"interest alignment contributed {interest_score}%, "
        f"and difficulty adjustment contributed {difficulty_score}%."
    )

    return {
        "fit_score": total_score,
        "confidence_level": level,
        "explanation": explanation
    }
def calculate_confidence(user_skills: list, required_skills: list):
    if not required_skills:
        return 0, "Unknown Fit", "No skill data available for this career."

    matched = [
        s for s in required_skills
        if any(us.lower() in s.lower() or s.lower() in us.lower() for us in user_skills)
    ]

    score = int((len(matched) / len(required_skills)) * 100)

    if score >= 80:
        level = "Strong Fit"
    elif score >= 60:
        level = "Good Fit"
    elif score >= 40:
        level = "Moderate Fit"
    else:
        level = "Weak Fit"

    explanation = (
        f"You already have {', '.join(matched)}, which are important for this career."
        if matched else
        "You currently lack most of the core skills required for this career."
    )

    return score, level, explanation
