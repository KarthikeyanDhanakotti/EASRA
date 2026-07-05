"""Build the EASRA LinkedIn carousel: cover, principles, layers, all key diagrams, CTA.

Idempotent. Re-run to regenerate `conference/EASRA-LinkedIn-Carousel.pptx`;
export to PDF via PowerPoint COM (see companion PowerShell one-liner).
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

from build_high_level_deck import (  # noqa: E402  reused primitives
    PALETTE,
    hex_to_rgb,
    add_box,
    add_text,
    build_hero,
    build_architecture,
    build_layer_index,
)


# ---------- helpers ---------- #

def slide_bg(prs: Presentation, color: str = "#FFFFFF"):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    W, H = prs.slide_width, prs.slide_height
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H)
    bg.fill.solid()
    bg.fill.fore_color.rgb = hex_to_rgb(color)
    bg.line.fill.background()
    return slide, W, H


def title_bar(slide, W, subtitle_right: str | None = None,
              text: str = "EASRA  ·  Enterprise AI Systems Reference Architecture",
              height: float = 0.65):
    h = Inches(height)
    tb = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, h)
    tb.fill.solid()
    tb.fill.fore_color.rgb = hex_to_rgb(PALETTE["titlebar"][0])
    tb.line.fill.background()
    add_text(
        slide, Inches(0.35), Inches(0.05), W - Inches(0.7), h - Inches(0.1),
        text, size=18, bold=True, color="#FFFFFF", align=PP_ALIGN.LEFT,
    )
    if subtitle_right:
        add_text(
            slide, Inches(0.35), Inches(0.05), W - Inches(0.7), h - Inches(0.1),
            subtitle_right, size=11, color="#B8CDEA", align=PP_ALIGN.RIGHT,
        )
    return h


def slide_footer(slide, W, H, text: str | None = None):
    footer = (
        text
        or "github.com/KarthikeyanDhanakotti/EASRA  ·  v0.1.0  ·  "
           "CC-BY-4.0 (docs) + Apache-2.0 (code)  ·  Karthikeyan Dhanakotti"
    )
    add_text(
        slide, Inches(0.35), H - Inches(0.32), W - Inches(0.7), Inches(0.28),
        footer, size=9, color="#8A94A0", align=PP_ALIGN.LEFT,
    )


def arrow_between(slide, x1, y1, x2, y2, color="#5A6470", weight=1.75):
    line = slide.shapes.add_connector(
        MSO_CONNECTOR.STRAIGHT, int(x1), int(y1), int(x2), int(y2)
    )
    line.line.color.rgb = hex_to_rgb(color)
    line.line.width = Pt(weight)
    return line


# ---------- individual slide builders ---------- #

def build_problem(prs: Presentation):
    slide, W, H = slide_bg(prs)
    title_bar(slide, W, subtitle_right="Why EASRA?")

    add_text(
        slide, Inches(0.6), Inches(1.0), W - Inches(1.2), Inches(1.0),
        "Enterprise AI stacks are one-offs.",
        size=40, bold=True, color="#0B1F3A", align=PP_ALIGN.LEFT,
    )
    add_text(
        slide, Inches(0.6), Inches(2.0), W - Inches(1.2), Inches(0.8),
        "Every team is redesigning the same architecture — badly, in isolation, "
        "with different vocabulary.",
        size=18, italic=True, color="#5A6470", align=PP_ALIGN.LEFT,
    )

    problems = [
        ("No shared vocabulary",
         "Teams argue about ‘agent’ vs ‘workflow’ vs ‘orchestrator’ before writing a line of code."),
        ("Security bolted on",
         "Prompt injection, tool safety and PII treated as add-ons, not architectural concerns."),
        ("Verification confused with evaluation",
         "Offline metrics ship to prod. No first-class verification of grounding, citation, factuality."),
        ("Cost & observability afterthoughts",
         "Token spend, latency SLOs and tool traces retrofitted after the outage."),
    ]

    col_w = (W - Inches(1.4)) / 2
    row_h = Inches(1.5)
    gap_x = Inches(0.2)
    gap_y = Inches(0.2)
    start_y = Inches(3.2)
    for i, (t, d) in enumerate(problems):
        col = i % 2
        row = i // 2
        x = Inches(0.6) + (col_w + gap_x) * col
        y = start_y + (row_h + gap_y) * row
        add_box(
            slide, x, y, col_w, row_h,
            PALETTE["security"][0], PALETTE["security"][1], d,
            title=t, title_size=14, font_size=11,
            title_color=PALETTE["security"][2],
            text_color="#4A2C29", align_left=True,
        )

    slide_footer(slide, W, H)


def build_what_is(prs: Presentation):
    slide, W, H = slide_bg(prs)
    title_bar(slide, W, subtitle_right="What is EASRA?")

    add_text(
        slide, Inches(0.6), Inches(1.0), W - Inches(1.2), Inches(1.0),
        "An open architecture standard for Enterprise AI.",
        size=36, bold=True, color="#0B1F3A", align=PP_ALIGN.LEFT,
    )
    add_text(
        slide, Inches(0.6), Inches(2.0), W - Inches(1.2), Inches(0.5),
        "Vendor-neutral. Production-grade. Standards-aligned.",
        size=16, italic=True, color="#3B7DDD", align=PP_ALIGN.LEFT,
    )

    quads = [
        ("Vendor-neutral",
         "Every layer maps cleanly to Azure, AWS, GCP and open-source. No lock-in.",
         "entry"),
        ("Security by design",
         "Zero trust, four trust boundaries, prompt-injection resistance in the layers, not on top.",
         "security"),
        ("Verification-first",
         "Grounding, citation, factuality, policy and safety verification separated from evaluation.",
         "obs"),
        ("Cost + observability by default",
         "Tokens, latency, cost, prompts, tools traced through OpenTelemetry from every component.",
         "data"),
    ]
    col_w = (W - Inches(1.4)) / 2
    row_h = Inches(1.55)
    start_y = Inches(2.85)
    for i, (t, d, kind) in enumerate(quads):
        col = i % 2
        row = i // 2
        x = Inches(0.6) + (col_w + Inches(0.2)) * col
        y = start_y + (row_h + Inches(0.2)) * row
        fill, border, tcol = PALETTE[kind]
        add_box(
            slide, x, y, col_w, row_h,
            fill, border, d,
            title=t, title_size=14, font_size=11,
            title_color=tcol, text_color=tcol, align_left=True,
        )

    slide_footer(slide, W, H)


def build_principles(prs: Presentation):
    slide, W, H = slide_bg(prs)
    title_bar(slide, W, subtitle_right="Ten design principles")

    principles = [
        ("P1", "Vendor Neutrality",
         "Logical layers; each maps to ≥ 2 independent implementations."),
        ("P2", "Security by Design",
         "Zero-trust, least-privilege, prompt-injection resistance are architectural."),
        ("P3", "Verification by Design",
         "Every AI output is verifiable; verification ≠ evaluation."),
        ("P4", "Observability by Default",
         "Traces, metrics, logs, token/cost accounting emitted from every component."),
        ("P5", "Loose Coupling",
         "Layers communicate only through published interfaces."),
        ("P6", "Externalized State",
         "Memory, sessions, caches live outside compute; compute is stateless."),
        ("P7", "Human-in-the-Loop",
         "Every autonomous action has escalation, override and audit paths."),
        ("P8", "Failure Isolation",
         "Layer failure degrades gracefully; no single layer cascades a full outage."),
        ("P9", "Cost Awareness",
         "Token, compute, storage cost are explicit design inputs."),
        ("P10", "Evolvability",
         "New models, tools, agents, channels added without redesigning the architecture."),
    ]

    cols = 2
    rows = 5
    top = Inches(0.95)
    left = Inches(0.35)
    col_gap = Inches(0.2)
    row_gap = Inches(0.08)
    total_w = W - Inches(0.7)
    col_w = (total_w - col_gap) / cols
    total_h = H - top - Inches(0.5)
    row_h = (total_h - row_gap * (rows - 1)) / rows

    for i, (code, name, desc) in enumerate(principles):
        col = i // rows
        row = i % rows
        x = left + (col_w + col_gap) * col
        y = top + (row_h + row_gap) * row
        fill, border, tcol = PALETTE["neutral"]

        chip_w = Inches(0.65)
        chip = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, chip_w, row_h)
        chip.fill.solid()
        chip.fill.fore_color.rgb = hex_to_rgb("#3B7DDD")
        chip.line.color.rgb = hex_to_rgb("#3B7DDD")
        chip.line.width = Pt(0.5)
        ctf = chip.text_frame
        ctf.vertical_anchor = MSO_ANCHOR.MIDDLE
        cp = ctf.paragraphs[0]
        cp.alignment = PP_ALIGN.CENTER
        cr = cp.add_run()
        cr.text = code
        cr.font.size = Pt(14)
        cr.font.bold = True
        cr.font.color.rgb = hex_to_rgb("#FFFFFF")
        cr.font.name = "Segoe UI"

        body_left = x + chip_w + Inches(0.06)
        body_w = col_w - chip_w - Inches(0.06)
        add_box(
            slide, body_left, y, body_w, row_h,
            fill, border, desc,
            title=name, title_size=13, font_size=11,
            title_color=tcol, text_color=tcol, align_left=True,
        )

    slide_footer(slide, W, H)


def build_trust_boundaries(prs: Presentation):
    slide, W, H = slide_bg(prs)
    title_bar(slide, W, subtitle_right="Four trust boundaries")

    add_text(
        slide, Inches(0.35), Inches(0.85), W - Inches(0.7), Inches(0.45),
        "Every request crosses four boundaries. Each has its own attackers, controls, and failure modes.",
        size=13, italic=True, color="#5A6470", align=PP_ALIGN.LEFT,
    )

    # Request path row
    path_y = Inches(1.6)
    path_h = Inches(0.7)
    boxes = [
        ("User", "#EAF3FF", "#3B7DDD", "#0B3D91"),
        ("L0 Channel", "#EAF3FF", "#3B7DDD", "#0B3D91"),
        ("L1 Gateway", "#EAF3FF", "#3B7DDD", "#0B3D91"),
        ("L2 Orch.", "#ECF0F1", "#2C3E50", "#1B2A3A"),
        ("L3 Prompt", "#ECF0F1", "#2C3E50", "#1B2A3A"),
        ("L6 Model Router", "#F5EAF7", "#8E44AD", "#4A1E5C"),
        ("L7 Tool Router", "#E8F8F5", "#16A085", "#0B5C4B"),
        ("L8 Guard", "#FDECEA", "#C0392B", "#6B1A11"),
        ("L9 Verify", "#FDECEA", "#C0392B", "#6B1A11"),
    ]
    total_w = W - Inches(0.7)
    n = len(boxes)
    gap = Inches(0.08)
    box_w = (total_w - gap * (n - 1)) / n
    for i, (label, fill, border, tcol) in enumerate(boxes):
        x = Inches(0.35) + (box_w + gap) * i
        add_box(
            slide, x, path_y, box_w, path_h, fill, border, label,
            font_size=10, text_color=tcol, title_size=10, bold_title=True,
        )

    # Trust boundary bands under the request path
    tbs = [
        ("TB-A · Edge Boundary",
         "untrusted → trusted", "#FDECEA", "#C0392B", "#6B1A11",
         "AuthN / AuthZ · WAF · rate limit · request validation · session"),
        ("TB-C · Model Boundary",
         "internal → provider", "#F5EAF7", "#8E44AD", "#4A1E5C",
         "Model registry · egress policy · prompt-inject defence · content filters · cost cap"),
        ("TB-D · Action Boundary",
         "reasoning → real world", "#E8F8F5", "#16A085", "#0B5C4B",
         "Tool registry · impact class · argument guardrails · HITL approval · audit"),
        ("TB-B · Response Boundary",
         "internal → observable", "#FDECEA", "#C0392B", "#6B1A11",
         "Output guardrails · verification verdict · PII redaction · citation · schema"),
    ]

    band_top = Inches(2.6)
    band_gap = Inches(0.15)
    band_h = (H - band_top - Inches(0.6) - band_gap * (len(tbs) - 1)) / len(tbs)

    for i, (code, direction, fill, border, tcol, controls) in enumerate(tbs):
        y = band_top + (band_h + band_gap) * i
        # code chip
        chip_w = Inches(2.7)
        add_box(
            slide, Inches(0.35), y, chip_w, band_h,
            border, border, direction,
            title=code, title_size=13, font_size=10,
            title_color="#FFFFFF", text_color="#FFECEB", align_left=True,
        )
        # controls box
        body_left = Inches(0.35) + chip_w + Inches(0.1)
        body_w = W - body_left - Inches(0.35)
        add_box(
            slide, body_left, y, body_w, band_h,
            fill, border, controls,
            title="Controls at this boundary",
            title_size=11, font_size=11,
            title_color=tcol, text_color=tcol, align_left=True,
        )

    slide_footer(slide, W, H)


def build_runtime_flow(prs: Presentation):
    slide, W, H = slide_bg(prs)
    title_bar(slide, W, subtitle_right="Runtime execution flow (D-R1)")

    add_text(
        slide, Inches(0.35), Inches(0.85), W - Inches(0.7), Inches(0.45),
        "One request through the seven decision points: identity, cache, retrieval, guardrails, model, tool, verification.",
        size=12, italic=True, color="#5A6470", align=PP_ALIGN.LEFT,
    )

    stages = [
        ("1", "Ingress",
         "L0 / L1: AuthN → AuthZ → rate limit → request validation → session",
         "entry"),
        ("2", "Cache lookup",
         "L11: prompt / semantic / response cache — return if hit",
         "cache"),
        ("3", "Context assembly",
         "L2 → L3: agent selection · context builder · memory + retrieval",
         "neutral"),
        ("4", "Retrieval",
         "L4 + L5: memory + hybrid retrieval (vector · BM25 · SQL · graph) → rerank",
         "data"),
        ("5", "Prompt + input guardrails",
         "L3 → L8: prompt builder → input / prompt guardrails",
         "security"),
        ("6", "Model routing",
         "L6: capability · cost · latency · policy → foundation or specialised model",
         "model"),
        ("7", "Tool execution",
         "L7 + L8: tool router → impact-class enforcer → MCP / enterprise API",
         "data"),
        ("8", "Output guardrails + verification",
         "L8 → L9: output guardrails → grounding · citation · factuality · policy · safety",
         "security"),
        ("9", "Format + stream + response",
         "L9 → L1 → L0: response formatter → streaming engine → user",
         "obs"),
    ]

    top = Inches(1.35)
    n = len(stages)
    row_gap = Inches(0.06)
    row_h = (H - top - Inches(0.5) - row_gap * (n - 1)) / n

    for i, (num, name, body, kind) in enumerate(stages):
        y = top + (row_h + row_gap) * i
        fill, border, tcol = PALETTE[kind]
        # circle number
        cw = Inches(0.55)
        circle = slide.shapes.add_shape(
            MSO_SHAPE.OVAL, Inches(0.35), y + (row_h - cw) / 2, cw, cw,
        )
        circle.fill.solid()
        circle.fill.fore_color.rgb = hex_to_rgb(border)
        circle.line.color.rgb = hex_to_rgb(border)
        ctf = circle.text_frame
        ctf.vertical_anchor = MSO_ANCHOR.MIDDLE
        cp = ctf.paragraphs[0]
        cp.alignment = PP_ALIGN.CENTER
        cr = cp.add_run()
        cr.text = num
        cr.font.size = Pt(14)
        cr.font.bold = True
        cr.font.color.rgb = hex_to_rgb("#FFFFFF")
        cr.font.name = "Segoe UI"

        body_left = Inches(0.35) + cw + Inches(0.15)
        body_w = W - body_left - Inches(0.35)
        add_box(
            slide, body_left, y, body_w, row_h,
            fill, border, body,
            title=name, title_size=12, font_size=10.5,
            title_color=tcol, text_color=tcol, align_left=True,
        )

    slide_footer(slide, W, H)


def build_llmops(prs: Presentation):
    slide, W, H = slide_bg(prs)
    title_bar(slide, W, subtitle_right="L12 · LLMOps & Delivery")

    add_text(
        slide, Inches(0.35), Inches(0.85), W - Inches(0.7), Inches(0.45),
        "Traditional CI/CD is not enough. LLMOps adds prompt tests, eval gates, model registry, canary + shadow, cost guardrails.",
        size=12, italic=True, color="#5A6470", align=PP_ALIGN.LEFT,
    )

    # top row: 5 stages pipeline
    stages = [
        ("Git / Repo",
         "Prompts · agents · tools · IaC · eval sets\nversioned as code",
         "neutral"),
        ("CI",
         "Lint · sec-scan · unit · prompt tests\nsafety tests · eval gate",
         "obs"),
        ("Artefact Registry",
         "Signed containers · pinned models\nprompt versions · SBOM",
         "data"),
        ("CD",
         "Blue / Green · Canary · Shadow\nRollback · progressive delivery",
         "model"),
        ("Runtime",
         "Continuous eval · drift · cost cap\nincident + rollback triggers",
         "security"),
    ]
    top = Inches(1.4)
    row_h = Inches(1.4)
    n = len(stages)
    gap = Inches(0.15)
    total_w = W - Inches(0.7)
    box_w = (total_w - gap * (n - 1)) / n
    for i, (title, body, kind) in enumerate(stages):
        x = Inches(0.35) + (box_w + gap) * i
        fill, border, tcol = PALETTE[kind]
        add_box(
            slide, x, top, box_w, row_h,
            fill, border, body,
            title=title, title_size=13, font_size=10,
            title_color=tcol, text_color=tcol, align_left=True,
        )

    # arrows between them
    ay = top + row_h / 2
    for i in range(n - 1):
        x1 = Inches(0.35) + (box_w + gap) * i + box_w
        x2 = x1 + gap
        arrow_between(slide, x1, ay, x2, ay)

    # second half: three side-by-side registries + evaluation
    reg_top = top + row_h + Inches(0.5)
    reg_h = Inches(2.6)
    reg_w = (W - Inches(0.7) - gap * 2) / 3
    regs = [
        ("Prompt lifecycle",
         "Draft → Test → Approved → Prod → Deprecated",
         [
             "Versioned prompt templates",
             "Prompt tests + regression suite",
             "Prompt registry as source of truth",
             "Prompt rollback independent of model",
         ],
         "neutral"),
        ("Model lifecycle",
         "Candidate → Shadow → Canary → Prod → Retired",
         [
             "Model registry (foundation + fine-tuned)",
             "Approved providers only (TB-C)",
             "Cost + latency + safety benchmarks",
             "Shadow traffic for regression",
         ],
         "model"),
        ("Tool lifecycle",
         "Onboarded → Restricted → GA → Deprecated",
         [
             "Tool registry with impact class",
             "Argument guardrails per tool",
             "HITL approval for high-impact",
             "Audit + rate limit per tool",
         ],
         "data"),
    ]
    for i, (title, sub, items, kind) in enumerate(regs):
        x = Inches(0.35) + (reg_w + gap) * i
        fill, border, tcol = PALETTE[kind]
        shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, reg_top, reg_w, reg_h)
        shp.fill.solid()
        shp.fill.fore_color.rgb = hex_to_rgb(fill)
        shp.line.color.rgb = hex_to_rgb(border)
        shp.line.width = Pt(1.25)
        tf = shp.text_frame
        tf.margin_left = Inches(0.15)
        tf.margin_right = Inches(0.12)
        tf.margin_top = Inches(0.12)
        tf.margin_bottom = Inches(0.12)
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        r = p.add_run()
        r.text = title
        r.font.size = Pt(14)
        r.font.bold = True
        r.font.name = "Segoe UI"
        r.font.color.rgb = hex_to_rgb(tcol)

        p2 = tf.add_paragraph()
        p2.alignment = PP_ALIGN.LEFT
        r2 = p2.add_run()
        r2.text = sub
        r2.font.size = Pt(10)
        r2.font.italic = True
        r2.font.name = "Segoe UI"
        r2.font.color.rgb = hex_to_rgb(tcol)

        for item in items:
            pi = tf.add_paragraph()
            pi.alignment = PP_ALIGN.LEFT
            pi.level = 0
            ri = pi.add_run()
            ri.text = "•  " + item
            ri.font.size = Pt(11)
            ri.font.name = "Segoe UI"
            ri.font.color.rgb = hex_to_rgb(tcol)

    slide_footer(slide, W, H)


def build_cloud_mapping(prs: Presentation):
    slide, W, H = slide_bg(prs)
    title_bar(slide, W, subtitle_right="Cloud implementations")

    add_text(
        slide, Inches(0.35), Inches(0.85), W - Inches(0.7), Inches(0.45),
        "Same 16 layers. Four independent mappings. Vendor-neutral by construction.",
        size=12, italic=True, color="#5A6470", align=PP_ALIGN.LEFT,
    )

    clouds = [
        ("Microsoft Azure", "entry", [
            ("L1 Gateway", "APIM · Front Door · Entra ID"),
            ("L2 Orch.",   "Container Apps · Durable Fn"),
            ("L5 Retrieval", "AI Search · Cosmos Gremlin · Fabric"),
            ("L6 Models", "Azure OpenAI · AI Foundry"),
            ("L7 Tools", "APIM · Logic Apps · MCP on ACA"),
            ("L10 Obs.", "App Insights · Azure Monitor"),
            ("L13 Sec.", "Entra · Key Vault · Purview · Defender"),
            ("L14 GRC", "Purview · Azure Policy · Foundry gov."),
        ]),
        ("Amazon AWS", "data", [
            ("L1 Gateway", "CloudFront · WAF · API Gateway · Cognito"),
            ("L2 Orch.",   "ECS / Fargate · Step Functions"),
            ("L5 Retrieval", "OpenSearch · Neptune · Athena"),
            ("L6 Models", "Bedrock · SageMaker"),
            ("L7 Tools", "API Gateway · Lambda · MCP on ECS"),
            ("L10 Obs.", "CloudWatch · X-Ray · OTel Collector"),
            ("L13 Sec.", "IAM · KMS · Secrets Manager · Macie"),
            ("L14 GRC", "Config · Audit Manager · Bedrock Guardrails"),
        ]),
        ("Google Cloud", "model", [
            ("L1 Gateway", "Cloud LB · Cloud Armor · API Gateway · IAP"),
            ("L2 Orch.",   "Cloud Run · Workflows"),
            ("L5 Retrieval", "Vertex AI Search · Spanner Graph"),
            ("L6 Models", "Vertex AI · Gemini · Model Garden"),
            ("L7 Tools", "API Gateway · Cloud Functions · MCP on Run"),
            ("L10 Obs.", "Cloud Ops Suite · OTel Collector"),
            ("L13 Sec.", "IAM · KMS · Secret Manager · SCC"),
            ("L14 GRC", "Assured Workloads · Vertex Model Registry"),
        ]),
        ("Open Source / K8s", "neutral", [
            ("L1 Gateway", "Envoy · Kong · Keycloak · OIDC"),
            ("L2 Orch.",   "K8s + Argo Workflows · LangGraph"),
            ("L5 Retrieval", "Qdrant · Weaviate · pgvector · Neo4j"),
            ("L6 Models", "vLLM · Ollama · TGI · TorchServe"),
            ("L7 Tools", "MCP servers · custom adapters"),
            ("L10 Obs.", "OTel · Prometheus · Grafana · Tempo · Loki"),
            ("L13 Sec.", "SPIFFE · Vault · Falco · Kyverno"),
            ("L14 GRC", "OPA / Gatekeeper · Kyverno · Sigstore"),
        ]),
    ]

    top = Inches(1.4)
    row_h = Inches(5.6)
    n = len(clouds)
    gap = Inches(0.14)
    total_w = W - Inches(0.7)
    box_w = (total_w - gap * (n - 1)) / n

    for i, (cloud_name, kind, items) in enumerate(clouds):
        x = Inches(0.35) + (box_w + gap) * i
        fill, border, tcol = PALETTE[kind]
        shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, top, box_w, row_h)
        shp.fill.solid()
        shp.fill.fore_color.rgb = hex_to_rgb(fill)
        shp.line.color.rgb = hex_to_rgb(border)
        shp.line.width = Pt(1.25)
        tf = shp.text_frame
        tf.margin_left = Inches(0.14)
        tf.margin_right = Inches(0.12)
        tf.margin_top = Inches(0.14)
        tf.margin_bottom = Inches(0.12)
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        r = p.add_run()
        r.text = cloud_name
        r.font.size = Pt(15)
        r.font.bold = True
        r.font.name = "Segoe UI"
        r.font.color.rgb = hex_to_rgb(tcol)

        for lname, svc in items:
            pl = tf.add_paragraph()
            pl.alignment = PP_ALIGN.LEFT
            rl = pl.add_run()
            rl.text = lname
            rl.font.size = Pt(10.5)
            rl.font.bold = True
            rl.font.name = "Segoe UI"
            rl.font.color.rgb = hex_to_rgb(tcol)

            pv = tf.add_paragraph()
            pv.alignment = PP_ALIGN.LEFT
            rv = pv.add_run()
            rv.text = svc
            rv.font.size = Pt(9.5)
            rv.font.name = "Segoe UI"
            rv.font.color.rgb = hex_to_rgb(tcol)

    slide_footer(slide, W, H)


def build_standards(prs: Presentation):
    slide, W, H = slide_bg(prs)
    title_bar(slide, W, subtitle_right="Standards & frameworks")

    add_text(
        slide, Inches(0.35), Inches(0.85), W - Inches(0.7), Inches(0.45),
        "EASRA maps explicitly to the frameworks your compliance, security and risk teams already recognise.",
        size=12, italic=True, color="#5A6470", align=PP_ALIGN.LEFT,
    )

    standards = [
        ("NIST AI RMF",  "Govern · Map · Measure · Manage",
         "L14 Governance · L10 Observability", "neutral"),
        ("ISO / IEC 42001", "AI management system",
         "L14 · L12 LLMOps · L15 Value", "neutral"),
        ("EU AI Act",   "Risk categorisation + provider duties",
         "L14 · L9 Verification · L13 Security", "security"),
        ("OWASP LLM Top 10", "LLM-specific application risks",
         "L1 · L6 · L7 · L8 · L9 · L11", "security"),
        ("MITRE ATLAS", "Adversary tactics + techniques for AI",
         "L1 · L8 Guardrails · L13 · L14", "security"),
        ("OpenTelemetry", "Traces / metrics / logs schema",
         "L10 Observability across every layer", "obs"),
        ("Model Context Protocol (MCP)",
         "Standardised tool interface",
         "L7 Tooling & Actions", "data"),
        ("TOGAF",       "Enterprise architecture context",
         "Positions EASRA as an AI-domain reference architecture", "neutral"),
    ]

    cols = 2
    rows = 4
    top = Inches(1.4)
    left = Inches(0.35)
    col_gap = Inches(0.2)
    row_gap = Inches(0.15)
    total_w = W - Inches(0.7)
    col_w = (total_w - col_gap) / cols
    total_h = H - top - Inches(0.5)
    row_h = (total_h - row_gap * (rows - 1)) / rows

    for i, (name, what, mapped, kind) in enumerate(standards):
        col = i // rows
        row = i % rows
        x = left + (col_w + col_gap) * col
        y = top + (row_h + row_gap) * row
        fill, border, tcol = PALETTE[kind]
        shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, col_w, row_h)
        shp.fill.solid()
        shp.fill.fore_color.rgb = hex_to_rgb(fill)
        shp.line.color.rgb = hex_to_rgb(border)
        shp.line.width = Pt(1.25)
        tf = shp.text_frame
        tf.margin_left = Inches(0.14)
        tf.margin_right = Inches(0.12)
        tf.margin_top = Inches(0.10)
        tf.margin_bottom = Inches(0.10)
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        r = p.add_run()
        r.text = name
        r.font.size = Pt(14)
        r.font.bold = True
        r.font.name = "Segoe UI"
        r.font.color.rgb = hex_to_rgb(tcol)

        p2 = tf.add_paragraph()
        p2.alignment = PP_ALIGN.LEFT
        r2 = p2.add_run()
        r2.text = what
        r2.font.size = Pt(10.5)
        r2.font.italic = True
        r2.font.name = "Segoe UI"
        r2.font.color.rgb = hex_to_rgb(tcol)

        p3 = tf.add_paragraph()
        p3.alignment = PP_ALIGN.LEFT
        r3 = p3.add_run()
        r3.text = "Mapped in EASRA at:  " + mapped
        r3.font.size = Pt(10)
        r3.font.name = "Segoe UI"
        r3.font.color.rgb = hex_to_rgb(tcol)

    slide_footer(slide, W, H)


def build_deliverables(prs: Presentation):
    slide, W, H = slide_bg(prs)
    title_bar(slide, W, subtitle_right="Ten deliverables of the standard")

    items = [
        ("1", "Architecture Specification",  "Twelve numbered specs (001–012). The frozen source of truth."),
        ("2", "Handbook",                    "Per-layer chapters and cross-cutting guides."),
        ("3", "Reference Architectures",     "Five views: logical · runtime · deployment · operational · security."),
        ("4", "Cloud Implementations",       "Azure · AWS · GCP · open-source (K8s + CNCF)."),
        ("5", "Benchmarks",                  "Latency · throughput · cost · safety · verification · reliability."),
        ("6", "Architecture Decision Records","Every consequential decision recorded and versioned."),
        ("7", "Security Reference",          "Threats · controls · standards mapping · threat models · red team."),
        ("8", "Verification Reference",      "Classes · checkers · metrics · golden-set methodology."),
        ("9", "LLMOps Guide",                "Delivery · lifecycles · evaluation · cost · incident response."),
        ("10", "Conference Materials",       "Slides · workshops · talks — this deck is one of them."),
    ]

    cols = 2
    rows = 5
    top = Inches(0.95)
    left = Inches(0.35)
    col_gap = Inches(0.2)
    row_gap = Inches(0.1)
    total_w = W - Inches(0.7)
    col_w = (total_w - col_gap) / cols
    total_h = H - top - Inches(0.5)
    row_h = (total_h - row_gap * (rows - 1)) / rows

    for i, (num, name, desc) in enumerate(items):
        col = i // rows
        row = i % rows
        x = left + (col_w + col_gap) * col
        y = top + (row_h + row_gap) * row
        fill, border, tcol = PALETTE["neutral"]

        chip_w = Inches(0.65)
        chip = slide.shapes.add_shape(MSO_SHAPE.OVAL, x, y + (row_h - chip_w) / 2, chip_w, chip_w)
        chip.fill.solid()
        chip.fill.fore_color.rgb = hex_to_rgb("#3B7DDD")
        chip.line.color.rgb = hex_to_rgb("#3B7DDD")
        ctf = chip.text_frame
        ctf.vertical_anchor = MSO_ANCHOR.MIDDLE
        cp = ctf.paragraphs[0]
        cp.alignment = PP_ALIGN.CENTER
        cr = cp.add_run()
        cr.text = num
        cr.font.size = Pt(14)
        cr.font.bold = True
        cr.font.color.rgb = hex_to_rgb("#FFFFFF")
        cr.font.name = "Segoe UI"

        body_left = x + chip_w + Inches(0.15)
        body_w = col_w - chip_w - Inches(0.15)
        add_box(
            slide, body_left, y, body_w, row_h,
            fill, border, desc,
            title=name, title_size=13, font_size=11,
            title_color=tcol, text_color=tcol, align_left=True,
        )

    slide_footer(slide, W, H)


def build_cta(prs: Presentation):
    slide, W, H = slide_bg(prs, color=PALETTE["hero_bg"][0])

    bar = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, Inches(6.55), W, Inches(0.15)
    )
    bar.fill.solid()
    bar.fill.fore_color.rgb = hex_to_rgb(PALETTE["hero_acc"][0])
    bar.line.fill.background()

    add_text(
        slide, Inches(0.9), Inches(0.9), W - Inches(1.8), Inches(0.5),
        "ADOPT · CONTRIBUTE · FORK",
        size=14, bold=True, color="#3B7DDD", align=PP_ALIGN.LEFT,
    )
    add_text(
        slide, Inches(0.9), Inches(1.35), W - Inches(1.8), Inches(1.4),
        "EASRA is an open architecture standard.",
        size=42, bold=True, color="#FFFFFF", align=PP_ALIGN.LEFT,
    )
    add_text(
        slide, Inches(0.9), Inches(2.55), W - Inches(1.8), Inches(0.7),
        "Vendor-neutral. Standards-aligned. Verifiable. Yours to fork.",
        size=18, italic=True, color="#B8CDEA", align=PP_ALIGN.LEFT,
    )

    ctas = [
        ("★ Star",       "github.com/KarthikeyanDhanakotti/EASRA",         "entry"),
        ("Fork & Adopt", "templates/repository-template/",                 "data"),
        ("Contribute",   "CONTRIBUTING.md  ·  GOVERNANCE.md",              "obs"),
        ("Follow",       "linkedin.com/in/karthikeyan-dhanakotti",         "model"),
    ]
    x = Inches(0.9)
    y = Inches(4.0)
    bw = Inches(2.75)
    bh = Inches(1.4)
    gap = Inches(0.2)
    for label, url, kind in ctas:
        fill, border, _ = PALETTE[kind]
        shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, bw, bh)
        shp.fill.solid()
        shp.fill.fore_color.rgb = hex_to_rgb("#12335F")
        shp.line.color.rgb = hex_to_rgb(border)
        shp.line.width = Pt(1.5)
        tf = shp.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = Inches(0.15)
        tf.margin_right = Inches(0.15)
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.alignment = PP_ALIGN.LEFT
        r1 = p1.add_run()
        r1.text = label
        r1.font.size = Pt(18)
        r1.font.bold = True
        r1.font.color.rgb = hex_to_rgb("#FFFFFF")
        r1.font.name = "Segoe UI"
        p2 = tf.add_paragraph()
        p2.alignment = PP_ALIGN.LEFT
        r2 = p2.add_run()
        r2.text = url
        r2.font.size = Pt(10)
        r2.font.color.rgb = hex_to_rgb("#8FA9CE")
        r2.font.name = "Segoe UI"
        x += bw + gap

    add_text(
        slide, Inches(0.9), Inches(6.85), W - Inches(1.8), Inches(0.35),
        "Karthikeyan Dhanakotti  ·  Enterprise AI Architect  ·  Independent open-source work",
        size=11, color="#8FA9CE", align=PP_ALIGN.LEFT,
    )


# ---------- main ---------- #

def main():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    build_hero(prs)                # 1  Hero
    build_problem(prs)             # 2  Problem
    build_what_is(prs)             # 3  What is EASRA?
    build_principles(prs)          # 4  Design principles
    build_layer_index(prs)         # 5  The 16 layers
    build_architecture(prs)        # 6  High-level architecture
    build_trust_boundaries(prs)    # 7  Trust boundaries
    build_runtime_flow(prs)        # 8  Runtime execution flow
    build_llmops(prs)              # 9  LLMOps & delivery
    build_cloud_mapping(prs)       # 10 Cloud implementations
    build_standards(prs)           # 11 Standards mapping
    build_deliverables(prs)        # 12 Ten deliverables
    build_cta(prs)                 # 13 CTA

    out = Path(__file__).parent / "EASRA-LinkedIn-Carousel.pptx"
    prs.save(out)
    print(f"Wrote {out}  ({out.stat().st_size / 1024:.1f} KB, {len(prs.slides.__iter__.__self__._sldIdLst)} slides)")


if __name__ == "__main__":
    main()
