from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Employee(Base):
    __tablename__ = "employee"
    employee_id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey('account.account_id'), index=True)
    role_id = Column(Integer, ForeignKey('role.role_id'), index=True)
    full_name = Column(String(255), nullable=False)
    certification_info = Column(String(255))
    phone_number = Column(String(255))
    address = Column(String(255))

    roles = relationship("Role", back_populates="employee")
    account = relationship("Account", back_populates="employee")

    def __repr__(self):
        return f"<Employee {self.full_name}>"
