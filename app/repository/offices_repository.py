import logging

from app.models.offices_model import AccountingOfficeModel
from app.repository.base_repository import BaseRepository
from app.utils.exceptions import ExistiException
from app.utils.logger import setup_logger

setup_logger()
setup_logger = logging.getLogger(__name__)


class OfficesRepository(BaseRepository):
    def __init__(self):
        super().__init__(AccountingOfficeModel)

    def create(self, payload):
        cnpj = payload.get("cnpj")
        exiting_office = self.collection.objects(cnpj=cnpj).first()

        if exiting_office:
            raise ExistiException("Office already exists!")

        self.collection(**payload).save()
        return {"status": "sucess", "menssage": "Office created", "error": None}
