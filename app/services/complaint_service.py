from sqlalchemy.orm import Session
from app.models.complaint_db import Complaint

def calculate_severity(text: str):
    text = text.lower()
    if "flood" in text or "severe" in text or "blocked" in text:
        return "High"
    elif "delay" in text or "broken" in text:
        return "Medium"
    return "Low"

def create_complaint(db: Session, data):
    severity = calculate_severity(data.description)

    complaint = Complaint(
        title=data.title,
        description=data.description,
        ward=data.ward,
        status="Open",
        severity=severity
    )
    db.add(complaint)
    db.commit()
    db.refresh(complaint)
    return complaint

def list_complaints(db: Session):
    return db.query(Complaint).all()
