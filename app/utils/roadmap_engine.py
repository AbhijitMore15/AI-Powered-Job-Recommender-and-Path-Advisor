# app/utils/roadmap_engine.py
from typing import List, Dict, Tuple
from app.utils.priority import compute_priority_scores
from app.utils.courses import recommend_courses_for_skills
from app.utils.projects import generate_projects

def build_timeline_phases(prioritized_skills: List[Tuple[str,float]], effort:int=3):
    """
    Produce three timeline arrays (3m,6m,12m) as lists of strings (milestones).
    effort: 1..5 -> higher means faster (we'll compress time)
    """
    speed_map = {1:0.6, 2:0.8, 3:1.0, 4:1.4, 5:1.8}
    speed = speed_map.get(effort, 1.0)

    # Select top skills to cover quickly
    top_skills = [s for s,_ in prioritized_skills[:6]]

    # 3-month plan (fast): focus on top 3 skills and a small project
    three = [
        f"Week 1-2: Fundamentals of {top_skills[0] if len(top_skills)>0 else 'core skill'}",
        f"Week 3-4: Hands-on mini project using {top_skills[0]}",
    ]
    if len(top_skills) > 1:
        three.append(f"Month 2: Learn {top_skills[1]} and apply in project")
    if len(top_skills) > 2:
        three.append(f"Month 3: Learn {top_skills[2]} and integrate with project")

    # 6-month plan: expand to more skills and intermediate project
    six = [
        "Months 1-2: Complete core courses for top skills",
        "Months 3-4: Build an integrated project combining core skills",
        "Months 5-6: Deploy, test, add monitoring, finalize portfolio"
    ]

    # 12-month plan: mastery + advanced project + interviews
    twelve = [
        "Months 1-3: Deepen foundations and complete intermediate projects",
        "Months 4-6: Learn advanced topics and cloud deployment",
        "Months 7-9: Build production-like system (streaming/scale)",
        "Months 10-12: Polish portfolio, mock interviews and job prep"
    ]

    # apply speed to textual durations (we keep text but annotate acceleration)
    def tag(plan):
        return [f"{p} (speed factor: {speed})" for p in plan]

    return tag(three), tag(six), tag(twelve)

def create_full_roadmap(career: dict, user_skills: List[str], effort:int=3):
    # compute priorities
    scores = compute_priority_scores(career, user_skills)  # skill -> numeric

    # create sorted prioritized list (skill,score) descending
    prioritized = sorted(list(scores.items()), key=lambda x: x[1], reverse=True)

    # prepare skill_gap: missing skills from required
    missing = [s for s in career.get("required_skills", []) if s.lower() not in [u.lower() for u in user_skills]]

    # enrich skill gap with difficulty/time + priority and numeric score
    skill_gap = []
    for s in missing:
        score = scores.get(s.lower(), scores.get(s, 0.0))
        # choose simple difficulty heuristic
        difficulty = "Medium"
        est = "3–6 weeks"
        sl = s.lower()
        if "c++" in sl or "kubernetes" in sl or "microservices" in sl:
            difficulty = "Hard"; est = "2–3 months"
        elif "git" in sl or "sql" in sl:
            difficulty = "Easy"; est = "1–2 weeks"

        # map numeric to high/med/low
        prio_label = "Low"
        if score >= 70: prio_label = "High"
        elif score >= 40: prio_label = "Medium"

        skill_gap.append({
            "skill": s,
            "difficulty": difficulty,
            "estimated_time": est,
            "priority": prio_label,
            "priority_score": round(score,2)
        })

    # courses for top missing or top prioritized skills
    top_skill_names = [s for s,_ in prioritized][:6]
    courses = recommend_courses_for_skills(top_skill_names, max_per_skill=1)

    # projects
    projects = generate_projects(career, missing)

    # timeline
    three, six, twelve = build_timeline_phases(prioritized, effort)

    timeline = {
        "three_months": three,
        "six_months": six,
        "twelve_months": twelve
    }

    # priority_scores object (handy map)
    priority_scores = {k: v for k,v in scores.items()}

    explanation = (
        f"Generated roadmap using {len(prioritized)} scored skills. "
        f"Effort level {effort} was used to scale pace. Top skills: {', '.join([s for s,_ in prioritized[:3]])}."
    )

    return {
        "skill_gap": skill_gap,
        "priority_scores": priority_scores,
        "courses": courses,
        "projects": projects,
        "timeline": timeline,
        "explanation": explanation
    }
