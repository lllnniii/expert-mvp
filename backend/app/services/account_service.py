from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import List
from ..models.accounts import Accounts
from ..models.refresh_token import RefreshTokens
from ..repositories.account_repository import AccountRepository
from ..repositories.refresh_token import RefreshTokenRepository
from ..schemas.account import AccountResponse, AccountCreate
from fastapi import HTTPException, status
from ..core.security import (hashed_password, verify_password, create_access_token,
                             create_refresh_token, get_refresh_token_expiration)
from datetime import datetime, timezone

class AccountService:
    def __init__(self, db : Session):
        self.repository = AccountRepository(db)
        self.refresh_repo = RefreshTokenRepository(db)

    def get_all_accounts(self) -> List[AccountResponse]:
        accounts = self.repository.get_all()
        return [AccountResponse.model_validate(ac) for ac in accounts]

    def get_account_by_id(self, account_id: int ) -> AccountResponse:
        account = self.repository.get_by_account_id(account_id)
        if not account:
            raise HTTPException(status_code=404,
                                detail=f"Account with {account_id} was not found")
        return AccountResponse.model_validate(account)

    def get_by_username(self, username: str) -> AccountResponse:
        account = self.repository.get_by_account_username(username)
        if not account:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Account with username '{username}' not found")
        return AccountResponse.model_validate(account)


    def register(self, username: str, password: str) -> AccountResponse:
        existing = self.repository.get_by_account_username(username)
        if existing:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"Account with username '{username}' already exists")
        new_account = AccountCreate(
            username=username,
            hashed_password=hashed_password(password))
        try:
            created = self.repository.create_account(new_account)
            return AccountResponse.model_validate(created)
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="Account already exists")

    def login(self, username: str, password: str) -> tuple[str, str]:
        account = self.repository.get_by_account_username(username)
        if not account or not verify_password(password, account.hashed_password):
            raise HTTPException(401, "Incorrect username or password")
        if not account.is_active:
            raise HTTPException(403, "Account is blocked")
        access_token = create_access_token(account.account_id)
        refresh_value = create_refresh_token()
        refresh_token = RefreshTokens(
            token=refresh_value,
            account_id=account.account_id,
            expires_at=get_refresh_token_expiration())
        self.refresh_repo.create(refresh_token)
        self.refresh_repo.db.commit()
        return access_token, refresh_value

    def refresh_tokens_service(self, refresh_token_value: str) -> tuple[str, str]:
        token = self.refresh_repo.get_by_token(refresh_token_value)
        if not token or token.revoked:
            raise HTTPException(403, "Invalid refresh token")
        if token.expires_at.replace(tzinfo=timezone.utc) < datetime.now(timezone.utc):
            self.refresh_repo.revoke(token)
            self.refresh_repo.db.commit()
            raise HTTPException(403, "Refresh token expired")
        account_id = token.account_id
        self.refresh_repo.revoke(token)
        new_refresh_value = create_refresh_token()
        new_refresh = RefreshTokens(
            token=new_refresh_value,
            account_id=account_id,
            expires_at=get_refresh_token_expiration()
        )
        self.refresh_repo.create(new_refresh)
        access_token = create_access_token(account_id)
        self.refresh_repo.db.commit()
        return access_token, new_refresh_value

    def logout_service(self, refresh_token_value: str):
        token = self.refresh_repo.get_by_token(refresh_token_value)
        if token and not token.revoked:
            self.refresh_repo.revoke(token)
            self.refresh_repo.db.commit()
