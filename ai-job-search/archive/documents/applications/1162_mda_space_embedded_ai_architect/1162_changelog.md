<!-- Job posting: https://ca.linkedin.com/jobs/view/embedded-artificial-intelligence-architect-at-mda-space-4414774301 -->

# 1162 MDA Space — Embedded AI Architect — Changelog (2026-09-03)

Pipeline: main-thread eval (57/100 Moderate Fit, eligibility FLAG) → Fable draft (from the 1127 Huawei V3 honest-reach pair) → main-thread review + compile + trim + verify. Codex exhausted until Oct 3.

> **GATING ISSUE — ITAR.** The posting requires passing a security assessment for the **Controlled Goods Program and ITAR**. Reliability status and CGP are PR-accessible; **ITAR restricts access to US-controlled technical data to "US persons"** and Nishal is a Sri-Lankan-citizen Canadian PR. **He should ask MDA directly whether a non-US-person PR can be accommodated for this role before submitting.** The cover letter raises this as a logistics item to confirm together, not a disqualification.

## CV — `cv/1128_main_mda_space_embedded_ai_architect.tex`
- **Variant V3 (Edge / Embedded).** Tagline `ML Research Engineer | Real-Time & Edge Inference | Audio, Sensor & Time-Series` (byte-identical in cover).
- Summary + "Edge & System Optimization" group re-led on the posting's vocabulary: **deploy/prototype ML on embedded targets** (Raspberry Pi named in the JD), select model architectures within embedded compute/power/memory/latency budgets, define metrics and evaluate model performance / robustness / **resource utilization on target platforms**, design **simulators and rule-based generators** for representative training data, dataset curation with frozen train/val/test protocols. Time-series / sequence modelling kept explicit and tied to **network traffic prediction as a forecasting problem**.
- Dropped the Huawei-specific compiler/runtime framing (TVM/MLIR/TensorRT); ONNX/TFLite trimmed to "familiarity". Added Jira/Confluence (JD nice-to-have). Added a one-line **Languages** highlight: "English (native); French (basic, improving)" — the JD says "English and/or French" with English sufficient and French only nice-to-have; NEVER "bilingual"/"fluent French".
- **Grounding:** all numbers verified (14 ms / F1 0.76 / 74x / 31.4% CPU; F1 0.78; 95% SSIM grounded KG §13/§16; 300% / 99.5%); MAS one entry Jan 2015-Jul 2020; Promptly not mentioned (no patent risk); reviewer/PC line matches KG §4. Softened Fable's "digital-twin-style synthetic data" → "rule-based and generative synthetic training data" (he has not built an aerospace-sense digital twin). English/French only.
- Does NOT claim: 10 years of embedded software development, satellite comms / RF / DVB-S2X / cognitive radio, Versal/FPGA, CUDA/GPU optimization, RL depth, or architect/technical-lead tenure — all named as growth areas in the cover letter.
- **Final: 3 pages** (V3 budget 2-3). Page 1 ends with Technical Stack, page 2 opens with Portfolio, page 3 opens with the MAS role — no orphaned titles. ATS text layer clean (0 cid/replacement, email + phone literal, single-ASCII-hyphen dates). Covered: embedded, Raspberry Pi, TensorFlow, PyTorch, C/C++, Python, simulator, dataset, metrics, robustness, resource utilization, latency, time-series. Honest gaps (cover letter): digital twin, FPGA/Versal, CUDA, DVB-S2X/satellite comms, RF.

## Cover Letter — `cover_letters/1128_cover_mda_space_embedded_ai_architect.tex`
- Plain `article`, 4 paragraphs, "Dear Hiring Manager,". **1 page.**
- P1: prototyping/deploying ML on embedded targets under a hard budget — JAES 2026 (14 ms on RPi4 at 31.4% CPU, F1 0.76, 74x) + the benchmark methodology for performance/resource-utilization on target platforms.
- P2: genuine overlap in the posting's terms — embedded deployment; architecture selection to budget; simulators / rule-based generators + VAE/diffusion synthetic data; dataset curation with frozen protocols; metrics/robustness/resource utilization on device; Python + TensorFlow (embedded) + PyTorch + production C/C++17 + embedded Linux + Git/CI-CD. **Network traffic prediction framed as time-series forecasting** he is equipped for.
- **P3 explicit about the stretch:** satellite comms / RF / DVB-S2X / cognitive radio / anti-jamming are new (DSP fundamentals transfer, comms domain to learn); architect / technical-lead is a step up, backed by end-to-end edge-ML ownership, evaluation-methodology definition, and mentoring.
- P4: AURORA / AI-in-space mission tie (AURORA named verbatim in the posting); PR / no sponsorship / immediate / open to relocating to Sainte-Anne-de-Bellevue; **willing to obtain reliability status + complete the CGP assessment**; **ITAR raised as a logistics item to confirm early** (PR + Sri Lankan citizen), not framed as a disqualification.

## Company research
- `company_research/mda-space.json` (MDA Space TSX:MDA, ~55-yr heritage; Satellite Systems Montreal = antennas/payloads/electronics for comm & radar sats; AURORA software-defined satellites; reliability/CGP/ITAR compliance context; the ITAR caveat is in `network_contacts_note`).

## Open flags for Nishal
- **ITAR** — the gating question; resolve with MDA before investing further.
- Architect / technical-lead / "single accountable architect" — a leadership role, his stated growth area (IC-focused).
- "10 years embedded software development" — his embedded is edge-ML deployment, not a decade of embedded SWE.
- Satellite communications / RF is a new domain.
- Montreal relocation. Comp not disclosed. No stated deadline.
