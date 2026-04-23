from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from backend.app.database import Base

class ExpertiseTypes (Base):
    __tablename__ = "expertise_types"
    expertise_type_id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(255))

    projects = relationship("Projects", back_populates="expertise_types")

    def __repr__(self):
        return f"<ExpertiseTypes {self.name}>"