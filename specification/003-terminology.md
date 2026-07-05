# Specification 003 — Terminology

| Field | Value |
|-------|-------|
| Specification | EASRA-SPEC-003 |
| Title | Terminology |
| Version | 0.1.0 (Draft) |
| Status | Draft |
| Depends on | 001, 002 |

---

## 1. Purpose

This specification is the single source of truth for EASRA vocabulary. Every other EASRA document uses these terms with the meanings given here. When a term appears elsewhere without a definition, the definition in this document governs.

Terms are grouped by category. Each entry gives a short definition, an optional longer note, and (where useful) a *"not to be confused with"* clarification.

---

## 2. Core Architecture

**Enterprise AI System.** A production-grade software system that uses one or more AI models, together with retrieval, memory, tools, guardrails, verification, and observability, to serve enterprise workloads.

**Reference Architecture.** A description of a class of systems in terms of layers, components, interfaces, and cross-cutting concerns, independent of any specific implementation.

**Layer.** A logical grouping of components with a single, well-defined responsibility, a defined interface, and defined observability signals. EASRA has 16 layers (L0–L15).

**Component.** A named unit of function inside a layer. Components are named in this specification but their internal design is not.

**Interface.** The published contract at a layer boundary. Interfaces have inputs, outputs, error modes, and invariants (Spec 006).

**Trust Boundary.** A named point at which identity, integrity, or confidentiality changes hands and where explicit controls apply (Spec 009).

**Cross-cutting Concern.** A concern that spans multiple layers by design (security, observability, governance, cost).

**Extension Point.** A place in the architecture where new implementations may be added without changing surrounding layers (routers, registries, policy engines).

**Conformance.** A system is *EASRA-conformant* if it implements every layer, honours every interface contract, enforces every trust boundary, and emits every required observability signal, as defined in the version of EASRA it claims to conform to.

---

## 3. Request Path

**Channel.** A user-facing surface — web, mobile, chat, API, voice, embedded. Lives in L0.

**Session.** A logical conversation or task boundary owned by one identity. Managed by the Session Manager in L1.

**Request.** A single unit of work traversing the response path.

**Response.** The reply produced for a request, including verification verdict and observability metadata.

**Prompt.** The structured input assembled by L3 and passed to the Model layer (L6).

**Prompt Trace.** The observable record of how a prompt was built, including inputs from context, memory, retrieval, and system instructions.

**System Prompt.** The immutable instructions from the platform, distinct from user input, tool output, and retrieved content.

**User Prompt.** The user-authored portion of the input.

**Grounding Evidence.** The retrieved content (documents, records, tool outputs) supplied to the model as the basis for its response.

**Response Formatter.** The L9-adjacent component that shapes the verified response into the client contract (JSON, markdown, streaming SSE, etc.).

---

## 4. Reasoning & Agents

**Agent.** An autonomous component that plans, uses tools, and produces actions or responses.

**Single Agent.** One agent handling the full request end-to-end.

**Multi-Agent System.** A set of specialised agents coordinated by a Multi-Agent Coordinator.

**Multi-Agent Coordinator.** The component in L2 that dispatches tasks to sub-agents and merges their results.

**Planner.** The reasoning component that decomposes a request into a plan of steps.

**Workflow Engine.** The execution engine that runs the plan; may be deterministic or agentic.

**Skill.** A capability an agent can invoke — usually a tool or a sub-agent — registered in the Skill Registry.

**Agent Registry.** The catalogue of available agents, their skills, their invocation contracts, and their impact classes.

**Skill Registry.** The catalogue of available skills, their inputs, outputs, and preconditions.

**Agent Marketplace.** A future extension point that lets agents be shared across teams or organisations under governance controls.

---

## 5. Memory & Context

**Context.** The information used to build a prompt: session, user profile, memory, retrieval, tool output.

**Context Builder.** The L2/L3 component that assembles context before prompt building.

**Short-Term Memory.** Recent turns within an active session; typically bounded, fast, evicted on session end.

**Long-Term Memory.** Persistent memory across sessions, keyed by user or entity.

**Session Memory.** State specific to the current session (working notes, intermediate results).

**Semantic Memory.** Vectorised recall of prior conversations or facts, retrieved by similarity.

**User Profile.** Structured, durable, identity-bound preferences and attributes.

**Working Memory.** Ephemeral state within a single request, not persisted.

---

## 6. Knowledge & Retrieval

**Retrieval.** The act of fetching grounding evidence from the Knowledge layer (L5) given a query.

**Vector Database.** A store optimised for approximate nearest-neighbour search over embeddings.

**Embedding.** A dense vector representation of a text, image, or other artefact, produced by an embedding model.

**Chunk.** A retrieval-sized unit of source content.

**Index.** A queryable data structure over embeddings, keywords, or graph relations.

**Hybrid Search.** A retrieval strategy combining lexical (BM25), semantic (vector), and structured (SQL, graph) signals.

**Reranker.** A model that re-scores retrieval results for relevance to the query.

**RAG (Retrieval-Augmented Generation).** A pattern that supplies retrieved evidence to a generative model.

**Feature Store.** A future extension point for structured, versioned features used by AI decisioning.

---

## 7. Models & Routing

**Model.** A trained AI artefact accessed via an inference interface (chat, completion, embedding, rerank, classify, moderate).

**Foundation Model.** A large, general-purpose model exposed as an API or self-hosted.

**Small Model.** A lower-cost, lower-latency model used for classification, routing, or specialised tasks.

**Model Router.** The L6 component that selects a model per request based on capability, cost, latency, availability, and policy.

**Fallback Model.** The model used when the primary model is unavailable or fails guardrails.

**Model Provider.** A service that hosts a model (cloud service or self-hosted inference server).

**Cost-Aware Routing.** A future extension in which the router weighs token cost as a first-class routing input.

---

## 8. Tools & Actions

**Tool.** A callable function exposed to agents, described by an interface (name, arguments, output schema, impact class).

**Tool Router.** The L7 component that resolves a requested tool to a runnable implementation.

**MCP (Model Context Protocol).** An open protocol for connecting agents to tools and data sources; used by EASRA as the default tool interface.

**MCP Client.** The agent-side implementation of MCP.

**MCP Server.** The tool-side implementation of MCP.

**Tool Trace.** The observable record of tool invocations: arguments, result, latency, cost, verification.

**Impact Class.** The classification of a tool by consequence — `read`, `write`, `high-impact` — used by the human-in-the-loop policy.

**Action.** A tool invocation with real-world side effects (write, high-impact).

---

## 9. Caching & Performance

**Cache Plane.** The set of caches maintained by L11.

**Prompt Cache.** A cache of assembled prompts keyed by their inputs.

**Semantic Cache.** A cache keyed by embedding similarity to prior responses.

**Embedding Cache.** A cache of computed embeddings.

**Memory Cache.** A cache in front of the memory store for hot keys.

**Response Cache.** A cache of prior responses for identical requests.

**Streaming.** The transport pattern in which the response is emitted incrementally (SSE, WebSockets).

---

## 10. Guardrails, Safety & Verification

**Guardrail.** A control that inspects, filters, or blocks inputs, prompts, tool arguments, or outputs based on a policy. Lives in L8.

**Input Guardrail.** A guardrail applied to user input (prompt injection, PII, toxicity, jailbreak).

**Output Guardrail.** A guardrail applied to model output (PII leakage, toxicity, policy violations, format).

**Tool-Argument Guardrail.** A guardrail applied to tool arguments before invocation.

**Verification.** The L9 process that checks a candidate response against stated properties (grounding, citation, factuality, format, policy, safety).

**Evaluation.** The offline process that measures a model or a system against a benchmark dataset. Distinct from verification.

**Verdict.** The structured result of a verification check — pass, warn, fail, with evidence.

**Continuous Evaluation.** A production-time evaluation pattern that runs on sampled traffic.

**Grader.** A component (rule, small model, foundation model) that produces a verdict.

---

## 11. Observability & Operations

**Trace.** A causally ordered set of spans across layers for one request.

**Span.** A named, timed unit of work with attributes and events.

**Metric.** A numeric measurement (counter, gauge, histogram).

**Log.** A structured event record with a timestamp, severity, and context.

**Token Usage.** The count of prompt tokens, completion tokens, and cached tokens for a model call.

**Cost.** The monetary cost of a request, attributable to tokens, storage, and compute.

**Agent Trace.** The observable record of an agent's plan, decisions, and tool calls.

**Prompt Trace.** See §3.

**Tool Trace.** See §8.

**Alert.** A monitored condition that triggers notification or an automated response.

---

## 12. Security & Governance

**Zero Trust.** An architecture in which no request is trusted implicitly; every request is authenticated, authorised, and inspected.

**Authentication.** Verifying the identity of a principal.

**Authorisation.** Determining whether a principal may perform a requested action.

**Secret.** A credential, token, or key requiring confidentiality.

**PII (Personally Identifiable Information).** Data that identifies or could identify a natural person.

**Policy Engine.** The L14 component that evaluates policy rules against context and returns allow/deny/require-approval verdicts.

**Audit Log.** The tamper-evident record of security-relevant events.

**Compliance.** Alignment with regulatory or industry standards (GDPR, HIPAA, SOC 2, ISO/IEC 42001, EU AI Act, etc.).

**Responsible AI.** The set of practices ensuring fairness, accountability, transparency, safety, and privacy.

---

## 13. Delivery & Platform

**LLMOps.** The operations discipline for AI systems, covering prompt versioning, model rollout, evaluation, and monitoring.

**Canary Deployment.** Progressive rollout of a new version to a subset of traffic.

**Blue/Green Deployment.** Two environments (blue = current, green = candidate) with atomic switchover.

**Prompt Test.** A regression test asserting a property of a prompt's behaviour.

**Evaluation Test.** A test asserting model or system quality on a dataset.

**Artefact Registry.** The store for container images, models, prompts, and other build outputs.

**Feature Flag.** A runtime toggle for enabling or disabling a capability.

---

## 14. Infrastructure

**Compute.** The stateless runtime hosting agents, orchestrators, and model clients.

**Data Plane.** The set of stateful stores: sessions, memory, caches, vector DBs, feature store, event bus.

**Event Bus.** A future extension: the async messaging backbone for workflows (Kafka, Event Grid, PubSub).

**Autoscaling.** Automatic scaling of compute based on demand.

**Multi-Region.** A future extension: a deployment across multiple geographic regions for latency, sovereignty, or DR.

**Disaster Recovery (DR).** A future extension: the plan and mechanisms to restore service after a catastrophic failure.

---

## 15. Not to be confused

| Term | Not the same as |
|------|-----------------|
| Verification | Evaluation |
| Semantic Cache | Semantic Memory |
| Session Memory | Session |
| Tool | Skill (a skill is a *capability*, which may be a tool or a sub-agent) |
| Model Router | Multi-Agent Coordinator |
| Guardrail | Verification |
| PII redaction | PII classification |
| Autoscaling | Multi-region |

---

## 16. Change Log

- **0.1.0 (2026-07-05)** — Initial draft with ~90 terms across 14 categories.

## 17. Next Specification

Continue to [Specification 004 — Reference Architecture](./004-reference-architecture.md).
