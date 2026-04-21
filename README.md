# AI-Assisted Form Autofill

Takes unstructured source text (OCR, email, notes) and proposes structured form values with confidence scores.

## Stack

- FastAPI backend
- Regex + heuristic extraction pipeline, ready for LLM fallback
- React frontend review panel

## Run Backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8050
```

## Run Frontend

```bash
cd web
npm install
npm run dev
```
