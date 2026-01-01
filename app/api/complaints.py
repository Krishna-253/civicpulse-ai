from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.complaint import ComplaintCreate, ComplaintResponse
from app.services.complaint_service import create_complaint, list_complaints
from app.core.deps import get_db

router = APIRouter(prefix="/complaints", tags=["Complaints"])

@router.post("/", response_model=ComplaintResponse)
def add_complaint(
    complaint: ComplaintCreate,
    db: Session = Depends(get_db)
):
    return create_complaint(db, complaint)

@router.get("/", response_model=list[ComplaintResponse])
def get_complaints(db: Session = Depends(get_db)):
    return list_complaints(db)
