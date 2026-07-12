# PAT-009 · Continuous Evaluation

**Status:** Stub (v0.0.1) · **Sprint:** planned Sprint-03 · **Layer:** L5 · **Taxonomy:** `PAT-`

> Placeholder page. The full Continuous Evaluation pattern will land in **Sprint-03**.

## Context

Offline evals catch known regressions on frozen datasets. They do **not** catch model drift, prompt drift, retrieval drift, or emerging failure modes on real traffic. Continuous eval runs graders against live traces on an ongoing sampled basis.

## Solution (outline)

- **Sampler** picks a fraction of production traces (per model / per prompt / per tenant)
- **Graders** score sampled traces asynchronously — never in the request path
- Score → time-series in the observability store
- **Drift detection** on grader scores; alert on statistical shift
- Failures → dataset curation (feeds offline eval + fine-tuning)
- Continuous eval scoreboards visible per model / per prompt / per tenant

## Interfaces (to be specified)

- Grader contract (input schema, output score + rationale)
- Sampling policy schema (versioned, tenant-scoped)

## Controls

- PII redaction before any grader ingest
- Consent policy for tenant traces used in shared graders
- Grader-as-a-service isolated from request-path infra

## KPIs

- Coverage (% of production traffic sampled)
- Grader latency (async, but still needs SLO)
- Drift-alert precision / recall
- Time-to-detect regression

## Trade-offs

- Sampling rate: more coverage vs. compute cost
- LLM-as-judge cheap but noisy vs. rule/human graders expensive but reliable

## Anti-patterns

- Grading in the request path
- Grading raw prompts without redaction
- Alerting on absolute scores instead of statistical shifts

## Related

- Realizes [EA-010 · Verification Plane](../architectures/EA-010-Verification-Plane.md)
- Pairs with [PAT-010 · Feedback Curation](PAT-010-Feedback-Curation.md)
- Related decisions (planned): ADR-003 Verification-First, ADR-007 OTel `gen_ai.*`

## Changelog

- v0.0.1 · Sprint-02 · Stub created as part of the pattern-catalog completion plan.
