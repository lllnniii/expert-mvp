from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class AccountBase(BaseModel):
    username : str = Field(..., min_length=4, max_length=70,
                           description="Username to login")
    hashed_password : str = Field(..., min_length=6, max_length=128)
    is_active : bool
    created_at : date
    last_login_at: Optional[date] = None

class AccountResponse(BaseModel):
    id: int = Field(..., description="UNIQUE ID")
    username: str
    is_active: bool
    created_at: date
    last_login_at: date

    class Config:
        from_attributes = True

class AccountCreate(AccountBase):
    pass
