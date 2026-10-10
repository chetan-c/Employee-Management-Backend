
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Employee Management API is running"
    }


def test_get_employees():
    response = client.get("/employees")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_employee_not_found():
    response = client.get("/employees/999999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Employee not found"
    }


def test_create_employee_rejects_invalid_data():
    response = client.post(
        "/employees",
        json={
            "id": 107,
            "name": "Test Employee",
            "age": 16,
            "department": "IT",
            "job_title": "Developer",
            "salary": 0
        }
    )

    assert response.status_code == 422