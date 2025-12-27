from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.clustering_engine import train_clusters, get_cluster_for_career

router = APIRouter()

# Train once at startup
train_clusters(n_clusters=10)

class ClusterRequest(BaseModel):
    career_name: str

@router.post("/")
def career_cluster(payload: ClusterRequest):
    result = get_cluster_for_career(payload.career_name)

    if not result:
        raise HTTPException(status_code=404, detail="Career not found in clusters")

    return {
        "career": payload.career_name,
        "cluster_id": result["cluster_id"],
        "cluster_careers": result["careers"]
    }
