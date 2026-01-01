from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.complaint_db import Complaint
from app.services.risk_model import predict_flood_risk

def calculate_ward_risk_index(
    db: Session,
    ward: str,
    rainfall_mm: float,
    drainage_score: int
):
    # Severity counts
    severity_counts = (
        db.query(Complaint.severity, func.count())
        .filter(Complaint.ward == ward)
        .group_by(Complaint.severity)
        .all()
    )

    counts = {"High": 0, "Medium": 0, "Low": 0}
    for severity, count in severity_counts:
        counts[severity] = count

    # Flood risk
    flood_risk = predict_flood_risk(rainfall_mm, drainage_score)
    flood_weight = {"High": 25, "Medium": 15, "Low": 5}[flood_risk]

    # Risk index calculation
    risk_index = (
        counts["High"] * 15
        + counts["Medium"] * 8
        + counts["Low"] * 3
        + flood_weight
    )

    return {
        "ward": ward,
        "risk_index": risk_index,
        "severity_breakdown": counts,
        "flood_risk": flood_risk
    }
