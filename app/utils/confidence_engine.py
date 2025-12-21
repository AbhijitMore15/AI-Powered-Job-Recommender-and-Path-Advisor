from typing import List, Dict

def calculate_confidence(required_skills: List[str], user_skills: List[str]) -> Dict:
    if not required_skills:
        return {
            "fit_score": 0,
            "confidence_level": "Unknown",
            "explanation": "No required skills defined for this career."
        }

    required = set(s.lower() for s in required_skills)
    user = set(s.lower() for s in user_skills)

    matched = len(required & user)
    score = int((matched / len(required)) * 100)

    if score >= 70:
        level = "Strong Fit"
    elif score >= 40:
        level = "Moderate Fit"
    else:
        level = "Weak Fit"

    return {
        "fit_score": score,
        "confidence_level": level,
        "explanation": f"You match {matched} out of {len(required)} core skills."
    }
