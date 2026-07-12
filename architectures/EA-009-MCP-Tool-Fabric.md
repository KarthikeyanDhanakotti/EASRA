# EA-009 · MCP / Tool Fabric

**Status:** Stub (v0.0.1) · **Sprint:** planned Sprint-03 · **Taxonomy:** `EA-`

> Placeholder page. The full MCP / Tool Fabric specification will land in **Sprint-03**.

## Purpose

Define how enterprise AI systems expose **tools and external capabilities** to agents — safely, discoverably, and with strong isolation. The plane where the [Model Context Protocol (MCP)](https://modelcontextprotocol.io) meets enterprise controls.

## Scope (draft)

- Native tool registry (typed schemas, versioning, allow-list, per-tenant scope)
- MCP server registry &amp; onboarding (adapter contract, health, freshness)
- Tool discovery for agents (advertised subset per role / task)
- Sandbox / isolation (ephemeral, no-net or egress-pinned, CPU/memory/time bounds)
- Egress policy (allow-list of destinations, egress attestation)
- Tool consent workflow (high-risk tools require HITL)
- Tool observability (`easra.tool.name`, `easra.tool.version`, `easra.tool.latency_ms`)
- Signed intent chain for tool call → external side-effect

## Design Goals (draft)

- G1 · A tool call is the only way an agent affects the world outside itself. Enforced at the plane boundary.
- G2 · Every tool is versioned, permission-tiered, and auditable end-to-end.
- G3 · MCP servers are onboarded through the same governance as native tools — no privileged shortcut.
- G4 · Sandbox isolation is verifiable, not assumed.

## Related

- Consumed by [EA-003 · Runtime Plane](EA-003-Runtime-Plane.md) (Tools band)
- Registry governed by [EA-004 · Control Plane](EA-004-Control-Plane.md)
- Related patterns (planned): PAT-002 Multi-Agent (already in repo), PAT-006 Memory
- Related decisions (planned): ADR-008 MCP as tool-server contract

## Changelog

- v0.0.1 · Sprint-02 · Stub created as part of the 15-view architecture map.
