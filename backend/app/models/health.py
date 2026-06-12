"""Health record model."""

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.database import Base


class HealthRecord(Base):
    """Health record model for tracking medical events."""

    __tablename__ = "health_records"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    cat_id = Column(UUID(as_uuid=True), ForeignKey("cats.id", ondelete="CASCADE"), nullable=False, index=True)
    record_type = Column(String(50), nullable=False)  # vaccination, checkup, medication, etc.
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    veterinarian = Column(String(255), nullable=True)
    clinic_name = Column(String(255), nullable=True)
    notes = Column(Text, nullable=True)
    cost = Column(String(20), nullable=True)
    recorded_date = Column(DateTime, nullable=False)
    next_due_date = Column(DateTime, nullable=True)
    is_completed = Column(String, default=True, nullable=False)
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
    cat = relationship("Cat", back_populates="health_records")

    def __repr__(self) -> str:
        return f"<HealthRecord {self.title}>"