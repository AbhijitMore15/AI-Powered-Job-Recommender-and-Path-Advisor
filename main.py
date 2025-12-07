from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.assessment import router as assessment_router
from app.routes.recommend import router as recommend_router
from app.routes.roadmap import router as roadmap_router
from app.routes.compare import router as compare_router
from app.routes.profile import router as profile_router
from app.routes.careers import router as careers_router

app = FastAPI(title="Career AI Backend")

# Register routes
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(assessment_router, prefix="/assessment", tags=["Assessment"])
app.include_router(recommend_router, prefix="/recommend", tags=["Recommend"])
app.include_router(roadmap_router, prefix="/roadmap", tags=["Roadmap"])
app.include_router(compare_router, prefix="/compare", tags=["Compare"])
app.include_router(profile_router, prefix="/profile", tags=["Profile"])
app.include_router(careers_router, prefix="/careers", tags=["Careers"])

@app.get("/")
def home():
    return {"message": "Career AI Backend Running"}
