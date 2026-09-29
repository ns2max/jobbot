# Evaluation: Liquid AI — Member of Technical Staff, Embedded ML Engineer (Audio/Omni)

**Date:** 2026-08-05
**URL:** https://jobs.ashbyhq.com/liquid-ai/4ee965fc-9a9e-43db-a2e9-2da654a73e86
**Archetype:** ML Research Engineer (primary) / Senior-Staff ML Engineer (secondary)
**Score:** 4.3/5
**Legitimacy:** Proceed with Caution
**PDF:** pending (script unavailable — `generate-pdf.mjs` missing from repo)
**Verification:** unconfirmed (batch mode) — Ashby is a JS-rendered SPA; WebFetch returned title/company only. Location and posting freshness cross-confirmed via WebSearch (LinkedIn cross-post: San Francisco, CA; posted ~1 week ago as of search date).

---

## A) Role Summary

| Field | Value |
|---|---|
| Archetype | ML Research Engineer / Senior-Staff ML Engineer |
| Domain | Embedded ML — audio + multimodal ("Omni") on-device inference |
| Function | Build (research-to-production embedded model engineering) |
| Seniority | MTS = Senior/Staff-equivalent individual contributor at Liquid AI |
| Remote | Not confirmed on this specific posting; strongly likely onsite San Francisco (Liquid AI's consistent pattern across all its "Embedded/Audio/Omni" and multimodal reqs) |
| Team size | Not disclosed |
| TL;DR | Embedded ML engineering role building on-device audio and multimodal ("Omni") inference at a frontier foundation-model startup — the closest verbatim keyword match to this candidate's real-time embedded audio background in Liquid AI's entire slate of open roles. |

## B) Match with CV

| JD requirement (inferred from title + Liquid AI's embedded/audio req pattern) | CV evidence |
|---|---|
| Embedded / on-device ML engineering | MAS Holdings: C++/Python real-time inference engines on embedded/IoT hardware, 5 years production; JAES 2026: 14ms inference on Raspberry Pi 4, 74× faster than DTW baseline |
| Audio-domain ML | MUSMET postdoc (EU-funded, University of Trento): real-time audio pattern detection, <30ms @ >90% F1; JAES 2026, DAFx 2022 (audio/symbolic pattern detection); McGill visiting researcher: multimodal sensor + gesture detection |
| Multimodal ("Omni") modeling | IEEE Internet of Sounds 2025: guitar gesture detection integrating motion + audio; McGill diffusion/VAE synthetic data for multimodal robustness |
| Latency/compute-constrained inference | Core Competencies: Real-Time / Low-Latency Inference; benchmark suites (baselines + ablations) under compute constraints (MUSMET) |
| C++ systems engineering | MAS Holdings: C++ real-time inference engines; Technical Stack lists C++, C |
| Research rigor at a frontier-model company | PhD (Trento), 10 peer-reviewed publications, ORCID/ResearchGate profile, experimental design & ablation methodology |

**Gaps:**
1. **Foundation-model / LFM architecture experience** — Liquid AI's core product is Liquid Foundation Models (LFMs); the resume shows no direct LFM/SSM-style architecture work. *Hard blocker?* No — this is a systems/embedded-deployment role, not core architecture research; adjacent experience (novel real-time architectures under MUSMET) covers it. *Mitigation:* cover letter should frame MUSMET's custom real-time detector work as "designing and deploying novel architectures under hard latency constraints," the same skill Liquid AI needs for embedding LFMs on-device.
2. **US work authorization** — candidate is a Canadian PR, not US-authorized; SF onsite would require employer visa sponsorship. *Hard blocker?* Not automatically — this project's history shows Liquid AI's sibling SF-onsite audio role (MTS Multi-Modal Audio, 4.1/5) was applied to without a visa rule-out, suggesting either unconfirmed sponsorship or the risk was accepted. *Mitigation:* confirm sponsorship availability before investing further (cover letter, interview loop) — flag explicitly to candidate, do not assume.
3. **Large-scale distributed training** — no evidence of multi-GPU/cluster-scale training experience. *Nice-to-have* for an embedded-inference-focused role, not core to the job.

## C) Level and Strategy

1. **Level detected:** MTS at Liquid AI is a flat, senior-IC title (no separate "Senior/Staff" ladder disclosed) — natural fit for a PhD + 10-year candidate targeting Senior/Staff ML Engineer roles.
2. **Sell senior without lying:** Lead with the JAES 2026 result (14ms on Raspberry Pi 4, 74× faster than baseline) as direct proof of embedded-audio inference optimization at the exact intersection Liquid AI needs. Pair with MAS Holdings' 5-year track record shipping C++ inference on production embedded hardware at scale — this is systems maturity most audio-ML researchers lack.
3. **If downleveled:** Liquid AI's MTS title is already the standard IC band; unlikely to be downleveled. If comp lands below range, negotiate using the JAES 2026 + DAFx 2022 dual publication record and MAS Holdings' quantified throughput/efficiency results as leverage.

## D) Comp and Demand

| Source | Data |
|---|---|
| Sibling Liquid AI role (Post-Training, Applied — Audio), Glassdoor | $130,000–$200,000 base (San Francisco) |
| Sibling Liquid AI role (GPU Performance Engineer), Glassdoor | $178,000–$234,000 base |
| Sibling Liquid AI role (Applied ML Lead), Ladders | $136,700–$241,500 |
| This specific req | Not disclosed; estimate **$150K–$220K USD** base by analogy to sibling audio/embedded reqs, plus equity (unicorn-stage) and 100% medical/dental/vision premium coverage per company benefits pattern |

No confirmed layoff or hiring-freeze signal found for Liquid AI as of this search (2026-08). Company continues actively posting across audio, multimodal, embedded, and infra tracks — consistent with active, well-funded hiring, not a freeze.

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---------|---------------|------------------|-----|
| 1 | Tagline | "Machine Learning Research Engineer \| Deep Learning, Time-Series, Pattern Detection \| Applied ML" | "Machine Learning Research Engineer \| Embedded & Real-Time Inference, Signal Processing, Edge AI \| Applied ML" | Matches the literal "Embedded" + on-device framing in the job title; body content already supports it |
| 2 | Professional Summary | Generic ML engineer framing | Lead with embedded/on-device inference result (14ms RPi4) and audio-domain publications in the first two sentences | Surfaces the single most relevant proof point immediately |
| 3 | Core Competencies | Domain Expertise lists Time-Series first | Reorder to lead with Signal Processing/DSP and Embedded Systems | ATS and human skim relevance |
| 4 | Experience bullets | As-is | No changes needed — MAS Holdings and MUSMET bullets already speak directly to embedded + audio + real-time | Body substance doesn't need editing, only framing |
| 5 | LinkedIn headline | Not reviewed | Mirror the swapped tagline | Consistency across channels |

**Top 5 CV changes:** tagline swap (above), summary opening reorder, competency reorder — all framing, zero fabricated content.
**Top 5 LinkedIn changes:** headline swap to match; pin JAES 2026 publication; feature MUSMET postdoc project card with the 14ms/74× metric; add "Embedded ML" and "Edge AI" as skills; request a MUSMET or MAS Holdings recommendation emphasizing real-time delivery.

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Embedded/on-device inference | JAES 2026 real-time detector | MUSMET needed real-time pattern detection on constrained hardware | Design a detector meeting <30ms/>90% F1 on embedded-class devices | Built and benchmarked custom lightweight architecture, validated on Raspberry Pi 4 | 14ms inference, 74× faster than DTW baseline, published | Learned that hardware-aware design decisions early (not post-hoc optimization) are what make embedded ML tractable |
| 2 | Audio + multimodal ("Omni") | Guitar gesture + music pattern fusion (I3DA 2025) | Extend guitar control beyond audio-only input | Integrate gesture (motion) sensing with musical pattern recognition | Built multimodal pipeline fusing sensor + audio streams | Presented at IEEE Internet of Sounds; validated extended control use case | Reflected that multimodal fusion needs careful synchronization/latency budgeting across modalities — directly relevant to "Omni" scope |
| 3 | Production embedded C++ at scale | MAS Holdings fabric/care-label QC systems | Manual inspection was slow and inconsistent at manufacturing scale | Automate visual QC via camera + embedded inference | Built and deployed C++/OpenCV inference on production camera hardware across sites | 300% throughput improvement, 99.5% inspection-time reduction | Learned to design for operational reliability (monitoring, quality checks) not just model accuracy |
| 4 | Research rigor / benchmarking under constraints | MUSMET benchmark suite design | Needed to compare architectures fairly under compute constraints | Design baselines + ablations isolating latency/accuracy trade-offs | Built reproducible benchmark suite guiding system-level architecture decisions | Directly informed which architecture shipped in the final real-time system | Benchmark-first discipline transfers directly to evaluating LFM-on-device trade-offs |
| 5 | Limited-label / synthetic data for robustness | McGill diffusion/VAE synthetic data | Real gesture-detection data was scarce | Generate synthetic training data to improve robustness | Implemented diffusion- and VAE-based synthetic generation, evaluated downstream impact | Findings directly shaped deployment decisions | Learned synthetic data augmentation must be validated against real-world distribution shift, not just added blindly |
| 6 | Working at a fast-moving frontier-model startup | Independent Researcher / Nebula OSS release | Existing C++ feature-extraction tooling for sequential data was fragmented | Build and release an open-source library solo | Designed, implemented, and published Nebula (C++17) | Released as open source; used as basis for 3 further publications | Comfortable operating independently and shipping production-quality tooling without a large team |

**Recommended case study:** JAES 2026 (14ms RPi4 real-time audio detector) — directly mirrors "embed a model on real hardware under a latency budget," the core of this role.

**Red-flag questions:**
- *"Why are you looking to leave academia/postdoc for a startup?"* → Frame as returning to industry deliberately: the PhD/postdoc was purposeful depth (real-time signal processing, embedded ML) to build better production systems, not an exit from industry — candidate started in industry (MAS Holdings) and is returning with sharper tools.
- *"Do you have LFM/SSM-specific architecture experience?"* → Be honest: no direct LFM experience, but direct experience designing and shipping novel real-time architectures under hard latency/hardware constraints — the transferable skill this role needs.
- *"Are you eligible to work in the US, or would we need to sponsor?"* → Answer directly: Canadian PR, not US-authorized; would require sponsorship — raise this proactively rather than let it surface as a late-stage surprise.

## G) Posting Legitimacy

**Assessment:** Proceed with Caution

| Signal | Finding | Weight |
|---|---|---|
| Posting freshness | ~1 week old per LinkedIn cross-post (as of search) | Positive |
| Description quality | Could not access full JD text (Ashby SPA blocked WebFetch); title itself is specific and non-generic ("Embedded ML Engineer (Audio/Omni)"), not boilerplate | Neutral |
| Company hiring signals | No layoffs/freeze found for Liquid AI in 2026 (broad AI-industry layoff wave found instead, unrelated to this company); Liquid AI has 18+ open roles currently listed on Glassdoor, spanning audio, multimodal, infra, and applied ML | Positive |
| Reposting detection | Not a repost — distinct from previously-seen Liquid AI reqs (MTS Multi-Modal Audio #333, MTS Post-Training Applied Audio #334, MTS ML Research Engineer VLM Data #229) in this project's scan history | Neutral |
| Role market context | Embedded/on-device ML engineer at a well-funded frontier-model startup with an active, broad hiring slate — plausible genuine need, not a common long-standing evergreen posting pattern | Positive |

**Context notes:** Could not directly verify JD text or confirm onsite-vs-remote status on this specific req (Ashby SPA); location inferred from a LinkedIn cross-post showing San Francisco, CA, consistent with Liquid AI's other Bay Area engineering roles. Recommend a direct visit to the Ashby link before applying to confirm exact requirements and any remote/relocation language.

---

## Keywords extracted (ATS optimization)

Embedded ML, On-Device Models, Audio, Multimodal, Omni, Member of Technical Staff, Real-Time Inference, Low-Latency, Edge AI, Signal Processing, DSP, C++, Foundation Models, Model Compression, Benchmarking, Ablations, Hardware-Aware Optimization, San Francisco, Frontier AI Lab, Systems Engineering, Production Deployment
