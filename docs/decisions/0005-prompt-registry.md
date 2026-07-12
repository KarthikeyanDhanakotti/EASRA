# 5. Prompts are first-class deployable artifacts

- **Status:** Accepted
- **Date:** 2026-07-12
- **Deciders:** @KarthikeyanDhanakotti
- **Consulted:** —
- **Informed:** EASRA contributors

## Context and Problem Statement

Prompts drive model behavior at least as much as model weights do — and often more, at the enterprise application layer. Yet in most organizations, prompts live as strings inside application code, un-versioned, un-reviewed, un-tested, un-observable. This is the equivalent of shipping SQL queries with no schema, no code review, and no query plan.

## Decision

**Prompts are first-class artifacts.** Every prompt used in a production path MUST be:

1. **Registered** in the Prompt Registry (`EA-007`) with an ID and semantic version.
2. **Reviewed** in a pull request like source code.
3. **Tested** against its associated eval dataset before promotion (`ADR-003`).
4. **Deployable** via the Control Plane (`EA-004`) with the same promotion rules as models.
5. **Observable** — every span carries `easra.prompt.id` and `easra.prompt.version`.

## Consequences

**Positive**
- Prompt regressions become debuggable and rollback-able.
- Prompt engineering becomes a reviewable engineering discipline.
- Enables A/B testing and canarying of prompts independently of models.

**Negative**
- Additional infrastructure: a Prompt Registry service and CI hooks.
- Teams accustomed to inline prompts must migrate.

## Follow-ups

- Prompt Registry API in `EA-007`.
- CI check that fails builds using unregistered prompt strings in production paths.

## Related

- `EA-007 · Prompt Intelligence`, `EA-004 · Control Plane`, `ADR-003 · Verification-First`
