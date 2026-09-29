<!-- Job posting: https://jobs.ashbyhq.com/eli/dd8575a8-60e0-472f-a8b9-6f7a6478699d -->

# 1139 Eli Health — CV + Cover Letter Changelog (2026-09-03)

Pipeline: eval on the main thread (Opus subagent hit a 529; Codex exhausted until Oct 3) → Fable draft → main-thread grounding review + compile + verify.

## CV — `cv/1139_main_eli_health_machine_learning_scientist.tex`
- **Variant V1 (AI-Industry)** with an applied-science / statistical-rigor lean — the role is explicitly "scientific problem solving and applied ML, not ML infrastructure". Tagline `Machine Learning Research Engineer | Deep Learning, Time-Series, Pattern Detection | Applied ML` (byte-identical in the cover letter).
- **Reframed** the summary and Core Competency groups around: signal processing + statistical modelling on noisy data, model validation / uncertainty / generalization, benchmark-and-ablation design that separates real gains from metric noise, evaluation under distribution shift, error analysis and production-failure diagnosis. Edge/latency/MLOps kept but demoted; Kubernetes / LLM-RAG language dropped as off-target. Stack line 3 renamed "Signal & Data".
- **Medical-signal adjacency** surfaced: the COVID-19 remote-vitals CV device (GMOA) is its own MAS bullet and appears in Domain Expertise + the summary; Forestpin kept as anomaly detection on "messy structured data".
- **Cut for the 2-page budget:** UVPA visiting-researcher role; the template `\newpage`; Independent Research trimmed to 1 bullet (LiveLaTeX dropped); Selected Projects 4 → 3 (kept real-time audio detection, SSIM 95%, open benchmark datasets; dropped standalone Nebula); Publications section merged into a single "Publications & Recognition" bullet; GMOA + Open-science highlights removed as duplicates. `\enlargethispage{3\baselineskip}` before the merged section.
- **Grounding fixes (main-thread review):** Fable's "ran two live user studies (20 audience, 6 performers)" → "ran a user study across two live concerts (20 audience, 6 performers, p < 0.05)" — KG has one study across two concerts, not two studies. Everything else verified: 14 ms / F1 0.76 / 74x / 1038 ms; **95% SSIM kept (grounded, KG §13/§16)**; F1 0.78 / 500-event corpus; up to 300% / 99.5%; MAS one entry Jan 2015-Jul 2020; no Promptly patent; MUSMET = 12-partner consortium (confirmed KG §4.1, though the partner-count line was cut in trimming); English only, no languages section.
- **Final: exactly 2 pages.** Page 1 ends with full Education, page 2 opens with Selected Projects — no orphaned titles. ATS text layer clean (0 cid/replacement, email + phone literal, single-ASCII-hyphen dates). All 15 posting keywords covered (signal processing, statistical, validation, generalization, distribution shift, error analysis, anomaly, experiment, reproducible, Python, feature engineering, model selection, uncertainty, deep learning, production).

## Cover Letter — `cover_letters/1139_cover_eli_health_machine_learning_scientist.tex`
- Plain `article`, 4 paragraphs, "Dear Hiring Manager,". **Exactly 1 page.**
- P1: JAES 2026 benchmark work as the hook, framed as "telling a real accuracy gain apart from metric noise, and keeping an honest record of what did not work".
- P2: mirrors the posting's asks (signal-processing / statistical modelling on imperfect data; meaningful vs metric-only improvements; production-failure diagnosis + distribution shift) with postdoc benchmarks, MAS deployed CV + human-in-the-loop, Forestpin anomaly scoring.
- P3: why Eli — from `company_research/eli-health.json` only (Hormometer saliva cortisol, FDA-registered, CES 2025 Best of Innovation in Digital Health, CAD 17M Series A, <25-person team, women's lifelong health); frames the at-home-device reliability problem as "fundamentally a noisy-measurement problem: confounding, measurement variability and distribution shift"; weaves in the posting's signature question ("what can we conclude with confidence, what remains uncertain, what should we do next") as how he already works; names assay / biochemistry as genuinely new, with the manufacturing + financial-forensics cold-start precedent.
- P4: PR / no sponsorship / available immediately / happy to relocate to Montreal for the on-site role (McGill CIRMMT reconnection from the 2024 visiting appointment).

## Company research
- `company_research/eli-health.json` written (verified via BetaKit + Athletech + search: Series A CAD 17M led by BDC Capital Thrive Venture Fund, ~CAD 28M total, US FDA-registered Hormometer, CES 2025 award, founded 2019 by Marina Pavlovic Rivas + Thomas Cortina).

## Open flags for Nishal
- **On-site Montreal** required (despite a distributed wider team) — a real relocation from Toronto.
- Comp not disclosed; Series A startup, likely equity-weighted, may sit below the CAD 120-150k benchmark.
- Assay / biochemistry / consumer-diagnostics domain is entirely new.
- No stated deadline.
