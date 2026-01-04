# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

# Routers
from app.routes.auth import router as auth_router
from app.routes.assessment import router as assessment_router
from app.routes.recommend import router as recommend_router
from app.routes.advisor import router as advisor_router
from app.routes.compare import router as compare_router
from app.routes.similar import router as similar_router
from app.routes.careers import router as careers_router
from app.routes.explain import router as explain_router
from app.routes.graph import router as graph_router
from app.routes.search import router as search_router

# Optional / advanced
from app.routes.roadmap import router as roadmap_router
from app.routes.profile import router as profile_router
from app.routes.generator import router as generator_router
from app.routes.confidence import router as confidence_router
from app.routes.cluster import router as cluster_router

app = FastAPI(
    title="Career AI Backend",
    description="Backend API for Career Assessment, Recommendations, Roadmap, and AI Advisor",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# =======================
# CORS
# =======================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =======================
# EXCEPTION HANDLERS
# =======================
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={
            "message": "Validation error",
            "details": exc.errors(),
        },
    )

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

# =======================
# ROUTES
# =======================
app.include_router(auth_router, tags=["Auth"])
app.include_router(assessment_router, prefix="/assessment", tags=["Assessment"])
app.include_router(recommend_router, prefix="/recommend", tags=["Recommend"])
app.include_router(search_router, prefix="/search", tags=["Search"])
app.include_router(advisor_router, prefix="/advisor", tags=["Advisor"])
app.include_router(compare_router, prefix="/compare", tags=["Compare"])
app.include_router(similar_router, prefix="/similar", tags=["Similarity"])
app.include_router(careers_router, prefix="/careers", tags=["Careers"])
app.include_router(explain_router, prefix="/explain", tags=["Explainability"])
app.include_router(graph_router, prefix="/graph", tags=["Knowledge Graph"])

# Optional
app.include_router(roadmap_router, prefix="/roadmap", tags=["Roadmap"])
app.include_router(profile_router, prefix="/profile", tags=["Profile"])
app.include_router(generator_router, prefix="/generator", tags=["Generator"])
app.include_router(confidence_router, prefix="/confidence", tags=["Confidence"])
app.include_router(cluster_router, prefix="/clusters", tags=["Clustering"])

# =======================
# HEALTH
# =======================
@app.get("/")
def home():
    return {
        "message": "Career AI Backend is Running 🚀",
        "docs": "/docs",
        "version": "1.0.0",
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}