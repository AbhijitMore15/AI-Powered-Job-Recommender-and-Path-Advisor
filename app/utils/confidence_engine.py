from typing import List, Dict


def calculate_confidence(
    career: Dict,
    user_skills: List[str]
) -> Dict:
    """
    Calculates how well user skills match career requirements.

    Returns a dict with:
    - fit_score (0–100)
    - confidence_level (Weak / Moderate / Strong Fit)
    - explanation
    - matched_skills
    - missing_skills
    - priority_skills
    """

    required_skills = career.get("required_skills", [])

    if not required_skills:
        return {
            "fit_score": 0,
            "confidence_level": "Unknown",
            "explanation": "No required skills defined for this career.",
            "matched_skills": [],
            "missing_skills": [],
            "priority_skills": []
        }

    user_set = {s.lower() for s in user_skills}
    required_set = {s.lower() for s in required_skills}

    matched = user_set.intersection(required_set)
    missing = required_set - matched

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
        f"Matched skills: {', '.join(sorted(matched)) if matched else 'None'}."
    )

    return {
        "fit_score": fit_score,
        "confidence_level": level,
        "explanation": explanation,
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
        "priority_skills": sorted(missing)[:3]
    }
