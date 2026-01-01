from pydantic import BaseModel
from datetime import datetime

class ComplaintCreate(BaseModel):
    title: str
    description: str
    ward: str

class ComplaintResponse(BaseModel):
    id: int
    title: str
    description: str
    ward: str
    status: str
    severity: str
    created_at: datetime

    class Config:
        from_attributes = True
