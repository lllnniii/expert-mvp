from sqlalchemy import Column, Integer, String, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship
from ..database import Base

class Reports(Base):
    __tablename__ = "reports"
    report_id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    number = Column(Integer, index=True)
    validity_period = Column(SmallInteger)
    description = Column(String(255))

    projects = relationship("Projects", back_populates="reports")
    employee_reports = relationship("EmployeeReport", back_populates="reports")

    def __repr__(self):
        return f"<Reports: {self.report_id}>"