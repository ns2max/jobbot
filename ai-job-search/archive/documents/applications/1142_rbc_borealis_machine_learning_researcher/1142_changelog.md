<!-- Job posting: https://freehire.me/jobs/machine-learning-researcher-pushing-ai-frontiers-in-banking-rbc-3j5ep3ds -->

# 1142 RBC Borealis — Machine Learning Researcher — Changelog (2026-09-03)

Pipeline: main-thread eval (63/100 Good Fit, **HOLD pending verification**) → Fable draft (from the 1145 V2 skeleton) → main-thread review + compile + verify. Codex exhausted until Oct 3.

> **DO NOT SUBMIT until verified.** (1) The posting is a thin whatjobs/freehire aggregator stub, not a verbatim RBC posting. (2) It may be a re-listing of ai-job-search IDs 1105/1106 (RBC Borealis roles scraped ~2026-08 and marked expired). (3) career-ops already applied to RBC Borealis (#107 "Senior ML Researcher Lead", 2026-04-16). Confirm a live, distinct opening on rbcborealis.com / RBC Careers and coordinate with the career-ops RBC application before sending. The draft is tailored to RBC Borealis's public "Machine Learning Researcher" role framing.

## CV — `cv/1142_main_rbc_borealis_machine_learning_researcher.tex`
- **Variant V2 (AI-Research).** Tagline `Research Scientist | Real-Time Multimodal ML, Benchmarks & Open Datasets` (byte-identical in cover). Only V2 carries the full publications / datasets / peer-review / supervision record a publishing AI institute rewards.
- Summary + Competencies re-led on: **time-series and sequence-modelling research** (RNN/LSTM/GRU, benchmark + evaluation methodology); **translating research into production-grade solutions** (postdoc owned the science + the pipeline; MAS shipped research prototypes to the factory floor with CI/CD); **generative modelling for time series and signals** (VAE- and diffusion-based synthetic-data prototypes — aligned with RBC Borealis's generative-time-series direction, NOT LLM/text); large datasets (4 open corpora, 9,800+ recordings; MAS high-frequency IoT ETL across three continents); **Forestpin financial-forensics anomaly-detection adjacency**; publications + reviewer/PC service + student supervision.
- Competency groups renamed toward the JD (Time-Series & Sequence Modelling / Research to Production / Generative Modelling & Data / Publication & Service); 3rd stack line "Signal & Time-Series Processing".
- Sections: Summary, Competencies, Stack, Education, Experience, Publications (8, Scholar footnote), Datasets (4), Scientific Committee & Peer Review, Student Supervision, Highlights. **No Talks section.**
- **Grounding:** all numbers verified (14 ms / F1 0.76 / 74x / 31.4% CPU; F1 0.78; 95% SSIM grounded KG §13/§16; 300% / 99.5%); MAS one entry Jan 2015-Jul 2020; **Promptly not mentioned** (no patent risk); Supervision = Collizoli (Aug 2023) + Battisti (Sep 2026) from KG §4.1a; Generative AI framed as VAE/diffusion for **time series and signals**, never LLM/text; English only; Claude Code named ("LLM-assisted tooling").
- **Final: exactly 3 pages** (V2 budget). Page 1 ends with Education (PhD thesis line), page 2 MSc/BEng + Experience, page 3 Publications onward — no orphaned titles. ATS text layer clean (0 cid/replacement, email + phone literal, single-ASCII-hyphen dates). Covered: time series / time-series, generative, machine learning research, large dataset, production, publish, anomaly, financial, benchmark, sequence.

## Cover Letter — `cover_letters/1142_cover_rbc_borealis_machine_learning_researcher.tex`
- Plain `article`, 4 paragraphs, "Dear Hiring Manager,". **~1 page.**
- P1: advances ML research and translates it to production — the JAES 2026 detector (14 ms real-time inference, F1 0.76, 74x), out of frozen-protocol benchmarks + ablations, shipped as a deployed system.
- P2: the role's asks in its own terms — advance ML research across time series and generative AI (RNN/LSTM/GRU sequence work + VAE/diffusion synthetic-data prototypes for signals); work with large datasets (4 open corpora, 9,800+ recordings; MAS IoT ETL across three continents); collaborate with engineering to translate research to production; publish (10+ peer-reviewed papers, reviewer for IEEE Access + JNSF Sri Lanka, PC for IEEE IS2 + I3DA).
- **P3 honest about gaps:** the connection is direct on two of the three pillars (time-series; and Forestpin financial-forensics anomaly detection for the banking angle). "NLP is not a track I have, and my publication venues (JAES, IEEE IS2, DAFx, Asilomar) are strong in audio and signal processing but not the NeurIPS or ICML tier" — with the open datasets, benchmark methodology, and review service standing alongside.
- P4: PR / no sponsorship / available immediately / open to relocating within Canada for an RBC Borealis office (Calgary or another).

## Company research
- `company_research/rbc-borealis.json` (RBC's AI research institute; pillars NLP / time-series / generative AI for banking; publication + conference support; multiple Canadian offices; **duplication caveat in `network_contacts_note`**).

## Update 2026-09-11 — Independent Researcher section added
- Added a new **"Independent Researcher | Self-directed" (Jan 2026-Present)** entry, first in Research and Work Experience (reverse-chronological, continues to Present): speakfrench (6-method pronunciation-scoring benchmark, 100k trials, ROC-AUC/EER/Cohen's d), melodiq (Airflow/S3/Snowflake ETL pipeline), poetry2music (in progress, flagged honestly), plus a pointer to the two 2026 papers accepted in this period (Smart Drums JAES, MIRaaS IEEE IS²) and Nebula — cross-referenced rather than restated to avoid duplicating the Publications and prior Highlights entries.
- Deduped: dropped Nebula from the Highlights "Open source and tooling" bullet (now lives in the new section instead); dropped the repeated F1 0.76/14ms/74x parenthetical from the JAES Publications line (already stated in Summary + Postdoc bullet) and the "(95% detection, training-free)" DAFx parenthetical (page-budget cut, metric not otherwise repeated in this CV).
- Compensating cuts to hold the **3-page V2 budget**: merged Scientific Committee & Peer Review + Student Supervision into one "Service, Review & Supervision" section; converted Datasets from a 4-item bulleted list to one dense paragraph; converted Highlights from 3 bulleted items to one dense paragraph; `\enlargethispage{3\baselineskip}` before Service section (kept conservative — an earlier attempt at 6-8\baselineskip visibly clipped text past the bottom margin, caught by re-rendering the PDF page image, not just checking `pdfinfo` page count).
- Recompiled clean: 3 pages exactly, no orphaned entry titles, only a pre-existing 6pt overfull-hbox warning (unrelated line, unchanged). Not re-run through ATS dump for this update (content-only patch on an already-verified file); worth a fresh ATS check before actually submitting, given the HOLD below.

## Update 2026-09-11 (2) — VarianceEngine added
- Added a **VarianceEngine** bullet, first in the Independent Researcher entry: LoRA fine-tune of MusicGen-medium (custom audio-to-audio conditioner) chosen over 4 other architectures, dual-GPU, generating expressive musical variations from a ground-truth recording, trained on his own DoPP dataset. Flagged "in progress" — real checkpoint/generated samples exist, no eval results yet, so no invented metrics used.
- Strongest generative-AI evidence in this CV for RBC's stated generative-AI pillar; a stronger, more concrete claim than the existing VAE/diffusion-prototype language elsewhere in Summary/Competencies, which this doesn't yet replace.
- **Not recompiled/re-verified per Nishal's request — he will compile and check the page count himself.** Before submitting, this file needs the same compile + page-budget + ATS pass every other draft got.

## Open flags for Nishal
- **HOLD** — verify the opening is live and distinct, and coordinate with career-ops's RBC Borealis application (#107), before submitting.
- NLP is not his track; generative AI here means generative *time series*, not LLMs; top-venue publication expectation is a gap.
- Large, process-bound bank. Likely relocation (Calgary or another RBC Borealis office). Comp not disclosed. No stated deadline.
