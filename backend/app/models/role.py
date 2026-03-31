from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Role(Base):
    __tablename__ = "role"
    role_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    employee = relationship("Employee", back_populates="role")

    def __repr__(self):
        return f"<Role {self.name}>"