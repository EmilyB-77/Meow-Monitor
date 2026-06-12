"""Feeding models."""

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Time, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.database import Base


class FeedingLog(Base):
    """Feeding log model for tracking individual meals."""

    __tablename__ = "feeding_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    cat_id = Column(UUID(as_uuid=True), ForeignKey("cats.id", ondelete="CASCADE"), nullable=False, index=True)
    food_type = Column(String(50), nullable=False)  # wet, dry, mixed
    portion_grams = Column(Float, nullable=False)
    meal_name = Column(String(255), nullable=True)
    notes = Column(String(500), nullable=True)
    fed_at = Column(DateTime, nullable=False)
    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # Relationships
    cat = relationship("Cat", back_populates="feeding_logs")

    def __repr__(self) -> str:
        return f"<FeedingLog {self.cat_id} at {self.fed_at}>"


class FeedingSchedule(Base):
    """Feeding schedule model for recurring meals."""

    __tablename__ = "feeding_schedules"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    cat_id = Column(UUID(as_uuid=True), ForeignKey("cats.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    food_type = Column(String(50), nullable=False)  # wet, dry, mixed
    portion_grams = Column(Float, nullable=False)
    time_of_day = Column(Time, nullable=False)
    days_of_week = Column(String(7), nullable=False)  # e.g., "1111111" for daily, "1010101" for weekdays
    is_active = Column(String, default=True, nullable=False)
    notes = Column(String(500), nullable=True)
    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # Relationships
    cat = relationship("Cat", back_populates="feeding_schedules")

    def __repr__(self) -> str:
        return f"<FeedingSchedule {self.name}>"