# FanTrail

A runnable, fictional vertical slice of a convention offsite map with a route planner and measurable check-in. Fans select 2–6 activations, get a deterministic trail, and verify a demo code. It does **not** collect location, issue tickets, or run a live backend.

## Run

Requires Node 24.22.2 and Python 3.13.

```bash
npm ci
npm run typecheck && npm run test:e2e && npm run build && npm audit --audit-level=high
cd api && uv sync --frozen && uv run pytest && uv run --with pip-audit pip-audit
```

Frontend: `npm run dev`. Backend source: `cd api && uv run uvicorn api.main:app --reload --app-dir ..`. The public GitHub Pages demo is frontend-only; FastAPI is tested source, not deployed.

## Product boundary

All activations, brands, map geometry, codes and interaction results are fictional. The source report is summarized in `research/notes.md`; raw report text and private email metadata are not included. See `docs/PRODUCT.md`, `docs/OFFICE_HOURS.md`, and `docs/CEO_REVIEW.md` for the go/no-go logic.
