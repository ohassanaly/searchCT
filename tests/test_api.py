from app.main import create_app
from fastapi.testclient import TestClient


def test_api():
    client = TestClient(create_app())
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the searchCT API"}
