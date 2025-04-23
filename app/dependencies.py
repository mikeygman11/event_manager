# app/dependencies.py
from typing import List, Union

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError

from app.database import Database
from app.services.email_service import EmailService
from app.utils.template_manager import TemplateManager
from app.services.jwt_service import decode_token
from settings.config import settings       # this is the singleton Settings() you defined
from app.models.user_model import UserRole

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_settings():
    """Return the global Settings object."""
    return settings


def get_email_service() -> EmailService:
    """Provide a fresh EmailService (with its TemplateManager) per‐request."""
    tm = TemplateManager()
    return EmailService(template_manager=tm)


async def get_db() -> AsyncSession:
    """
    Yield a database session per‐request. Rolls back & 500s on errors.
    """
    factory = Database.get_session_factory()
    async with factory() as session:
        try:
            yield session
        except Exception as e:
            # bubble up as a 500 so your global error‐handler can catch it
            raise HTTPException(status_code=500, detail=str(e))


def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """
    Decode the Bearer JWT, ensure it has sub & role, or 401.
    Returns: {"email": "...", "role": "ADMIN"}
    """
    creds_exc = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_token(token)
    except JWTError:
        raise creds_exc

    if not payload:
        raise creds_exc

    user_email = payload.get("sub")
    user_role  = payload.get("role")
    if not user_email or not user_role:
        raise creds_exc

    return {"email": user_email, "role": user_role}


def require_role(allowed: List[Union[str, UserRole]]):
    """
    Returns a dependency which 403s unless current_user["role"] ∈ allowed.
    You can pass in enum members or strings, e.g. [UserRole.ADMIN] or ["ADMIN"].
    """
    # normalize everything to the string names
    allowed_names = { r.name if isinstance(r, UserRole) else r for r in allowed }

    def role_checker(current_user: dict = Depends(get_current_user)) -> dict:
        if current_user["role"] not in allowed_names:
            raise HTTPException(status_code=403, detail="Operation not permitted")
        return current_user

    return role_checker
