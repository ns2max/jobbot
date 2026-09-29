# Evaluation: Audimee — Audio Machine Learning Engineer (Machine Learning Developer)

**Date:** 2026-08-05
**URL:** https://careers.audimee.com/jobs/7167136-audio-machine-learning-engineer-machine-learning-developer
**Archetype:** Research Scientist (audio/MIR) / ML Research Engineer — hybrid
**Score:** 3.6/5
**Legitimacy:** Proceed with Caution
**Verification:** WebFetch-confirmed (batch mode — no browser tool available this session); JD content retrieved successfully, role-specific and detailed
**PDF:** pending (generate-pdf.mjs script is missing from this repo — CV delivered as Markdown only)

---

## A) Role Summary

| Field | Value |
|---|---|
| Archetype | Research Scientist / ML Research Engineer (audio-generative hybrid) |
| Domain | Generative audio ML — singing voice synthesis (SVS) and voice conversion |
| Function | Build (model R&D + production integration) |
| Seniority | Mid-Senior ("strong experience as ML Developer"; Master's minimum) |
| Remote | Fully remote, restricted to GMT−3 to GMT+4 hire band |
| Team size | Not disclosed (small startup signal) |
| TL;DR | A remote, early-stage voice-tech startup wants a PyTorch engineer to build and productionize diffusion-based singing-voice-synthesis and voice-conversion models — deep generative-audio fit, but the specific SVS/vocoder subdomain is new territory for this candidate. |

## B) Match with CV

| JD Requirement | CV Evidence |
|---|---|
| Python, PyTorch | Primary language across all roles; PyTorch listed in ML/AI stack (knowledge-graph.md) |
| Diffusion-based generative audio models | McGill visiting researcher: diffusion-based + VAE-based synthetic audio generation for limited-label regimes |
| Audio feature extraction pipelines | MFCC, STFT, S-transform, Librosa/SciPy pipelines; MUSMET postdoc feature-engineering ownership |
| Working with large vocal/audio datasets | Designed and published DoMP/DoPP/DoDP/DoDP2 — 7,000+ recordings, 70 musicians (Zenodo) |
| Model quality/robustness/inference-speed optimization | JAES 2026: 14ms inference, F1=0.76, 74× faster than DTW baseline; benchmark-first methodology (baselines + ablations) |
| Production integration | MUSMET: models integrated into live on-stage production systems; MAS Holdings: C++/Python real-time inference engines in production |
| Master's degree (minimum) | PhD — exceeds requirement |
| Bonus: music/audio background | Performing/recording guitarist; entire research career embedded in music technology |

**Gaps:**

1. **Singing voice synthesis (SVS) and voice conversion specifically** — Hard requirement, not a nice-to-have; this is the core deliverable of the role.
   - Hard blocker or nice-to-have? Significant gap, not an absolute blocker — it's a generative-audio *subdomain* gap, not a total domain mismatch.
   - Adjacent experience? Yes — diffusion/VAE generative audio (McGill), deep audio feature engineering, and MIR pattern modeling on vocal-adjacent monophonic/polyphonic material (DoMP/DoPP) transfer partially.
   - Portfolio coverage? No project directly does SVS or voice timbre conversion.
   - Mitigation: cover letter should be explicit that the generative-modeling and audio-DSP foundations transfer, and propose a fast ramp-up (cite the McGill diffusion/VAE work as the closest precedent), rather than implying direct SVS experience.

2. **Neural vocoders (HiFi-GAN-style)** — No direct experience.
   - Nice-to-have relative to #1, but named explicitly in the JD.
   - Adjacent: real-time audio signal reconstruction/DSP background (JUCE, Elk Audio OS, S-transform) is conceptually close to vocoder work.
   - Mitigation: name specific vocoder papers/architectures studied if asked in interview; do not overstate.

3. **Timezone window (GMT−3 to GMT+4)** — Toronto is GMT−4 (EDT, summer) to GMT−5 (EST, winter): inside the window in summer, ~1 hour outside the floor in winter.
   - Not a hard blocker; worth a direct, upfront question rather than silently assuming compatibility.

## C) Level and Strategy

1. **Level detected:** JD says "strong experience as a Machine Learning Developer" with a Master's minimum — reads as mid-to-senior IC, not a research-lab title. Candidate's natural level (PhD + 10 yrs + 10 publications) is above this bar.
2. **Sell senior without lying:** Lead with production-grade inference optimization (14ms, 74×) and dataset-scale experience (7,000+ recordings) rather than publication count — a startup wants a builder, not primarily a researcher. Frame the PhD as "shipped real-time audio models at 14ms" credibility, not academic distance.
3. **If they downlevel or question seniority:** Unlikely — the fit risk here is domain (SVS specifically), not seniority. If comp reflects a more junior band, negotiate based on production-ML delivery record, not title.

## D) Comp and Demand

| Source | Data |
|---|---|
| JD | "Competitive compensation based on experience" — no range disclosed |
| Market (Glassdoor/industry aggregates, 2026) | Voice AI specialists: $39–$60/hr median; senior voice AI engineers: $150K–$300K total comp; AI engineer base salaries averaging ~$206K (general AI, not voice-specific); senior voice AI contractors $200–$400/hr |
| Assessment | Early-stage voice-tech startups typically compensate below these broader-market medians in base, sometimes offset with equity — no confirmation Audimee does either. Given profile's $80K–$220K CAD target range and no disclosed figure, this is a **comp-risk unknown** — get a number before investing significant interview time. |

Sources: [AI Voice Engineer Hiring Market 2026](https://callsphere.ai/blog/vw9c-ai-voice-engineer-hiring-market-2026-salaries-comp), [Salary: AI Engineer in Remote 2026 | Glassdoor](https://www.glassdoor.com/Salaries/remote-ai-engineer-salary-SRCH_IL.0,6_IS12617_KO7,18.htm)

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---------|-----------------|------------------|-----|
| 1 | Tagline | Standard: "Machine Learning Research Engineer \| Deep Learning, Time-Series, Pattern Detection \| Applied ML" | **No change** | "Pattern Detection" plus the publication line already signals core audio-ML/MIR credentials; the JD doesn't reward an "embedded/edge" reframe |
| 2 | Summary | Generic ML summary | Foreground diffusion/VAE generative-audio work and Zenodo dataset scale in the first two sentences | Directly answers the JD's two named techniques (diffusion, large vocal datasets) |
| 3 | Core Competencies | Generic ML block | Add explicit "Generative Audio ML: diffusion, VAE" line | ATS keyword match for "diffusion-based generative audio models" |
| 4 | Experience bullets | Standard MUSMET/McGill bullets | Emphasize McGill diffusion/VAE bullet first, ahead of gesture-detection bullet | Puts the JD's #1 required technique at the top of relevant experience |
| 5 | Cover letter (if applying) | N/A | One paragraph directly naming the SVS/vocoder gap and proposing it as a fast, motivated ramp — honesty framing | Domain gap is significant enough that silence would read as evasive at interview |

Top 5 LinkedIn changes: mirror the above — headline stays as-is; About section should surface "diffusion-based generative audio" and dataset scale near the top.

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Diffusion/VAE generative modeling | McGill synthetic data generation | Limited labeled gesture+audio data for robust model training | Improve model robustness under label scarcity | Built diffusion-based and VAE-based synthetic data generators | Measurably improved downstream model robustness | Generative augmentation is a technique, not a domain — same math applies to vocal timbre space, just a different conditioning signal |
| 2 | Inference speed / model quality optimization | JAES 2026 RPi4 detector | Needed sub-30ms detection on embedded hardware | Hit real-time budget without sacrificing accuracy | Iterated benchmark suite (baselines + ablations), optimized architecture | 14ms, F1=0.76, 74× faster than DTW baseline | Optimization discipline (measure, ablate, don't guess) transfers directly to vocoder inference-speed work |
| 3 | Large-dataset audio ML | DoMP/DoPP/DoDP dataset design | No suitable public benchmark existed for musical pattern research | Needed a large, well-labeled audio dataset | Designed and published 7,000+ recordings from 70 musicians on Zenodo | Now a citable, reusable benchmark for the field | Understands dataset design trade-offs (label quality, coverage, size) that also govern vocal-conversion training data |
| 4 | Production integration | MUSMET live deployment | Research models needed to run reliably on stage in front of audiences | Zero-failure production integration | Built monitoring, documentation, reproducible pipelines | Models ran live in real performances without incident | Production-audio reliability bar (no silent failures) is the same whether the output is a pattern-detection flag or a synthesized voice |
| 5 | Audio feature engineering | MFCC/STFT/S-transform pipeline work | Needed frequency-domain features for onset detection | Build a training-free, accurate detector | Applied S-transform frequency-band splitting | Asilomar 2018 publication; still-cited technique | Comfortable working at the DSP/ML boundary, which vocoder work also requires |
| 6 | Honesty about domain gap (red flag question: "Have you worked on SVS/voice conversion before?") | — | — | — | — | — | Answer directly: no direct SVS work, but diffusion/VAE generative-audio fundamentals and DSP-level audio engineering transfer; name specific readiness (papers studied, willingness to ramp fast) rather than overselling |

**Recommended case study:** JAES 2026 (RPi4 real-time detector) — demonstrates the exact skill this role needs (deep learning + real-time audio + rigorous benchmarking), even though the output modality differs from SVS.

**Red-flag questions:**
- *"Why haven't you worked on voice conversion specifically?"* → Be candid; pivot to transferable generative-audio and DSP depth.
- *"Can you commit to overlap with GMT-3 to +4?"* → Confirm willingness to shift hours in winter (EST is ~1hr outside the floor); don't let this surface unprompted at offer stage.

## G) Posting Legitimacy

**Assessment:** Proceed with Caution

| Signal | Finding | Weight |
|---|---|---|
| Posting freshness | Not determinable via WebFetch (no posted date, no browser tool this session) | Neutral |
| Description quality | Highly specific — names diffusion models, HiFi-GAN-style vocoders, SVS, voice conversion explicitly; not generic boilerplate | Positive |
| Company existence | Confirmed real, shipping product — Audimee is an operating AI vocal-conversion platform for musicians/creators (independently verified via web search, not just the JD) | Positive |
| Compensation disclosure | None ("competitive compensation based on experience") | Neutral/Concerning (common for early-stage, but a risk to flag) |
| Team size / org context | Not disclosed | Neutral |
| Hiring-freeze/layoff signals | None found; too early-stage for typical layoff coverage | Neutral |
| Reposting detection | Not previously seen in `scan-history.tsv` under a different URL | Neutral |

**Context Notes:** Small, likely early-stage/pre-scale voice-tech startup — vague comp and thin org detail is typical at this stage and should not be read as a red flag on its own. The specificity of the technical requirements (diffusion, HiFi-GAN, SVS) is a strong positive signal that this is a real, currently-open technical need, not a placeholder listing.

---

## Keywords extracted

Machine Learning Developer, Audio Machine Learning Engineer, Python, PyTorch, singing voice synthesis, voice conversion, diffusion-based generative models, neural vocoders, HiFi-GAN, audio feature extraction, vocal datasets, model inference speed, model robustness, production integration, remote, GMT timezone band, Master's degree, music production, vocals, audio engineering, scalable Python code
