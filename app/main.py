# Civicpulse AI/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.complaints import router as complaints_router
from app.api.risk import router as risk_router
from app.api.analytics import router as analytics_router
from app.api.risk_index import router as risk_index_router
from app.api.auth import router as auth_router
from app.core.database import engine, Base

app = FastAPI(title="CivicPulse AI")

# ✅ CORS (THIS WAS MISSING HERE)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(complaints_router)
app.include_router(risk_router)
app.include_router(analytics_router)
app.include_router(risk_index_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "CivicPulse AI backend is running"}
