from datetime import datetime

complaints_db = []

def create_complaint(data):
    complaint = {
        "id": len(complaints_db) + 1,
        "title": data.title,
        "description": data.description,
        "ward": data.ward,
        "status": "Open",
        "created_at": datetime.utcnow()
    }
    complaints_db.append(complaint)
    return complaint

def list_complaints():
    return complaints_db
