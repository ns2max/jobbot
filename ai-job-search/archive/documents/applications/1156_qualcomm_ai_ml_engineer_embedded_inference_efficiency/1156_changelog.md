<!-- Job posting: https://ca.linkedin.com/jobs/view/ai-machine-learning-engineer-embedded-systems-inference-efficiency-at-qualcomm-4447193368 -->

# 1156 Qualcomm — Embedded Systems, Inference Efficiency — Changelog (2026-09-03)

Pipeline: main-thread eval (62/100 Good Fit, REACH) → Fable draft (cloned from the 1127 Huawei reach-role application, re-tailored) → main-thread review + compile + verify. Codex exhausted until Oct 3.

## CV — `cv/1122_main_qualcomm_ai_ml_engineer_embedded_inference_efficiency.tex`
- **Variant V3 (Edge / Embedded).** Tagline `ML Research Engineer | Real-Time & Edge Inference | Audio, Sensor & Time-Series` (byte-identical in cover).
- Structurally the same as the 1127 Huawei CV (same reach-role shape: edge inference-efficiency research with compiler/accelerator/top-venue gaps). Summary + "Edge & System Optimization" group led on: efficient inference under a hard device budget as the research question, hardware-aware benchmarking methodology + frozen-protocol regression suites, model quantization for deployment, ARM CPU latency + memory profiling on real devices, model-development-pipeline ownership (training/fine-tuning/evaluation/performance optimization — matching the posting's requirement wording).
- Compiler-stack tools (ONNX, TFLite, TVM, MLIR, TensorRT) kept as **"familiarity" only** in both the competency and stack lines. No compiler/accelerator/KD/pruning/PEFT/efficient-architecture claims.
- No template `\newpage`. Trimmed to fit: shortened the Publications SSIM parenthetical, `\needspace` 7→5 before Portfolio, `\enlargethispage{3\baselineskip}` before Highlights.
- **Grounding:** all numbers verified (14 ms / F1 0.76 / 74x / 31.4% CPU / 1038 ms; F1 0.78; **95% SSIM kept, labelled as symbolic-music training-free detection** — grounded KG §13/§16; 300% / 99.5%); MAS one entry Jan 2015-Jul 2020; Promptly not mentioned (no patent risk); English only; Claude Code named.
- **Final: 3 pages** (V3 budget 2-3). Page 1 ends with Technical Stack, page 2 opens with Portfolio, page 3 opens with the MAS role — no orphaned titles. ATS text layer clean (0 cid/replacement, email + phone literal, single-ASCII-hyphen dates). Covered: inference, efficiency, quantization, compression, benchmark, regression, latency, memory, profiling, ARM, device, pipeline. Honest gaps (cover letter, not stuffed): compiler, pruning, distillation, accelerator, PEFT, efficient-architecture design, top-venue publications.

## Cover Letter — `cover_letters/1122_cover_qualcomm_ai_ml_engineer_embedded_inference_efficiency.tex`
- Plain `article`, 4 paragraphs, "Dear Hiring Manager,". **Exactly 1 page.**
- P1: JAES 2026 edge result (14 ms / F1 0.76 / 74x / 31.4% CPU) framed as inference-efficiency research + the frozen-protocol benchmark methodology behind it.
- P2: genuine-coverage parts in the posting's vocabulary (efficient inference under device constraints; hardware-aware benchmarking + performance-regression suites; ARM CPU latency + memory profiling on real devices; model quantization for deployment; end-to-end model-development-pipeline ownership; Nebula; MIRaaS edge-to-server split).
- **P3 explicit honest-gap paragraph:** names compiler stack / ML system optimization for AI accelerators (graph transformation, tiling, scheduling, tensor-layout/memory optimization), advanced model-compression research (research-grade quantization, structured pruning, KD, PEFT, efficient architecture design), and accelerator-dataflow co-design as deliberate growth areas; states plainly that JAES/IEEE IS2/DAFx/Asilomar are strong in audio + signal processing but not the NeurIPS/ICML/CVPR tier the posting names, with benchmark methodology + open datasets + reviewer/PC service standing alongside.
- P4: why Qualcomm's Markham Global Centre of Excellence for ML / Low Power AI Solution team (on-device low-power AI via SW-HW co-design, research-with-a-shipping-target) + logistics (PR, no sponsorship, Toronto-based so **no relocation** for Markham, available immediately).

## Notes for Nishal
- **This is a reach role** (62, down from triage's 73), same compiler/accelerator/advanced-compression/top-venue gap profile as Huawei 1127. The cover letter is deliberately upfront.
- **The sibling role 1129 (AI Processors, applied, score 75, comp CAD 131-181k) is the stronger Qualcomm application.** Applying to both is reasonable — different teams.
- Comp band CAD 114,400-164,400 (a notch below 1129). GTA, no relocation. No stated deadline.
