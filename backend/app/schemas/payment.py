from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import date
from decimal import Decimal
from .project import ProjectResponse

PaymentStatus = Literal["ожидает оплаты", "оплачен", "частично оплачен", "просрочен"]

class PaymentBase(BaseModel):
    project_id: int
    amount: Decimal
    date: Optional[date] = None
    status: PaymentStatus = "ожидает оплаты"

class PaymentCreate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    payment_id: int
    project : ProjectResponse

    class Config:
        from_attributes = True

class PaymentUpdate(PaymentBase):
    pass