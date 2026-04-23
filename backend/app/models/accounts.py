from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from datetime import date
from backend.app.database import Base

class Accounts(Base):
    __tablename__ = "accounts"
    account_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255),index=True, unique=True, nullable=False)
    hashed_password = Column(String(255),nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(Date, default=date.today)
    last_login_at = Column(Date)

    employees = relationship("Employees", back_populates="accounts", uselist=False)

    def __repr__(self):
        return f"<Accounts {self.username}>"