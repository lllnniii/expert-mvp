from pydantic import BaseModel, Field
from typing import Optional
from app.schemas.client import ClientResponse

class ObjectBase(BaseModel):
    client_id: int
    object_name: str = Field(..., max_length=255)
    object_address: Optional[str] = None
    opos_category: Optional[str] = None
    description: Optional[str] = None


class ObjectCreate(ObjectBase):
    pass

class ObjectResponse(BaseModel):
    object_id: int
    client_id: int
    object_name: str = Field(..., max_length=255)
    object_address: Optional[str] = None
    opos_category: Optional[str] = None
    description: Optional[str] = None
    client: ClientResponse
    class Config:
        from_attributes = True

class ObjectUpdate(BaseModel):
    object_name: Optional[str] = None
    object_address: Optional[str] = None
    opos_category: Optional[str] = None
    description: Optional[str] = None

class ObjectListResponses(BaseModel):
    objects : list[ObjectResponse]
    total : int