from datetime import datetime, timedelta, timezone
from typing import Optional
import bcrypt
from jose import jwt, JWTError
from app.config import settings
import secrets


def hashed_password(password: str) -> str:
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")


def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))


def create_access_token(account_id: int, expires_minutes: Optional[int] = None) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=expires_minutes or settings.JWT_EXPIRE_MINUTES)
    payload = {
        "sub": str(account_id),
        "type": "access",
        "exp": expire,
    }
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
    return token


def decode_access_token(token: str) -> Optional[int]:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        return int(payload.get("sub"))
    except (JWTError, ValueError, TypeError, KeyError):
        return None


def create_refresh_token() -> str:
    return secrets.token_urlsafe(64)


def get_refresh_token_expiration(refresh_expire_days: int = 7) -> datetime:
    return datetime.now(timezone.utc) + timedelta(days=refresh_expire_days
                                                       or settings.REFRESH_EXPIRE_DAYS)