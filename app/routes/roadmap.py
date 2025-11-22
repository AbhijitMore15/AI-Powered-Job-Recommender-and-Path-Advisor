from fastapi import APIRouter, HTTPException
from app.models.roadmap_models import RoadmapRequest, RoadmapResponse
from app.utils.data_loader import load_careers_json
from app.utils.skill_gap_engine import skill_gap_analysis
from app.utils.roadmap_engine import create_ai_roadmap

router = APIRouter()
CAREERS = load_careers_json()

@router.post("/", response_model=RoadmapResponse)
def generate_roadmap(payload: RoadmapRequest):
    career_name = payload.career.lower()

    # Find the career in the dataset
    selected = None
    for c in CAREERS:
        if c["career_name"].lower() == career_name:
            selected = c
            break

    if not selected:
        raise HTTPException(status_code=404, detail="Career not found")

    # Extract required skills
    required_skills = selected.get("required_skills", [])

    # Skill gap analysis
    skill_gap = skill_gap_analysis(payload.current_skills, required_skills)

    # Roadmap (unpack the tuple)
    _, roadmap = create_ai_roadmap(selected, payload.current_skills)

    return {
        "career": selected["career_name"],
        "difficulty": selected.get("difficulty_level", "Medium"),
        "skill_gap": skill_gap,
        "roadmap": roadmap
    }
