from fastapi.testclient import TestClient
from backend.main import app  # or just `from main import app` if same directory

client = TestClient(app)

def test_home_status_code():
    response = client.get("/")
    assert response.status_code == 200

def test_home_content():
    response = client.get("/")
    data = response.json()
    assert data["status"] == "OK"
    assert data["message"] == "Feedback API is running"
