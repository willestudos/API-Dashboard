from fastapi import HTTPException, status


class UnprocessableData(HTTPException):
    def __init__(self, detail="Dados não processaveis."):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)


class ExistiException(HTTPException):
    def __init__(self, detail="Este recurso ja existe."):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)
