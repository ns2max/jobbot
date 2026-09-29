<!-- Job posting: https://ca.linkedin.com/jobs/view/applied-scientist-alexa-smart-home-at-amazon-science-4456974123 -->

# 1145 Amazon — Senior Applied Scientist, Alexa Smart Home Science — Changelog (2026-09-03)

Pipeline: main-thread eval (57/100 Moderate Fit) → Fable draft → main-thread review + compile + trim + verify. Codex exhausted until Oct 3.

> **Medium priority.** The Senior Applied Scientist title, CAD 195,900-327,200 comp, and publication culture are real draws (and the eBay Applied Researcher 2 interview shows the archetype is reachable), but the domain core — **LLMs / agentic orchestration / personalization / preference learning** — is Nishal's weakest area and a pivot away from his edge/audio/signal strengths, and the role carries a senior-scientist leadership scope. The application is deliberately honest about this.

## CV — `cv/1145_main_amazon_science_applied_scientist_alexa_smart_home.tex`
- **Variant V2 (AI-Research).** Tagline `Research Scientist | Real-Time Multimodal ML, Benchmarks & Open Datasets` (byte-identical in cover). Only V2 foregrounds the full publications / datasets / peer-review / supervision record that carries this application.
- Section order per V2: Summary, Competencies, Stack, Education, Experience, Publications (retitled, Google Scholar bibliometric footnote), Datasets (full), Scientific Committee & Peer Review, Student Supervision, Highlights. **Talks section cut** (KG §15.8 — first to go when V2 overflows).
- Summary + Competencies re-led on: framing ill-defined problems and delivering end-to-end with limited guidance; frozen-protocol benchmark + ablation design; evaluation under distribution shift; adapting techniques to latency/cost/reliability budgets; **multimodal sensor + device/occupant heterogeneity** as the bridge to "real-world heterogeneity across homes, devices, occupants"; publications + review + supervision. Added literal "deep learning" for ATS.
- Stack ML line kept **honest**: TensorFlow/Keras, PyTorch, scikit-learn, numpy/scipy/pandas actual; JAX / HuggingFace / ONNX / LLM tooling demoted to "familiar with" (the JD does not name them). Java not claimed (no KG evidence) despite the JD listing it.
- **Grounding:** all numbers verified (14 ms / F1 0.76 / 74x / 31.4% CPU; F1 0.78; 95% SSIM grounded KG §13/§16; 300% / 99.5% / 50%); MAS one entry Jan 2015-Jul 2020; Promptly = geometry-alignment algorithm + RIP integration + mechanism consulting, **no patent**; Supervision uses exactly Collizoli (Aug 2023) + Battisti (Sep 2026) from KG §4.1a; English only; Claude Code named.
- **Cut for the 3-page V2 budget:** Talks section; Publications 13 → 8 (dropped the two Demo entries, FRUCT 2020, the MSc thesis, Melody & Motion, one I3DA); redundant "open datasets" highlight (already its own section); `\enlargethispage{4\baselineskip}` before Highlights.
- **Final: exactly 3 pages** (V2 budget). Page 1 ends with Education (MSc), page 2 B.Eng + Experience, page 3 Publications onward — no orphaned titles. ATS text layer clean (0 cid/replacement, email + phone literal, single-ASCII-hyphen dates). Covered: experimentation, evaluation, production, latency, deep learning, multimodal, sensor, publications, mentor, end-to-end. Honest gaps: personalization, large-scale distributed systems (Hadoop/Spark), LLM/agentic depth.

## Cover Letter — `cover_letters/1145_cover_amazon_science_applied_scientist_alexa_smart_home.tex`
- Plain `article`, 4 paragraphs, "Dear Hiring Manager,". **~1 page.**
- P1: turns ambiguous open-ended problems into production systems, evaluated rigorously — JAES 2026 (14 ms real-time inference, F1 0.76, 74x) from frozen-protocol benchmarks + ablations as much as the model; MAS shipped ML/CV at scale.
- P2: the role's asks in its own terms (frame + solve ill-defined problems with limited guidance; adapt techniques to latency/cost/reliability; rigorous experimentation to quantify impact; mentor; publish) each mapped to a concrete item; multimodal-sensor / device-heterogeneity angle for "why this team".
- **P3 honest about the domain:** LLMs and agentic orchestration are an area he would be growing into — strong ML fundamentals, a habit of learning applied fields cold (apparel manufacturing, financial forensics), AI-assisted workflows (Claude Code) in his own tooling. Then why this team (from `company_research/amazon-science.json`: research-grounded decisions, hands-on work, long-horizon bets; scientists own areas end-to-end and publish).
- P4: PR / no sponsorship / available immediately / open to relocating to Vancouver.

## Company research
- `company_research/amazon-science.json` (Alexa Smart Home Science, Vancouver; scientists own areas end-to-end + publish; comp CAD 195.9-327.2k + sign-on + RSU; eBay Applied Researcher 2 interview as reach calibration).

## Open flags for Nishal
- Domain: LLM / agentic / personalization — his weakest area; the role would under-use his edge/audio/signal strengths.
- Senior-scientist leadership scope (own the research agenda, raise the bar in hiring, influence roadmaps across teams).
- Vancouver relocation. Better-aligned fits exist in this batch — send this one if title/comp/company outweigh domain fit.
- No stated deadline.
