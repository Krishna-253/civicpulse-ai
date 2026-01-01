from fastapi import APIRouter
from app.services.risk_model import predict_flood_risk

router = APIRouter(prefix="/risk", tags=["Flood Risk"])

@router.get("/predict")
def predict(rainfall_mm: float, drainage_score: int):
    risk = predict_flood_risk(rainfall_mm, drainage_score)
    return {
        "rainfall_mm": rainfall_mm,
        "drainage_score": drainage_score,
        "risk_level": risk
    }
