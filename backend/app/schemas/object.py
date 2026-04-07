from pydantic import BaseModel, Field
from typing import Optional

class ObjectBase(BaseModel):
    client_id: int
    object_name: str = Field(..., max_length=255)
    object_address: Optional[str] = None
    opos_category: Optional[str] = None
    description: Optional[str] = None


class ObjectCreate(ObjectBase):
    pass


class ObjectResponse(ObjectBase):
    object_id: int

    class Config:
        from_attributes = True
