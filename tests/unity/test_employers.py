import pytest

from app.schemas.employees_schema import Employee, EmployeeIn
from app.utils.exceptions import UnprocessableData


def test_create_employee_in_with_valid_data():
    """
    Testa a criação bem-sucedida de um EmployeeIn com dados válidos.
    """
    valid_data = {
        "document": "796.346.000-18",
        "name": "João da Silva",
        "pis": "12345678901",
        "email": "joao.silva@example.com",
        "cellphone": "11987654321",
        "marital_status": "solteiro",
        "skin_color": "parda",
        "education_level": "superior completo",
        "receives_biweekly_salary": False,
        "receives_transport_allowance": True,
        "has_children_under_14": False,
    }
    # Nenhuma exceção deve ser levantada
    employee_in = EmployeeIn(**valid_data)

    assert employee_in.name == "João da Silva"
    assert employee_in.email == "joao.silva@example.com"
    assert employee_in.document == "79634600018"
    assert employee_in.receives_transport_allowance is True


def test_create_employee_in_with_invalid_cpf_raises_error():
    """
    Testa se um ValidationError é levantado ao tentar criar um EmployeeIn com um CPF inválido.
    """
    invalid_data = {
        "document": "123.456.789-33",  # Inválido, não corresponde à regex r"\d{11}"
        "name": "Maria",
        "pis": "12345678901",
        "email": "maria@example.com",
        "cellphone": "11987654321",
        "marital_status": "casado",
        "skin_color": "branca",
        "education_level": "médio",
        "receives_biweekly_salary": True,
        "receives_transport_allowance": True,
        "has_children_under_14": True,
    }

    # Verifica se um ValidationError é levantado
    with pytest.raises(UnprocessableData) as exc_info:
        EmployeeIn(**invalid_data)
    assert "Dígitos verificadores do CPF inválidos." in str(exc_info.value)


def test_create_employee_in_with_invalid_email_raises_error():
    """
    Testa se um ValidationError é levantado para um e-mail inválido.
    """
    invalid_data = {
        "document": "796.346.000-18",
        "name": "Carlos",
        "pis": "12345678901",
        "email": "email-invalido",  # Inválido
        "cellphone": "11987654321",
        "marital_status": "divorciado",
        "skin_color": "preta",
        "education_level": "pós-graduado",
        "receives_biweekly_salary": False,
        "receives_transport_allowance": False,
        "has_children_under_14": False,
    }

    with pytest.raises(UnprocessableData) as exc_info:
        EmployeeIn(**invalid_data)

    assert "Email inválido ou vazio." in str(exc_info.value)


def test_create_full_employee_model_with_valid_data():
    """
    Testa a criação bem-sucedida do modelo Employee completo, que herda de EmployeeIn.
    """
    full_employee_data = {
        "id": "some-unique-id-123",
        "files": ["file_id_1.pdf", "file_id_2.jpg"],
        "document": "79634600018",
        "name": "Ana Pereira",
        "pis": "12345678901",
        "email": "ana.pereira@example.com",
        "cellphone": "21912345678",
        "marital_status": "viúvo",
        "skin_color": "amarela",
        "education_level": "técnico",
        "receives_biweekly_salary": True,
        "receives_transport_allowance": False,
        "has_children_under_14": True,
    }

    employee = Employee(**full_employee_data)

    assert employee.id == "some-unique-id-123"
    assert employee.name == "Ana Pereira"
    assert len(employee.files) == 2
    assert employee.files[0] == "file_id_1.pdf"


def test_create_employee_model_with_invalid_phone():
    """
    Testa a criação bem-sucedida do modelo Employee completo, que herda de EmployeeIn.
    """
    full_employee_data = {
        "id": "some-unique-id-123",
        "files": ["file_id_1.pdf", "file_id_2.jpg"],
        "document": "79634600018",
        "name": "Ana Pereira",
        "pis": "12345678901",
        "email": "ana.pereira@example.com",
        "cellphone": "016912345678",
        "marital_status": "viúvo",
        "skin_color": "amarela",
        "education_level": "técnico",
        "receives_biweekly_salary": True,
        "receives_transport_allowance": False,
        "has_children_under_14": True,
    }

    employee = Employee(**full_employee_data)

    assert employee.id == "some-unique-id-123"
    assert employee.name == "Ana Pereira"
    assert len(employee.files) == 2
    assert employee.files[0] == "file_id_1.pdf"
