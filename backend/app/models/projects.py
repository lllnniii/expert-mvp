from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Projects(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey('employees.employee_id'), nullable=False)
    expertise_type_id = Column(Integer, ForeignKey('expertise_types.expertise_type_id'), nullable=False)
    object_id = Column(Integer, ForeignKey('objects.object_id'), nullable=False)
    contract_number = Column(String(30), index=True, nullable=False)
    contract_date = Column(Date)
    name = Column(String(255))
    status = Column(String(255))
    deadline = Column(Date)

    employees = relationship("Employees", back_populates="projects")
    expertise_types = relationship("ExpertiseTypes", back_populates="projects")
    objects = relationship("Objects", back_populates="projects")
    payments = relationship("Payments", back_populates="projects")
    reports = relationship("Reports", back_populates="projects")

    def __repr__(self):
        return f"<Projects {self.name}>"