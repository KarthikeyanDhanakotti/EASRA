# L10 — Observability & Evaluation

| Field | Value |
|-------|-------|
| Layer | L10 |
| Depends on Specs | 004, 005, 006, 010 |
| Status | Skeleton |

## 1. Purpose

L10 emits and stores the operational, cost, quality, and safety signals for every request; runs continuous evaluation on sampled traffic; issues alerts.

## 2. Responsibilities

- **In scope.** OTel collector, metric / log / trace / evaluation stores, alert manager, continuous-evaluation runner, dashboards.
- **Out of scope.** Verification (L9), guardrails (L8), CI/CD (L12).

## 3. Design principles

**P4 Observability**, **P9 Cost** (cost as first-class signal), **P2 Security** (PII redaction pre-persistence).

## 4. Patterns

- OTel-shaped spans with EASRA attributes (`easra.layer`, `easra.model_id`, `easra.tokens.*`, `easra.cost.*`, `easra.verdict.*`).
- Continuous evaluation on statistically sampled traffic.
- Cost attribution tree: tenant → user → agent → request.
- Alert catalogue as code; deduplication; escalation cap.

## 5. Anti-patterns

- PII in traces or logs.
- Alerts without runbooks.
- Cost tracked only in monthly bills.

## 6. Failure modes

| Failure | Degraded mode |
|---------|---------------|
| Collector outage | Local buffering; drop with metric on overflow |
| Backend store slow | Sampling turned up; retention reduced |

## 7. Production checklist

- [ ] End-to-end trace on every request.
- [ ] Token + cost telemetry on every model call.
- [ ] PII redaction verified on all exports.
- [ ] Alert runbooks linked from alerts.
