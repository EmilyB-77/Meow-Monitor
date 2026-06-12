"""Cat schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CatBase(BaseModel):
    """Base cat schema."""

    name: str = Field(..., min_length=1, max_length=255)
    breed: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    color: Optional[str] = None
    weight_kg: Optional[float] = Field(None, ge=0)
    microchip_number: Optional[str] = None
    description: Optional[str] = None


class CatCreate(CatBase):
    """Cat creation schema."""

    pass


class CatUpdate(BaseModel):
    """Cat update schema."""

    name: Optional[str] = None
    breed: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    color: Optional[str] = None
    weight_kg: Optional[float] = None
    microchip_number: Optional[str] = None
    description: Optional[str] = None
    profile_picture_url: Optional[str] = None


class CatResponse(CatBase):
    """Cat response schema."""

    id: str
    owner_id: str
    profile_picture_url: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True