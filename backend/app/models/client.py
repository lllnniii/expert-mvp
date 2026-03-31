from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Client(Base):
    __tablename__ = "client"
    client_id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String(255),index=True, unique=True, nullable=False)
    full_name = Column(String(255), nullable=False, index=True, unique=True)
    inn = Column(String(255), unique=True, nullable=False)
    address_legal = Column(String(255))
    address_actual = Column(String(255))
    contact_person = Column(String(255))
    contact_phone = Column(String(20))
    contact_email = Column(String(255))

    object = relationship("Object", back_populates="client")

    def __repr__(self):
        return "<Client %r>" % self.client_name