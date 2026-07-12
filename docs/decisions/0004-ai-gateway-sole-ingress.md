# 4. AI Gateway is the sole ingress for model traffic

- **Status:** Accepted
- **Date:** 2026-07-12
- **Deciders:** @KarthikeyanDhanakotti
- **Consulted:** —
- **Informed:** EASRA contributors

## Context and Problem Statement

Once an enterprise adopts multiple models, providers, and use-cases, ad-hoc SDK calls to model endpoints proliferate. Each call becomes a shadow ingress: uncontrolled cost, unlogged prompts, missing safety checks, inconsistent routing.

## Decision

**All model traffic — chat, embeddings, tool-augmented generation, agent turns, RAG grounding — MUST traverse the Enterprise AI Gateway (`EA-002`).** Direct SDK calls to model providers from application code are prohibited outside `implementations/` reference examples.

Enforced by:
- Network policy where feasible (egress only via gateway ranges).
- SDK convention: internal SDKs point to the gateway endpoint by default.
- Audit: continuous eval flags any span that shows a direct-to-provider call.

## Consequences

**Positive**
- Every model call goes through the same pipeline: identity, policy, prompt intelligence, routing, safety, cost accounting, tracing, cache.
- Single place to add a new control (jailbreak filter, cost cap, region pin).
- Consistent observability contract (`gen_ai.*`).

**Negative**
- The gateway becomes a critical dependency — requires HA + multi-region.
- Development teams must adopt the gateway SDK/endpoint.
- Latency budget for gateway must stay strict (p95 targets in `EA-002`).

## Follow-ups

- Gateway HA and multi-region topology captured in `EA-002` and its `IMPL-` pages.
- Exception process for edge cases (e.g., local dev, batch training) documented in `EA-002`.

## Related

- `EA-002 · Enterprise AI Gateway`, `PAT-004 · Cost Guardrails`, `PAT-008 · Router`
