"""Cat endpoints."""

from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.cat import CatCreate, CatResponse, CatUpdate

router = APIRouter(prefix="/cats", tags=["cats"])


@router.get("", response_model=List[CatResponse])
async def list_cats(db: AsyncSession = None, skip: int = 0, limit: int = 100):
    """List all cats for current user."""
    # TODO: Implement list cats
    # - Get current user
    # - Query cats for that user
    return []


@router.post("", response_model=CatResponse, status_code=status.HTTP_201_CREATED)
async def create_cat(cat: CatCreate, db: AsyncSession = None):
    """Create a new cat."""
    # TODO: Implement create cat
    # - Get current user
    # - Create cat record
    pass


@router.get("/{cat_id}", response_model=CatResponse)
async def get_cat(cat_id: UUID, db: AsyncSession = None):
    """Get cat details."""
    # TODO: Implement get cat
    # - Verify ownership
    # - Return cat details
    pass


@router.put("/{cat_id}", response_model=CatResponse)
async def update_cat(cat_id: UUID, cat_update: CatUpdate, db: AsyncSession = None):
    """Update cat information."""
    # TODO: Implement update cat
    pass


@router.delete("/{cat_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cat(cat_id: UUID, db: AsyncSession = None):
    """Delete a cat."""
    # TODO: Implement delete cat
    pass