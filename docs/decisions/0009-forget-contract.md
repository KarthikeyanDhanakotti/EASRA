# 9. Every memory tier must implement the Forget contract

- **Status:** Accepted
- **Date:** 2026-07-12
- **Deciders:** @KarthikeyanDhanakotti
- **Consulted:** —
- **Informed:** EASRA contributors

## Context and Problem Statement

Agent memory (session, long-term, vector, shared) is a data store. Data stores that persist personal or sensitive data must be able to *actually delete* on request — for GDPR, CCPA, tenant offboarding, consent revocation, and simple "user changed their mind." Soft-delete flags and TTLs are not deletion.

## Decision

**Every EASRA memory tier MUST implement `POST /v1/memory/forget?subject=<id>` with strong-guarantee removal semantics.** A `200 OK` response means:

1. Original records removed from primary store.
2. Any derived artifacts (embeddings, summaries, indices, caches) removed or invalidated.
3. Backups scheduled for purge per the tier's declared purge SLA.
4. An audit event is emitted (`easra.memory.forget`) with `{subject, tier, ts, requester}`.

Tiers unable to implement this contract (e.g., a read-only external corpus) are prohibited from storing subject-identifiable memory.

## Consequences

**Positive**
- Legal defensibility for GDPR "right to be forgotten" and analogous regimes.
- Consent revocation becomes a first-class operation, not a project.
- Tenant offboarding is a bounded, auditable operation.

**Negative**
- Increases engineering cost of every memory backend — no more "just append."
- Vector stores that don't support delete-by-metadata must be filtered out at design time.

## Follow-ups

- Forget-latency SLA per tier declared in `EA-008 · Memory Plane`.
- Compliance test suite (part of `CHK-memory-forget`) that exercises the contract per tier.

## Related

- `EA-008 · Memory Plane`, `PAT-006 · Memory`, `SPEC-forget-contract` (planned)
