# L9 — Verification

| Field | Value |
|-------|-------|
| Layer | L9 |
| Depends on Specs | 002 (P3), 004, 005, 006, 008 |
| Status | Skeleton |

## 1. Purpose

L9 verifies the candidate response against grounding, citation, factuality, format, policy, and safety — on the response path, per request. Verification is **not** evaluation (L10, offline).

## 2. Responsibilities

- **In scope.** Verification Engine, Grader Registry, Verdict emitter, Escalation router, Response Formatter, Streaming Engine.
- **Out of scope.** Guardrails (L8), evaluation (L10), policy authorship (L14).

## 3. Design principles

**P3 Verification by Design**, **P4 Observability** (verdict per check), **P9 Cost Awareness** (bounded verification budget).

## 4. Patterns

- Rule → small-model → foundation-model grader ladder.
- Parallel checks where independent.
- Attach `Verdict` to every response.
- Escalation policy per data class and tenant.

## 5. Anti-patterns

- Using an eval dataset as the response-path verifier.
- Silently retrying on verification failure.
- Verdicts without evidence.

## 6. Failure modes

| Failure | Policy |
|---------|--------|
| Grader outage | Policy: block / warn / pass-with-degraded-verdict |
| Verification timeout | Treated as fail; escalate |

## 7. Observability

Verdict per check, grader latency, grader cost, escalation events, distribution of verdicts by check and by tenant.

## 8. Production checklist

- [ ] Every response carries a verdict.
- [ ] Escalation matrix documented and tested.
- [ ] Verification cost inside budget.
- [ ] Verdicts queryable per request.
