from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Optional
from app.models.employees import Employees
from app.schemas.employee import EmployeeCreate, EmployeeUpdate

class EmployeeRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Employees]:
        result = self.db.execute(select(Employees))
        return list(result.scalars().all())

    def get_by_employee_id(self, employee_id: int) -> Optional[Employees]:
        slct = select(Employees).where(Employees.employee_id == employee_id)
        result = self.db.execute(slct)
        return result.scalars().first()

    def get_by_employee_name(self, employee_name: str) -> List[Employees]:
        slct = select(Employees).where(
            Employees.full_name.ilike(f"{employee_name}"))
        result = self.db.execute(slct)
        return list(result.scalars().all())

    def set_account(self, employee: Employees, account_id: int):
        employee.account_id = account_id
        self.db.flush()

    def create_employee(self, employee_data : EmployeeCreate) -> Employees:
        db_employee = Employees(**employee_data.model_dump())
        self.db.add(db_employee)
        try:
            self.db.commit()
            self.db.refresh(db_employee)
            return db_employee
        except Exception:
            self.db.rollback()
            raise

    def update_employee(self, employee_id: int, employee_data: EmployeeUpdate) -> Optional[Employees]:
        db_employee = self.get_by_employee_id(employee_id)
        if not db_employee:
            return None
        update_data = employee_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_employee, key, value)
        try:
            self.db.commit()
            self.db.refresh(db_employee)
            return db_employee
        except Exception:
            self.db.rollback()
            raise

    def delete_employee(self, employee_id: int):
        db_employee = self.get_by_employee_id(employee_id)
        if not db_employee:
            return False
        try:
            self.db.delete(db_employee)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            raise