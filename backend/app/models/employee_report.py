from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class EmployeeReports(Base):
    __tablename__ = "employee_reports"
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
    report_id = Column(Integer, ForeignKey('reports.reports_id'))

    employees = relationship("Employees", back_populates="employee_reports")
    reports = relationship("Reports", back_populates="employee_reports")
