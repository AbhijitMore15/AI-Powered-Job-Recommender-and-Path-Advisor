🎯 AI-Powered Career Recommender – Backend (FastAPI)

This backend powers the AI-Driven Career Recommendation & Roadmap System, handling authentication, assessment storage, ML-based career prediction, roadmap generation, and progress tracking.

Developed by Abhijit More
🔗 Backend Repository: https://github.com/AbhijitMore-15/Ai-Powered-Career-Recommender-Backend

🚀 Features (Backend)
🔐 Authentication

User registration

Login with JWT

Secure token-based authorization

Password hashing using Argon2

📝 Assessment System

Accepts user skills, interests, education, goals

Stores assessment data securely in the database

🎯 Career Recommendation Engine

TF-IDF + Cosine Similarity

Optional ML classifier (RandomForest)

Returns top career matches with confidence scores

📚 Roadmap Generator

Dynamic skill-gap analysis

Auto-generated learning roadmap

Courses, tools, projects, timeline suggestions

📊 Progress Tracking

Update and fetch completed skills

Tracks user journey toward selected career

🛠 Tech Stack
Component	Technology
Framework	FastAPI (Python)
Database	MongoDB
Authentication	JWT + Argon2
ML Models	TF-IDF, RandomForest, SBERT (optional)
Data Validation	Pydantic
Server	Uvicorn
📦 Installation & Setup
1️⃣ Clone the backend repository
git clone https://github.com/AbhijitMore-15/Ai-Powered-Career-Recommender-Backend.git
cd Ai-Powered-Career-Recommender-Backend

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Create your .env file
SECRET_KEY=your-secret-key
ALGORITHM=HS256
MONGODB_URL=your-mongodb-url

4️⃣ Run the FastAPI server
uvicorn app.main:app --reload

5️⃣ Test API Docs

Once running, open:
👉 http://127.0.0.1:8000/docs

(Interactive Swagger API docs)

📂 Project Structure
backend/
│── app/
│   ├── routers/          # API routes (auth, career, roadmap, progress)
│   ├── models/           # Database models
│   ├── schemas/          # Pydantic schemas
│   ├── core/             # Security, JWT, hashing
│   ├── database/         # MongoDB connection
│   └── main.py           # Main FastAPI entry point
│
├── requirements.txt
└── README.md

🔌 API Endpoints
🧑‍💻 Auth
POST /auth/register
POST /auth/login
GET  /auth/me

📊 Assessment
POST /assessment/submit

🎯 Career Recommendation
POST /career/recommend
POST /career/predict

🛣 Roadmap Generator
POST /career/roadmap

📈 Progress Tracking
POST /progress/update
GET  /progress/fetch

👨‍💻 Developer

Backend Developed By:

Abhijit More

🔗 GitHub: https://github.com/AbhijitMore-15

🔗 Backend Repo: https://github.com/AbhijitMore-15/Ai-Powered-Career-Recommender-Backend

📜 License

MIT License – Free to use and contribute.
