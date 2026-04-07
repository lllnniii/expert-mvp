from pydantic import BaseModel, Field
from typing import Optional
from .project import ProjectResponse

class ReportBase(BaseModel):
    project_id: int
    number: int
    validity_period: Optional[int] = None
    description: Optional[str] = None

class ReportCreate(ReportBase):
    pass

class ReportResponse(ReportBase):
    report_id: int
    project : ProjectResponse = Field(description="Project details")
    class Config:
        from_attributes = True

class ReportListResponse(BaseModel):
    reports: list[ReportResponse]