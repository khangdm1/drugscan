# app/models/prediction_log.py
from sqlalchemy import Column, Integer, DateTime, Float, Text, ForeignKey
from sqlalchemy.sql import func
from app.core.db import Base

class PredictionLog(Base):
    __tablename__ = "prediction_log"

    id = Column(Integer, primary_key=True, index=True)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    predicted_drug_id = Column(Integer, ForeignKey("drug.id"), nullable=True)
    confidence = Column(Float, nullable=True)
    image_path = Column(Text, nullable=True)
