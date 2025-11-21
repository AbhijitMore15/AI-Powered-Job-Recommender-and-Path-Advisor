🚀 AI-Powered Career Recommender — Backend

Developed by Abhijit More

The backend powers the AI-driven recommendation engine, user authentication, secure token handling, and seamless communication with the frontend using FastAPI.

🛠️ Tech Stack

FastAPI (Python)

MongoDB

JWT Authentication

Passlib Argon2 Password Hashing

Uvicorn

📦 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/AbhijitMore-15/Ai-Powered-Career-Recommender-Backend.git
cd Ai-Powered-Career-Recommender-Backend

📁 Create & Activate Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

Mac / Linux
python3 -m venv venv
source venv/bin/activate

📥 Install Dependencies
pip install -r requirements.txt

⚙️ Environment Variables

Create a .env file in the root folder:

SECRET_KEY=your_secret_key
ALGORITHM=HS256
MONGO_URI=your_mongodb_url
ACCESS_TOKEN_EXPIRE_MINUTES=30

▶️ Run the Backend Server
uvicorn main:app --reload


The API will now be live at:
👉 http://localhost:8000

🔐 Authentication

The backend uses:

JWT for secure token-based authentication

Argon2 hash using Passlib for strong password security

📡 API Endpoints Overview
🔑 Authentication
Method	Endpoint	Description
POST	/register	Register new user
POST	/login	Login user & receive token
🧠 Recommendation System
Method	Endpoint	Description
POST	/predict-career	Predict career based on inputs
POST	/generate-roadmap	Generate AI-powered learning roadmap
🏗️ Project Structure
Ai-Powered-Career-Recommender-Backend/
│── main.py
│── routes/
│── models/
│── database/
│── utils/
│── requirements.txt
│── .env

✨ Abhijit More
Backend Repository:
👉 https://github.com/AbhijitMore-15/Ai-Powered-Career-Recommender-Backend
