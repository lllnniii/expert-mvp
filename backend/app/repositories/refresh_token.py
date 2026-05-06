from datetime import datetime, timezone
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.refresh_token import RefreshTokens


class RefreshTokenRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, token: RefreshTokens):
        self.db.add(token)
        self.db.flush()
        return token

    def get_by_token(self, token_value: str):
        slct = select(RefreshTokens).where(RefreshTokens.token == token_value)
        result = self.db.execute(slct)
        return result.scalars().first()

    def revoke(self, token: RefreshTokens):
        token.revoked = True
        self.db.flush()
        return token

    @staticmethod
    def is_expired(refresh_token: RefreshTokens) -> bool:
        return refresh_token.expires_at.replace(tzinfo=timezone.utc) < datetime.now(timezone.utc)
