# 🚀 AI-Powered Career Recommender & Path Advisor

**Backend System** | *Built with FastAPI + Explainable ML*

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/ML-TF--IDF%20%7C%20KMeans-FF6F00?style=for-the-badge)

---

## 📌 Overview

This is the **backend** for an intelligent Career Recommender and Path Advisor platform. It leverages **explainable AI** to deliver personalized career guidance with full transparency.

### Key Capabilities
- Personalized Career Recommendations  
- Career Comparison & Similarity Analysis  
- Skill Gap Assessment  
- Confidence Scoring  
- Personalized Learning Roadmaps  
- Career Clustering & Intelligent Search  

The system is built with a **clean, modular FastAPI architecture** and prioritizes **interpretable machine learning** over black-box models.

> **Note:** The frontend was developed separately by my friend and is not included in this repository.

---

## 🛠️ Tech Stack

| Layer              | Technologies |
|--------------------|--------------|
| **Framework**      | FastAPI |
| **Language**       | Python |
| **ML / AI**        | TF-IDF Vectorization, Cosine Similarity, KMeans Clustering |
| **Data**           | JSON, CSV, Pickle (precomputed artifacts) |
| **Architecture**   | Modular (Routes → Services → Utils → ML → Data) |

---

## 🧠 Explainable AI Approach

This project deliberately avoids opaque models. Every recommendation is **transparent and justifiable**:

- **TF-IDF + Cosine Similarity** — Matches user skills/profile to careers  
- **KMeans Clustering** — Groups similar career paths  
- **Rule-based Logic** — Generates clear, human-readable explanations  

Precomputed artifacts (vectors, similarity matrices, clusters) ensure **fast, production-ready responses**.

---

## 🏗️ Project Structure

```plaintext
career-ai-backend/
├── app/
│   ├── data/                    # Datasets & precomputed ML artifacts
│   │   ├── careers.csv
│   │   ├── careers.json
│   │   ├── skill_difficulty.json
│   │   ├── career_vectors.pkl
│   │   ├── tfidf_vectorizer.pkl
│   │   ├── tfidf_matrix.pkl
│   │   ├── career_similarity.pkl
│   │   └── career_clusters.pkl
│   │
│   ├── database/                # Database connection
│   ├── ml/                      # Machine Learning core logic
│   │   ├── preprocess.py
│   │   ├── similarity.py
│   │   ├── clustering.py
│   │   └── classifier.py
│   │
│   ├── models/                  # Pydantic data models & schemas
│   ├── routes/                  # API route handlers
│   ├── services/                # Business logic layer
│   └── utils/                   # Helper utilities
│
├── main.py                      # Application entry point
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🔌 API Endpoints

| Endpoint          | Description                              |
|-------------------|------------------------------------------|
| `/recommend`      | Get personalized career recommendations |
| `/advisor`        | Comprehensive career advice + roadmap   |
| `/compare`        | Compare multiple careers                 |
| `/confidence`     | Calculate career fit confidence score   |
| `/similar`        | Find similar career suggestions         |
| `/cluster`        | View career clusters                    |
| `/roadmap`        | Generate personalized learning roadmap  |
| `/search`         | Search careers                          |
| `/profile`        | User profile management                 |
| `/assessment`     | Skill assessment                        |
| `/auth`           | Authentication                          |

Full interactive documentation available at `/docs` (Swagger UI) when running locally.

---

## ⚙️ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/career-ai-backend.git
cd career-ai-backend
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Server
```bash
uvicorn main:app --reload
```

### 5. Explore the API
Open your browser and go to:  
**http://127.0.0.1:8000/docs**

---

## 📊 What This Project Demonstrates

- Production-grade **FastAPI** architecture
- Seamless integration of **Machine Learning** into REST APIs
- **Explainable AI** principles in real-world applications
- Clean separation of concerns (modular design)
- Efficient use of **precomputed ML artifacts** for performance
- Practical solution to a meaningful problem — career guidance

---

## 🤝 Credits

- **Backend Developer**: Abhijit More(https://github.com/AbhijitMore15)
- **Frontend Developer**:Arsh Mishra(https://github.com/ArshMishra20)

---

## 🚀 Future Enhancements

- Containerization & deployment (Docker + AWS / Render / Railway)
- Real-time recommendation updates
- Integration with external job boards (LinkedIn, Indeed APIs, etc.)
- User analytics dashboard
- Advanced ML models (while maintaining explainability)

---

## ⭐ Acknowledgments

This project showcases strong backend engineering, practical ML implementation, and thoughtful system design for a real-world use case.

---

**Made with ❤️ for career aspirants and tech enthusiasts.**

Feel free to ⭐ the repo if you find it useful!
```

### Why this version is better:
- **Professional tone** and consistent formatting
- **Badges** for visual appeal (you can customize them)
- **Clean tables** for tech stack and endpoints
- **Code blocks** for commands (easy to copy)
- **Better visual hierarchy** with clear sections
- **Concise yet comprehensive** content
- Ready-to-use structure that looks great on GitHub
