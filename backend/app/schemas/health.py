"""Health record schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class HealthRecordBase(BaseModel):
    """Base health record schema."""

    record_type: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    veterinarian: Optional[str] = None
    clinic_name: Optional[str] = None
    notes: Optional[str] = None
    cost: Optional[str] = None
    recorded_date: datetime
    next_due_date: Optional[datetime] = None


class HealthRecordCreate(HealthRecordBase):
    """Health record creation schema."""

    pass


class HealthRecordUpdate(BaseModel):
    """Health record update schema."""

    record_type: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    veterinarian: Optional[str] = None
    clinic_name: Optional[str] = None
    notes: Optional[str] = None
    cost: Optional[str] = None
    recorded_date: Optional[datetime] = None
    next_due_date: Optional[datetime] = None
    is_completed: Optional[bool] = None


class HealthRecordResponse(HealthRecordBase):
    """Health record response schema."""

    id: str
    cat_id: str
    is_completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True