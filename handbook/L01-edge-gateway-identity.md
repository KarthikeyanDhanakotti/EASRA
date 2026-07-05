# L1 — Edge · Gateway · Identity

| Field | Value |
|-------|-------|
| Layer | L1 |
| Depends on Specs | 004, 005, 006, 009 |
| Status | Skeleton |

## 1. Purpose

L1 is the enforcement point for **Trust Boundary A** (Edge). It turns an untrusted external request into an authenticated, authorised, rate-limited, session-bearing internal request.

## 2. Responsibilities

- **In scope.** CDN, WAF, LB, API Gateway, Authentication, coarse Authorisation, Rate Limiter, Bot Protection, Session Manager, Request Validator.
- **Out of scope.** Prompt-injection detection (L8), fine-grained tool authorisation (L7 + L14).

## 3. Components

- **CDN + WAF + Bot Protection** — edge defence.
- **API Gateway** — request routing, throttling, contract enforcement.
- **Authentication** — OIDC/OAuth2/SSO; propagates a verified `Identity`.
- **Authorisation (coarse)** — is this identity allowed on this API at all?
- **Rate Limiter** — per-identity, per-tenant, per-channel.
- **Session Manager** — externalised (P6); loads/creates session state.
- **Request Validator** — schema and semantic validation.

## 4. Design principles

**P2 Security**, **P8 Failure Isolation**, **P6 Externalised State**.

## 5. Patterns

- Token exchange at the edge; internal service-to-service uses short-lived signed tokens.
- Fail-open cache for identity provider (bounded TTL) to survive IdP outages within limits.
- 429 with `retry-after` before back-end saturation.

## 6. Anti-patterns

- Sticky sessions pinned to instance (breaks P6).
- Auth logic duplicated inside L2+ layers.
- Rate limits applied only after expensive work.

## 7. Failure modes

| Failure | Degraded mode |
|---------|---------------|
| IdP outage | Cached tokens honoured within TTL; new sessions refused |
| Session store outage | Session-less read-only fallback; writes refused |
| WAF outage | Fail closed on ingress |

## 8. Observability

Auth outcome, auth latency, rate-limit decisions, session load latency, request size, validation errors, edge-tier saturation.

## 9. Security

Enforces **TB-A**. Every request past L1 has a verified identity or a documented anonymous mode. Interacts with L13 (secrets, audit).

## 10. Production checklist

- [ ] TLS policy modern (TLS 1.3, HSTS, secure ciphers).
- [ ] WAF rules published and version-controlled.
- [ ] IdP outage runbook tested.
- [ ] Rate limits per tenant tuned and observable.
- [ ] Session store latency budget honoured.

## 11. References

- NIST SP 800-207 Zero Trust Architecture
- OWASP API Security Top 10
- W3C TraceContext
