# ADR-0002: Vendor-neutral scope for EASRA

- **Status.** Accepted
- **Date.** 2026-07-05
- **Deciders.** Karthikeyan Dhanakotti (Lead Maintainer)
- **Consulted.** —
- **Public comment period.** N/A (foundational)
- **Supersedes.** —

## Context and problem statement

Enterprise AI reference material available today is overwhelmingly vendor-specific. Azure, AWS, and GCP each publish detailed guidance that maps their products to AI architectures, and framework vendors (LangChain, LlamaIndex, Semantic Kernel, Bedrock Agents, etc.) publish guidance tied to their SDKs. This is useful but insufficient: it does not describe the architectural surface the products implement, and it does not survive vendor churn.

EASRA must decide whether to:

- (a) present a vendor-specific reference (e.g., Azure-first), or
- (b) present a framework-first reference (e.g., LangChain-first), or
- (c) present a vendor-neutral reference that maps to any of the above.

## Decision drivers

- Long-term durability across a 5–10 year horizon during which models, vendors, and frameworks will change substantially.
- Adoption breadth — teams on all three major clouds and on-premises must be able to use EASRA.
- Trustworthiness as a standard — a vendor-neutral document is more credible as a "TOGAF for Enterprise AI".
- Practicality — every layer must map to *at least two* real implementations, or the specification is impractical.

## Considered alternatives

### Alt A — Azure-first reference
*Pros:* concrete, actionable, aligned with maintainer's day-to-day. *Cons:* immediate loss of adoption on AWS/GCP; conflates architecture with vendor products; long-term risk.

### Alt B — Framework-first reference (e.g., LangChain/LlamaIndex)
*Pros:* concrete abstractions to build against. *Cons:* framework churn every 3–6 months; incompatible with self-hosted or non-framework implementations; not durable.

### Alt C — Vendor-neutral reference with implementation mappings
*Pros:* durable, credible, broad adoption; separates architecture from implementation as required by P1. *Cons:* more work — every layer needs ≥ 2 implementation mappings; harder to write concretely without collapsing into vendor prose.

## Decision

Adopt **Alt C**. EASRA is defined in logical, vendor-neutral terms. Vendor mappings appear only in dedicated "Cloud Implementation" subsections in the handbook and must cover at least two of {Azure, AWS, GCP, open-source} for every layer. Specification and interface signatures may not name a vendor product.

This decision is codified as design principle **P1 Vendor Neutrality** in [Specification 002](../specification/002-design-principles.md#p1--vendor-neutrality) and enforced by the contribution rules in [`../CONTRIBUTING.md`](../CONTRIBUTING.md).

## Consequences

### Positive
- EASRA is credible as a neutral standard.
- Adopters on any platform can use it without translation.
- Vendor churn does not invalidate the specification.

### Negative
- Specification prose is more abstract than a vendor-specific guide.
- Every handbook chapter carries the cost of ≥ 2 implementation mappings.
- Initial content coverage is thinner than a vendor-first would be at the same phase.

### Neutral
- Vendor mappings become an ongoing, discrete workstream.

## Impact on the specification

- **Specifications affected.** All ten; P1 in Spec 002 is the direct expression.
- **Interfaces affected.** No proprietary types allowed in Spec 006 signatures.
- **Trust boundaries affected.** None.
- **Migration required.** No (foundational).

## Compliance and security notes

Vendor neutrality does not weaken compliance. Each cloud mapping in the handbook enumerates the compliance controls native to that cloud that satisfy the EASRA control requirements.

## References

- [Specification 001 §6 — Non-Goals](../specification/001-introduction.md#6-non-goals)
- [Specification 002 §P1 — Vendor Neutrality](../specification/002-design-principles.md#p1--vendor-neutrality)
- [`../CONTRIBUTING.md` § Ground rules](../CONTRIBUTING.md)
