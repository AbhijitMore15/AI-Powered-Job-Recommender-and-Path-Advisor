from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

DATA_DIR = "app/data"
VEC_PATH = os.path.join(DATA_DIR, "career_vectorizer.pkl")
MAT_PATH = os.path.join(DATA_DIR, "career_vectors.pkl")

def build_career_corpus(careers):
    texts = []
    names = []

    for c in careers:
        combined = " ".join(
            c.get("interests", []) +
            c.get("tags", []) +
            c.get("keywords", []) +
            c.get("required_skills", [])
        )
        texts.append(combined.lower())
        names.append(c["career_name"])

    return texts, names

def train_similarity(careers):
    texts, names = build_career_corpus(careers)

    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    matrix = vectorizer.fit_transform(texts)

    with open(VEC_PATH, "wb") as f:
        pickle.dump(vectorizer, f)

    with open(MAT_PATH, "wb") as f:
        pickle.dump((matrix, names), f)

def load_similarity():
    with open(VEC_PATH, "rb") as f:
        vectorizer = pickle.load(f)

    with open(MAT_PATH, "rb") as f:
        matrix, names = pickle.load(f)

    return vectorizer, matrix, names

def get_similar_careers(career_name, top_n=5):
    _, matrix, names = load_similarity()

    if career_name not in names:
        return []

    idx = names.index(career_name)
    scores = cosine_similarity(matrix[idx], matrix)[0]

    ranked = sorted(
        enumerate(scores),
        key=lambda x: x[1],
        reverse=True
    )

    results = []
    for i, score in ranked[1: top_n + 1]:
        results.append({
            "career": names[i],
            "score": round(float(score), 3)
        })

    return results
