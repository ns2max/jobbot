# User Profile Context — career-chuck

<!-- NISHAL STANISLAUS SILVA, PhD — Toronto, ON
     This is the personal layer. System logic lives in modes/_shared.md.
     Customize archetypes, narrative, framing, comp, location policy here. -->

## Target archetypes

| Archetype | Thematic axes | What they buy |
|-----------|---------------|---------------|
| **Senior / Staff ML Engineer** | End-to-end pipelines, real-time inference, embedded deployment, audio/CV/time-series | Someone who ships production ML at scale with measurable impact |
| **ML Research Engineer** | Applied research, experimental design, benchmarking, signal processing | Bridges rigorous research and production engineering |
| **Applied Scientist** | Proof-of-concept to production, ablation methodology, domain-specific ML | Goes from hypothesis to deployed system with metrics |
| **Research Scientist** | MIR, audio/signal processing, pattern recognition, time-series | Deep domain expertise; publishes and builds |
| **AI/ML Technical Lead** | Team enablement, system design, research-to-production translation | Leads technical direction and mentors engineers |
| **Solutions Architect (AI/ML)** | End-to-end architecture, multi-modal systems, cloud + embedded | Designs integrated AI systems from sensor to inference |
| **Assistant/Adjunct Professor (AI/ML)** | Teaching, curriculum design, applied research supervision, grant-funded projects | PhD + postdoc + published record who can also ship production systems, not just theory |
| **AI/ML Consultant** | Short-cycle diagnosis, prototype-to-decision, client-facing technical advisory | Fast, credible outside expert who de-risks AI bets with working prototypes and benchmarks |
| **K-12 STEM/CS Teacher** | Curriculum design, robotics/coding instruction, student mentorship | PhD-level technical depth brought down to secondary/middle-school STEM/CS programs |
| **College/Polytechnic Instructor** | Applied curriculum (ML/AI/CS), industry-informed teaching, smaller cohort mentorship | Industry + research background translated into practical, career-focused instruction |

## Adaptive framing — proof points by archetype

| If the role is... | Emphasize... | Proof points |
|-------------------|--------------|--------------|
| **Senior / Staff ML Engineer** | End-to-end pipeline ownership, real-time inference at scale, multi-domain delivery | MAS Holdings CV (300% throughput, 99.5% inspection time reduction); JAES 2026 (F1=0.76, 14ms RPi4); Forestpin anomaly detection |
| **ML Research Engineer** | PhD-trained rigor + production instinct; embedded ML; published benchmarking methodology | JAES 2026 (74× faster than DTW baseline); DAFx 2022 (SSIM, training-free, 95% accuracy); DoMP/DoPP/DoDP Zenodo datasets |
| **Applied Scientist** | Hypothesis → system → metrics pipeline; low-resource ML; ablation and experimental design | JAES 2026 (polyphonic detection <30ms RPi4); IEEE I3DA 2025 (p<.05 coherence improvement); SSIM (training-free detection) |
| **Research Scientist** | Deep MIR / signal-processing expertise; EU-funded postdoc; peer-reviewed publication record | MUSMET EU postdoc (Univ. Trento); JAES 2026; DAFx 2022; IEEE I3DA 2025; Zenodo open datasets (7,000 recordings, 70 musicians) |
| **AI/ML Technical Lead** | Industry → research → industry arc; translating ambiguous problems to specs; multi-domain track record | MAS Holdings (CV across manufacturing lines); MUSMET postdoc (real-time inference pipeline); COVID-19 IoT (recognized by Govt. Medical Officers' Assoc. of Sri Lanka) |
| **Solutions Architect (AI/ML)** | Multi-modal system design (audio + CV + IoT + sensor); embedded-to-cloud architectures; full integration ownership | IoMusT concert ecosystem (IEEE I3DA 2025); MAS Holdings fabric + care-label + garment-print pipelines; COVID-19 IoT remote patient monitoring |
| **Assistant/Adjunct Professor (AI/ML)** | Published research record, EU-funded postdoc, ability to design + teach signal processing / ML curriculum | JAES 2026, DAFx 2022, IEEE I3DA 2025, MUSMET EU postdoc (Univ. Trento), Zenodo open datasets |
| **AI/ML Consultant** | Rapid prototyping, cross-domain diagnosis (audio/CV/embedded), benchmark-driven recommendations, client delivery under tight timelines | MAS Holdings (300% throughput in live client environment); JAES 2026 (rapid embedded benchmarking); MUSMET (delivered under EU grant constraints) |

## Exit narrative

**The arc:** Started in industry building production ML and computer vision at scale — MAS Holdings, where CV automation delivered **300% throughput improvement** and **99.5% reduction in inspection time** across manufacturing lines. PhD for depth in real-time signal processing, embedded ML, and Music Information Retrieval. Postdoc on the **EU-funded MUSMET project** at the University of Trento — inference at **<30ms on Raspberry Pi 4**, 74× faster than the DTW baseline. Now returning to industry to build high-impact applied ML at the intersection of research and production engineering.

**Deployment:**
- **PDF Summaries** → open with the industry → research → industry arc. The PhD is purposeful depth, not a detour.
- **STAR stories** → MAS Holdings (manufacturing scale, hard constraints) or MUSMET postdoc (research rigor under latency constraints). Proof-point metrics as the "Result."
- **Interview opener** → *"I went into the PhD specifically because I wanted to understand the research deeply enough to build better production systems. I wasn't stepping away from industry — I was going back to get sharper tools."*
- **Research-heavy roles** → lead with JAES 2026 + DAFx 2022. Frame publications as proof of methodology.
- **Industry / product roles** → lead with MAS Holdings metrics. PhD = sharper tools.

## Document generation rules (resumes + cover letters)

- **LaTeX only.** Every resume and cover letter is produced as a `.tex` file, built from `input/cv-template.tex` and `input/coverletter-template.tex`. No Markdown, no HTML, no PDF output unless explicitly asked.
- **Source of truth:** `input/knowledge-graph.md` (full refresh 2026-09-03). Read it, not the old variant files. `input/knowledge-graph-old.md` is retired — ignore.
- **Job posting link** goes at the very top of each `.tex` file, but **commented out** (`% Job posting: <url>`).
- Pick exactly ONE variant (V1–V6, see template header / KG §15.1). Do not mix rows. Emit a short changelog with each doc: variant, why, what was cut, page count.
- Never write ">90% F1" — cite F1 = 0.76 (KG §16). Verified numbers before self-reported ones.
- Never mention the Promptly patent (Nishal is not a listed inventor).
- Output files: `output/{num}-{company-slug}-{role-slug}.tex` and `output/{num}-{company-slug}-{role-slug}-coverletter.tex`.

## Cross-cutting advantage

Frame as: **"Real-time ML systems engineer with published research proof and industrial-scale delivery."**

Rare combination:
- **Low-latency / embedded ML** — 14ms inference on Raspberry Pi 4
- **Academic depth + production instinct** — PhD + postdoc without losing the "ships things" muscle (300% throughput at MAS)
- **Signal-native** — audio, CV, sensor, time-series. Most ML engineers specialize in one; you have all four with deployed systems
- **Benchmark-first methodology** — F1, SSIM, coherence, ablations. Measure, don't guess
- **Multi-constraint engineering** — embedded hardware, live production, EU research deliverables, pandemic conditions

**One-line bio:**
> *"PhD ML Research Engineer who has shipped real-time inference at <30ms on embedded hardware and delivered 300% throughput gains in live manufacturing — now bringing that combination back to industry."*

## Public artifacts

| Asset | URL | Best for |
|-------|-----|----------|
| Portfolio | https://nishal.xyz | All roles |
| Research page | https://nishal.xyz/research.html | Senior MLE, Tech Lead, Solutions Architect |
| GitHub | https://github.com/ns2max | All roles |
| Nebula (C++17 audio-feature lib, ARM latency benchmarks) | https://github.com/ns2max/nebula | Edge/embedded, audio ML, C++ roles |
| LiveLaTeX (published VS Code extension) | https://marketplace.visualstudio.com/items?itemName=ns2max.livelatex | Dev-tools, shipping-software signal |
| ORCID | https://orcid.org/0000-0003-0406-7459 | Research-heavy |
| ResearchGate | https://researchgate.net/profile/Nishal-Silva-3 | Research-heavy |
| JAES 2026 | https://aes.org/publications/elibrary-page?id=23129 | ML Research Eng, Applied Scientist, Research Scientist |
| DAFx 2022 | https://dafx2020.mdw.ac.at/proceedings/papers/DAFx20in22_paper_18.pdf | Research Scientist, ML Research Eng |
| Zenodo datasets | https://zenodo.org/record/10818617 | Research Scientist, Applied Scientist |
| IEEE I3DA 2025 | https://ieeexplore.ieee.org/document/11202042 | Solutions Architect, Applied Scientist |
| MAS Holdings case study | https://nishal.xyz/research.html | Senior MLE, AI/ML Tech Lead |

**Sharing rules:**
- Audio / signal-ML roles → JAES 2026, DAFx 2022, Zenodo
- Industrial CV / production ML → MAS Holdings case study
- Research Scientist roles → full publications + Zenodo
- Every application → portfolio + GitHub

## Comp targets

**Ideal:** CAD $120K–$150K base. Flexible below for a strong role with clear progression. Soft benchmark (KG §16, provided 2026-09), NOT a hard filter — do not auto-penalize roles under $120K.

Market context (for negotiation, not for filtering):

| Role | Market range (CAD) | Notes |
|------|--------------------|-------|
| Senior ML Engineer (Toronto) | $140K–$188K base | Indeed avg $188K Toronto; GTA median $148K Levels.fyi |
| Applied Scientist (Senior) | $154K–$210K total comp | Amazon Canada AS L5: $209K total |
| Research Scientist (Senior) | $130K–$180K base | Product orgs higher than academia-adjacent |
| AI/ML Contractor (Senior) | $130–$200/hr | Embedded/real-time specialists exceed $150/hr |

When an offer lands near or above the ideal band, that is a positive comp signal — score accordingly.

## Location & visa
- **Base:** Toronto, ON, Canada
- **Status:** Canadian Permanent Resident — eligible to work in Canada without sponsorship
- **Modes:** open to onsite, hybrid, and remote
- **Relocation:** open within Canada with short notice
- **Scope (2026-08-20): Canada-only.** Only consider roles physically located in Canada, or explicitly Canada-remote. Non-Canadian roles (US, EU, APAC, etc.), including "remote" roles scoped to another country's workforce, are a **hard exclude** — do not evaluate, do not score, do not generate CV/report for them. This replaces the prior looser "flag <3.0" policy; it's now a filter, not a scoring penalty.
- **City preference ranking (highest to lowest):**
  1. Montreal, QC
  2. Toronto, ON
  3. Any other Canadian city (Vancouver, Ottawa, Calgary, Waterloo, etc.)
- Note preference rank in Block A (Role Summary) for every evaluated role so comparisons across offers are easy at a glance.
- Ambiguous/unlisted location on a posting ("Remote" with no country stated) → don't auto-exclude, verify via JD text or company hiring page before evaluating.
