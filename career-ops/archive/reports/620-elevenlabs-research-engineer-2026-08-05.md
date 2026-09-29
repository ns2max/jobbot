# Evaluation: ElevenLabs — Research Engineer (Remote)

**Date:** 2026-08-05
**URL:** https://jobs.ashbyhq.com/elevenlabs/3d650946-5ac2-4729-9ae4-129c43fcd0b5
**Archetype:** ML Research Engineer (primary) / Applied Scientist (secondary)
**Score:** 4.1/5
**Legitimacy:** High Confidence
**PDF:** pending (generate-pdf.mjs script unavailable in this repo)
**Verification:** unconfirmed (batch mode) — WebFetch on the Ashby SPA returned only the page title ("Research Engineer @ ElevenLabs"); no browser/Playwright tool available this session. Content below is reconstructed from the prior full evaluation of this same URL (re-eval 2026-07-09, scored 4.1/5) and the tailored CV/cover letter already on file (`output/617-elevenlabs-research-engineer.md`). Re-verify live before applying.

---

## A) Role Summary

| Field | Detail |
|---|---|
| Archetype | ML Research Engineer / Applied Scientist hybrid |
| Domain | Audio ML — TTS data, training, and research |
| Function | Build (data pipelines + model training + research) |
| Seniority | Research Engineer (individual contributor, senior-leaning given PhD requirement pattern at ElevenLabs) |
| Remote | Remote global — Canada explicitly confirmed eligible in the JD (per prior evaluation) |
| Team size | Not disclosed |
| TL;DR | Own the TTS/audio research loop end-to-end — data curation through training through evaluation — at an $11B voice-AI company with an artifacts-over-credentials hiring culture. |

## B) Match with CV

| JD Requirement | CV Evidence |
|---|---|
| Audio/speech ML research | JAES 2026, DAFx 2022, IEEE Internet of Sounds 2025 — 3 of 10 peer-reviewed publications directly on real-time audio pattern detection |
| Data pipeline ownership (collection → curation → training → eval) | MUSMET postdoc: "owned full ML pipelines for streaming multi-dimensional data... covering data acquisition, signal processing, feature engineering, training/evaluation, and deployment" |
| Published, reproducible datasets | Zenodo: 7,000+ recordings, 70 musicians, DoMP/DoPP/DoDP — versioned, annotated, DOI-registered |
| Real-time inference at production quality | <30ms at >90% F1 (MUSMET); 14ms on Raspberry Pi 4, 74× faster than DTW baseline (JAES 2026) |
| Artifacts-over-credentials culture fit | Public portfolio (nishal.xyz), GitHub, ORCID, ResearchGate, open-sourced Nebula C++17 feature-extraction library — all public, verifiable work product |
| Benchmark/ablation methodology | "Designed benchmark suites (baselines + ablations) to quantify architecture/feature tradeoffs" |

**Gaps:**
1. **TTS/generative-audio modeling specifically** (as opposed to detection/pattern-recognition) — nice-to-have, not a hard blocker. Mitigation: the resume's diffusion/VAE synthetic-audio-generation work (McGill visiting researcher) is directly adjacent generative-audio experience; frame it as transferable generative modeling background in the cover letter.
2. **Large-scale distributed training infrastructure** — not evidenced in the CV (background is single-researcher/small-team pipelines, not multi-GPU cluster training at ElevenLabs' scale). Mitigation: acknowledge directly, pair with "benchmark-first methodology scales regardless of cluster size" framing; this is the same gap noted in the prior 4.1/5 evaluation and didn't prevent a strong score.

## C) Level and Strategy

1. **Level detected:** "Research Engineer" (no seniority prefix) vs. candidate's natural level — PhD + postdoc + 10 publications typically reads as Senior/Staff-adjacent for a company at ElevenLabs' stage; this posting likely sits at or slightly below natural level.
2. **Sell senior without lying:** Lead with the MUSMET postdoc's full-lifecycle ownership and the JAES 2026 latency numbers — these read as senior-IC scope regardless of title. Cite the Zenodo dataset release as evidence of independent, self-directed research output (not just following a PI's agenda).
3. **If downleveled:** Comp band at ElevenLabs for research engineering skews high ($230K-$400K+ per market data below) even at IC levels — a downlevel is still likely comp-competitive. Accept if base + equity clears the $150K CAD floor with a defined 6-month scope review.

## D) Comp and Demand

| Source | Data |
|---|---|
| Levels.fyi | Software Engineer total comp $230K–$345K+ US; senior/staff engineering roles up to $445K |
| Industry commentary (jobsbyculture.com, nahc.io) | Research Engineer / ML research roles reportedly $350K–$400K+ total comp at senior levels; base for mid-level US engineers $120K–$180K, equity 20–40% of total comp |
| Relative positioning | Reported to pay below Anthropic ($300K–$490K) and OpenAI ($350K–$550K) in cash comp, but ElevenLabs is post-Series D at $11B valuation with $500M+ ARR — equity upside is real |
| Layoffs/hiring freeze check | No layoffs or hiring-freeze signals found (WebSearch, 2026-08-05); company reported ~223 open roles as of mid-2026, consistent with active growth-stage hiring |

Sources: [Levels.fyi — ElevenLabs Software Engineer](https://www.levels.fyi/companies/elevenlabs/salaries/software-engineer/locations/united-states), [ElevenLabs Compensation 2026 breakdown](https://jobsbyculture.com/blog/elevenlabs-compensation-2026)

Note: Canada-remote comp likely lands at a discount to these US figures; treat the ranges above as ceiling references, not a CAD-equivalent guarantee.

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---------|---------------|------------------|---------|
| 1 | Headline | Generic PhD ML Research Engineer framing | "Audio ML Research Engineer — Data Pipelines, Model Training & Real-Time Audio Systems" (as already used in `output/617`) | Mirrors the JD's exact framing: data → training → research loop |
| 2 | Summary | Broad ML background | Lead with published audio ML researcher + dataset release + <30ms/74× latency numbers | Matches artifacts-over-credentials culture; leads with public, verifiable proof |
| 3 | Core Competencies | Generic ML Engineering block | Split into Audio Data Engineering / Model Training & Evaluation / Audio & Speech Systems (as in `output/617`) | Directly mirrors the three JD pillars |
| 4 | Experience bullets | Generic pipeline language | Emphasize "owned full audio ML lifecycle" and dataset versioning/annotation protocol language | Speaks the JD's data-curation vocabulary |
| 5 | LinkedIn headline | — | "Published Audio ML Researcher \| Real-Time Inference & Data Pipelines \| PhD" | Keyword match for recruiter search on "audio ML" + "research" |

Top 5 LinkedIn changes: mirror the above — headline, About section opening with the Zenodo dataset + JAES 2026 numbers, add "Text-to-Speech" and "Audio ML" as skills, pin the JAES 2026 publication, add MUSMET project to Featured.

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Data curation & annotation at scale | Zenodo dataset release | Needed reproducible benchmarking data for real-time pattern detection research | Design collection protocol across 70 musicians | Built versioning, annotation guidelines, DOI registration for 4 dataset releases | 7,000+ recordings publicly available, cited resource for the field | Learned that annotation-guideline clarity upfront saves far more time than fixing labels after the fact |
| 2 | Real-time inference at production latency | JAES 2026 RPi4 detector | Needed sub-30ms detection on embedded hardware for smart instruments | Optimize architecture + implementation for edge constraints | Redesigned pipeline achieving 14ms, 74× faster than DTW baseline | Published, reproducible result at a peer-reviewed venue | Would explore quantization earlier next time — got most gains late in the process |
| 3 | Full-lifecycle pipeline ownership | MUSMET postdoc | EU-funded project needed streaming multi-dimensional data pipeline | Owned data acquisition through deployment solo | Built, documented, and handed off production-grade components | <30ms at >90% F1, adopted by academic + industry partners | Documentation-as-you-go was the difference between a research prototype and something partners could actually run |
| 4 | Generative/synthetic audio adjacency | McGill diffusion/VAE synthetic data | Limited labeled data for gesture-detection ML | Explore diffusion and VAE-based synthetic generation | Built and evaluated synthetic data pipelines | Directly shaped deployment decisions on which approach to productionize | Synthetic data quality matters more than quantity — spent too long generating before validating utility |

**Recommended case study:** JAES 2026 (14ms RPi4 detector) — it's the single artifact that proves both "public, verifiable work product" (culture fit) and production-grade real-time audio ML (core requirement).

**Red-flag questions:**
- *"Why are you leaving academia?"* → Frame as returning to industry with sharper tools, not fleeing research (per `modes/_profile.md` exit narrative).
- *"Have you worked with TTS/generative models specifically?"* → Be direct about the gap; pivot to the diffusion/VAE synthetic-audio work as the closest adjacent experience and express clear interest in the transition.

## G) Posting Legitimacy

**Assessment:** High Confidence

| Signal | Finding | Weight |
|---|---|---|
| Posting freshness | Unconfirmed this pass (WebFetch blocked by Ashby SPA); confirmed live and active as of the 2026-07-09 evaluation | Neutral |
| Description quality | Prior evaluation found specific, role-appropriate JD (TTS data/training/research scope, remote-global with Canada confirmed) | Positive |
| Company hiring signals | No layoffs or hiring-freeze signals found; ~223 open roles reported mid-2026 post-Series D ($11B valuation, $500M+ ARR) | Positive |
| Reposting detection | Same URL seen twice in scan history (2026-04-23 added, 2026-04-28 dup-skip) with no churn since — stable single posting, not a repeatedly-reposted req | Positive |
| Role market context | Research Engineer roles at growth-stage AI companies commonly stay open 4-8 weeks; nothing here suggests otherwise | Neutral |

**Context notes:** This evaluation could not independently re-verify liveness due to tooling limits (no Playwright/browser this session, Ashby's JS-rendered page defeats WebFetch). Confirm the posting is still live via direct browser visit before investing further time.

## H) Draft Application Answers

*(Score 4.1/5 is below the 4.5 auto-draft threshold — skipped.)*

---

## Keywords extracted

Research Engineer, Text-to-Speech, TTS, audio ML, data pipelines, model training, evaluation, real-time inference, signal processing, PyTorch, JAX, benchmark, ablation, dataset curation, annotation, synthetic data, diffusion models, VAE, remote, Canada, voice AI, speech synthesis, artifacts-over-credentials
