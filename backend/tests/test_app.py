from fastapi.testclient import TestClient
from backend.main import app  # Adjust import if needed

client = TestClient(app)

def test_home_status_code():
    response = client.get("/")
    assert response.status_code == 200

def test_home_content():
    response = client.get("/")
    assert "Feedback App" in response.text
