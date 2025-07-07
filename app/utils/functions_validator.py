import re

from app.utils.exceptions import UnprocessableData

EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
PHONE_REGEX = r"^(" r"(\+55)?0?\d{2}\d{9}$" r"|(\+55)?\(?0?\d{2}\)?\d{5}-?\d{4}$" r")"
CNPJ_REGEX = r"^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$"


def clean_cpf_cnpj_phone(number: str) -> str:
    clean_number = "".join(filter(str.isdigit, number))
    return clean_number


def validate_cpf(cpf: str) -> str:
    cpf = clean_cpf_cnpj_phone(cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        raise UnprocessableData(
            "CPF deve conter 11 dígitos e não pode ter todos os dígitos iguais."
        )

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    if cpf[-2:] != f"{digito1}{digito2}":
        raise UnprocessableData("Dígitos verificadores do CPF inválidos.")
    return cpf


def validate_cnpj(cnpj: str) -> str:
    if cnpj == "" or not re.fullmatch(CNPJ_REGEX, cnpj) or ".." in cnpj:
        raise UnprocessableData("CNPJ inválido ou vazio.")
    cnpj = clean_cpf_cnpj_phone(cnpj)
    return cnpj


def validate_email(email: str) -> str:
    if email == "" or not re.fullmatch(EMAIL_REGEX, email) or ".." in email:
        raise UnprocessableData("Email inválido ou vazio.")
    return email


def validate_phone(phone: str) -> str:
    phone = clean_cpf_cnpj_phone(phone)

    if re.fullmatch(r"^\d{9}$", phone):
        raise UnprocessableData("Número de telefone sem DDD .")

    if not (
        re.fullmatch(r"^\d{11}$", phone)  # DDD com 2 dígitos, celular 9 dígitos
        or re.fullmatch(r"^0\d{2}\d{9}$", phone)  # DDD com 0 à esquerda, celular 9 dígitos
        or re.fullmatch(r"^55\d{2}\d{9}$", phone)  # internacional sem +
        or re.fullmatch(r"^550\d{2}\d{9}$", phone)  # internacional, DDD com zero à esquerda
    ):
        raise UnprocessableData("Número de telefone inválido.")

    return phone
