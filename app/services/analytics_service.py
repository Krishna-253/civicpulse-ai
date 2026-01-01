from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.complaint_db import Complaint

def ward_analytics(db: Session, ward: str):
    total = db.query(Complaint).filter(Complaint.ward == ward).count()

    severity_counts = (
        db.query(Complaint.severity, func.count())
        .filter(Complaint.ward == ward)
        .group_by(Complaint.severity)
        .all()
    )

    severity_summary = {severity: count for severity, count in severity_counts}

    return {
        "ward": ward,
        "total_complaints": total,
        "severity_breakdown": severity_summary
    }
