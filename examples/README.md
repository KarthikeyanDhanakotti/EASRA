# EASRA Examples

Worked-through examples showing spec-conformant Enterprise AI systems for common patterns. Each example:

- Names the EASRA layers it uses.
- Points to the specification sections it depends on.
- Includes a Mermaid architecture diagram.
- Enumerates its trust boundaries, guardrails, verification checks, observability signals, and cost profile.
- Lists what it deliberately *does not* include (so it does not accidentally imply completeness).

## Catalogue

| # | Example | Mode | Status |
|---|---------|------|--------|
| E1 | [Single-Agent RAG](./single-agent-rag/) | M2 (RAG) + M1 (chat) | Draft |
| E2 | Multi-Agent Coordinator *(planned)* | M5 | Placeholder |
| E3 | Single-Agent Tool Use with MCP *(planned)* | M4 | Placeholder |
| E4 | Cost-aware Multi-Model Routing *(planned)* | M1/M2 | Placeholder |
| E5 | Async Workflow with Event Bus *(planned)* | future | Placeholder |

## Purpose of examples

Examples are **reference-quality**, not production systems. They are meant to:

- Show a spec-conformant shape for a common pattern.
- Serve as a starting point for teams adopting EASRA.
- Test the specification against real cases — friction here drives spec improvements.

They are **not**:

- Optimised for cost, latency, or scale.
- Complete in every layer (guardrails, verification, and observability may be minimal).
- Endorsement of any vendor or product.

## Contributing an example

See [`../CONTRIBUTING.md`](../CONTRIBUTING.md). Every example must:

1. Follow the folder structure of `single-agent-rag/`.
2. Include an architecture diagram in Mermaid.
3. Map to EASRA layers with a table.
4. Declare its non-goals.
5. Be dual-licensed under the repo's licences.
