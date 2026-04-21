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

<!-- REPO_ANALYSIS_OVERVIEW_START -->
## Repository Analysis Snapshot

Generated: 2026-04-21

- Primary stack: Unknown
- Key paths: `backend`, `docs`, `.github/workflows`, `README.md`
- Files scanned (capped): 22
- Test signal: Test-named files detected
- CI workflows present: Yes
- GitHub slug: igor-kan/ai-assisted-form-autofill
- GitHub last push: 2026-04-21T20:50:18Z

### Quick Commands

Setup:
- `Review repository README for setup steps`

Run:
- `Review repository README for run/start command`

Quality:
- `Review CI/workflow commands in .github/workflows`

### Companion Docs

- `AGENTS.md`
- `TASKS.md`
- `PLANNING.md`
- `RESEARCH.md`
- `PROJECT_BRIEF.md`

### Web Research References

- Origin remote: `https://github.com/igor-kan/ai-assisted-form-autofill.git`
- GitHub homepage: Not set
- `N/A`
<!-- REPO_ANALYSIS_OVERVIEW_END -->
