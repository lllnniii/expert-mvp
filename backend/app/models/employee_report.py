from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class EmployeeReport(Base):
    __tablename__ = "employee_report"
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
    report_id = Column(Integer, ForeignKey('reports.reports_id'))

    employee = relationship("Employees", back_populates="employee_report")
    report = relationship("Reports", back_populates="employee_report")
