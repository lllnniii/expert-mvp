from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from backend.app.database import get_db
from backend.app.services.employee_service import EmployeeService
from backend.app.schemas.employee import EmployeeResponse, EmployeeCreate, EmployeeUpdate

router = APIRouter(
    prefix="/api/employees",
    tags=["employees"])

@router.get("", response_model=List[EmployeeResponse], status_code=status.HTTP_200_OK)
def get_employees(db: Session = Depends(get_db)):
    service = EmployeeService(db)
    return service.get_all_employees()

@router.get("/{employee_id}", response_model=EmployeeResponse, status_code=status.HTTP_200_OK)
def get_employee_by_id(employee_id: int, db: Session = Depends(get_db)):
    service = EmployeeService(db)
    return service.get_employee_by_id(employee_id)

@router.get("/by-name/{name}", response_model= EmployeeResponse, status_code=status.HTTP_200_OK)
def get_employee_by_name(name: str, db: Session = Depends(get_db)):
    service = EmployeeService(db)
    return service.get_employee_by_name(name)

@router.post("", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(data : EmployeeCreate,db: Session = Depends(get_db)):
    service = EmployeeService(db)
    return service.create_employee(data)

@router.patch("/{employee_id}", response_model=EmployeeResponse, status_code=status.HTTP_200_OK)
def update_employee_by_id(employee_id: int, data: EmployeeUpdate, db: Session = Depends(get_db)):
    service = EmployeeService(db)
    return service.update_employee(employee_id, data)

@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee_by_id(employee_id: int, db: Session = Depends(get_db)):
    service = EmployeeService(db)
    return service.delete_employee(employee_id)