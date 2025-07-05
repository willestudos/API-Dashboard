class CPFInvalidError(Exception):
    def __init__(self, message="CPF inválido."):
        super().__init__(message)


class EmailInvalidError(Exception):
    def __init__(self, message="E-mail inválido."):
        super().__init__(message)


class PhoneInvalidError(Exception):
    def __init__(self, message="Telefone inválido."):
        super().__init__(message)
