import re

from app.utils.exceptions import CPFInvalidError, EmailInvalidError, PhoneInvalidError

EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
PHONE_REGEX = r"^(" r"(\+55)?0?\d{2}\d{9}$" r"|(\+55)?\(?0?\d{2}\)?\d{5}-?\d{4}$" r")"


def clean_cpf_cnpj_phone(number: str) -> str:
    clean_number = "".join(filter(str.isdigit, number))
    return clean_number


def validate_cpf(cpf: str) -> str:
    cpf = clean_cpf_cnpj_phone(cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        raise CPFInvalidError("CPF deve conter 11 dígitos e não pode ter todos os dígitos iguais.")

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    if cpf[-2:] != f"{digito1}{digito2}":
        raise CPFInvalidError("Dígitos verificadores do CPF inválidos.")
    return cpf


def validate_email(email: str) -> str:

    if email == "" or not re.fullmatch(EMAIL_REGEX, email):
        raise EmailInvalidError("Email inválido ou vazio.")
    return email


def validate_phone(phone: str) -> str:
    phone = clean_cpf_cnpj_phone(phone)

    if re.fullmatch(r"^\d{9}$", phone):
        raise PhoneInvalidError("Número de telefone sem DDD .")

    if not (
        re.fullmatch(r"^\d{11}$", phone)  # DDD com 2 dígitos, celular 9 dígitos
        or re.fullmatch(r"^0\d{2}\d{9}$", phone)  # DDD com 0 à esquerda, celular 9 dígitos
        or re.fullmatch(r"^55\d{2}\d{9}$", phone)  # internacional sem +
        or re.fullmatch(r"^550\d{2}\d{9}$", phone)  # internacional, DDD com zero à esquerda
    ):
        raise PhoneInvalidError("Número de telefone inválido.")

    return phone
