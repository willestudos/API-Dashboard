from app.repository.offices_repository import OfficesRepository


class OfficesMembersService:
    def __init__(self):
        self.offices_repository = OfficesRepository()

    def create_office_member(self, payload, auth_user):
        response = self.offices_repository.create(payload.dict())
        return response
