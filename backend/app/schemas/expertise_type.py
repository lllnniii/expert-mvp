from pydantic import BaseModel, Field

class ExpertiseTypeBase(BaseModel):
    name: str = Field(..., max_length=255)

class ExpertiseTypeResponse(ExpertiseTypeBase):
    expertise_type_id: int

    class Config:
        from_attributes = True

class ExpertiseTypeCreate(ExpertiseTypeBase):
    pass