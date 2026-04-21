from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_templates_and_providers() -> None:
    templates = client.get("/api/templates")
    providers = client.get("/api/providers")
    assert templates.status_code == 200
    assert providers.status_code == 200
    assert any(item["id"] == "vendor_registration" for item in templates.json()["items"])
    assert any(item["id"] == "heuristic" for item in providers.json()["items"])


def test_autofill_review_required_fields() -> None:
    payload = {
        "raw_text": "Jane Citizen\\njane.citizen@example.com\\nToronto, ON",
        "template_id": "vendor_registration",
        "provider_id": "heuristic",
        "min_confidence": 0.8,
    }
    response = client.post("/api/autofill", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "company" in body["missing_required_fields"]
    assert "full_name" in body["review_required_fields"]
