"""Mood log model."""

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.database import Base


class MoodLog(Base):
    """Mood log model for tracking behavioral patterns."""

    __tablename__ = "mood_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    cat_id = Column(UUID(as_uuid=True), ForeignKey("cats.id", ondelete="CASCADE"), nullable=False, index=True)
    mood = Column(String(50), nullable=False)  # happy, content, neutral, anxious, grumpy, playful, tired
    energy_level = Column(Integer, nullable=False)  # 1-10 scale
    appetite_level = Column(Integer, nullable=False)  # 1-10 scale
    sleep_quality = Column(Integer, nullable=True)  # 1-10 scale
    activities = Column(Text, nullable=True)  # comma-separated or JSON
    notes = Column(Text, nullable=True)
    recorded_at = Column(DateTime, nullable=False)
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
    cat = relationship("Cat", back_populates="mood_logs")

    def __repr__(self) -> str:
        return f"<MoodLog {self.mood} for {self.cat_id}>"