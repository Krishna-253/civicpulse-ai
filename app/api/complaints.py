from fastapi import APIRouter
from app.models.complaint import ComplaintCreate, ComplaintResponse
from app.services.complaint_service import create_complaint, list_complaints

router = APIRouter(prefix="/complaints", tags=["Complaints"])

@router.post("/", response_model=ComplaintResponse)
def add_complaint(complaint: ComplaintCreate):
    return create_complaint(complaint)

@router.get("/", response_model=list[ComplaintResponse])
def get_complaints():
    return list_complaints()
