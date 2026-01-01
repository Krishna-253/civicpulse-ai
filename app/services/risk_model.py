import numpy as np

# Dummy risk prediction logic (replace with trained model later)
def predict_flood_risk(rainfall_mm: float, drainage_score: int):
    """
    rainfall_mm: recent rainfall in mm
    drainage_score: 1 (poor) to 5 (excellent)
    """
    risk_score = rainfall_mm * 0.6 + (6 - drainage_score) * 10

    if risk_score > 80:
        return "High"
    elif risk_score > 40:
        return "Medium"
    else:
        return "Low"
