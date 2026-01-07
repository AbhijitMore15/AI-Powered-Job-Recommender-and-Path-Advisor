from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database.connect import SessionLocal
from app.models.auth_models import (
    SignupRequest,
    LoginRequest,
    TokenResponse,
    User,
)
from app.utils.password import hash_password, verify_password
from app.utils.jwt_handler import create_token

router = APIRouter()


# ==========================
# DB Dependency
# ==========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==========================
# SIGNUP
# ==========================
@router.post("/signup", status_code=201)
def signup(payload: SignupRequest, db: Session = Depends(get_db)):
    email = payload.email.lower()

    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(
        name=payload.name,
        email=email,
        password=hash_password(payload.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "Signup successful"}


# ==========================
# LOGIN
# ==========================
@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    email = payload.email.lower()

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(payload.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    token = create_token({"sub": user.email})

    return {
        "access_token": token,
        "token_type": "bearer",
    }
