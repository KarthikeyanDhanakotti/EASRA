# EA-003 · Runtime Plane (Agent Orchestration)

**Status:** v0.1 (Sprint-02) · **Companion:** [EA-001](EA-001-Enterprise-AI-Systems.md), [EA-002](EA-002-Enterprise-AI-Gateway.md) · **Diagram:** [`diagrams/EA-003-Runtime-Plane.png`](../diagrams/EA-003-Runtime-Plane.png)

![EA-003](../diagrams/EA-003-Runtime-Plane.png)

## Purpose

EA-002 delivers a request *to* the AI system with policy enforcement. **EA-003 defines what happens next inside the system** — how a single request becomes plans, tool calls, memory reads, and audited outputs, without losing observability, budget bounds, or safety guarantees.

This is where "agentic" moves from marketing to engineering: **the runtime plane is the smallest piece of the architecture where an agent gains autonomy, and therefore the largest piece where controls must exist.**

## Design Goals

| # | Goal | How EA-003 addresses it |
|---|------|-------------------------|
| G1 | Bounded autonomy | Explicit budgets (steps, tokens, $, wall-clock) enforced at execution |
| G2 | Deterministic reproducibility | Idempotent step runner + durable task state |
| G3 | Tool safety | Only path to the outside world is the Tools plane; all tool calls signed, allow-listed, sandboxed |
| G4 | Memory hygiene | 4 distinct memory tiers with explicit TTL, consent, and forget semantics |
| G5 | Multi-agent scaling | Explicit handoff envelope carrying scope, budget, provenance |
| G6 | Human-in-the-loop | HITL is a first-class pillar, not an afterthought |
| G7 | Full observability | Every step emits an OpenTelemetry span with `gen_ai.*` attributes |

## Architecture

Four bands + one cross-cutting pillar:

| Band | Plane | Purpose |
|------|-------|---------|
| B1 · Orchestration | Planner · Workflow · Critic · Multi-Agent Coordinator | Turn intent into a plan; supervise its execution |
| B2 · Execution     | Step Runner · Retry · Cancellation · Budget · Spans | Run one step deterministically with observability |
| B3 · Tools &amp; Actions | Native tools · MCP servers · HTTP callers · Code interp · Sandbox · Consent | The only path to the outside world |
| B4 · Memory &amp; State | Working · Session · Long-term · Vector · Shared · Task state | What the agent knows, remembers, and can resume from |
| Pillar · HITL &amp; Safety | Approval · Queue · Kill-switch · Budget · Trace · Policy · Handoff · Audit | Human control &amp; safety enforced across every band |

## Component Details

### Orchestration Plane

**Planner** — Decomposes user intent into a plan graph. Consumes: user goal, active policies, budget envelope. Emits: plan graph + acceptance criteria. Reference algorithms: ReAct, Plan-and-Execute, LLM Compiler.

**Workflow Engine** — Durable DAG / graph runtime with retries, timers, cycles, and branches. Must survive process restart (checkpoint to Task State).

**Reflection Loop** — Plan → Act → Observe → Revise. **Must be bounded** — enforce `max_steps`, `max_tokens`, `max_wall_clock`, and `max_cost_usd` at every iteration.

**Critic / Verifier** — Post-step check. Combines rule-based validation (schema, allow-list, format), LLM-as-judge scoring, and pattern-based safety checks. Non-passing steps are either revised, escalated to HITL, or aborted.

**Multi-Agent Coordinator** — For multi-agent topologies (router-and-specialists, hierarchical, debate). Every agent handoff produces a signed **handoff envelope** carrying `{scope, budget_remaining, provenance_chain, parent_trace_id}`.

### Execution Plane

**Step Runner** — Idempotent, retryable. A step has a stable ID and a deterministic input hash so re-runs produce identical spans. Native retries live here, not in the Planner.

**Retry &amp; Backoff** — Exponential + jitter, with circuit breakers per tool and per model. Correlated with Budget Meter.

**Cancellation** — Cooperative cancellation triggered by user, budget exhaustion, or kill-switch. Must be honored within N seconds (system-configured).

**Budget Meter** — Live count of `$`, tokens, and wall-clock consumed by the current request. Exposed to Planner + Critic + HITL for informed decisions.

**Span Emitter** — Every step emits an OpenTelemetry span with `gen_ai.request.model`, `gen_ai.response.model`, `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, plus EASRA-specific attributes: `easra.plan.node_id`, `easra.tool.name`, `easra.budget.remaining_usd`.

### Tools &amp; Actions Plane

**Native Tool Registry** — Typed, versioned, allow-listed tools. Per-tenant scope + rate limits. Registry entry: `{name, version, schema_in, schema_out, permission_level, rate_per_tenant, cost_hint}`.

**MCP Servers** — Model Context Protocol adapters for external capabilities. Same registration discipline as native tools.

**HTTP / API Callers** — Signed and scoped token holders (short-lived, from workload identity). Egress policy enforced (allow-list of hostnames).

**Code Interpreter** — Python / JS runtime for analysis tasks. Always runs inside the sandbox.

**Sandbox / Isolation** — Ephemeral, no-network or egress-pinned. CPU / memory / time bounded. Preferably one sandbox per request (containers, gVisor, Firecracker, or hosted equivalents).

**Tool Consent** — Any `permission_level >= high` tool call goes through HITL approval. The consent decision is captured as a signed intent link in the trace.

### Memory &amp; State Plane

| Tier | Scope | TTL | Backing store |
|------|-------|-----|---------------|
| Working memory | Turn / step | Request | In-process object |
| Session memory | User + conversation | Session (default 24h) | Redis / KV |
| Long-term memory | User / tenant | Consent-gated, revocable | DB with forget API |
| Vector memory | Episodic embeddings | Decayed by recency | ANN store (Redis, Cosmos DB vector, AI Search) |
| Shared / team memory | Cross-agent workspace | Explicit RBAC per key namespace | Blob + index |
| Task state | Workflow checkpoints | Until task terminal | Durable store (Cosmos, Postgres, Durable Task Framework) |

**Forget contract:** every memory tier that stores identifiable data must implement a `POST /forget?subject=X` endpoint that returns 200 only after complete removal (including embeddings, indices, and derived artifacts).

### HITL &amp; Safety Pillar

- **Approval Checkpoint** — Configurable trigger: high-risk tool, high-cost action, unusual pattern.
- **HITL Queue** — Reviewer inbox with SLAs; unfulfilled after SLA either escalates or aborts.
- **Kill-Switch** — Scoped: single agent, single tool, whole tenant. Immediate effect.
- **Budget Guard** — Global $, tokens, and step budgets per request, per session, per tenant.
- **Trace &amp; Span** — OTel `gen_ai.*` conventions, correlated with the ingress `x-easra-trace-id`.
- **Policy Guardrails** — Tool allow-list, scope-of-action restrictions, per-role capabilities.
- **Agent-to-Agent Handoff** — Signed, attested envelope; receiver validates before continuing.
- **Post-hoc Audit** — Every request produces an immutable evidence bundle written to WORM storage.

## Interface Contract (v0.1)

An agent request enters EA-003 already authenticated and policy-checked by EA-002. The runtime plane exposes:

```
POST /v1/runtime/tasks
{
  "task_id": "opt-client-supplied",
  "goal": "string",
  "context": { "tenant": "...", "user": "...", "trace_id": "..." },
  "budget": { "usd_max": 0.50, "tokens_max": 50000, "steps_max": 20, "wall_clock_sec_max": 60 },
  "tools_allow": ["tool.name@version", "..."],
  "memory_scope": { "session_id": "...", "long_term": true }
}
→ 202 Accepted
{
  "task_id": "...",
  "state_uri": "/v1/runtime/tasks/{task_id}",
  "stream_uri": "/v1/runtime/tasks/{task_id}/events"
}
```

Streaming events (SSE) carry `plan.updated`, `step.started`, `step.completed`, `tool.invoked`, `memory.written`, `hitl.requested`, `budget.consumed`, `task.completed`, `task.failed`.

## Observability Contract

Every step MUST emit an OpenTelemetry span with:

| Attribute | Notes |
|-----------|-------|
| `gen_ai.system` | model provider |
| `gen_ai.request.model` | model version |
| `gen_ai.usage.input_tokens` / `output_tokens` | usage |
| `easra.task_id` | correlates all steps of one task |
| `easra.plan.node_id` | which node in the plan graph |
| `easra.tool.name` / `easra.tool.version` | for tool calls |
| `easra.budget.remaining_usd` | for FinOps aggregation |
| `easra.hitl.decision` | for HITL steps |
| `easra.memory.tier` / `easra.memory.op` | for memory reads/writes |

## Failure Modes

| Failure | Detection | Response |
|---------|-----------|----------|
| Runaway loop | Step count / budget exceeded | Cancellation → 429-style task_aborted |
| Tool unavailable | Circuit-break triggered | Retry with alternative or degrade |
| Sandbox breakout attempt | Sandbox telemetry | Kill-switch + tenant audit alert |
| Memory forget lag | Forget contract test | Bounded audit + block on-write until reconciled |
| Handoff signature invalid | Coordinator validation | Refuse handoff, log security event |
| HITL SLA breach | Queue watchdog | Escalate → default policy (abort by default) |

## Related Patterns

- [PAT-002 · Multi-Agent Orchestration](../patterns/PAT-002-Multi-Agent.md)
- [PAT-003 · Verification &amp; Grounding](../patterns/PAT-003-Verification.md)
- [PAT-004 · Prompt Intelligence](../patterns/PAT-004-Prompt-Intelligence.md)

## Reference Implementations

| Cloud | Path | Status |
|-------|------|--------|
| Azure (Durable Functions + Foundry Agent) | *(planned)* `implementations/azure/runtime-plane/` | ⏳ Sprint-03 |

## Related Architectures

- [EA-001 · Enterprise AI Systems](EA-001-Enterprise-AI-Systems.md) — where EA-003 sits
- [EA-002 · Enterprise AI Gateway](EA-002-Enterprise-AI-Gateway.md) — what feeds EA-003
- [EA-005 · Knowledge &amp; Retrieval Plane](EA-005-Knowledge-Retrieval-Plane.md) *(planned)*
- [EA-006 · Evaluation &amp; Telemetry Plane](EA-006-Evaluation-Telemetry-Plane.md) *(planned)*

## Changelog

- v0.1 · Sprint-02 · Initial specification, diagram, interface contract, observability contract.
