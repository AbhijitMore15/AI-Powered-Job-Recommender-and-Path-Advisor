```markdown
# 🚀 AI-Powered Career Recommender — Backend

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104%2B-009688.svg?style=flat&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-4.0%2B-green.svg?style=flat&logo=mongodb)
![JWT](https://img.shields.io/badge/JWT-Authentication-black)
![License](https://img.shields.io/github/license/AbhijitMore-15/Ai-Powered-Career-Recommender-Backend)

A high-performance, secure backend built with **FastAPI** that powers an intelligent career recommendation engine. It handles user authentication, processes skill/personality inputs, delivers AI-driven career predictions, and generates personalized learning roadmaps.

Developed & maintained by **Abhijit More**

---

### 🌟 Features

- **Secure User Authentication** with JWT tokens
- **Strong Password Hashing** using Argon2 (via Passlib)
- **AI-Powered Career Prediction** endpoint
- **Dynamic Learning Roadmap Generation** tailored to recommended careers
- **MongoDB** for flexible and scalable data storage
- **Clean, modular project structure**
- **Fully async-ready** FastAPI architecture
- **Automatic OpenAPI (Swagger) documentation** at `/docs`

---

### 🛠️ Tech Stack

| Technology              | Purpose                              |
|-------------------------|--------------------------------------|
| **FastAPI**             | High-performance API framework       |
| **Python 3.10+**        | Core language                        |
| **MongoDB (PyMongo)**   | NoSQL database                       |
| **JWT (PyJWT)**         | Token-based authentication           |
| **Passlib + Argon2**    | Secure password hashing              |
| **Pydantic**            | Data validation and settings management |
| **Uvicorn**             | ASGI server                          |
| **python-dotenv**       | Environment variable management      |

---

### 📦 Installation & Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/AbhijitMore-15/Ai-Powered-Career-Recommender-Backend.git
cd Ai-Powered-Career-Recommender-Backend
```

#### 2. Create & Activate Virtual Environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**MacOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Create `.env` File
Copy the example and fill in your values:
```env
SECRET_KEY=your_very_secure_random_secret_key_here
ALGORITHM=HS256
MONGO_URI=mongodb://localhost:27017/your_database_name
ACCESS_TOKEN_EXPIRE_MINUTES=4320   # 3 days recommended
```

> Generate a strong secret key using: `openssl rand -hex 32`

#### 5. Run the Server
```bash
uvicorn main:app --reload
```

Server will be live at:  
👉 **http://localhost:8000**  
Interactive API docs: **http://localhost:8000/docs**

---

### 🔐 Authentication Flow

1. **Register** → `POST /register`
2. **Login** → `POST /login` → Receive JWT token
3. Include token in protected routes:
   ```http
   Authorization: Bearer <your_jwt_token>
   ```

---

### 📡 API Endpoints

| Method | Endpoint               | Description                              | Auth Required |
|--------|------------------------|------------------------------------------|---------------|
| POST   | `/register`            | Create a new user                        | No            |
| POST   | `/login`               | Login and receive access token           | No            |
| POST   | `/predict-career`      | Get AI-powered career recommendations    | Yes           |
| POST   | `/generate-roadmap`    | Generate personalized learning roadmap   | Yes           |

---

### 🏗️ Project Structure

```
Ai-Powered-Career-Recommender-Backend/
├── main.py                  # Entry point & FastAPI app
├── routes/                  # All API routes (auth, predict, roadmap)
├── models/                  # Pydantic schemas
├── database/                # MongoDB connection & helpers
├── utils/                   # Security, token, hashing utilities
├── requirements.txt
├── .env                     # Environment variables (gitignored)
└── README.md
```

---

### 🔒 Security Best Practices Implemented

- Argon2id hashing (memory-hard, resistant to GPU cracking)
- JWT with configurable expiration
- Secure secret key management
- Input validation using Pydantic
- Protected routes with dependency injection

---

### 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

### 📄 License

This project is licensed under the **Apache License** – see the [LICENSE](LICENSE) file for details.

---

### 👨‍💻 Author

**Abhijit More**  
Backend Developer | AI Enthusiast

🔗 GitHub: [github.com/AbhijitMore-15](https://github.com/AbhijitMore-15)  
🔗 Repository: [Ai-Powered-Career-Recommender-Backend](https://github.com/AbhijitMore-15/Ai-Powered-Career-Recommender-Backend)

---
