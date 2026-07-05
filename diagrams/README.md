# EASRA Diagrams

Publication-grade architecture, sequence, and topology diagrams for EASRA. The canonical high-level diagram is the visual entry point to the whole framework — see [`high-level-architecture.md`](./high-level-architecture.md).

## Contents

| File | Purpose | Source |
|------|---------|--------|
| [high-level-architecture.md](./high-level-architecture.md) | The canonical 16-layer high-level architecture (Mermaid + ASCII + colour-plane view). | Spec 004 |
| [trust-boundaries.md](./trust-boundaries.md) | The four trust boundaries with OWASP LLM Top 10 threat mapping. | Spec 009 |
| [deployment-topology.md](./deployment-topology.md) | Logical deployment topology across tiers. | Spec 004 §8 |
| [cicd-pipeline.md](./cicd-pipeline.md) | Delivery pipeline (L12 · TP-2) with gates and rollback. | Spec 005 L12 |
| [observability-plane.md](./observability-plane.md) | Observability plane (L10) with emitters, collector, backends, products. | Spec 005 L10 |

## Format

- **Mermaid** is the source of truth. It renders on GitHub and copy-pastes into any Mermaid-capable tool.
- **ASCII** versions accompany the flagship diagram for terminals and plain-text media.
- Exports (`.svg`, `.png`, `.drawio`) are added post-v0.1 for slides, papers, and the docs site. Sources always take precedence over exports.

## Contributing a diagram

1. Prefer Mermaid; only add an image if Mermaid cannot express the idea.
2. Keep layer names, interface names, checkpoint names, and boundary IDs (TB-A/B/C/D, TP-1/2) *identical* to the specification.
3. Use the colour table in [`high-level-architecture.md` §3](./high-level-architecture.md#3-color-coded-plane-view-for-presentations) — do not introduce new plane colours.
4. Include a Change Log at the bottom of the diagram file.

See [`../CONTRIBUTING.md`](../CONTRIBUTING.md) for the full process.
