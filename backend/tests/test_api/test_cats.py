"""Cat endpoints tests."""

import pytest


@pytest.mark.asyncio
async def test_list_cats(client):
    """Test list cats endpoint."""
    response = await client.get("/api/v1/cats")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)