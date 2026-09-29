# Evaluation: Perceptive Space — ML Scientist, All Levels

**Date:** 2026-07-07
**URL:** https://perceptive-space-systems-inc.breezy.hr/p/399654796260-ml-scientist-all-levels
**Archetype:** Applied Scientist (hybrid: ML Research Engineer)
**Score:** 4.3/5
**Legitimacy:** Proceed with Caution (long-running/evergreen posting; company itself checks out)
**Verification:** Active via WebFetch 2026-07-07 (title + JD + apply present; Playwright not used this session)
**PDF:** pending

---

## A) Role Summary

| Field | Value |
|-------|-------|
| Archetype | Applied Scientist / ML Research Engineer |
| Domain | ML for space weather forecasting — temporal/scientific data |
| Function | Build (research → production) |
| Seniority | All levels (2+ yrs min; senior welcome) |
| Remote | Fully remote, Canada only |
| Team size | Very small (~5-10; pre-seed startup, remote-first: Toronto/Oakville/LA/Norway) |
| Comp | Not disclosed; benefits + stock options |

**TL;DR:** Pre-seed Toronto space-weather startup wants a deep-learning scientist for sequential/temporal forecasting models, taking research to production on cloud infra — a near-direct hit on Nishal's time-series + sensor + research-to-production core.

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|----------------|-------------|-------|
| DL for sequential/temporal data | Time-series modeling core skill; RNN real-time detectors (JAES 2026); IoT time-series at MAS (millions of events/day); Forestpin time-series anomaly detection | ✅✅ Exceptional |
| Transformers, attention, representation learning | HuggingFace Transformers in stack; embeddings/representation learning listed; but flagship published work is RNN/DSP, not transformer-based | ⚠️ Partial |
| ML infrastructure: cloud, Airflow, Docker | AWS (EC2/S3/ECS/MWAA/RDS), Apache Airflow, Docker, Kubernetes, MLFlow — exact tool match (MWAA *is* managed Airflow) | ✅✅ Exact |
| Research → production transition | Career thesis: MUSMET postdoc prototypes → documented production deployments; MAS research → factory floor | ✅✅ Exceptional |
| Validation strategies, performance metrics for operational systems | Benchmark-first methodology: baselines, ablations, F1/latency trade-off suites | ✅✅ Exceptional |
| Advanced technical degree | PhD (Information Eng & CS) + MSc + BEng (Electronic Eng) | ✅ |
| 2+ yrs industry DL experience | 10+ yrs | ✅ |
| Startup mindset, high ownership | Solo-owned full pipelines (MUSMET); consultant delivery (Forestpin); intrapreneurial systems at MAS | ✅ |
| AI-assisted coding tools | Runs an AI-agent job pipeline; daily AI-tooling user — demonstrable but not on CV | ⚠️ Add to CV |
| Nice: C/Rust/performance languages | C++ and C, real-time engines — direct hit | ✅ (nice-to-have) |
| Nice: aerospace & defence | None. But space weather = solar/geomagnetic **sensor time-series forecasting**, structurally identical to his sensor-fusion + signal-processing work | ⚠️ Bridgeable gap |
| Nice: early-stage startup | Forestpin (small consultancy), no true early-stage employee stint | ⚠️ Minor |

**Gaps + mitigation:**
1. **Transformers depth** — not a hard blocker (JD says "proficiency," role is all-levels). Mitigation: cite HF Transformers use + sequential-modeling depth; frame RNN-vs-DTW benchmarking as architecture-selection rigor: "I choose the architecture the constraints justify." Optional: small temporal-transformer demo on a public space-weather dataset (OMNI/Kp index) — 1-2 day project, would be a killer application artifact.
2. **Aerospace domain** — nice-to-have only. Mitigation: physics-informed framing — MSc/BEng in electronic engineering + DSP = comfort with physical sensor data; space weather is time-series from instruments, his native format.
3. **AI-assisted coding** — trivially covered; state it explicitly in CV/CL.

## C) Level and Strategy

- **JD level:** "All levels" — they'll level on interview performance.
- **Natural level:** Senior Applied Scientist. 10 yrs + PhD + production record.
- **Sell senior:** lead with end-to-end ownership (acquisition → deployment → monitoring = their exact pipeline need); 14ms/74× optimization story; benchmark-suite design (their "validation strategies" bullet is his specialty).
- **If downleveled:** pre-seed = flat titles anyway; negotiate equity + 6-month review instead of title.

## D) Comp and Demand

| Item | Data | Source |
|------|------|--------|
| Company funding | Pre-seed US$2.8M / C$3.9M (2024), led by Panache Ventures; emerged from stealth 2024 | VentureBeat, SpaceNews, BetaKit |
| Founder | Padmashri Suresh (PhD, NASA fellowship, space weather modeling) | BetaKit |
| Salary for this role | Not disclosed ("based on seniority + location"); stock options + full benefits | JD |
| Market anchor | ML/AI engineer Canada avg ~C$161-173K; pre-seed typically pays below market + equity | Pin.com 2026 benchmarks |
| Realistic expectation | ~C$110-150K + meaningful options | inference — no company-specific data exists |

Pre-seed comp will likely land below the $140K+ senior target; equity and domain uniqueness are the compensators. Within stated floor.

## E) Customization Plan (top changes)

| # | Section | Change | Why |
|---|---------|--------|-----|
| 1 | Headline | "ML Scientist — Time-Series Forecasting & Real-Time Sensor ML" | Mirror JD language |
| 2 | Summary | Lead with temporal/sequential DL + research-to-production; name Airflow/Docker/AWS explicitly | Their 3 core asks in first 3 lines |
| 3 | Skills | Add "AI-assisted development (Claude Code, agentic pipelines)" | Explicit JD requirement, unusual to see |
| 4 | MAS bullets | Reframe IoT ingestion as "high-frequency sensor time-series forecasting + anomaly detection across distributed sites" | Space weather = same shape of problem |
| 5 | McGill | Emphasize spatio-temporal multimodal sensor modeling + synthetic data for sparse-label regimes | Space weather data is sparse/irregular — direct relevance |

LinkedIn: same headline swap; pin JAES paper + Zenodo datasets; add "time-series forecasting" and "transformers" to skills.

## F) Interview Plan (STAR+R selection)

| # | JD Requirement | Story | R (result) | Reflection |
|---|----------------|-------|------------|------------|
| 1 | Temporal DL in production | MUSMET real-time pattern detection | 14ms RPi4, 74× vs DTW, JAES 2026 | Architecture choice must follow deployment constraints, not fashion |
| 2 | Research → production | MUSMET prototype → documented deployment | Production-grade components + reproducible pipelines | Docs/reproducibility are the product, not overhead |
| 3 | Validation strategy design | Benchmark suites w/ baselines + ablations | Quantified architecture/feature trade-offs | Metrics chosen before models, not after |
| 4 | ML pipelines/infra | MAS real-time ETL, millions of IoT events/day | 300% efficiency; distributed sites | Boring reliability beats clever models at scale |
| 5 | Ownership/startup pace | Forestpin consulting: reqs → production scoring services solo | Shipped compliance/risk pipeline | Small-team speed = ruthless scoping |
| 6 | Sparse/noisy scientific data | McGill synthetic data (diffusion+VAE) | Improved robustness under limited labels | Data strategy often beats model strategy |

**Case study to present:** JAES 2026 end-to-end — problem framing → data (own Zenodo datasets) → architecture comparison → hard-constraint optimization → publication. Maps to every JD bullet.
**Red-flag questions:** "No aerospace background?" → "Space weather is sensor time-series with physics underneath — that's been my data format for a decade; domain physics is learnable, engineering judgment isn't." "Why a tiny startup after a postdoc?" → ownership + speed narrative.

## G) Posting Legitimacy

**Assessment: Proceed with Caution**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply state | Active — title + JD + apply button (WebFetch 2026-07-07) | Positive |
| Description quality | Specific tech (transformers, Airflow, Docker), clear scope, real domain | Positive |
| Company reality | Funded (C$3.9M 2024), named investors, credible founder, press coverage | Positive |
| Salary disclosure | Absent ("based on seniority") | Neutral (typical pre-seed) |
| Reposting | Same/similar "Machine Learning Scientist" posting live since **May 2025** (Remotive) — 13+ months | Concerning |
| Layoffs/freeze | None found (Glassdoor "Perceptive" layoff hits = different company) | Positive |
| "All Levels" title | Wide-net/evergreen pattern | Neutral-Concerning |

**Context notes:** 13-month open ML role at a 5-10 person startup = either evergreen pipeline, very high bar, or funding-gated hiring. Not a ghost-job profile (company too small and too real), but calibrate: application may sit until they're ready. Cold outreach to the founder matters more than the form here.

---

## Keywords extracted

machine learning scientist, deep learning, time series, temporal data, sequential data, transformers, attention mechanisms, representation learning, forecasting, space weather, spatio-temporal, ML pipelines, model validation, performance metrics, Airflow, Docker, cloud platforms, AWS, production ML, startup, ownership, AI-assisted coding, C, Rust, aerospace
