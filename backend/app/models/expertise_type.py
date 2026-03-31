from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from ..database import Base

class ExpertiseType (Base):
    __tablename__ = "expertise_type"
    expertise_type_id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(255))

    projects = relationship("Project", back_populates="expertise_type")

    def __repr__(self):
        return f"<ExpertiseType {self.name}>"