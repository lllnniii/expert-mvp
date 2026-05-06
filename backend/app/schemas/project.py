from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import date
from app.schemas.object import ObjectResponse
from app.schemas.expertise_type import ExpertiseTypeResponse
from app.schemas.employee import EmployeeResponse


ProjectStatus = Literal["в процессе", "завершен"]

class ProjectBase(BaseModel):
    employee_id: int
    expertise_type_id: int
    object_id: int
    contract_number: str = Field(..., max_length=30)
    contract_date: Optional[date] = None
    name: str = Field(..., max_length=255)
    status: ProjectStatus = "в процессе"
    deadline: Optional[date] = None

class ProjectResponse(BaseModel):
    project_id: int
    employee_id: int
    expertise_type_id: int
    object_id: int
    contract_number: str
    contract_date: Optional[date] = None
    name: str
    status: ProjectStatus
    deadline: Optional[date] = None
    employees: EmployeeResponse
    expertise_types: ExpertiseTypeResponse
    objects: ObjectResponse

    class Config:
        from_attributes = True

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass