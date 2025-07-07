import logging

from fastapi import APIRouter, Depends

from app.schemas.offices_schemas import AccountingOffice
from app.services.offices_members import OfficesMembersService
from app.utils.logger import setup_logger

setup_logger()
setup_logger = logging.getLogger(__name__)

router = APIRouter(prefix="/offices")


@router.get("/")
async def get_office():
    setup_logger.info("get_offices")
    response = {"offices": ["office1", "office2"]}
    return response


@router.post("/create")
async def create_office(
    office_payload: AccountingOffice,
    service: OfficesMembersService = Depends(OfficesMembersService),
):
    setup_logger.info("Enviando data office")
    return service.create_office_member(office_payload, None)
