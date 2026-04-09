from pydantic import BaseModel, Field
from typing import Optional
from .role import  RoleResponse
from .account import AccountResponse

class EmployeeBase(BaseModel):
    account_id : int = Field(..., description="Account ID")
    role_id : int = Field(..., description="Role ID")
    full_name : str = Field(..., min_length=2, max_length=255,
                            description="Full name of the employee")
    certification_info : str = Field(... ,description="Certification information of the employee")
    phone_number : Optional[str] = Field(None,description="Employee's phone")
    address :Optional[str]


class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(BaseModel):
    employee_id : int = Field(..., description="unique employee id")
    account_id : int
    role_id : int
    full_name : str
    certification_info : Optional[str]
    phone_number : Optional[str]
    address : Optional[str]
    role : RoleResponse
    account : AccountResponse

    class Config:
        from_attributes = True

class EmployeeUpdate(BaseModel):
    account_id: Optional[int] = Field(None, description="Account ID")
    role_id: Optional[int] = Field(None, description="Role ID")
    full_name: Optional[str] = Field(None, min_length=2, max_length=255,
                           description="Full name of the employee")
    certification_info: Optional[str] = Field(None, description="Certification information of the employee")
    phone_number: Optional[str] = Field(None, description="Employee's phone")
    address: Optional[str] = Field(None, description="Employee's address")

class EmployeeListResponse(BaseModel):
    employees : list[EmployeeResponse]
