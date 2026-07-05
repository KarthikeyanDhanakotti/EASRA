# L3 — Prompt Intelligence

| Field | Value |
|-------|-------|
| Layer | L3 |
| Depends on Specs | 004, 005, 006 |
| Status | Skeleton |

## 1. Purpose

L3 turns context into a prompt: grounded, safe, cost-aware, deterministic, versioned.

## 2. Responsibilities

- **In scope.** Context Builder, Prompt Builder, Prompt Registry client, prompt-template versioning, token-budget enforcement.
- **Out of scope.** Retrieval (L5), memory retrieval (L4), guardrail application (L8), model selection (L6).

## 3. Components

- **Context Builder** — assembles memory, retrieval, tool schemas, system instructions.
- **Prompt Builder** — applies the selected template; enforces token budget.
- **Prompt Registry client** — versioned template lookup.

## 4. Design principles

**P3 Verification by Design** (deterministic inputs for reproducibility), **P4 Observability** (prompt trace), **P9 Cost Awareness** (token budget).

## 5. Patterns

- Explicit system / user / tool boundaries in the assembled prompt (mitigates prompt injection at TB-C).
- Prompt templates versioned by semver; deployment behind evaluation gate (L12).
- Token budget priorities: system > user > grounding > memory > tool schemas.

## 6. Anti-patterns

- Prompts assembled inline in application code — no registry, no version.
- Mixing user input into system instructions without boundaries.
- No token budget → provider errors or ballooning cost.

## 7. Failure modes

| Failure | Degraded mode |
|---------|---------------|
| Token budget exceeded | Truncate lowest-priority context; emit metric |
| Template missing | Fail closed; alert |
| Registry outage | Serve last-known-good template with warning telemetry |

## 8. Observability

Prompt trace (template ID, version, inputs, token counts by section), cache hit/miss, truncation events, PII classification of inputs.

## 9. Production checklist

- [ ] Every prompt has a registered template + version.
- [ ] Token budget enforced deterministically.
- [ ] System boundaries clearly labelled in the assembled prompt.
- [ ] Prompt trace queryable per request.
