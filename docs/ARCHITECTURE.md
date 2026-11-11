# Architecture

The prototype keeps one explicit fixture in `data/demo.json`. The React client and FastAPI read the same activation records. `lib/trail.ts` and `POST /trail` implement the same deterministic domain rule: validate 2–6 stops, group them by zone/opening, wait for openings, include dwell plus transfer time, and warn about likely closures. `POST /checkin` verifies a stop-scoped demo code.

GitHub Pages serves only the static Next.js export under the repository base path. FastAPI is tested source and is not live. Production boundaries would be: ingestion/editor → Postgres/PostGIS; public read API → CDN; check-in service → rotating signed tokens and rate-limited writes; aggregation worker → immutable recap snapshots. OpenTelemetry spans, structured event IDs, check-in rejection counters, inventory freshness alerts and SLOs are required before a real event.

Failure modes include stale hours, duplicated activations, forged/replayed tokens, queue lag, a venue cancellation, map-provider outage and traffic spikes. The public view should degrade to cached list mode; check-in requests should be idempotent; sponsor metrics should label late or incomplete data.
