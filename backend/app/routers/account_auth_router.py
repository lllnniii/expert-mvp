from fastapi import APIRouter, Depends, Response, status, HTTPException, Body
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.core.dependencies import get_current_account
from backend.app.models.accounts import Accounts
from backend.app.schemas.account import AccountResponse, AccountCreate, AccountLogin
from backend.app.services.account_service import AccountService
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/account",
    tags=["account"])


@router.post("/register", response_model=AccountResponse,
             status_code=status.HTTP_201_CREATED)
def register(account_data: AccountCreate, db: Session = Depends(get_db)):
    service = AccountService(db)
    return service.register(
        username=account_data.username,
        password=account_data.hashed_password
    )


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)):
    service = AccountService(db)
    access_token, refresh_token = service.login(
        username=form_data.username,
        password=form_data.password,)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"}


@router.post("/refresh")
def refresh(
    refresh_token: str = Body(..., embed=True),
    db: Session = Depends(get_db)):
    service = AccountService(db)
    try:
        access_token, new_refresh_token = service.refresh_tokens_service(
            refresh_token_value=refresh_token)
    except HTTPException  as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=str(e))
    return {
        "access_token": access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer"}


@router.post("/logout")
def logout(
    refresh_token: str = Body(..., embed=True),
    db: Session = Depends(get_db)):
    service = AccountService(db)
    service.logout_service(refresh_token_value=refresh_token)
    return {"detail": "Logged out"}


@router.get("/me")
def me(account: Accounts = Depends(get_current_account)):
    return account

# @router.post("/login")
# def login(account_data: AccountLogin,
#           response: Response,
#           db: Session = Depends(get_db)):
#     service = AccountService(db)
#     token = service.login(
#         username=account_data.username,
#         password=account_data.hashed_password
#     )
#     response.set_cookie(
#         key="access_token",
#         value=token,
#         httponly=True,
#         samesite="lax",
#         max_age=COOKIE_MAX_AGE)
#     return {"message": "LOg in"}
#
# @router.post("/logout")
# def logout(response: Response):
#     response.delete_cookie(key="access_token")
#     return {"message": "Log out"}