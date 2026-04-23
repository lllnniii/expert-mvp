from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.app.database import Base

class Employees(Base):
    __tablename__ = "employees"
    employee_id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey('accounts.account_id'), index=True)
    role_id = Column(Integer, ForeignKey('roles.role_id'), index=True)
    full_name = Column(String(255), nullable=False)
    certification_info = Column(String(255))
    phone_number = Column(String(255))
    address = Column(String(255))

    roles = relationship("Roles", back_populates="employees")
    accounts = relationship("Accounts", back_populates="employees")
    employee_reports = relationship("EmployeeReports", back_populates="employees")
    projects = relationship("Projects", back_populates="employees")

    def __repr__(self):
        return f"<Employees {self.full_name}>"
