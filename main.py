from fastapi import FastAPI
from database import SessionLocal
from models import Employee
from fastapi import HTTPException
from schemas import EmployeeResponse ,EmployeeCreate , EmployeeUpdate


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Employee Management API is running"}

@app.get("/employees", response_model=list[EmployeeResponse])
def get_employee():
    session = SessionLocal()
    employees = session.query(Employee).all()
    session.close()
    return employees

@app.post("/employees" , response_model= EmployeeResponse , status_code=201)
def create_employee(employee_data : EmployeeCreate):
    session = SessionLocal()

    try:
        employee = Employee(
            id=employee_data.id,
            name=employee_data.name,
            age= employee_data.age,
            department = employee_data.department,
            job_title=employee_data.job_title,
            salary=employee_data.salary
        )

        session.add(employee)
        session.commit()
        session.refresh(employee)

        return employee
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int):
    session = SessionLocal()

    try:
        employee = session.query(Employee).filter(
            Employee.id == employee_id
        ).first()

        if employee is None:
            raise HTTPException(
                status_code=404,
                detail="Employee not found"
            )

        return employee

    finally:
        session.close()


@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(employee_id: int, employee_data: EmployeeUpdate):
    session = SessionLocal()

    try:
        employee = session.query(Employee).filter(
            Employee.id == employee_id
        ).first()

        if employee is None:
            raise HTTPException(
                status_code=404,
                detail="Employee not found"
            )

        employee.name = employee_data.name
        employee.age = employee_data.age
        employee.department = employee_data.department
        employee.job_title = employee_data.job_title
        employee.salary = employee_data.salary

        session.commit()
        session.refresh(employee)

        return employee

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()



@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    session = SessionLocal()

    try:
        employee = session.query(Employee).filter(
            Employee.id == employee_id
        ).first()

        if employee is None:
            raise HTTPException(
                status_code=404,
                detail="Employee not found"
            )

        session.delete(employee)
        session.commit()

        return {
            "message": "Employee deleted successfully",
            "employee_id": employee_id
        }

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()

