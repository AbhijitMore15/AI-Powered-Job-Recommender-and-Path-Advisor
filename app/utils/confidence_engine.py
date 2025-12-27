# app/utils/confidence_engine.py
from typing import List, Tuple

def calculate_confidence(
    user_skills: List[str],
    required_skills: List[str]
) -> Tuple[int, str, str]:
    """
    Calculates how well user skills match career requirements.
    Returns:
    - fit_score (0–100)
    - confidence_level (Weak / Moderate / Strong Fit)
    - explanation (human-readable)
    """

    if not required_skills:
        return 0, "Unknown", "No required skills defined for this career."

    user_set = {s.lower() for s in user_skills}
    required_set = {s.lower() for s in required_skills}

    matched = user_set.intersection(required_set)
    match_count = len(matched)
    total = len(required_set)

    fit_score = int((match_count / total) * 100) if total > 0 else 0

    if fit_score >= 70:
        level = "Strong Fit"
    elif fit_score >= 40:
        level = "Moderate Fit"
    else:
        level = "Weak Fit"

    explanation = (
        f"You match {match_count} out of {total} core skills. "
        f"Matched skills: {', '.join(matched) if matched else 'None'}."
    )

    return fit_score, level, explanation
