from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.services.analytics_service import ward_analytics

router = APIRouter(prefix="/analytics", tags=["Ward Analytics"])

@router.get("/ward/{ward}")
def get_ward_analytics(ward: str, db: Session = Depends(get_db)):
    return ward_analytics(db, ward)
