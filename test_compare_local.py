from app.utils.data_loader import load_careers_json
from app.ml.similarity import build_tfidf_matrix, compute_similarity_matrix

careers = load_careers_json()

tfidf_matrix, vectorizer = build_tfidf_matrix(careers)
similarity = compute_similarity_matrix(tfidf_matrix)

print(tfidf_matrix.shape)
print(similarity.shape)
