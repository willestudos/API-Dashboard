import pytest


@pytest.mark.asyncio
async def test_get_offices(client):
    response = await client.get("/offices/")
    assert response.status_code == 200
    assert response.json() == {"offices": ["office1", "office2"]}
