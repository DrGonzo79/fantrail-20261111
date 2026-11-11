# Product and execution plan

## ICP and JTBD

Primary ICP: US experiential agency producers running offsite activations at major cultural conventions. JTBD: “When my brand spends on an offsite, help fans discover it and give me defensible aggregate visit evidence for the recap.” Secondary users are fan-media editors and attendees.

## MVP

One event, 50–150 curated offsites, mobile-web discovery, hours/reservation links, 10 paid pins, expiring QR check-ins, aggregate recap export, and an operator console. No app, indoor navigation, facial recognition, passive location, real-time crowd claims or attribution beyond verified scan semantics.

## Data model

`Event` owns `Zone` and `Activation`; `Activation` has windows, organizer, source provenance and optional `Campaign`; `Campaign` defines sponsor, offer and disclosure; `CheckinToken` is signed, rotating and stop-scoped; `Checkin` stores pseudonymous event/session IDs, consent version and fraud flags; `Recap` freezes metric definitions and aggregates. Retention should default short and raw identifiers should never enter the public map.

## Architecture and AI strategy

Next.js static/mobile UI is CDN-hostable. FastAPI owns trail feasibility and check-in validation. Production adds Postgres/PostGIS, a queue for imports/recaps, object storage and observability. AI may propose dedupes and extract hours from public pages, but a human editor approves every activation; AI never invents inventory or validates visits.

## Economics

Lead magnet $0; promoted pin $750/event; measurement pilot $750–$2,500; city quest $25K; eligible affiliate revenue 5–10%. The report's five-pin case yields $3,750; a single quest dominates revenue. Gross margin is attractive only if curation, local verification and agency servicing stay bounded. Seasonality makes ARR framing misleading until several event calendars repeat.

## Validation and moat

Run 20 qualified agency conversations, seek two paid $750 pilots, pre-agree the exact recap metric, and recruit one fan-media distribution partner. Measure deposit rate, map unique users, activation detail views, valid/deduped check-ins, and buyer acceptance of the recap. Moat can emerge from trusted distribution deals, verified inventory provenance, cross-event benchmarks and producer workflows; the map and route algorithm are commodities.

## Risks

Incumbent fan maps can add paid pins; agencies may bundle the work; check-ins can be gamed; privacy language can suppress usage; event cancellations and seasonality concentrate revenue; incomplete inventory destroys fan trust; sponsor placement can corrupt editorial neutrality. Controls: prominent disclosures, provenance and freshness, token rotation, rate limits, aggregate-only reporting, manual audit, and no causal lift claims.

## 30/60/90

- **0–30 days:** 20 buyer interviews, one recap shadow, fan-media partnership ask, event inventory rubric, two signed pilot scopes.
- **31–60 days:** concierge map for one event, 50 verified pins, one paid activation, consent/fraud runbook, dry-run recap.
- **61–90 days:** execute event, deliver recap in 72 hours, conduct buyer postmortem, decide whether to repeat, partner, or kill. Only then consider quest sales.
