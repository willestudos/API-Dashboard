import logging

from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.utils.logger import setup_logger

setup_logger()
setup_logger = logging.getLogger(__name__)

router = APIRouter(prefix="/healthcheck")


@router.get("/", summary="Health check", tags=["Health"])
async def health_check():
    return JSONResponse(
        status_code=200, content={"status": "ok", "message": "API está rodando com sucesso!"}
    )
