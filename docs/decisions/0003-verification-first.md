# 3. Verification-first: no promotion without passing evals

- **Status:** Accepted
- **Date:** 2026-07-12
- **Deciders:** @KarthikeyanDhanakotti
- **Consulted:** —
- **Informed:** EASRA contributors

## Context and Problem Statement

Enterprise AI systems fail slowly and quietly. A model degrades on a new task class; a prompt regresses on an edge case; a retriever loses recall after a corpus reindex. Without an eval gate, these regressions ship to production undetected until customers notice.

## Decision

**No model, prompt, agent, or retriever artifact may be promoted to a higher environment without a passing evaluation bundle.** The Control Plane (`EA-004`) enforces this gate. The Verification Plane (`EA-010`) supplies the graders and datasets.

Defaults:
- Promotion `dev → stg`: passing offline eval on the artifact's baseline dataset.
- Promotion `stg → prod`: passing offline eval + a passing "sanity slice" of continuous eval.
- Emergency override: allowed but requires a signed HITL approval and an incident ADR.

## Consequences

**Positive**
- Regressions are caught at promote-time, not by customers.
- Every promotion produces evidence — auditable and reviewable.
- Encourages investment in graders and datasets from day one.

**Negative**
- Slower promotion cadence for teams without mature eval assets — self-correcting incentive.
- Requires the eval infrastructure to be reliable enough not to become a bottleneck.

## Follow-ups

- Grader library and dataset schema live in `EA-010`.
- `CHK-verification-readiness` checklist codifies the minimum eval bundle per artifact type.

## Related

- `EA-004 · Control Plane`, `EA-010 · Verification Plane`, `PAT-003 · Verification`, `PAT-009 · Continuous Eval`
