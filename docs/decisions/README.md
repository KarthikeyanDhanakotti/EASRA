# EASRA Architecture Decision Records (ADRs)

**ADRs** capture the *why* behind EASRA's design — the non-obvious, load-bearing choices that shape the architectures, patterns, and reference models.

Format: [Nygard-style ADRs](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions.html), extended with a lightweight Deciders/Consulted/Informed header. See [ADR-0001](0001-record-architecture-decisions.md) for the meta-decision to use ADRs at all.

## Numbering

- 4-digit, zero-padded, monotonically increasing (`0001`, `0002`, …).
- Never renumber. Superseded ADRs are marked `Status: Superseded by ADR-NNNN`.

## Catalog

| ID   | Title                                                                   | Status         |
|------|-------------------------------------------------------------------------|----------------|
| 0001 | [Record architecture decisions](0001-record-architecture-decisions.md)  | 🟢 Accepted    |
| 0002 | [Vendor-neutrality principle](0002-vendor-neutrality.md)                | 🟢 Accepted    |
| 0003 | [Verification-first: no promotion without passing evals](0003-verification-first.md) | 🟢 Accepted    |
| 0004 | [AI Gateway is the sole ingress for model traffic](0004-ai-gateway-sole-ingress.md) | 🟢 Accepted    |
| 0005 | [Prompts are first-class deployable artifacts](0005-prompt-registry.md) | 🟢 Accepted    |
| 0006 | [The 7-layer Capability Model is the canonical taxonomy](0006-capability-model.md) | 🟢 Accepted    |
| 0007 | [OpenTelemetry `gen_ai.*` is the canonical observability contract](0007-otel-gen-ai.md) | 🟢 Accepted    |
| 0008 | [MCP is the canonical tool-server contract](0008-mcp-tool-contract.md)  | 🟢 Accepted    |
| 0009 | [Every memory tier must implement the Forget contract](0009-forget-contract.md) | 🟢 Accepted    |

## Legend

- 🟢 **Accepted** — decision is in force.
- 🟡 **Proposed** — under discussion.
- 🔴 **Rejected** — considered and declined; kept for the record.
- ⚫ **Superseded** — replaced by a later ADR (referenced by number).

## Adding an ADR

1. Copy [`0001-record-architecture-decisions.md`](0001-record-architecture-decisions.md) as a template.
2. Number it with the next free 4-digit id.
3. Fill in: Status / Date / Deciders / Consulted / Informed, Context, Decision, Consequences, Follow-ups, Related.
4. Add a row to the catalog above.
5. If the ADR changes a Sprint-02+ canonical artifact, add a `CHANGELOG.md` entry.
