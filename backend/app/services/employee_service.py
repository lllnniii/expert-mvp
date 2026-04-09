from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import List
from ..models.employees import Employees
from ..repositories.employee_repository import EmployeeRepository
from ..schemas.employee import EmployeeResponse, EmployeeCreate, EmployeeUpdate
from fastapi import HTTPException, status

class EmployeeService:
    def __init__(self, db : Session):
        self.repository = EmployeeRepository(db)

    def get_all_employees(self) -> List[EmployeeResponse]:
        employees = self.repository.get_all()
        return [EmployeeResponse.model_validate(e) for e in employees]

    def get_employee_by_id(self, employee_id: int ) -> EmployeeResponse:
        employee = self.repository.get_by_employee_id(employee_id)
        if not employee:
            raise HTTPException(status_code=404,
                                detail=f"Employee with {employee_id} was not found")
        return EmployeeResponse.model_validate(employee)

    def get_employee_by_name(self, employee_name: str) -> List[EmployeeResponse]:
        employee = self.repository.get_by_employee_name(employee_name)
        if not employee:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee with name '{employee_name}' not found")
        return [EmployeeResponse.model_validate(cl) for cl in employee]

    def create_employee(self, employee_data: EmployeeCreate) -> EmployeeResponse:
        try:
            employee = self.repository.create_employee(employee_data)
            return EmployeeResponse.model_validate(employee)
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail="Employee with this data already exists or violates constraints")
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An unexpected error occurred: {str(e)}")

    def update_employee(self, employee_id: int, employee_data: EmployeeUpdate) -> EmployeeResponse:
        updated_employee = self.repository.update_employee(employee_id, employee_data)
        if not updated_employee:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee with id {employee_id} not found")
        return EmployeeResponse.model_validate(updated_employee)

    def delete_employee(self, employee_id: int) -> None:
        success = self.repository.delete_employee(employee_id)
        if not success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee with id {employee_id} not found")
        return None