from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Optional
from backend.app.models.accounts import Accounts
from backend.app.schemas.account import AccountCreate


class AccountRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Accounts]:
        result = self.db.execute(select(Accounts))
        return list(result.scalars().all())

    def get_by_account_id(self, account_id: int) -> Optional[Accounts]:
        slct = select(Accounts).where(Accounts.account_id == account_id)
        result = self.db.execute(slct)
        return result.scalars().first()

    def get_by_account_username(self, username: str) -> Optional[Accounts]:
        slct = select(Accounts).where(Accounts.username == username)
        result = self.db.execute(slct)
        return result.scalars().first()

    def create_account(self, account_data : AccountCreate) -> Accounts:
        db_acc = Accounts(**account_data.model_dump())
        self.db.add(db_acc)
        try:
            self.db.commit()
            self.db.refresh(db_acc)
            return db_acc
        except Exception:
            self.db.rollback()
            raise

    def delete_account(self, account_id: int):
        db_account = self.get_by_account_id(account_id)
        if not db_account:
            return False
        try:
            self.db.delete(db_account)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            raise
