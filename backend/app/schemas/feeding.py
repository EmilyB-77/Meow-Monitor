"""Feeding schemas."""

from datetime import datetime, time
from typing import Optional

from pydantic import BaseModel, Field


class FeedingLogBase(BaseModel):
    """Base feeding log schema."""

    food_type: str = Field(..., min_length=1)
    portion_grams: float = Field(..., ge=0)
    meal_name: Optional[str] = None
    notes: Optional[str] = None
    fed_at: datetime


class FeedingLogCreate(FeedingLogBase):
    """Feeding log creation schema."""

    pass


class FeedingLogResponse(FeedingLogBase):
    """Feeding log response schema."""

    id: str
    cat_id: str
    created_at: datetime

    class Config:
        from_attributes = True


class FeedingScheduleBase(BaseModel):
    """Base feeding schedule schema."""

    name: str = Field(..., min_length=1, max_length=255)
    food_type: str = Field(..., min_length=1)
    portion_grams: float = Field(..., ge=0)
    time_of_day: time
    days_of_week: str = Field(..., min_length=7, max_length=7)
    notes: Optional[str] = None


class FeedingScheduleCreate(FeedingScheduleBase):
    """Feeding schedule creation schema."""

    pass


class FeedingScheduleUpdate(BaseModel):
    """Feeding schedule update schema."""

    name: Optional[str] = None
    food_type: Optional[str] = None
    portion_grams: Optional[float] = None
    time_of_day: Optional[time] = None
    days_of_week: Optional[str] = None
    is_active: Optional[bool] = None
    notes: Optional[str] = None


class FeedingScheduleResponse(FeedingScheduleBase):
    """Feeding schedule response schema."""

    id: str
    cat_id: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True