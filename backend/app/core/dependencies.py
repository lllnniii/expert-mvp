from fastapi import Cookie, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import Optional
from backend.app.database import get_db
from backend.app.core.security import decode_access_token
from backend.app.models.accounts import Accounts
from backend.app.models.employees import Employees


def get_current_account(access_token: Optional[str] = Cookie(default=None),
        db: Session = Depends(get_db)):
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Un authorized"
        )
    account_id = decode_access_token(access_token)
    if not account_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    account = db.get(Accounts, account_id)
    if not account or not account.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Account is not found or active"
        )
    return account


def get_current_employee(current_account: Accounts = Depends(get_current_account),
        db: Session = Depends(get_db)):
    employee = db.query(Employees).filter(
        Employees.account_id == current_account.account_id
    ).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    return employee
