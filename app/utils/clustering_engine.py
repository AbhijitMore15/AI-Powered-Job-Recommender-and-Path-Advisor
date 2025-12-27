from sklearn.cluster import KMeans
import pickle
import os
from app.utils.similarity_engine import load_similarity

DATA_DIR = "app/data"
CLUSTER_PATH = os.path.join(DATA_DIR, "career_clusters.pkl")

def train_clusters(n_clusters: int = 10):
    _, matrix, names = load_similarity()

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )
    labels = model.fit_predict(matrix)

    clusters = {}
    for name, label in zip(names, labels):
        clusters.setdefault(int(label), []).append(name)

    with open(CLUSTER_PATH, "wb") as f:
        pickle.dump(clusters, f)

    return clusters

def load_clusters():
    with open(CLUSTER_PATH, "rb") as f:
        return pickle.load(f)

def get_cluster_for_career(career_name: str):
    clusters = load_clusters()
    for cid, careers in clusters.items():
        if career_name in careers:
            return {
                "cluster_id": cid,
                "careers": careers
            }
    return None
