from typing import List, Dict, Tuple

from app.utils.priority import compute_priority_scores
from app.utils.courses import recommend_courses_for_skills
from app.utils.projects import generate_projects


def build_timeline_phases(
    prioritized_skills: List[Tuple[str, float]],
    effort: int = 3
):
    """
    Build 3, 6, and 12 month roadmap timelines.
    effort: 1–5 (higher = faster pace)
    """

    speed_map = {1: 0.6, 2: 0.8, 3: 1.0, 4: 1.4, 5: 1.8}
    speed = speed_map.get(effort, 1.0)

    top_skills = [s for s, _ in prioritized_skills[:6]]

    # --------------------
    # 3 MONTH ROADMAP
    # --------------------
    three_months = []

    if top_skills:
        three_months.append(f"Week 1–2: Learn fundamentals of {top_skills[0]}")
        three_months.append(f"Week 3–4: Build a mini project using {top_skills[0]}")

    if len(top_skills) > 1:
        three_months.append(f"Month 2: Learn {top_skills[1]} and integrate it")

    if len(top_skills) > 2:
        three_months.append(f"Month 3: Add {top_skills[2]} and finalize a basic system")


    # --------------------
    # 6 MONTH ROADMAP
    # --------------------
    six_months = []

    if top_skills:
        six_months.append(f"Month 1: Deep dive into {top_skills[0]} with hands-on practice")

    if len(top_skills) > 1:
        six_months.append(f"Month 2: Learn {top_skills[1]} and extend the project")

    if len(top_skills) > 2:
        six_months.append(f"Month 3: Implement {top_skills[2]} and improve system quality")

    if len(top_skills) > 3:
        six_months.append(f"Month 4: Learn {top_skills[3]} and optimize performance or design")

    if len(top_skills) > 4:
        six_months.append(f"Month 5: Add {top_skills[4]} and build an intermediate project")

    six_months.append(
        "Month 6: Testing, documentation, deployment, and portfolio refinement"
    )


    # --------------------
    # 12 MONTH ROADMAP
    # --------------------
    twelve_months = []

    if top_skills:
        twelve_months.append(f"Months 1–2: Build strong fundamentals in {top_skills[0]}")

    if len(top_skills) > 1:
        twelve_months.append(f"Months 3–4: Master {top_skills[1]} with real-world use cases")

    if len(top_skills) > 2:
        twelve_months.append(f"Months 5–6: Apply {top_skills[2]} in a scalable project")

    if len(top_skills) > 3:
        twelve_months.append(f"Months 7–8: Learn advanced concepts of {top_skills[3]}")

    if len(top_skills) > 4:
        twelve_months.append(
            f"Months 9–10: Integrate {top_skills[4]} into a production-level system"
        )

    twelve_months.append(
        "Months 11–12: System optimization, interview prep, mock interviews, and job applications"
    )


    def tag(plan):
        return [f"{step} (pace x{speed})" for step in plan]

    return tag(three_months), tag(six_months), tag(twelve_months)


def generate_roadmap(
    career: Dict,
    user_skills: List[str],
    effort: int = 3
) -> Dict:
    """
    Core roadmap generator.
    """

    user_skills_lower = [s.lower() for s in user_skills]

    scores: Dict[str, float] = compute_priority_scores(
        career=career,
        user_skills=user_skills
    )

    prioritized = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    missing_skills = [
        s for s in career.get("required_skills", [])
        if s.lower() not in user_skills_lower
    ]

    skill_gap = []

    for skill in missing_skills:
        sl = skill.lower()
        score = scores.get(sl, 0.0)

        difficulty = "Medium"
        est_time = "3–6 weeks"

        if any(k in sl for k in ["kubernetes", "microservices", "c++"]):
            difficulty = "Hard"
            est_time = "2–3 months"
        elif any(k in sl for k in ["git", "sql", "excel"]):
            difficulty = "Easy"
            est_time = "1–2 weeks"

        if score >= 70:
            priority = "High"
        elif score >= 40:
            priority = "Medium"
        else:
            priority = "Low"

        skill_gap.append({
            "skill": skill,
            "difficulty": difficulty,
            "estimated_time": est_time,
            "priority": priority,
            "priority_score": round(score, 2)
        })

    courses = recommend_courses_for_skills(
        [s for s, _ in prioritized[:6]],
        max_per_skill=1
    )

    projects = generate_projects(
        career=career,
        missing_skills=missing_skills
    )

    three, six, twelve = build_timeline_phases(
        prioritized_skills=prioritized,
        effort=effort
    )

    return {
        "skill_gap": skill_gap,
        "priority_scores": scores,
        "courses": courses,
        "projects": projects,
        "timeline": {
            "three_months": three,
            "six_months": six,
            "twelve_months": twelve
        },
        "explanation": (
            f"Roadmap generated using {len(prioritized)} scored skills. "
            f"Effort level {effort} adjusted learning pace."
        )
    }


# ✅ WRAPPER FOR API & ADVISOR
def create_full_roadmap(
    career: Dict,
    user_skills: List[str],
    effort: int = 3
) -> Dict:
    """
    Public-facing roadmap API.
    """
    return generate_roadmap(
        career=career,
        user_skills=user_skills,
        effort=effort
    )
