def create_ai_roadmap(career, user_skills):
    required = set(career.get("required_skills", []))
    user = set(user_skills)

    # Identify missing skills
    missing = list(required - user)

    # Build skill gap list correctly
    skill_gap = [
        {
            "skill": s,
            "difficulty": "Medium",
            "estimated_time": "2–4 weeks"
        }
        for s in missing
    ]

    # Build roadmap list correctly (NOT nested)
    roadmap = [
        {
            "phase": "Beginner",
            "steps": [
                f"Learn the basics of {career['career_name']}",
                "Understand foundational concepts",
                "Start simple projects"
            ]
        },
        {
            "phase": "Intermediate",
            "steps": [
                f"Learn missing skills: {', '.join(missing)}" if missing else "You already have intermediate skills",
                "Build portfolio-level projects",
                "Take intermediate courses"
            ]
        },
        {
            "phase": "Advanced",
            "steps": [
                "Master advanced tools & frameworks",
                "Work on real-world projects",
                "Prepare for certifications",
                "Apply for internships / jobs"
            ]
        }
    ]

    return skill_gap, roadmap
