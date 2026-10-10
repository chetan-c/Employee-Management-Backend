from database import SessionLocal
from models import Employee
from sqlalchemy import func

def add_employee():
    print()
    print("Add Employee")
    print("------------")

    try:
        employee_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        department = input("Enter department: ")
        job_title = input("Enter job title: ")
        salary = float(input("Enter monthly salary: "))

    except ValueError:
        print("Invalid input. Please enter the correct data.")
        return

    if age < 18:
        print("Employee cannot be registered because age is below 18.")
        return

    if salary <= 0:
        print("Invalid salary.")
        return

    session = SessionLocal()

    employee = Employee(
        id=employee_id,
        name=name,
        age=age,
        department=department,
        job_title=job_title,
        salary=salary
    )

    session.add(employee)

    session.commit()

    session.close()

    print("Employee added successfully.")


def view_employees():
    print()
    print("Employee List")
    print("-------------")

    session = SessionLocal()

    employees = session.query(Employee).all()

    if len(employees) == 0:
        print("No employees found.")

    else:
        for employee in employees:
            print("ID:", employee.id)
            print("Name:", employee.name)
            print("Age:", employee.age)
            print("Department:", employee.department)
            print("Job Title:", employee.job_title)
            print("Salary:", employee.salary)
            print("----------------------")

    session.close()


def search_employee():
    print()
    print("Search Employee")
    print("----------------")

    try:
        employee_id = int(input("Enter employee ID: "))
    except ValueError:
        print("Employee ID must be a number.")
        return

    session = SessionLocal()

    employee = session.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee:
        print()
        print("Employee Found")
        print("--------------")
        print("ID:", employee.id)
        print("Name:", employee.name)
        print("Age:", employee.age)
        print("Department:", employee.department)
        print("Job Title:", employee.job_title)
        print("Salary:", employee.salary)
    else:
        print("Employee not found.")

    session.close()


def update_employee():
    print()
    print("Update Employee")
    print("----------------")

    try:
        employee_id = int(input("Enter employee ID: "))
    except ValueError:
        print("Employee ID must be a number.")
        return

    session = SessionLocal()

    employee = session.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee is None:
        print("Employee not found.")
        session.close()
        return

    print()
    print("Employee Found")
    print("1. Update Salary")
    print("2. Update Department")

    choice = input("Enter your choice: ")

    if choice == "1":

        try:
            new_salary = float(input("Enter new salary: "))
        except ValueError:
            print("Salary must be a number.")
            session.close()
            return

        if new_salary <= 0:
            print("Invalid salary.")
            session.close()
            return

        employee.salary = new_salary

        session.commit()

        print("Salary updated successfully.")

    elif choice == "2":

        new_department = input("Enter new department: ")

        if new_department == "":
            print("Department cannot be empty.")
            session.close()
            return

        employee.department = new_department

        session.commit()

        print("Department updated successfully.")

    else:
        print("Invalid choice.")

    session.close()


def delete_employee():
    print()
    print("Delete Employee")
    print("----------------")

    try:
        employee_id = int(input("Enter employee ID: "))
    except ValueError:
        print("Employee ID must be a number.")
        return

    session = SessionLocal()

    employee = session.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee is None:
        print("Employee not found.")
        session.close()
        return

    session.delete(employee)
    session.commit()

    print("Employee deleted successfully.")

    session.close()


def count_employees():
    print()
    print("Employee Count")
    print("--------------")

    session = SessionLocal()

    count = session.query(func.count(Employee.id)).scalar()

    print("Total Employees:", count)

    session.close()