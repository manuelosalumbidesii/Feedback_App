from fastapi.testclient import TestClient
from backend.main import app


client = TestClient(app)


def test_home_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_home_content():
    response = client.get("/")
    assert "Feedback API is running" in response.text
