from typing import Dict, List
from app.utils.similarity_engine import get_similar_careers
from app.utils.clustering_engine import get_cluster_for_career


def build_career_graph(
    career_name: str,
    top_k: int = 5
) -> Dict[str, List[dict]]:
    """
    Build graph nodes + edges for a career
    """

    nodes = []
    edges = []

    # root node
    root_cluster = get_cluster_for_career(career_name)
    nodes.append({
        "id": career_name,
        "cluster": root_cluster["cluster_id"] if root_cluster else None
    })

    similars = get_similar_careers(career_name, top_k=top_k)

    for name, score in similars:
        cluster = get_cluster_for_career(name)

        nodes.append({
            "id": name,
            "cluster": cluster["cluster_id"] if cluster else None
        })

        edges.append({
            "source": career_name,
            "target": name,
            "weight": round(score, 3)
        })

    return {
        "nodes": nodes,
        "edges": edges
    }
