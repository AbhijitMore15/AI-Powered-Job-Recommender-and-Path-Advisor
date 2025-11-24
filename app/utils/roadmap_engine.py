def create_ai_roadmap(career, user_skills, effort=3):
    phases = []

    speed = {
        1: 0.5,   # very slow
        2: 0.75,  # slow
        3: 1,     # normal
        4: 1.5,   # fast
        5: 2      # very fast
    }.get(effort, 1)

    # Estimate timeline
    def duration(base_months):
        adjusted = base_months / speed
        return f"{round(adjusted,1)} months"

    # Phase 1 — Beginner
    phases.append({
        "phase": "Beginner",
        "steps": [
            f"Learn the basics of {career['career_name']}",
            "Understand foundational concepts",
            "Start simple guided projects"
        ],
        "duration": duration(1.5)
    })

    # Phase 2 — Intermediate
    phases.append({
        "phase": "Intermediate",
        "steps": [
            f"Study missing skills deeply",
            "Build portfolio-level projects",
            "Follow intermediate structured courses"
        ],
        "duration": duration(2.5)
    })

    # Phase 3 — Advanced
    phases.append({
        "phase": "Advanced",
        "steps": [
            "Work on real-world projects",
            "Master advanced tools & frameworks",
            "Prepare for certification",
            "Apply for internships / jobs"
        ],
        "duration": duration(3)
    })

    return phases
