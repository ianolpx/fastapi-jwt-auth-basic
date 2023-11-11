
from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)


def signup():
    response = client.post(
        "/signup",
        json={
            "email": "tester",
            "password": "tester"
        }
    )
    return response.json()


def login():
    response = client.post(
        "/login",
        data={
            "username": "tester",
            "password": "tester"
        }
    )
    return response.json()


@pytest.fixture
def fixture_token():
    res1 = signup()
    res2 = login()
    return res2['access_token']


# client.get with fixture_token (access_token)
# url '/me'
def test_always_passes(fixture_token):
    response = client.get(
        "/me",
        headers={"Authorization": f"Bearer {fixture_token}"}
    )
    assert response.status_code == 200

 