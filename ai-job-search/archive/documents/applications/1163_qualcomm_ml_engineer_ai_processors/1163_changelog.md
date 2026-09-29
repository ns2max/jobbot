<!-- Job posting: https://ca.linkedin.com/jobs/view/machine-learning-engineer-ai-processors-sr-to-staff-at-qualcomm-4439865484 -->

# 1163 Qualcomm — AI Processors (Sr to Staff) — Changelog (2026-09-03)

Pipeline: main-thread eval (75/100 Strong Fit) → Fable draft → main-thread grounding review + compile + verify. (Opus subagents 529-ing; Codex exhausted until Oct 3.)

## CV — `cv/1129_main_qualcomm_ml_engineer_ai_processors.tex`
- **Variant V3 (Edge / Embedded).** Tagline `ML Research Engineer | Real-Time & Edge Inference | Audio, Sensor & Time-Series` (byte-identical in cover).
- Summary reframed to lead with **translating ML algorithms into efficient edge software end-to-end** and **HW/SW trade-off engineering** (latency/compute/memory/thermal/power vs accuracy/UX), then CV + multimodal fusion, then the 14 ms / F1 0.76 / 74x result. Audio kept as one strand, not the headline (this is an applied CV+multimodal edge role, and audio/speech is one of several named preferred areas).
- Competencies: added "computer vision and image processing (OpenCV, template and feature matching, registration and warping, industrial inspection)" for the posting's "video/image processing algorithms" line; multimodal sensor fusion added to ML Engineering. Compiler stack trimmed to "familiarity with ONNX and TFLite" — TVM/MLIR/TensorRT dropped (not this role's ask, and overclaiming).
- Postdoc 4 bullets (incl. the MUSMET multimodal audio+EEG+MR reference-demonstrator); MAS 3 bullets (99.5% + 50% + COVID vitals device); McGill reframed around the self-powered instrument + power-envelope trade-off; Highlights added "Reference applications" (MUSMET concerts + Hot Licks) and "HW/SW trade-off methodology".
- **Grounding fix (Fable stretch flag was right):** Fable's Projects bullet conflated MAS care-label inspection with the PhD SSIM training-free *music*-pattern method (95%) as if one project — split: the Projects bullet is now MAS industrial inspection only (99.5% + loom-side 50%); the SSIM 95% figure still appears where it belongs (real-time detection work). All other numbers verified (14 ms / F1 0.76 / 74x / 31.4% CPU / 1038 ms; F1 0.78; 300% / 99.5% / 50%); MAS one entry Jan 2015-Jul 2020; Promptly not mentioned (no patent risk); English only; Claude Code named.
- **Final: 3 pages** (V3 budget 2-3). Page 1 ends with Technical Stack, page 2 opens with Portfolio — no orphaned titles. ATS text layer clean (0 cid/replacement, email + phone literal, single-ASCII-hyphen dates). Covered: computer vision, multimodal, edge, embedded, PyTorch, TensorFlow, Python, C++, power, latency, deploy, reference application, XR, IoT, audio, image processing. Honest gaps (cover letter, not stuffed): Snapdragon/QNN/AI Engine tooling, agentic AI, foundation models.

## Cover Letter — `cover_letters/1129_cover_qualcomm_ml_engineer_ai_processors.tex`
- Plain `article`, 4 paragraphs, "Dear Hiring Manager,". **Exactly 1 page.**
- P1: hook on translating an algorithm into efficient device software + JAES 2026 (14 ms / F1 0.76 / 74x / 31.4% CPU).
- P2: the role's asks in its vocabulary — translate ML to edge software (MAS shipped CV/IoT, postdoc RPi4 deployment, McGill instrument); HW/SW trade-offs for performance/power/UX; CV + multimodal AI (F1 0.78); audio/speech + video/image processing; reference applications (MUSMET concerts, Hot Licks).
- P3: brief honest ramp note — agentic AI / foundation models and Qualcomm's own on-device toolchain (AI Engine, QNN) are areas to ramp on, built on the ARM/RPi profiling + quantization + benchmark-methodology foundation.
- P4: why Qualcomm's Markham Global Centre of Excellence for ML (on-device AI mission, moving model capability onto the device for latency/power/privacy) + logistics (PR, no sponsorship, Toronto-based so **no relocation** for this Markham role, available immediately).

## Company research
- `company_research/qualcomm.json` (shared with 1122): Markham = Qualcomm's Global Centre of Excellence for ML; Snapdragon + on-device Qualcomm AI Engine (Hexagon NPU); Snapdragon Summit 2025 "AI everywhere" on-device direction. Comp disclosed in the posting.

## Notes for Nishal
- One of the cleaner fits in the pipeline: work + level (Sr/Staff IC) + location (GTA, no relocation) + comp (CAD 131-181k, above target) all line up.
- Peripheral gaps: agentic AI, foundation models, Qualcomm-specific tooling — addressed honestly and briefly in the cover letter.
- Sibling role 1122 (Inference Efficiency, research/compiler) also drafted — weaker fit (62); this is the stronger Qualcomm application.
- No stated deadline.
