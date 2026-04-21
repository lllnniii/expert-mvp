from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..core.dependencies import get_current_account
from ..models.accounts import Accounts
from ..schemas.account import AccountResponse, AccountCreate, AccountLogin
from ..services.account_service import AccountService

router = APIRouter(
    prefix="/account",
    tags=["account"]
)
COOKIE_MAX_AGE = 60 * 480

@router.post("/register", response_model=AccountResponse,
             status_code=status.HTTP_201_CREATED)
def register(account_data: AccountCreate, db: Session = Depends(get_db)):
    service = AccountService(db)
    return service.register(
        username=account_data.username,
        password=account_data.hashed_password
    )

@router.post("/login")
def login(account_data: AccountLogin,
          response: Response,
          db: Session = Depends(get_db)):
    service = AccountService(db)
    token = service.login(
        username=account_data.username,
        password=account_data.hashed_password
    )
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        samesite="lax",
        max_age=COOKIE_MAX_AGE)
    return {"message": "LOg in"}

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {"message": "Log out"}

@router.get("/me", response_model=AccountResponse)
def get_me(current_account: Accounts = Depends(get_current_account)):
    return current_account

