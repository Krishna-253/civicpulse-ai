from sqlalchemy.orm import Session
from app.models.complaint_db import Complaint

def create_complaint(db: Session, data):
    complaint = Complaint(
        title=data.title,
        description=data.description,
        ward=data.ward,
        status="Open"
    )
    db.add(complaint)
    db.commit()
    db.refresh(complaint)
    return complaint

def list_complaints(db: Session):
    return db.query(Complaint).all()
