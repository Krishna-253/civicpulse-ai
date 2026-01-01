from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.database import Base

class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    ward = Column(String, index=True)
    status = Column(String, default="Open")
    severity = Column(String, default="Medium")
    created_at = Column(DateTime, default=datetime.utcnow)
