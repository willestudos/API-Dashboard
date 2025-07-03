from typing import List

from pydantic import BaseModel, Field

EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


class EmployeeIn(BaseModel):
    document: str = Field(..., pattern=r"\d{11}")  # CPF (Brazilian ID)
    name: str
    pis: str  # Brazilian social security number
    email: str = Field(..., pattern=EMAIL_REGEX)
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
