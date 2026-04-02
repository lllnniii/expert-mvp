from pydantic import BaseModel, Field

class RoleBase(BaseModel):
    name : str = Field(..., description="Name of the role")

class RoleResponse(RoleBase):
    role_id: int

    class Config:
        from_attributes = True

class RoleCreate(RoleBase):
    pass

