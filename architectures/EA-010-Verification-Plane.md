# EA-010 · Verification Plane

**Status:** Stub (v0.0.1) · **Sprint:** planned Sprint-03 · **Taxonomy:** `EA-`

> Placeholder page. The full Verification Plane specification will land in **Sprint-03**.

## Purpose

Define how EASRA **knows whether the system is working** — through offline evaluation, online (continuous) evaluation, grounded-response checks, and human feedback capture.

## Scope (draft)

- Evaluation dataset registry (versioned, tenant-scoped, PII-safe)
- Grader library (rule-based, LLM-as-judge, human-in-the-loop)
- Offline eval runs — regression + promotion gates
- Continuous eval — sampled traffic scored against graders
- Drift detection (input · output · retrieval · grounding)
- Feedback capture (thumbs, corrections, rewrites, HITL decisions)
- Dataset curation from traces → next-round eval &amp; fine-tuning
- **Verification-first principle** — no promotion without passing evals (see ADR-003)

## Design Goals (draft)

- G1 · Every model/prompt/agent promotion requires a passing eval bundle. Enforced by the Control Plane.
- G2 · Continuous eval runs in production, on a sampled slice, without adding to user latency.
- G3 · Feedback loops close automatically — sampled corrections feed curation and re-training.
- G4 · Eval failures are observable, root-causeable, and roll-back-triggering.

## Related

- Gates promotions in [EA-004 · Control Plane](EA-004-Control-Plane.md)
- Consumes traces from [EA-003 · Runtime Plane](EA-003-Runtime-Plane.md) and [EA-002 · AI Gateway](EA-002-Enterprise-AI-Gateway.md)
- Related patterns (in repo): [PAT-003 · Verification](../patterns/PAT-003-Verification.md); planned: PAT-009 Continuous Eval, PAT-010 Feedback Curation
- Related decisions (planned): ADR-003 Verification-First, ADR-007 OTel `gen_ai.*`

## Changelog

- v0.0.1 · Sprint-02 · Stub created as part of the 15-view architecture map.
