# EASRA LLMOps Guide

The **LLMOps Guide** is EASRA's cross-cutting reference for delivering, operating, and evolving Enterprise AI systems safely. It combines discipline from DevOps, MLOps, and SRE with the AI-specific control loops EASRA requires: prompt lifecycle, evaluation-gated release, cost budgeting, incident response for AI-specific failure modes, and continuous verification.

This guide is the working companion to the [Operational Architecture view](../architectures/operational/) and to layer chapters L10 (Observability & Evaluation), L11 (Performance, Caching & Cost), and L12 (Delivery).

## Scope

- **Delivery pipeline** — CI, evaluation gates, artefact promotion, canary / blue-green / shadow, rollback.
- **Prompt lifecycle** — authoring, review, registration, versioning, testing, rollback.
- **Model lifecycle** — selection, registration, evaluation, promotion, retirement.
- **Tool lifecycle** — impact-class classification, registration, rate limits, decommissioning.
- **Evaluation strategy** — offline, canary, production, continuous.
- **Cost engineering** — budgets, ledger, per-request cost, cost anomalies, optimisation levers.
- **Observability** — SLOs, dashboards, tracing conventions, alerting.
- **Incident response** — AI-specific runbooks.
- **Multi-region delivery** — coordinated rollout across regions with regional guardrails.

## 1. Delivery pipeline (reference)

```
source (git) ─┬─► lint ─► sec-scan ─► unit ─► prompt tests ─► offline eval ─► artefact registry
              └─► IaC plan
                                                    │
                                                    ▼
                                     ┌────► shadow (mirror traffic)
                                     │
                        canary (1%) ─┼────► auto-eval gate ─┬─► progressive ramp (5% → 25% → 100%)
                                     │                     │
                                     │                     └─► rollback (auto)
                                     ▼
                              blue-green swap
```

Every promotion between stages is gated by:

- **Unit** — traditional code tests.
- **Prompt tests** — golden-set responses within regression tolerance.
- **Offline evaluation** — verification checkers (grounding, factuality, format, policy, BR) meet threshold.
- **Auto-eval gate** — production-mirrored traffic evaluations for ≥ 30 min (canary) or ≥ 2 h (shadow).
- **Cost gate** — per-request cost within budget.

## 2. Prompt lifecycle

| Stage | Owner | Artefact | Registry (`K-L3-PR`) status |
|-------|-------|----------|------------------------------|
| Author | Prompt engineer | Draft template | not-registered |
| Review | Peer | PR + review notes | not-registered |
| Register | CI | Signed, versioned template | Draft |
| Golden-set test | CI | Passing metrics | Candidate |
| Canary | LLMOps | Passing production evaluations | Active |
| Retire | LLMOps | Successor active for ≥ 1 minor release | Retired (immutable) |

## 3. Model lifecycle

| Stage | Owner | Artefact | Registry (`K-L6-MRG`) status |
|-------|-------|----------|------------------------------|
| Select | Architect | Selection ADR | not-registered |
| Register | Platform | Signed, versioned model deployment | Draft |
| Evaluate | Evaluator | Passing capability + safety + cost thresholds | Candidate |
| Canary | LLMOps | Passing production evaluations | Active |
| Retire | LLMOps | Fallback route in place | Retired |

## 4. Tool lifecycle

Every tool MUST declare an impact class (read / write / high-impact) before registration. High-impact tools require an HITL gate wired to `K-L7-IMP` before promotion beyond canary.

## 5. Evaluation strategy

| Where | Purpose | Cadence |
|-------|---------|---------|
| Offline | Gate promotion. | Every PR. |
| Canary | Detect regression pre-100%. | Every canary. |
| Production | Verify each response. | Every request (`K-L9-VE`). |
| Continuous | Detect drift, regressions, cost anomalies. | Continuous (`K-L10-EVAL`). |

## 6. Cost engineering

- Every request emits a cost record to `K-L11-LG`.
- Every capability has an owner-declared per-request cost budget (`K-L1-TBM`).
- Budget breaches degrade gracefully: cache → smaller model → fallback → error.
- Weekly cost review compares actual vs. budget per capability and per tenant.

## 7. Observability conventions

- Every trace uses W3C TraceContext.
- Every span records: `easra.layer`, `easra.component`, `easra.capability`, `easra.request_id`, `easra.prompt_version`, `easra.model_version`, `easra.tool_version` where applicable.
- Every cost event carries the request ID.

## 8. SLOs (reference; adopters set their own)

| SLO | Target |
|-----|--------|
| End-to-end request latency (p95) | ≤ 3 s for single-agent RAG. |
| Availability | ≥ 99.9% monthly. |
| Verification allow-rate | ≥ 95% (below this indicates prompt / retrieval regression). |
| Cost per request (p95) | Within capability budget. |
| Safety incidents | Zero user-visible bypasses. |

## 9. AI-specific runbooks (planned)

- Prompt-injection incident.
- Indirect prompt-injection incident.
- Grounding regression.
- PII leakage.
- Cost anomaly.
- Tool misuse (excessive agency).
- Model policy bypass.

## 10. Multi-region delivery

- Every artefact promoted region-by-region, with regional evaluators.
- Guardrails and verification checkers pinned per region for jurisdictional policy.
- Rollback is region-local by default.

## Related

- [Spec 010 — Non-Functional Requirements](../specification/010-nfr.md)
- [Spec 011 §C10, §C11, §C12](../specification/011-capability-model.md)
- [Spec 012 §L10, §L11, §L12](../specification/012-component-catalogue.md)
- [Architectures / Operational](../architectures/operational/)
- [Diagrams — D-O1..D-O5](../diagrams/CATALOGUE.md)
