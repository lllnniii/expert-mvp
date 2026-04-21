from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import List
from ..models.accounts import Accounts
from ..repositories.account_repository import AccountRepository
from ..schemas.account import AccountResponse, AccountCreate
from fastapi import HTTPException, status
from ..core.security import hashed_password, verify_password, create_access_token


class AccountService:
    def __init__(self, db : Session):
        self.repository = AccountRepository(db)

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
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Account with username '{username}' already exists")
        new_account = AccountCreate(
            username=username,
            hashed_password=hashed_password(password))
        try:
            created = self.repository.create_account(new_account)
            return AccountResponse.model_validate(created)
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Account already exists")

    def login(self, username: str, password: str) -> str:
        account = self.repository.get_by_account_username(username)
        if not account or not verify_password(password, account.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
        if not account.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account is blocked"
            )
        return create_access_token(account.account_id)