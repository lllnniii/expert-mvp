from pydantic import BaseModel
from .employee import EmployeeResponse
from .report import ReportResponse

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