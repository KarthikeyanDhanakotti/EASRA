# L2 — AI Orchestration

| Field | Value |
|-------|-------|
| Layer | L2 |
| Depends on Specs | 004, 005, 006, 008 |
| Status | Skeleton |

## 1. Purpose

L2 decides *how* a request is executed: single agent, multi-agent, or deterministic workflow. It owns the plan and the control flow, but never the prompt (L3), the model (L6), or the tool (L7).

## 2. Responsibilities

- **In scope.** AI Router, Single Agent runtime, Multi-Agent Coordinator, Planner, Workflow Engine.
- **Out of scope.** Prompt building, retrieval, model selection, tool execution, guardrails, verification.

## 3. Components

- **AI Router** — chooses between agent modes based on request features and policy.
- **Single Agent** — one agent runs the full request.
- **Multi-Agent Coordinator** — dispatches to sub-agents; merges results with bulkhead policy.
- **Planner / Workflow Engine** — decomposition and execution.

## 4. Design principles

**P5 Loose Coupling**, **P8 Failure Isolation**, **P7 Human-in-the-Loop**, **P10 Evolvability**.

## 5. Patterns

- Plan-and-execute vs ReAct — choose per task class.
- Deterministic workflows for high-impact processes; agents for exploratory or ambiguous tasks.
- Bulkheaded sub-agents; failure in one does not fail the coordinator.

## 6. Anti-patterns

- Unbounded plans (no step count or wall-clock cap).
- Agents bypassing L7 to invoke tools directly.
- Coordinator holding state in memory rather than the session store.

## 7. Failure modes

| Failure | Degraded mode |
|---------|---------------|
| Plan bound exceeded | Terminate with structured error; escalate per policy |
| Sub-agent failure | Coordinator bulkheads; degraded response if permitted |
| Loop detected | Break loop; alert |

## 8. Observability

Agent trace (plan steps, decisions), turn count, wall-clock, per-step latency and cost, sub-agent outcomes.

## 9. Production checklist

- [ ] Every plan has a step and time bound.
- [ ] Loop detection is active.
- [ ] Approval hooks wired to L14 for high-impact tools.
- [ ] Coordinator writes state to external store.
