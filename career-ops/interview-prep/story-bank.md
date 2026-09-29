# Story Bank — Master STAR+R Stories

This file accumulates your best interview stories over time. Each evaluation (Block F) adds new stories here. Instead of memorizing 100 answers, maintain 5-10 deep stories that you can bend to answer almost any behavioral question.

## How it works

1. Every time `/career-ops oferta` generates Block F (Interview Plan), new STAR+R stories get appended here
2. Before your next interview, review this file — your stories are already organized by theme
3. The "Big Three" questions can be answered with stories from this bank:
   - "Tell me about yourself" → combine 2-3 stories into a narrative
   - "Tell me about your most impactful project" → pick your highest-impact story
   - "Tell me about a conflict you resolved" → find a story with a Reflection

## Stories

<!-- Stories will be added here as you evaluate offers -->
<!-- Format:
### [Theme] Story Title
**Source:** Report #NNN — Company — Role
**S (Situation):** ...
**T (Task):** ...
**A (Action):** ...
**R (Result):** ...
**Reflection:** What I learned / what I'd do differently
**Best for questions about:** [list of question types this story answers]
-->

### [Pipeline Ownership] MUSMET Full ML Pipeline
**Source:** Report #656 — Reddit — Senior Machine Learning Infrastructure Engineer, Embedding Platform
**S (Situation):** EU-funded MUSMET project needed a real-time musical pattern detection pipeline built from raw sensor data to deployed inference.
**T (Task):** Own the full ML lifecycle: acquisition → signal processing → feature engineering → training/eval → edge deployment → monitoring.
**A (Action):** Designed and built each stage as a maintainable, documented, reproducible component; coordinated with academic and industry partners to harden research prototypes into production-grade components.
**R (Result):** Achieved <30 ms real-time inference on edge hardware (published: 14 ms, F1 = 0.76 on Raspberry Pi 4, JAES 2026).
**Reflection:** Pipeline reproducibility — not just model accuracy — is what actually survives handoff to other researchers/engineers.
**Best for questions about:** end-to-end ownership, "tell me about your most impactful project", production ML pipelines, research-to-production translation.

### [Benchmark Design] JAES 2026 RNN vs DTW Baseline
**Source:** Report #656 — Reddit — Senior Machine Learning Infrastructure Engineer, Embedding Platform
**S (Situation):** Needed real-time polyphonic pattern detection on resource-constrained embedded hardware (RPi4).
**T (Task):** Design an architecture and inference path that beat the existing DTW baseline on both accuracy and latency.
**A (Action):** Built and benchmarked an RNN-based detector with rigorous ablation testing against the baseline.
**R (Result):** 14ms inference, F1=0.76, 74x faster than the DTW baseline.
**Reflection:** Would formalize the benchmark harness earlier next time — it became the reusable asset, not the model itself.
**Best for questions about:** performance optimization, evaluation methodology, "describe a time you improved a system's efficiency."

### [Reliability at Scale] MAS Holdings IoT Pipelines
**Source:** Report #656 — Reddit — Senior Machine Learning Infrastructure Engineer, Embedding Platform
**S (Situation):** Manufacturing sites generated millions of IoT events per day across distributed locations with no unified ingestion.
**T (Task):** Build real-time ETL pipelines reliable enough for operational decision-making.
**A (Action):** Built and scaled ingestion and processing infrastructure across geographically distributed sites.
**R (Result):** Enabled real-time monitoring and long-term capacity planning at scale.
**Reflection:** Learned to design for partial failure — distributed sensor networks fail unpredictably, and the pipeline needed graceful degradation.
**Best for questions about:** distributed systems, scaling data infrastructure, handling failure modes.

### [Adoption & Trust] MAS Holdings CV Deployment
**Source:** Report #656 — Reddit — Senior Machine Learning Infrastructure Engineer, Embedding Platform
**S (Situation):** Fabric and care-label QC needed automated, reliable inspection replacing a manual process.
**T (Task):** Deploy CV models into live production with monitoring and human-in-the-loop fallback.
**A (Action):** Built and deployed inspection models with CI/CD and code-review practices to scale adoption across teams.
**R (Result):** 300% efficiency improvement, 99.5% inspection time reduction, 50% headcount reduction.
**Reflection:** Adoption required as much stakeholder trust-building as technical accuracy.
**Best for questions about:** driving adoption, human-in-the-loop systems, organizational change, quantified impact.

### [Systems Integration] Promptly RIP + PLC Integration
**Source:** Report #1405 — Crystal Fountains — Senior Software Developer
**S (Situation):** MAS/Twinery's on-demand direct-to-garment printing concept needed a vendor printer (closed RIP software, PLC-driven mechanics) to run inside an automated cell.
**T (Task):** Make vendor software, PLC triggers and a vision-based garment-alignment step work as one loop.
**A (Action):** Reverse-engineered PLC trigger points, built the RIP integration hooks, designed the geometry-alignment algorithm, and coordinated three closed-loop subsystems in custom C++.
**R (Result):** Promptly became a shipped product with facilities in the USA, Mexico, France and Sri Lanka.
**Reflection:** Documenting the vendor system's undocumented behaviour first saved every later integration.
**Best for questions about:** integrating with third-party/legacy systems, hardware-software integration, most commercially successful project.

### [Open Source / Data Tooling] Nebula + Zenodo Datasets
**Source:** Report #1406 — MobilityData — Software Developer
**S (Situation):** No lightweight ARM-ready audio-feature library with latency numbers; no public benchmark data for musical pattern detection.
**T (Task):** Build and publish reusable tooling and validated datasets.
**A (Action):** Wrote Nebula (C++17, per-feature ARM latency benchmarks, docs) and designed, validated and published four Zenodo datasets (70+ musicians).
**R (Result):** Public library (13 stars) and four DOI-backed datasets used in peer-reviewed work.
**Reflection:** Benchmarks in the README drew more users than the feature list; validation rules belong in code.
**Best for questions about:** open-source maintenance, data quality, documentation, community work.

### [Multi-partner Delivery] MUSMET Live Multisensory Concerts
**Source:** Report #1407 — Kelluu — R&D Project Manager
**S (Situation):** EU MUSMET needed two live concerts combining stage lights, smoke, 10 Meta Quest 3 headsets, haptic phones, musicians and partner hardware.
**T (Task):** Deliver working shows on fixed dates with 20 audience + 6 performer participants.
**A (Action):** Coordinated partners, built the Hot Licks Mapper routing tool, ran lighting (QLC+) and rehearsed failure paths.
**R (Result):** Both concerts ran; results published at IEEE I3DA 2025 (p < .05 coherence improvement).
**Reflection:** Rehearse the failure modes, not just the happy path.
**Best for questions about:** coordinating multi-vendor work, fixed-date delivery, live systems, stakeholder management.
