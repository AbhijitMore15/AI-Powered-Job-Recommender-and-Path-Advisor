🚀 AI-Powered Career Recommender – Backend (FastAPI)

This is the backend service for the AI-Powered Career Recommender & Roadmap Generator, responsible for authentication, assessment management, machine-learning career predictions, roadmap generation, and user progress tracking.

Backend Developed by: Abhijit More
📌 GitHub: https://github.com/AbhijitMore-15

🔥 Features
🔐 Authentication

User registration & login

JWT-based authorization

Password hashing with Argon2

📝 Assessment Handling

Accepts user skills, interests, education & goals

Secure database storage (MongoDB)

🎯 Career Recommendation Engine

TF-IDF + Cosine Similarity

RandomForest model support

Returns ranked career matches

🛣 AI Roadmap Generator

Skill gap analysis

Course, tools, and project suggestions

Timeline-based roadmap creation

📈 Progress Tracking

Track user skill completion

Roadmap completion percentage

🛠 Tech Stack
Component	Technology
Framework	FastAPI
Database	MongoDB
Authentication	JWT + Argon2
ML Models	TF-IDF, RandomForest, SBERT (optional)
Validation	Pydantic
Server	Uvicorn
📦 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/AbhijitMore-15/Ai-Powered-Career-Recommender-Backend.git
cd Ai-Powered-Career-Recommender-Backend

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Create Your .env File
SECRET_KEY=your-secret-key
ALGORITHM=HS256
MONGODB_URL=your-mongodb-url

4️⃣ Start the Server
uvicorn app.main:app --reload

5️⃣ Open API Docs

Swagger UI → http://127.0.0.1:8000/docs

Redoc → http://127.0.0.1:8000/redoc

📂 Project Structure
backend/
│── app/
│   ├── routers/          # API routes (auth, assessment, career, roadmap, progress)
│   ├── models/           # Database models
│   ├── schemas/          # Pydantic schemas
│   ├── core/             # Security utils (JWT, hashing)
│   ├── database/         # MongoDB connection
│   └── main.py           # Main FastAPI application
│
├── requirements.txt
└── README.md

🔌 API Endpoints
🔐 Auth
POST /auth/register
POST /auth/login
GET  /auth/me

📝 Assessment
POST /assessment/submit

🎯 Career Recommendation
POST /career/recommend
POST /career/predict

🛣 Roadmap Generator
POST /career/roadmap

📈 Progress Tracking
POST /progress/update
GET  /progress/fetch

🙌 Credits
Backend Developed By:AbhijitMore-15

Abhijit More
🔗 Backend Repository:
https://github.com/AbhijitMore-15/Ai-Powered-Career-Recommender-Backend

📜 License

MIT License
