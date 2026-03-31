from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Object(Base):
    __tablename__ = "object"
    object_id = Column(Integer, primary_key=True, nullable=False)
    client_id = Column(Integer, ForeignKey("client.client_id"), nullable=False)
    object_name = Column(String(255), nullable=False)
    object_address = Column(String(255))
    opos_category = Column(String(255))
    description = Column(String)

    client = relationship("Client", back_populates="object")

    def __repr__(self):
        return "<Object %r>" % self.object_id