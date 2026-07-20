from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime, timezone
from database.database import Base

class PredictionHistory(Base):
    __tablename__ = "prediction_history"

    id = Column(Integer, primary_key=True, index=True)
    prediction = Column(Integer, nullable=False)
    probability = Column(Float, nullable=False)
    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )