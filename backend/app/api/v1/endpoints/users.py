"""User endpoints."""

from fastapi import APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import create_access_token, create_refresh_token, get_password_hash
from app.db.database import get_db
from app.schemas.user import TokenResponse, UserCreate, UserLogin

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=dict)
async def register(user: UserCreate, db: AsyncSession = None):
    """Register a new user."""
    # TODO: Implement user registration
    # - Check if user already exists
    # - Hash password
    # - Create user in database
    return {"message": "User registration endpoint"}


@router.post("/login", response_model=TokenResponse)
async def login(credentials: UserLogin, db: AsyncSession = None):
    """Login user and return tokens."""
    # TODO: Implement user login
    # - Find user by email
    # - Verify password
    # - Create and return tokens
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
    )


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(refresh_token: str):
    """Refresh access token."""
    # TODO: Implement token refresh
    pass


@router.get("/me")
async def get_current_user():
    """Get current user profile."""
    # TODO: Implement get current user
    pass