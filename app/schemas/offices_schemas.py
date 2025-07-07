import datetime
from typing import Optional

from pydantic import BaseModel, field_validator

from app.utils.functions_validator import (
    validate_cnpj,
    validate_cpf,
    validate_email,
    validate_phone,
)


class Address(BaseModel):
    street: Optional[str]
    number: Optional[str]
    district: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]


class Manager(BaseModel):
    name: str
    cpf: str
    email: Optional[str]

    @field_validator("cpf", mode="after")
    def validate_cpf(cls, value: str) -> str:
        cpf = validate_cpf(value)
        return cpf


class AccountingOffice(BaseModel):
    name: str
    cnpj: str
    address: Address
    phone: str
    email: Optional[str]
    manager: Optional[Manager]
    is_active: bool = True
    created_at: str = datetime.datetime.now(datetime.timezone.utc).isoformat()
    updated_at: Optional[str] = None

    @field_validator("cnpj", mode="after")
    def validate_cnpj(cls, value: str) -> str:
        cnpj = validate_cnpj(value)
        return cnpj

    @field_validator("email", mode="after")
    def validate_email(cls, value: str) -> str:
        email = validate_email(value)
        return email

    @field_validator("phone", mode="after")
    def validate_phone(cls, value: str) -> str:
        phone = validate_phone(value)
        return phone
