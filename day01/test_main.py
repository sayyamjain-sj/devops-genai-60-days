
from fastapi.testclient import TestClient
from day01.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["engineer"] == "Sayyam Jain"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_system():
    response = client.get("/system")
    assert response.status_code == 200
    assert "os" in response.json()
    assert "architecture" in response.json()
