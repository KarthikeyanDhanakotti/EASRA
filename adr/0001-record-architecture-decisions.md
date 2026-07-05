# ADR-0001: Record architecture decisions

- **Status.** Accepted
- **Date.** 2026-07-05
- **Deciders.** Karthikeyan Dhanakotti (Lead Maintainer)
- **Consulted.** —
- **Public comment period.** N/A (foundational)
- **Supersedes.** —

## Context and problem statement

EASRA is intended to become a durable, vendor-neutral reference architecture. Its long-term credibility depends on transparent, reviewable decision-making — especially for changes to layer boundaries, interfaces, principles, and trust boundaries. Without a written record of *why* the architecture is shaped the way it is, future maintainers cannot know which properties are load-bearing and which are incidental.

## Decision drivers

- Long-term maintainability by contributors who were not present at the original design.
- Reviewable, auditable history of architectural choices.
- A lightweight process that does not deter contributions.
- Compatibility with common industry practice (MADR is widely used).

## Considered alternatives

### Alt A — No ADRs; rely on commit history and PR discussions
*Pros:* zero overhead. *Cons:* rationale is scattered, opaque, and lost as tooling changes.

### Alt B — RFCs (long-form, versioned in a separate repo)
*Pros:* structured discussion, versioning. *Cons:* heavyweight, delays decisions, discourages contributions.

### Alt C — MADR-style ADRs in `adr/`, with EASRA-specific additions
*Pros:* lightweight, well-known format, in-repo, discoverable. *Cons:* requires discipline.

## Decision

Adopt **Alt C**. Every significant architectural decision in EASRA is recorded as an ADR under [`adr/`](./). Structural decisions (layer boundaries, interfaces, principles, trust boundaries) *require* an ADR and a 14-day public comment period per [`../GOVERNANCE.md`](../GOVERNANCE.md).

ADRs use the MADR format with EASRA-specific fields: Public comment period, Impact on the specification, Compliance and security notes.

## Consequences

### Positive
- Every architectural choice is traceable.
- Contributors can propose changes through a well-understood, lightweight process.
- Superseded decisions remain visible with explicit succession.

### Negative
- Structural changes take at least 14 days by design.
- Some contributor overhead to write an ADR.

### Neutral
- The ADR folder becomes part of the reviewable surface of EASRA.

## Impact on the specification

- **Specifications affected.** None directly. All future spec changes are gated by ADRs when structural.
- **Interfaces affected.** None.
- **Trust boundaries affected.** None.
- **Migration required.** No.

## Compliance and security notes

None.

## References

- MADR — Markdown Architecture Decision Records — https://adr.github.io/madr/
- Michael Nygard, "Documenting Architecture Decisions" (2011).
