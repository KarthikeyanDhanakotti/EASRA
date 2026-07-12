# EA-007 · Prompt Intelligence

**Status:** Stub (v0.0.1) · **Sprint:** planned Sprint-03 · **Taxonomy:** `EA-`

> Placeholder page. The full Prompt Intelligence specification will land in **Sprint-03**.

## Purpose

Define how EASRA **understands, classifies, and enriches** every inbound prompt before it reaches a model — the "make the prompt legible to the platform" plane.

## Scope (draft)

- Language / locale detection
- Task classification (chat · code · extraction · reasoning · agentic · analysis · retrieval)
- Sensitivity scoring (regulated data · PII probability · confidentiality tier)
- Jailbreak / injection risk scoring
- Cost hint (input length, likely output length)
- **Prompt registry** — versioned, testable, promotable prompts (system + tool prompts)
- Prompt template validation (schema + eval-gated promotion)
- Redaction contract (what is scrubbed, what is preserved as span metadata)

## Design Goals (draft)

- G1 · Every prompt is enriched with `easra.prompt.*` attributes before Stage 5 (Router) runs.
- G2 · No prompt reaches production without passing minimum quality/safety graders.
- G3 · Prompt lifecycle mirrors code lifecycle — versioned, reviewed, deployed, revertible.
- G4 · Prompt intelligence must degrade gracefully — a classifier outage becomes a heuristic + trace flag, not a request block.

## Related

- Lives inside [EA-002 · AI Gateway](EA-002-Enterprise-AI-Gateway.md) as Stage 4
- Registry governed by [EA-004 · Control Plane](EA-004-Control-Plane.md)
- Consumed by [EA-006 · Model Router](EA-006-Model-Router.md)
- Related patterns (planned): PAT-004 Prompt Intelligence (already in repo)
- Related decisions (planned): ADR-005 Prompt Registry

## Changelog

- v0.0.1 · Sprint-02 · Stub created as part of the 15-view architecture map.
