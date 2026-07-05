# EASRA Reference Implementation

The **reference implementation** is a minimal, open-source, spec-conformant Enterprise AI system. Its purpose is to prove that EASRA is buildable, provide a starting point for adopters, and serve as the substrate for the conformance test suite.

## Status

**Scaffold only.** Version 0.1 ships the intent, folder layout, and conformance-test outline. Code lands in Phase 3 of the [ROADMAP](../ROADMAP.md).

## Goals

- Implement every layer in [Specification 005](../specification/005-layer-definitions.md), at the minimum useful level.
- Honour every interface contract in [Specification 006](../specification/006-interface-specification.md).
- Pass a conformance test suite that mirrors the specification.
- Run locally with `docker compose up` and against ≥ 1 cloud with an `azd`/`terraform` deployment.
- Stay small — this is a *reference*, not a product.

## Non-goals

- Not production-hardened.
- Not multi-tenant at scale.
- Not opinionated about model provider (adapters ship for at least two).

## Planned layout

```
reference-implementation/
├── README.md                  (this file)
├── schemas/                   JSON Schema for every interface in Spec 006
│   ├── ClientRequest.json
│   ├── ValidatedRequest.json
│   ├── ContextRequest.json
│   ├── PromptManifest.json
│   ├── ModelRequest.json
│   ├── ModelResponse.json
│   ├── ToolInvocation.json
│   ├── ToolResult.json
│   ├── GuardrailCheck.json
│   ├── Verdict.json
│   ├── ErrorEnvelope.json
│   └── CostRecord.json
├── conformance/               Conformance test outline
│   ├── README.md
│   ├── layer-contracts/
│   ├── trust-boundaries/
│   └── sequences/
├── src/                       Implementation (Phase 3)
│   ├── l1-gateway/
│   ├── l2-orchestrator/
│   ├── l3-prompt/
│   ├── l4-memory/
│   ├── l5-retrieval/
│   ├── l6-model-router/
│   ├── l7-tools-mcp/
│   ├── l8-guardrails/
│   ├── l9-verification/
│   ├── l10-observability/
│   └── l11-cache/
├── deploy/
│   ├── docker-compose.yml
│   ├── kubernetes/
│   └── azd/
└── tests/
    ├── contract/
    ├── e2e/
    └── chaos/
```

## Conformance test suite (planned)

Tests are grouped by what they assert:

- **Layer contract tests** — for each layer, each interface, each error envelope.
- **Trust boundary tests** — that each TB has the required controls and fails closed / safe correctly.
- **Sequence tests** — that each canonical sequence in Spec 008 executes as specified.
- **NFR tests** — smoke tests for the categories in Spec 010 (not benchmarks; conformance, not performance).

The test suite will be usable against *any* implementation of EASRA (not just this one) that exposes a defined test-harness endpoint.

## Contributing

Reference-implementation contributions are gated on the specification being stable in the relevant area. See the phase gates in [ROADMAP](../ROADMAP.md) and open a discussion before starting a large slice.
