import logging

from fastapi import FastAPI

from app.config.connection import on_appliction_shutdown, on_appliction_startup
from app.config.lifetime import shutdown, startup
from app.config.settings import settings
from app.utils.logger import setup_logger
from app.views import offices

setup_logger()
LOGGER = logging.getLogger(__name__)


def get_app() -> FastAPI:
    app = FastAPI(
        title="Office Quotability",
        version=settings.version,
        debug=settings.debug,
        reloader=settings.reload,
        openapi_url="/openapi.json",
    )

    LOGGER.info(f"Application started on " f"{settings.host}: " f"{settings.fastapi_port}")

    app.on_event("startup")(startup(on_appliction_startup))
    app.on_event("shutdown")(shutdown(on_appliction_shutdown))

    app.include_router(offices.router)
    return app
