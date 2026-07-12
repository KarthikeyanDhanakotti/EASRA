# EASRA Architecture Map

**Architectures** (`EA-`) are canonical, capability-driven blueprints of the EASRA reference. Each page is vendor-neutral, maps to one or more layers of the [Capability Model](../reference-models/capability-model.md), and is realized by one or more [Patterns](../patterns/README.md) and [Implementations](../implementations/README.md).

See [ADR-002 · Vendor-neutrality](../docs/decisions/0002-vendor-neutrality.md) and [ADR-006 · Capability Model](../docs/decisions/0006-capability-model.md) for the governance rules that shape these pages.

## Catalog

| ID     | Architecture                                                        | Layer(s)                    | Status         |
|--------|---------------------------------------------------------------------|-----------------------------|----------------|
| EA-001 | [Enterprise AI Systems — Reference Model](EA-001-Enterprise-AI-Systems.md) | L1–L7 (system-level)         | 🟢 Canonical (v0.1) |
| EA-002 | [Enterprise AI Gateway](EA-002-Enterprise-AI-Gateway.md)             | L2 Orchestration / L7 Foundation | 🟢 Canonical (v0.1) |
| EA-003 | [Runtime Plane](EA-003-Runtime-Plane.md)                             | L3 Runtime                   | 🟢 Canonical (v0.1) |
| EA-004 | [Control Plane](EA-004-Control-Plane.md)                             | L6 Control                   | 🌱 Stub (Sprint-03) |
| EA-005 | [Knowledge Plane](EA-005-Knowledge-Plane.md)                         | L4 Knowledge                 | 🌱 Stub (Sprint-03) |
| EA-006 | [Model Router](EA-006-Model-Router.md)                               | L2 Orchestration             | 🌱 Stub (Sprint-03) |
| EA-007 | [Prompt Intelligence](EA-007-Prompt-Intelligence.md)                 | L2 Orchestration             | 🌱 Stub (Sprint-03) |
| EA-008 | [Memory Plane](EA-008-Memory-Plane.md)                               | L3 Runtime                   | 🌱 Stub (Sprint-03) |
| EA-009 | [MCP / Tool Fabric](EA-009-MCP-Tool-Fabric.md)                       | L3 Runtime                   | 🌱 Stub (Sprint-03) |
| EA-010 | [Verification Plane](EA-010-Verification-Plane.md)                   | L5 Verification              | 🌱 Stub (Sprint-03) |

## Legend

- 🟢 **Canonical** — v0.1+ published, reviewed, considered stable within the sprint.
- 🌱 **Stub** — placeholder page committed so the taxonomy is complete; body lands in Sprint-03.
- 🟡 **Draft** — being written, subject to change.

## Relationships

```
                     EA-001 · Enterprise AI Systems
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
    EA-002 Gateway       EA-003 Runtime        EA-004 Control
        │                     │                     │
   ┌────┼────┐          ┌─────┼─────┐          (registries,
   │    │    │          │     │     │           policy,
 EA-006 EA-007 …    EA-008 EA-009 EA-010     promotion,
 Router  Prompt-I   Memory Tool-F Verify       cost)
                                     │
                              EA-005 Knowledge
```

## Adding a new architecture

1. Reserve the next `EA-NNN` in this table with the status set to 🌱 Stub.
2. Create `EA-NNN-<Slug>.md` from the stub template (see any Sprint-02 stub in this folder).
3. Add an entry to the [top-level Architecture Map](../README.md).
4. Map the new architecture to at least one layer in the [Capability Model](../reference-models/capability-model.md).
5. If the architecture introduces a design principle, propose an ADR under [`docs/decisions/`](../docs/decisions/README.md).
