# 7. OpenTelemetry `gen_ai.*` is the canonical observability contract

- **Status:** Accepted
- **Date:** 2026-07-12
- **Deciders:** @KarthikeyanDhanakotti
- **Consulted:** —
- **Informed:** EASRA contributors

## Context and Problem Statement

Every AI framework, SDK, and gateway wants to invent its own telemetry format. That fragments observability — each backend needs a bespoke adapter, and cross-tool comparability collapses. The industry already has a converging standard: OpenTelemetry `gen_ai.*` semantic conventions.

## Decision

**OpenTelemetry `gen_ai.*` semantic conventions are the canonical observability contract for EASRA.** All EASRA components emit spans, metrics, and events that conform to `gen_ai.*` (and EASRA extension attributes prefixed `easra.*`).

Baseline required attributes on every model span:
- `gen_ai.system`, `gen_ai.request.model`, `gen_ai.response.model`
- `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`
- `gen_ai.request.temperature`, `gen_ai.request.top_p` (when relevant)

EASRA extensions (namespaced `easra.*`):
- `easra.prompt.id`, `easra.prompt.version` (from ADR-005)
- `easra.route.decision`, `easra.route.reason` (from `PAT-008`)
- `easra.hitl.decision`, `easra.hitl.reviewer_id` (from `PAT-007`)
- `easra.memory.tier`, `easra.memory.op` (from `PAT-006`)

## Consequences

**Positive**
- Any OTel-compatible backend (Azure Monitor, Datadog, Grafana, Honeycomb, …) works out of the box.
- Cross-vendor comparability — traces from Gateway A and Runtime B compose naturally.
- Adopters aren't locked into a proprietary telemetry stack.

**Negative**
- `gen_ai.*` conventions are still evolving — EASRA must track upstream changes.
- Some SDKs don't emit `gen_ai.*` yet — need adapter shims in `implementations/`.

## Follow-ups

- Publish an EASRA `gen_ai.*` conformance checklist (`CHK-observability`).
- Track upstream OTel Gen-AI SIG changes and note breaking updates in `CHANGELOG.md`.

## Related

- `EA-002 · Enterprise AI Gateway`, `EA-003 · Runtime Plane`, `SPEC-observability` (planned)
