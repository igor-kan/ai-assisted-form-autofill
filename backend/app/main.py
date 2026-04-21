from fastapi import FastAPI
from pydantic import BaseModel

from .extract import extract_fields

app = FastAPI(title="AI-Assisted Form Autofill")


class AutofillRequest(BaseModel):
    raw_text: str


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/api/autofill")
def autofill(request: AutofillRequest) -> dict:
    extracted = extract_fields(request.raw_text)
    return {"fields": extracted}
