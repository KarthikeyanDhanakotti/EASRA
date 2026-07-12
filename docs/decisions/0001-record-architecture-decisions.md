# 1. Record architecture decisions

- **Status:** Accepted
- **Date:** 2026-07-12
- **Deciders:** @KarthikeyanDhanakotti
- **Consulted:** —
- **Informed:** EASRA contributors

## Context and Problem Statement

EASRA is a reference architecture, so the *why* behind each choice matters more than the choice itself. We need a lightweight, auditable way to capture architectural decisions and their trade-offs over time.

## Decision Drivers

- Contributors and readers must understand *why* a design looks the way it does.
- Decisions must be reversible; we need to record when they expire or should be revisited.
- The format must be low-friction to write and to review in a PR.

## Considered Options

1. **Architecture Decision Records (ADRs)** stored as Markdown in `docs/decisions/`.
2. Design docs in a shared wiki (Notion, Confluence).
3. Decisions captured only in PR descriptions.

## Decision Outcome

**Chosen option: 1 — ADRs as Markdown in the repo.**

Rationale:

- Version-controlled next to the artifacts they describe.
- Reviewable via normal PR flow.
- Portable — no vendor lock-in on where documentation lives.
- Established industry pattern (Nygard-style ADRs).

## ADR Template

New ADRs must use the following structure and be named `NNNN-short-kebab-title.md` (four-digit, zero-padded, sequential).

```markdown
# NNNN. <Short imperative title>

- Status: Proposed | Accepted | Deprecated | Superseded by ADR-XXXX
- Date: YYYY-MM-DD
- Deciders: @handle, @handle
- Consulted: @handle
- Informed: @handle

## Context and Problem Statement
<Why is a decision needed? What forces are at play?>

## Decision Drivers
- <driver 1>
- <driver 2>

## Considered Options
1. <option 1>
2. <option 2>

## Decision Outcome
Chosen option: <n> — <one-liner>

<Explain rationale, trade-offs, and any conditions under which this
decision should be revisited.>

## Consequences
- Positive: ...
- Negative: ...
- Neutral: ...

## Links
- <related ADRs, patterns, external references>
```

## Consequences

- **Positive:** transparent decision history; easy onboarding; PR-based review of architectural moves.
- **Negative:** small ongoing authoring cost.
- **Neutral:** ADRs are not a substitute for architecture diagrams or specs — they complement them.

## Links

- Michael Nygard, *Documenting Architecture Decisions* (2011)
- [adr.github.io](https://adr.github.io/)
