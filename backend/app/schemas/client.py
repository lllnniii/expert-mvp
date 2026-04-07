from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class ClientBase(BaseModel):
    client_name : str = Field(..., min_length=4, max_length=70)
    full_name : str = Field(..., max_length=255)
    inn : str = Field(..., max_length=255)
    address_legal : str = Field(..., max_length=255)
    address_actual : str = Field(..., max_length=255)
    contact_person : str = Field(..., max_length=255)
    contact_phone : str = Field(..., max_length=255)
    contact_email : Optional[EmailStr] = Field(None, max_length=255)


class ClientResponse(BaseModel):
    id: int = Field(..., description="UNIQUE ID")
    client_name : str
    full_name : str
    inn : str
    address_legal : Optional[str]
    address_actual : Optional[str]
    contact_person : Optional[str]
    contact_phone : Optional[str]
    contact_email : Optional[EmailStr]
    class Config:
        from_attributes = True

class ClientCreate(ClientBase):
    pass
