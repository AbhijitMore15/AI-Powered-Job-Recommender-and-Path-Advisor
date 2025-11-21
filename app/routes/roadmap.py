from fastapi import APIRouter
from app.models.roadmap_models import RoadmapRequest, RoadmapResponse

router = APIRouter()

@router.post("/", response_model=RoadmapResponse)
def generate_roadmap(payload: RoadmapRequest):
    roadmap = [
        "Learn basics",
        "Take online courses",
        "Build 3 projects",
        "Apply for internships",
    ]

    return RoadmapResponse(career=payload.career, steps=roadmap)
