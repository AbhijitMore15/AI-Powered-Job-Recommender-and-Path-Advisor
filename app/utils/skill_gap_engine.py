import json
import os

# LOAD SKILL DIFFICULTY MAP
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "skill_difficulty.json")

if os.path.exists(DATA_PATH):
    with open(DATA_PATH, "r") as f:
        SKILL_MAP = json.load(f)
else:
    SKILL_MAP = {}


def get_skill_difficulty(skill: str):
    return SKILL_MAP.get(skill, "Medium")


def estimate_learning_time(difficulty: str):
    if difficulty == "Easy":
        return "1–2 weeks"
    elif difficulty == "Medium":
        return "3–6 weeks"
    else:
        return "2–3 months"


def skill_gap_analysis(user_skills, required_skills):
    missing = [s for s in required_skills if s not in user_skills]

    analyzed = []
    for skill in missing:
        difficulty = get_skill_difficulty(skill)
        time_needed = estimate_learning_time(difficulty)

        analyzed.append({
            "skill": skill,
            "difficulty": difficulty,
            "estimated_time": time_needed
        })

    return analyzed
