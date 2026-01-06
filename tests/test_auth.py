import pytest


@pytest.mark.asyncio
async def test_register_and_token(async_client):
    ac = async_client

    # register
    resp = await ac.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "password": "pass",
            "first_name": "Test",
            "last_name": "User",
        },
    )
    assert resp.status_code == 200

    # token (oauth2 password flow)
    resp2 = await ac.post(
        "/api/v1/auth/token",
        data={
            "username": "test@example.com",
            "password": "pass",
            "grant_type": "password",
        },
    )
    assert resp2.status_code == 200
    body = resp2.json()
    assert "access_token" in body
