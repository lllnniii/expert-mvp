from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import List
from ..models.accounts import Accounts
from ..repositories.account_repository import AccountRepository
from ..schemas.account import AccountResponse, AccountCreate
from fastapi import HTTPException, status

class AccountService:
    def __init__(self, db : Session):
        self.repository = AccountRepository(db)

    def get_all_accounts(self) -> List[AccountResponse]:
        accounts = self.repository.get_all()
        return [AccountResponse.model_validate(ac) for ac in accounts]

    def get_accountt_by_id(self, acccount_id: int ) -> AccountResponse:
        account = self.repository.get_by_account_id(acccount_id)
        if not account:
            raise HTTPException(status_code=404,
                                detail=f"Account with {acccount_id} was not found")
        return AccountResponse.model_validate(account)

    def get_by_username(self, username: str) -> AccountResponse:
        account = self.repository.get_by_account_username(username)
        if not account:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Account with username '{username}' not found")
        return AccountResponse.model_validate(account)
