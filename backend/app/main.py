from fastapi import FastAPI
from pydantic import BaseModel

from .providers import list_providers, resolve_provider
from .templates import TEMPLATES, get_template

app = FastAPI(title="AI-Assisted Form Autofill", version="0.2.0")


class AutofillRequest(BaseModel):
    raw_text: str
    template_id: str = "contact_intake"
    provider_id: str = "heuristic"
    min_confidence: float = 0.7


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok", "version": app.version}


@app.get("/api/templates")
def templates() -> dict:
    return {"items": [{"id": key, **value} for key, value in TEMPLATES.items()]}


@app.get("/api/providers")
def providers() -> dict:
    return {"items": list_providers()}


@app.post("/api/autofill")
def autofill(request: AutofillRequest) -> dict:
    provider = resolve_provider(request.provider_id)
    extracted = provider.run(request.raw_text)
    template = get_template(request.template_id)
    required = template["required_fields"]

    missing_required = []
    review_required = []

    for field_name in required:
        field = extracted.get(field_name, {"value": "", "confidence": 0.0})
        if not field["value"]:
            missing_required.append(field_name)
        if field["confidence"] < request.min_confidence:
            review_required.append(field_name)

    return {
        "template_id": request.template_id,
        "provider_id": request.provider_id,
        "fields": extracted,
        "missing_required_fields": missing_required,
        "review_required_fields": sorted(set(review_required)),
    }
