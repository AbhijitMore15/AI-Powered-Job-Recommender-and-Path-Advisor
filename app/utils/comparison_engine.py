# app/utils/comparison_engine.py
from typing import Dict, List
from app.utils.ranking_engine import (
    compute_skill_match,
    compute_interest_match,
    compute_effort_score
)
from app.utils.confidence_engine import calculate_confidence


def compare_two_careers(
    career_a: Dict,
    career_b: Dict,
    user_skills: List[str],
    interest: str,
    effort: int
) -> Dict:

    def score(career: Dict) -> Dict:
        skill = compute_skill_match(career, user_skills)
        interest_score = compute_interest_match(career, interest)
        confidence = calculate_confidence(
            career_data=career,
            user_skills=user_skills
        )
        effort_score = compute_effort_score(career, effort)

        final = (
            0.4 * skill +
            0.25 * interest_score +
            0.25 * confidence["fit_score"] +
            0.1 * effort_score
        )

        return {
            "final": round(final, 2),
            "skill": round(skill, 2),
            "interest": round(interest_score, 2),
            "confidence": round(confidence["fit_score"], 2),
            "effort": round(effort_score, 2)
        }

    a = score(career_a)
    b = score(career_b)

    winner = career_a["career_name"] if a["final"] > b["final"] else career_b["career_name"]

    explanation = []
    if a["skill"] != b["skill"]:
        explanation.append("Skill match differs significantly.")
    if a["interest"] != b["interest"]:
        explanation.append("Interest alignment favors one career.")
    if a["confidence"] != b["confidence"]:
        explanation.append("Confidence / readiness level is different.")
    if a["effort"] != b["effort"]:
        explanation.append("Effort vs difficulty balance differs.")

    if not explanation:
        explanation.append("Both careers are similarly suitable.")

    return {
        "career_a": {
            "name": career_a["career_name"],
            "scores": a
        },
        "career_b": {
            "name": career_b["career_name"],
            "scores": b
        },
        "winner": winner,
        "why": explanation
    }
