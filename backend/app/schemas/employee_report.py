from pydantic import BaseModel
from backend.app.schemas.employee import EmployeeResponse
from backend.app.schemas.report import ReportResponse

class EmployeeReportBase(BaseModel):
    employee_id: int
    report_id: int

class EmployeeReportCreate(EmployeeReportBase):
    pass

class EmployeeReportResponse(EmployeeReportBase):
    id: int
    employee : EmployeeResponse
    report : ReportResponse

    class Config:
        from_attributes = True