import pytest

from app.utils.exceptions import CPFInvalidError, EmailInvalidError, PhoneInvalidError
from app.utils.functions_validator import (
    clean_cpf_cnpj_phone,
    validate_cpf,
    validate_email,
    validate_phone,
)


@pytest.mark.parametrize(
    "input_value,expected_output",
    [
        ("123.456.789-00", "12345678900"),
        ("11 222 333 4444", "112223334444"),
        ("+55 (21) 98888-7777", "5521988887777"),
        ("", ""),
        ("abc123!@#", "123"),
        ("000.000.000-00", "00000000000"),
        ("55-99-8888-7777", "559988887777"),
    ],
)
def test_clean_cpf_cnpj_phone(input_value, expected_output):
    assert clean_cpf_cnpj_phone(input_value) == expected_output


@pytest.mark.parametrize(
    "valid_email",
    [
        "usuario@example.com",
        "user.name+ext@sub.domain.com",
        "user_name@domain.co",
        "user-name@domain.io",
        "test123@email.com",
    ],
)
def test_validate_email_accepts_valid_emails(valid_email):
    assert validate_email(valid_email) == valid_email


@pytest.mark.parametrize(
    "invalid_email",
    [
        "",
        "plainaddress",
        "@no-local-part.com",
        "noatsign.com",
        "user@.com",
        "user@domain",
        "user@domain..com",
        "user@domain,com",
        "user@domain com",
        "user@domain@domain.com",
    ],
)
def test_validate_email_raises_for_invalid_emails(invalid_email):
    with pytest.raises(EmailInvalidError) as exc_info:
        validate_email(invalid_email)
    assert "Email inválido" in str(exc_info.value)


@pytest.mark.parametrize(
    "valid_phone",
    [
        # celulares com DDD (nove dígitos, formato mais comum)
        "11987654321",  # DDD 11
        "(11)987654321",  # Com parênteses e sem traço
        "011987654321",  # Com zero à esquerda do DDD
        "+5511987654321",  # Com +55 (internacional)
        "5511987654321",  # Sem o sinal de + no internacional
        "55011987654321",  # Internacional e DDD com zero
        "21 91234-5678",  # Com espaço e traço
        # outros formatos que serão limpos com clean_cpf_cnpj_phone
        "21-98765-4321",
        "21.98765.4321",
    ],
)
def test_validate_phone_accepts_valid_phones(valid_phone):
    # Deve retornar só os números
    result = validate_phone(valid_phone)
    assert result.isdigit()
    assert len(result) in {11, 12, 13, 14}  # Possíveis formatos limpos


@pytest.mark.parametrize(
    "invalid_phone",
    [
        "",  # vazio
        "987654321",  # 9 dígitos, mas sem DDD
        "12345",  # muito curto
        "+550119876543",  # internacional, mas faltando dígitos
        "a1987654321",  # caractere inválido
        "1187654321",  # só 10 dígitos (faltando 1 do número moderno)
        "0211234567",  # formato inválido
        "1199999-999",  # dígitos insuficientes após limpeza
    ],
)
def test_validate_phone_raises_error_for_invalid_phones(invalid_phone):
    with pytest.raises(PhoneInvalidError):
        validate_phone(invalid_phone)


@pytest.mark.parametrize(
    "cpf",
    [
        "796.346.000-18",  # Válido, com pontos e traço
        "79634600018",  # Válido, apenas números
        "123.456.789-09",  # Válido (exemplo genérico válido)
        "529.982.247-25",  # Válido, comum em bases públicas
    ],
)
def test_validate_cpf_accepts_valid_cpfs(cpf):
    result = validate_cpf(cpf)
    assert isinstance(result, str)
    assert result.isdigit()
    assert len(result) == 11


@pytest.mark.parametrize(
    "cpf",
    [
        "111.111.111-11",  # Todos dígitos iguais
        "123.456.789-33",  # Dígitos verificadores inválidos
        "00000000000",  # Todos dígitos iguais
        "123456789",  # Menos de 11 dígitos
        "00011122233",  # Dígitos verificadores inválidos
        "",  # String vazia
        "123abc45678",  # Caracteres não numéricos
        "529.982.247.250",  # Formato inválido (ponto extra, dígito torto)
    ],
)
def test_validate_cpf_rejects_invalid_cpfs(cpf):
    with pytest.raises(CPFInvalidError):
        validate_cpf(cpf)
