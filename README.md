# AI-Powered Career Recommender & Path Advisor

## Overview
A backend system that recommends careers, compares paths, and generates skill roadmaps using explainable AI logic.

## Tech Stack
- FastAPI
- Python
- TF-IDF + Cosine Similarity
- KMeans Clustering
- Modular ML Utilities

## Core Features
- Career recommendation
- Career comparison
- Confidence scoring
- Skill gap analysis
- Personalized roadmaps
- Career similarity & clustering

## AI Usage (Honest)
This project uses:
- TF-IDF for skill/career similarity
- Clustering for career grouping
- Rule-based explainability
No black-box learning models are used.

## Architecture
(app → routes → utils → data)

## How to Run
```bash


---

### B2️⃣ API Overview Table

```md
| Endpoint | Purpose |
|-------|-------|
| /advisor | Career + roadmap |
| /compare | Career comparison |
| /recommend | Career ranking |
| /confidence | Fit score |
| /similar | Similar careers |
| /cluster | Career clusters |
| /profile | User profiling |

uvicorn main:app --reload
---
```

## What This Project Demonstrates
- Real backend architecture
- Explainable AI systems
- ML integration without overfitting
- Error handling & system safety
