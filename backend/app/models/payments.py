from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Payments(Base):
    __tablename__ = "payments"
    payment_id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    amount = Column(Numeric(10,2))
    date = Column(Date)
    status = Column(String)

    projects = relationship("Projects", back_populates="payments")

    def __repr__(self):
        return f"<Payments payment_id: {self.payment_id}>"