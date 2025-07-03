import logging

from fastapi import APIRouter

from app.utils.logger import setup_logger

setup_logger()
setup_logger = logging.getLogger(__name__)

router = APIRouter(prefix="/offices")


@router.get("/")
async def get_offices():
    setup_logger.info("get_offices")
    response = {"offices": ["office1", "office2"]}
    return response
