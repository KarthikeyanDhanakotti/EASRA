# L7 — Tooling & Actions (MCP)

| Field | Value |
|-------|-------|
| Layer | L7 |
| Depends on Specs | 004, 005, 006, 009 |
| Status | Skeleton |

## 1. Purpose

L7 exposes tools to agents via **Model Context Protocol (MCP)**, enforces impact-class policy, and executes actions. It is the enforcement point for **Trust Boundary D** (Action).

## 2. Responsibilities

- **In scope.** Tool Router, MCP Client, MCP Server catalogue, Enterprise API adapters, Impact-Class enforcer, Tool audit logger.
- **Out of scope.** Model calls (L6), retrieval (L5), memory (L4).

## 3. Design principles

**P7 Human-in-the-Loop**, **P2 Security** (TB-D), **P10 Evolvability** (MCP as the extension point).

## 4. Patterns

- Tools declared in the Tool Registry (L14) with impact class.
- Idempotency keys for retriable side effects.
- Compensating actions declared for high-impact tools.
- Read tools separated from write and high-impact tools.

## 5. Anti-patterns

- Tools bypassed by direct API calls from L2/L6.
- Impact class not enforced (all tools treated equal).
- Side effects without an audit record.

## 6. Failure modes

| Failure | Degraded mode |
|---------|---------------|
| Tool unavailable | Structured error; agent retry or alternate |
| Tool timeout | Cancel; alert |
| Approval timeout | Fail closed |

## 7. Observability

Tool ID, arguments (redacted), result, latency, cost, impact class, approval outcome, side-effect record ID.

## 8. Security

Enforces **TB-D**. Every side effect audited. High-impact requires approval (L14).

## 9. Production checklist

- [ ] Tool registry versioned and reviewed.
- [ ] Impact class enforced.
- [ ] Approval path tested end-to-end.
- [ ] Idempotency keys wherever possible.
