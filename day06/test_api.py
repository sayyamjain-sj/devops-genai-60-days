from fastapi.testclient import TestClient

from day06.api import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_server_alert():
    response = client.post(
        "/server/check",
        json={
            "hostname": "web01",
            "cpu": 90,
            "memory": 50,
            "disk": 85,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "alert"
    assert "cpu" in data["alerts"]
    assert "disk" in data["alerts"]


def test_server_healthy():
    response = client.post(
        "/server/check",
        json={
            "hostname": "web02",
            "cpu": 50,
            "memory": 60,
            "disk": 40,
        },
    )

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_invalid_cpu():
    response = client.post(
        "/server/check",
        json={
            "hostname": "web03",
            "cpu": 150,
            "memory": 60,
            "disk": 40,
        },
    )

    assert response.status_code == 400