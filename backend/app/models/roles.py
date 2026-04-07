from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Roles(Base):
    __tablename__ = "roles"
    role_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    employees = relationship("Employees", back_populates="roles")

    def __repr__(self):
        return f"<Roles {self.name}>"