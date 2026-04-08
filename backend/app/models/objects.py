from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Objects(Base):
    __tablename__ = "objects"
    object_id = Column(Integer, primary_key=True, nullable=False)
    client_id = Column(Integer, ForeignKey("clients.client_id"), nullable=False)
    object_name = Column(String(255), nullable=False)
    object_address = Column(String(255))
    opos_category = Column(String(255))
    description = Column(String)

    clients = relationship("Clients", back_populates="objects")
    projects = relationship("Projects", back_populates="objects")

    def __repr__(self):
        return "<Objects %r>" % self.object_id