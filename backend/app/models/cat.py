"""Cat model."""

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.database import Base


class Cat(Base):
    """Cat model for tracking individual cats."""

    __tablename__ = "cats"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    breed = Column(String(255), nullable=True)
    date_of_birth = Column(DateTime, nullable=True)
    color = Column(String(255), nullable=True)
    weight_kg = Column(Float, nullable=True)
    microchip_number = Column(String(255), nullable=True, unique=True)
    description = Column(String(500), nullable=True)
    profile_picture_url = Column(String(500), nullable=True)
    is_active = Column(String, default=True, nullable=False)
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
    health_records = relationship("HealthRecord", back_populates="cat", cascade="all, delete-orphan")
    feeding_logs = relationship("FeedingLog", back_populates="cat", cascade="all, delete-orphan")
    feeding_schedules = relationship("FeedingSchedule", back_populates="cat", cascade="all, delete-orphan")
    mood_logs = relationship("MoodLog", back_populates="cat", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Cat {self.name}>"