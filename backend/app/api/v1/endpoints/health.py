"""Health record endpoints."""

from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.health import HealthRecordCreate, HealthRecordResponse, HealthRecordUpdate

router = APIRouter(prefix="/cats/{cat_id}/health", tags=["health"])


@router.get("", response_model=List[HealthRecordResponse])
async def list_health_records(cat_id: UUID, db: AsyncSession = None, skip: int = 0, limit: int = 100):
    """List health records for a cat."""
    # TODO: Implement list health records
    return []


@router.post("", response_model=HealthRecordResponse, status_code=status.HTTP_201_CREATED)
async def create_health_record(cat_id: UUID, record: HealthRecordCreate, db: AsyncSession = None):
    """Create a health record."""
    # TODO: Implement create health record
    pass


@router.get("/{record_id}", response_model=HealthRecordResponse)
async def get_health_record(cat_id: UUID, record_id: UUID, db: AsyncSession = None):
    """Get health record details."""
    # TODO: Implement get health record
    pass


@router.put("/{record_id}", response_model=HealthRecordResponse)
async def update_health_record(
    cat_id: UUID, record_id: UUID, record_update: HealthRecordUpdate, db: AsyncSession = None
):
    """Update health record."""
    # TODO: Implement update health record
    pass


@router.delete("/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_health_record(cat_id: UUID, record_id: UUID, db: AsyncSession = None):
    """Delete health record."""
    # TODO: Implement delete health record
    pass