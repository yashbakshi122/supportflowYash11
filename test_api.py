from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_refund_query():
    r = client.post("/support", json={"message": "How long do refunds take?"})
    assert r.status_code == 200
    data = r.json()
    assert "refund" in data["intent"]
    assert data["source_ids"]
