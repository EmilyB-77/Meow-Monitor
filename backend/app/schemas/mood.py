"""Mood log schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class MoodLogBase(BaseModel):
    """Base mood log schema."""

    mood: str = Field(..., min_length=1)
    energy_level: int = Field(..., ge=1, le=10)
    appetite_level: int = Field(..., ge=1, le=10)
    sleep_quality: Optional[int] = Field(None, ge=1, le=10)
    activities: Optional[str] = None
    notes: Optional[str] = None
    recorded_at: datetime


class MoodLogCreate(MoodLogBase):
    """Mood log creation schema."""

    pass


class MoodLogResponse(MoodLogBase):
    """Mood log response schema."""

    id: str
    cat_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True