from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Numeric


class Base(DeclarativeBase):
    pass


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    department = Column(String(100))
    job_title = Column(String(100))
    salary = Column(Numeric(10, 2))