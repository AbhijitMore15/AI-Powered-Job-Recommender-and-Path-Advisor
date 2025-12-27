from fastapi import APIRouter, HTTPException
from app.utils.graph_engine import build_career_graph

router = APIRouter()

@router.get("/{career_name}")
def career_graph(career_name: str, top_k: int = 5):
    graph = build_career_graph(career_name, top_k)

    if not graph["nodes"]:
        raise HTTPException(status_code=404, detail="Career not found")

    return graph
