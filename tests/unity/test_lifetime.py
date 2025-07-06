import asyncio

import pytest
from fastapi import FastAPI

from app.config.lifetime import (  # Ajuste o import conforme o caminho real do seu projeto
    shutdown,
    startup,
)


@pytest.fixture
def app():
    """Fixture para criar a instância do FastAPI."""
    return FastAPI()


@pytest.mark.asyncio
async def test_startup_returns_coroutine_and_runs(app):
    startup_callable = startup(app)
    assert callable(startup_callable)
    # Deve retornar uma coroutine (função async sem argumentos)
    result = startup_callable()
    assert asyncio.iscoroutine(result)
    await result  # Deve executar sem erro


@pytest.mark.asyncio
async def test_shutdown_returns_coroutine_and_runs(app):
    shutdown_callable = shutdown(app)
    assert callable(shutdown_callable)
    # Deve retornar uma coroutine (função async sem argumentos)
    result = shutdown_callable()
    assert asyncio.iscoroutine(result)
    await result  # Deve executar sem erro
