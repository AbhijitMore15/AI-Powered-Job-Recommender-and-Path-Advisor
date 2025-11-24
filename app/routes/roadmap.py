from fastapi import APIRouter, HTTPException
from app.models.roadmap_models import RoadmapRequest, RoadmapResponse
from app.utils.data_loader import load_careers_json
from app.utils.skill_gap_engine import skill_gap_analysis
from app.utils.roadmap_engine import create_ai_roadmap

router = APIRouter()
CAREERS = load_careers_json()

@router.post("/", response_model=RoadmapResponse)
def generate_roadmap(payload: RoadmapRequest):

    name = payload.career.lower()
    selected = None

    for c in CAREERS:
        if c["career_name"].lower() == name:
            selected = c
            break

    if not selected:
        raise HTTPException(status_code=404, detail="Career not found")

    skill_gap = skill_gap_analysis(payload.current_skills, selected.get("required_skills", []))

    roadmap = create_ai_roadmap(
        selected,
        payload.current_skills,
        payload.effort
    )

    explanation = (
        f"AI generated this roadmap based on your current skills and effort level {payload.effort}. "
        f"Higher effort reduces timeline and accelerates learning."
    )

    return {
        "career": selected["career_name"],
        "difficulty": selected.get("difficulty_level", "Medium"),
        "skill_gap": skill_gap,
        "roadmap": roadmap,
        "explanation": explanation
    }
