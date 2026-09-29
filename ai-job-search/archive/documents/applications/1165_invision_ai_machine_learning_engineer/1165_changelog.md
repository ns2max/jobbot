<!-- Job posting: https://ca.linkedin.com/jobs/view/machine-learning-engineer-at-invision-ai-4460322410 -->

# 1165 Invision AI — CV + Cover Letter Changelog (2026-09-03)

Pipeline: Codex eval (87/100 Strong Fit) → Fable draft → Codex reviewer (hit its usage limit mid-run; feedback saved, edits applied on the main thread) → Sonnet revise + compile + verify.

## CV — `cv/1131_main_invision_ai_machine_learning_engineer.tex`
- **Variant V5 (Computer Vision / Industrial).** Tagline `Computer Vision & ML Engineer | Industrial Inspection, IoT & Edge Deployment` (byte-identical in the cover letter). Eval scored Experience 95 / Technical 93 on a near-exact functional match: MAS shipped production OpenCV inspection with camera/sensor/IoT integration + embedded C++/Python inference + CI/CD.
- **Emphasized:** MAS as 5 bullets (care-label QC 99.5%, loom-side microscopic array -50% operators, Promptly alignment + RIP, real-time IoT/ETL + CI/CD, +300% efficiency); postdoc trimmed to 2 (14 ms RPi4 / F1 0.76 / 74x + frozen-protocol benchmarks); McGill sensor-fusion (F1 0.78); Competency groups CV & Perception / ML Engineering / Systems & Deployment; stack 3rd line swapped to Computer Vision; added literal "resource-constrained" and "sensor fusion" for ATS.
- **Cut:** Forestpin role; Selected Publications section (folded "10+ peer-reviewed papers" into a Highlights bullet — V5 industrial, pubs are the weakest signal); Selected Projects from 7 → 4 (kept tech-pack OCR, lace/ERP search, real-time audio detection, SSIM 95% training-free; dropped care-label/loom/Promptly which are already detailed in the Experience bullets); hardcoded template `\newpage`; MIDI Innovation Awards highlight.
- **Grounding (per reviewer):** ONNX/quantization/TFLite phrased as "familiarity" only; TensorRT / experiment-tracking / modern production CNNs / 3D digital twins / geospatial tracking left as honest gaps (named in the cover letter as ramp-up, never claimed as experience); "I own the full lifecycle" softened to "My work runs from ..."; MAS = one entry Jan 2015 - Jul 2020; no Promptly patent; **95% SSIM figure kept** (grounded in knowledge-graph §13/§16).
- Layout: `\enlargethispage{4\baselineskip}` before Highlights to pull the last bullet back onto page 2. **Final: exactly 2 pages** (V5 budget). No orphaned titles (page 1 ends with full Education, page 2 opens with the Experience heading). ATS text layer clean (pdftotext, 0 cid/replacement, email + phone literal, single-ASCII-hyphen dates).
- Keyword coverage: covered — computer vision, production, edge, resource-constrained, sensor fusion, OpenCV, C++, Python, TensorFlow, PyTorch, Docker, embedded, monitoring, deployment, ONNX, CI/CD, label. Honest gaps (in cover letter, not stuffed): object detection, image classification, modern CNN backbones, TensorRT, experiment tracking / dataset versioning / ML observability.

## Cover Letter — `cover_letters/1131_cover_invision_ai_machine_learning_engineer.tex`
- Plain `article`, 4 paragraphs, "Dear Hiring Manager,". No posting override (eval: "None stated").
- P1: MAS shipped industrial CV (99.5%) as the hook, substantiated by the 14 ms RPi4 / F1 0.76 / 74x result. The draft's "I have already done the core of this job" opening was **removed** (overclaimed the transportation / 3D-digital-twin domain, which is adjacent not documented).
- P2: production CV + edge optimization + full-lifecycle + sensor fusion, each tied to a concrete item; honest gaps (experiment tracking, ONNX Runtime, TensorRT, modern CNN backbones) named as ramp-up.
- P3: why Invision — uses the verified `company_research/invision-ai.json` wording ("single-camera 3-D awareness and collaborative multi-camera meshes for smart infrastructure and mobility"), not the LinkedIn about-text; connects to his industrial-CV + edge record; first 6-12 months = "help build" data-labeling and evaluation systems (softened from "take ownership of a product line").
- P4: PR / no sponsorship / Toronto / 3-day downtown hybrid / available immediately (postdoc ended Dec 2025).
- **Final: exactly 1 page.**

## Company research
- `company_research/invision-ai.json` written by Codex (Toronto, founded 2017, 11-50 employees, edge AI / CV / embedded / sensor fusion / intelligent transportation; small mixed Glassdoor sample; no funding stage disclosed).

## Open flags for Nishal
- LinkedIn tags the role "entry level" — inconsistent with a PhD + ~11 yrs; clarify title, scope, comp, growth path.
- Mixed Glassdoor culture signal (older leadership/workload/growth concerns vs recent ownership/mentorship positives) — test in interviews.
- No stated deadline.
