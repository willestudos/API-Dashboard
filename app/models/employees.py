from typing import List

from pydantic import BaseModel, EmailStr, Field


class EmployeeIn(BaseModel):
    cpf: str = Field(..., regex=r"\d{11}")
    nome: str
    pis: str
    email: EmailStr
    celular: str
    estado_civil: str
    cor_pele: str
    escolaridade: str
    recebe_quinzena: bool
    recebe_vale_transporte: bool
    filhos_menor_14: bool


class Employee(EmployeeIn):
    id: str
    arquivos: List[str]  # ids do GridFS
