from fastapi import FastAPI
from app.api.complaints import router as complaints_router
from app.api.risk import router as risk_router
from app.api.analytics import router as analytics_router
from app.api.risk_index import router as risk_index_router
from app.core.database import engine, Base

app = FastAPI(title="CivicPulse AI")

Base.metadata.create_all(bind=engine)

app.include_router(complaints_router)
app.include_router(risk_router)
app.include_router(analytics_router)
app.include_router(risk_index_router)

@app.get("/")
def root():
    return {"message": "CivicPulse AI backend is running"}
