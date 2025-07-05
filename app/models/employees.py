from typing import List

from pydantic import BaseModel, Field, field_validator

from app.utils.functions_validator import validate_cpf, validate_email, validate_phone


class EmployeeIn(BaseModel):
    document: str = Field(..., title="CPF", description="Numeros do CPF")  # CPF (Brazilian ID)
    name: str = Field(..., title="Nome", description="Nome Complerto")
    pis: str = Field(..., title="Pais", description="Pais nascimento")
    email: str = Field(..., title="E-mail", description="Email Valido")
    cellphone: str = Field(..., title="Celular", description="Numero Celular")
    marital_status: str = Field(..., title="CPF", description="Numeros do CPF")
    skin_color: str = Field(..., title="Cor", description="Cor da péle")
    education_level: str = Field(..., title="Escolaridade", description="Grau de escolaridade")
    receives_biweekly_salary: bool = Field(
        ..., title="Quizena", description="Receber salário quinzenal"
    )
    receives_transport_allowance: bool = Field(
        ..., title="Vale transporte", description="Receber vale transporte"
    )
    has_children_under_14: bool = Field(
        ..., title="Filhos menor 14", description="Filhos menor 14 anos de idade"
    )

    @field_validator("document", mode="after")
    def validate_cpf(cls, value: str) -> str:
        cpf = validate_cpf(value)
        return cpf

    @field_validator("email", mode="after")
    def validate_email(cls, value: str) -> str:
        email = validate_email(value)
        return email

    @field_validator("cellphone", mode="after")
    def validate_phone(cls, value: str) -> str:
        phone = validate_phone(value)
        return phone


class Employee(EmployeeIn):
    id: str
    files: List[str]  # ids do GridFS
