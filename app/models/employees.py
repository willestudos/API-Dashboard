from typing import List

from pydantic import BaseModel, EmailStr, Field


class EmployeeIn(BaseModel):
    document: str = Field(..., regex=r"\d{11}")  # CPF (Brazilian ID)
    name: str
    pis: str  # Brazilian social security number
    email: EmailStr
    cellphone: str
    marital_status: str
    skin_color: str
    education_level: str
    receives_biweekly_salary: bool
    receives_transport_allowance: bool
    has_children_under_14: bool


class Employee(EmployeeIn):
    id: str
    files: List[str]  # ids do GridFS
