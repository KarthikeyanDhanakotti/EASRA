# EASRA Ecosystem Style Guide

Every repository in the EASRA ecosystem (EASRA itself, EAEC, EAVF, CognitiveAgentLab, EnterpriseAIExamples, EnterpriseAIBench, EnterpriseAIPatterns, EnterpriseAIOps) follows this style guide so the ecosystem reads as one coherent body of work.

## 1. Writing

- **Voice.** Neutral, precise, technology-neutral. Never breathless.
- **Person.** Third person; avoid "we" and "you" outside contribution guides.
- **Definitions before diagrams.** Never introduce a component in a diagram before it exists in prose.
- **Every claim cites its spec, capability, or component.**
- **Standards.** Reference standards by name and link (NIST AI RMF, ISO/IEC 42001, EU AI Act, OWASP LLM Top 10, MITRE ATLAS, OpenTelemetry, W3C TraceContext, MCP).

## 2. Naming

- **Repository names.** PascalCase acronyms (`EASRA`, `EAEC`, `EAVF`) or `EnterpriseAI<Thing>` (`EnterpriseAIBench`, `EnterpriseAIExamples`, `EnterpriseAIPatterns`, `EnterpriseAIOps`, `EnterpriseAIAgents`).
- **Component IDs.** `K-L<layer>-<short>` per [Spec 012](../specification/012-component-catalogue.md). Never invent a component without a catalogue entry.
- **Capability IDs.** `C<n>` for domains, `C<n>.<m>` for subcapabilities per [Spec 011](../specification/011-capability-model.md).
- **Diagram IDs.** `D-<view><n>` per the [Diagram Catalogue](../diagrams/CATALOGUE.md).
- **Benchmark IDs.** `B-<category>[-<workload>]` per [benchmarks/](../benchmarks/README.md).
- **Interface IDs.** `IX.L<n>→L<n>` per [Spec 006](../specification/006-interface-specification.md).

## 3. README shape

Every repository README opens with:

1. Title and one-sentence positioning.
2. "Part of the EASRA ecosystem" banner linking to EASRA.
3. Elevator pitch (2–3 sentences).
4. Architecture diagram.
5. Quick start.
6. Screenshot / example output.
7. Diagrams, Roadmap, Examples, References, Research, Contributing, License, Maintainer.

Use the [repository starter template](./repository-template/README.md).

## 4. Diagrams

- **Preferred tool.** Mermaid, then drawio for complex diagrams.
- **Never** use empty-label dotted edges (`A -. .-> B`) — invalid on `github.com`. Use `A -.-> B` or `A -.->|"label"| B`.
- **ASCII fallback** for any Mermaid diagram in a spec-critical location.
- Every named element must exist in the [Component Catalogue](../specification/012-component-catalogue.md).
- Every diagram registered in the [Diagram Catalogue](../diagrams/CATALOGUE.md) with an ID.
- Colour is used only to distinguish planes (user / observability / security / data). See §5.

## 5. Colour palette (accessible, print-safe)

| Purpose | Hex | Notes |
|---------|-----|-------|
| User / entry | `#3B7DDD` on `#EAF3FF` | Ingress and channel components. |
| Observability | `#B58900` on `#FFF6E5` | L10 and cross-cutting telemetry. |
| Security / trust boundary | `#C0392B` on `#FDECEA` | Boundary lines, guardrail nodes. |
| Data / storage | `#16A085` on `#E8F8F5` | Memory, retrieval, cost ledger. |
| Model | `#8E44AD` on `#F5EAF7` | Model router, models, fallback. |
| Neutral component | `#2C3E50` on `#ECF0F1` | Default nodes. |

## 6. Logos

- **Word-mark.** `EASRA` in a monospaced or geometric sans (e.g., JetBrains Mono, Inter Tight).
- **Family lockup.** `EASRA · EAEC · EAVF · CognitiveAgentLab · EnterpriseAI*`.
- **Placement.** Repository social preview image + docs site header.
- **Working files** live under [`../docs/assets/`](../docs/) — planned.

## 7. Licensing

- **Documentation, specifications, diagrams:** CC-BY-4.0.
- **Code and reference implementation:** Apache-2.0.
- **Combined LICENSE file** stating both.
- **Attribution:** "Dhanakotti, K. (2026). Enterprise AI Systems Reference Architecture (EASRA), v0.x."

## 8. Governance

- **Structural change** → ADR + 14-day comment period.
- **Deprecation** → announced in a minor release; removed no earlier than the next major.
- **Version pinning** → consumers pin to a commit hash until v1.0.

## 9. Change to this guide

Requires an ADR under [`../adr/`](../adr/).
