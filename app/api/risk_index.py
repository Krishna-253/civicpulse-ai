from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.services.risk_index_service import calculate_ward_risk_index

router = APIRouter(prefix="/risk-index", tags=["Ward Risk Index"])

@router.get("/ward/{ward}")
def get_risk_index(
    ward: str,
    rainfall_mm: float,
    drainage_score: int,
    db: Session = Depends(get_db)
):
    return calculate_ward_risk_index(
        db=db,
        ward=ward,
        rainfall_mm=rainfall_mm,
        drainage_score=drainage_score
    )
