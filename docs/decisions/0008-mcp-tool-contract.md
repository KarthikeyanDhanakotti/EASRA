# 8. MCP is the canonical tool-server contract

- **Status:** Accepted
- **Date:** 2026-07-12
- **Deciders:** @KarthikeyanDhanakotti
- **Consulted:** —
- **Informed:** EASRA contributors

## Context and Problem Statement

Agents need tools. Every framework (LangGraph, Semantic Kernel, Microsoft Agent Framework, OpenAI Assistants, Anthropic, custom orchestrators) has its own tool-registration format. Enterprises end up re-implementing the same tool wrapper 4-5 times, once per framework, with divergent auth, logging, and error contracts.

## Decision

**The Model Context Protocol (MCP) is EASRA's canonical tool-server contract.** All shared enterprise tools MUST be exposed as MCP servers. Native (in-process) tools MUST implement the same tool interface (name, JSON-schema arguments, structured return) so a tool can graduate from native to MCP without behavior change.

Enforced by:
- Tool registry in `EA-009 · MCP / Tool Fabric` accepts MCP-conformant tools only.
- SDK convention: framework-native tool adapters are thin wrappers over MCP calls.
- Tools that cannot be MCP-wrapped (e.g., in-process performance-critical helpers) are exceptions and documented as such.

## Consequences

**Positive**
- Write a tool once, use it from any orchestrator.
- Auth, sandboxing, egress policy, and observability apply uniformly (see `EA-009`).
- Compatible with the broader MCP ecosystem — inbound and outbound.

**Negative**
- MCP is young; spec is evolving. EASRA must track upstream changes.
- Some frameworks require adapter layers.

## Follow-ups

- MCP server onboarding checklist in `EA-009`.
- Reference MCP server implementation under `implementations/`.

## Related

- `EA-009 · MCP / Tool Fabric`, `PAT-002 · Multi-Agent Orchestration`, `SPEC-tool-contract` (planned)
