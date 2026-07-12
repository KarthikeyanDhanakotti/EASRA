# PAT-002 · Multi-Agent Orchestration

> **Layer:** L3 Runtime
> **Status:** Draft

## Context

A task is too complex, too specialized, or too parallelizable for a single agent. You need multiple agents that plan, delegate, execute, and critique each other's work — while remaining observable, safe, and cost-bounded.

## Problem

- Single monolithic agents become **brittle prompt spaghetti** at high complexity
- No clear **ownership boundary** between reasoning, tool use, and critique
- Hard to **evaluate** what went wrong (which agent? which step?)
- Runaway loops burn budget without producing outcomes

## Solution

Decompose the task across specialized agents with **explicit roles, contracts, and arbitration**:

- **Planner** — decomposes the task into a plan
- **Executor(s)** — execute plan steps, invoking tools
- **Critic / verifier** — reviews executor output, requests re-work
- **Router / arbitrator** — decides which agent handles the next step (deterministic or LLM-driven)
- **Memory** — shared working state, plus per-agent scratch

Every hop traverses the gateway (see [EA-002](../architectures/EA-002-Enterprise-AI-Gateway.md) and [PAT-001](PAT-001-AI-Gateway.md)) so quota, safety, and cost apply uniformly.

### Minimal design sketch

```
                     ┌── Planner ──┐
Task ──► Router ─────┤             ├─► Aggregator ─► Response
                     ├── Exec 1 ──┤
                     ├── Exec 2 ──┤
                     └── Critic ──┘
                             │
                             └── loops back through Router
```

## Interfaces

- **Agent contract:** `role`, `capabilities[]`, `tool_allow_list[]`, `budget_ceiling`, `max_turns`
- **Handoff message:** shared plan + state + provenance chain
- **Termination:** either goal-reached, max-turns exceeded, or budget-exceeded

## Controls

- Per-agent **tool allow-list** enforced at the gateway
- **Max turns / max cost** hard-stops in the orchestrator
- **Cycle detection** to break infinite handoff loops
- **Provenance chain** — every action traceable to the deciding agent

## KPIs

- **Task success rate** (graded end-to-end)
- **Cost per task** — USD & tokens
- **Turns to completion** distribution
- **% tasks terminated by budget** — high = badly-scoped plans
- **Critic disagreement rate** — quality signal on executor

## Trade-offs

- Higher total token cost than single-agent
- Higher latency (more round-trips)
- Debugging is harder → mitigated by strict tracing (per-agent span)

## Anti-patterns

- **Everything-is-an-agent** — agents that could be deterministic code
- **No budget ceiling** — always set a hard budget & turn cap
- **Implicit handoffs** — always require explicit `handoff` events for traceability
- **Shared unbounded memory** — bounded, scoped memory only

## Variants

- **Hierarchical** — one supervising agent + workers
- **Peer-to-peer** — flat mesh with routing
- **Pipeline** — deterministic order, agents as stages
- **Debate** — two agents argue, third arbitrates

## Related

- [PAT-001 · AI Gateway](PAT-001-AI-Gateway.md) — every agent hop still traverses it
- [PAT-003 · Verification Loop](PAT-003-Verification.md) — how to grade multi-agent outcomes
- [EA-003 · Runtime Plane](../architectures/EA-002-Enterprise-AI-Gateway.md) *(planned)*
