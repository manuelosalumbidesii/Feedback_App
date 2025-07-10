# backend/tests/test_app.py

from main import app

def test_home_status_code():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

def test_home_content():
    tester = app.test_client()
    response = tester.get('/')
    assert b'Feedback App' in response.data
