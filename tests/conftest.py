import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from app.application import get_app


@pytest.fixture(scope="session")
def app() -> FastAPI:
    return get_app()


@pytest_asyncio.fixture(scope="function")
async def client(app: FastAPI) -> AsyncClient:
    """
    Cliente de teste HTTP assíncrono com suporte ao app FastAPI.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
