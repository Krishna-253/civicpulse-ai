from fastapi import FastAPI
from app.api.complaints import router as complaints_router

app = FastAPI(title="CivicPulse AI")

app.include_router(complaints_router)

@app.get("/")
def root():
    return {"message": "CivicPulse AI backend is running"}
