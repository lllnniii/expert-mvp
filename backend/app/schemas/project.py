from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import date
from .object import ObjectResponse
from .expertise_type import ExpertiseTypeResponse
from .employee import EmployeeResponse


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
    employee: EmployeeResponse
    expertise: ExpertiseTypeResponse
    object: ObjectResponse

    class Config:
        from_attributes = True

class ProjectListResponse(BaseModel):
    projects: list[ProjectResponse]

class ProjectCreate(ProjectBase):
    pass