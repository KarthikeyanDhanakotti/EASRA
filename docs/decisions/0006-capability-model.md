# 6. The 7-layer Capability Model is the canonical taxonomy

- **Status:** Accepted
- **Date:** 2026-07-12
- **Deciders:** @KarthikeyanDhanakotti
- **Consulted:** External reviewer (Sprint-02)
- **Informed:** EASRA contributors

## Context and Problem Statement

Every architecture description eventually needs a taxonomy — a shared vocabulary for what a system does, independent of how it is built. Without one, each architecture page invents its own boxes and arrows, and cross-architecture reasoning breaks.

## Decision

**The 7-layer Capability Model in `reference-models/capability-model.md` is the canonical EASRA taxonomy.** Every architecture (`EA-`), pattern (`PAT-`), and implementation (`IMPL-`) MUST map itself to one or more capabilities in this model.

The seven layers are:

| # | Layer | Purpose (short) |
|---|-------|-----------------|
| L1 | Experience | User-facing surfaces (chat, copilots, embedded UI) |
| L2 | Orchestration | Agents, workflows, tool-use, routing |
| L3 | Runtime | Execution, memory, HITL, safety, quotas |
| L4 | Knowledge | Corpora, chunk/embed, retrievers, feature store |
| L5 | Verification | Datasets, graders, offline + continuous eval |
| L6 | Control | Registries, policy, promotion, cost |
| L7 | Foundation | Identity, network, secrets, observability, data platform |

## Consequences

**Positive**
- Every artifact traces to a capability — enables cross-cutting queries ("what governs L3 execution?").
- Reviewers can spot capability gaps in any proposed architecture.
- Adopters can start by scoring themselves against the model.

**Negative**
- Any change to the 7 layers is a breaking change — high governance bar.
- Some real systems don't fit cleanly into one layer — must be labeled multi-layer.

## Follow-ups

- Every `EA-` / `PAT-` page must have a `Layer:` header.
- A capability-coverage matrix should be published per architecture in Sprint-03.

## Related

- `reference-models/capability-model.md`
- All `EA-`, `RM-`, `PAT-`, `IMPL-` pages
