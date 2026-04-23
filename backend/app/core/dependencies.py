from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.core.security import decode_access_token
from backend.app.models.accounts import Accounts
from backend.app.models.refresh_token import RefreshTokens
# from backend.app.models.employees import Employees

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/account/login")

def get_current_account(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)) -> Accounts:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized")
    account_id = decode_access_token(token)
    if not account_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token")
    account = db.get(Accounts, account_id)
    if not account or not account.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Account is not found or active")

    active_refresh = db.query(RefreshTokens).filter(
        RefreshTokens.account_id == account_id,
        RefreshTokens.revoked == False).first()
    if not active_refresh:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session is done, log in again"
        )
    return account


# def get_current_employee(current_account: Accounts = Depends(get_current_account),
#         db: Session = Depends(get_db)):
#     employee = db.query(Employees).filter(
#         Employees.account_id == current_account.account_id
#     ).first()
#     if not employee:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Employee not found"
#         )
#     return employee
