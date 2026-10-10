
from pydantic import BaseModel, Field, ConfigDict


class EmployeeCreate(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=18)
    department: str = Field(min_length=1, max_length=100)
    job_title: str = Field(min_length=1, max_length=100)
    salary: float = Field(gt=0)


class EmployeeUpdate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=18)
    department: str = Field(min_length=1, max_length=100)
    job_title: str = Field(min_length=1, max_length=100)
    salary: float = Field(gt=0)


class EmployeeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    age: int
    department: str
    job_title: str
    salary: float