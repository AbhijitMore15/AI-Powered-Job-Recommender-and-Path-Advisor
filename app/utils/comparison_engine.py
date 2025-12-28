from typing import List, Dict, Optional
from app.utils.confidence_engine import calculate_confidence


def find_career_by_name(careers: List[Dict], name: str) -> Optional[Dict]:
    """
    Find a career dict by name (case-insensitive).
    """
    name = name.lower()
    for career in careers:
        if career.get("career_name", "").lower() == name:
            return career
    return None


def compare_careers(
    careers: List[Dict],
    career_names: List[str],
    user_skills: List[str],
    effort: int = 3,
) -> Dict:
    """
    Compare multiple careers and recommend the best one
    based on confidence (skill match).
    """

    comparisons: List[Dict] = []

    for name in career_names:
        career = find_career_by_name(careers, name)
        if not career:
            continue

        # ✅ CORRECT call — positional, matches confidence_engine exactly
        confidence = calculate_confidence(career, user_skills)

        comparisons.append({
            "career": career["career_name"],
            "fit_score": confidence["fit_score"],
            "confidence_level": confidence["confidence_level"],
            "confidence_explanation": confidence["explanation"],
            "matched_skills": confidence["matched_skills"],
            "missing_skills": confidence["missing_skills"],
            "priority_skills": confidence["priority_skills"],
            "summary": (
                f"{career['career_name']} has a "
                f"{confidence['confidence_level']} based on your current skills."
            )
        })

    if not comparisons:
        return {
            "comparison": [],
            "recommended": None,
            "why_selected": "No valid careers were found for comparison."
        }

    best = max(comparisons, key=lambda x: x["fit_score"])

    return {
        "comparison": comparisons,
        "recommended": best["career"],
        "why_selected": (
            f"{best['career']} is recommended due to the highest "
            f"fit score ({best['fit_score']})."
        )
    }
