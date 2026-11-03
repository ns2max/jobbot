# Story Bank — Master STAR+R Stories

This file accumulates your best interview stories over time. Each evaluation (Block F) adds new stories here. Instead of memorizing 100 answers, maintain a set of deep stories that you can bend to answer almost any behavioral question.

**Last full rebuild:** 2026-10-16, from `ai-job-search/input/knowledge-graph.md` (canonical), the golden resume, the 7 stories already here, and the behavioural sections of the SciNet and Amii/ZeroKey preps. Every number below is in the knowledge graph. Anything marked **[fill in]** is a personal detail that isn't on record anywhere. Add it in your own words before you use the story. Don't let an interviewer hear a guess.

## How it works

1. Every time `/career-ops oferta` generates Block F (Interview Plan), new STAR+R stories get appended under **Stories** (bottom of the file)
2. Before your next interview, review this file — your stories are already organized by theme
3. The "Big Three" questions can be answered with stories from this bank:
   - "Tell me about yourself" → combine 2-3 stories into a narrative (scripts in §2)
   - "Tell me about your most impactful project" → pick your highest-impact story (S01 commercial, S09 technical)
   - "Tell me about a conflict you resolved" → find a story with a Reflection (S02, S08, S11; see §4 for the gaps)

**Prep routine (20 minutes the night before):** read the JD → pick the §2 opener that matches → circle 6 stories in the §1 matrix that match the JD's verbs → say each one aloud in under 2 minutes → read §5 guardrails.

---

## 1. Question → story matrix

Primary story first, backup second. Story IDs refer to the **Stories** section.

| Question type | Primary | Backup |
|---|---|---|
| Most impactful project | S01 Promptly | S09 RNN vs DTW 74× |
| Most technically challenging | S09 RNN vs DTW | S11 Multimodal sync pipeline |
| End-to-end ownership / prototype → production | S10 MUSMET pipeline | S02 Care-label QC |
| Shipped something people actually use | S01 Promptly | S05 COVID vitals |
| Improving performance / efficiency | S09 RNN vs DTW | S03 Fabric inspection |
| Working under hard constraints (latency, compute, power) | S03 Fabric inspection (5–6 s budget) | S13 Smart guitar |
| Driving adoption / getting users to trust a system | S02 Care-label QC | S14 User-centred evaluation |
| Human-in-the-loop design | S02 Care-label QC | S03 Fabric inspection |
| Integrating with legacy / third-party / closed systems | S06 Aeoon Kyo PLC integration | S01 Promptly RIP |
| Hardware–software integration | S06 Aeoon Kyo | S13 Smart guitar |
| Distributed systems / scale / reliability | S04 Sewing-floor IoT | S17 MIRaaS |
| Architecture decision / trade-off | S17 MIRaaS (edge vs server) | S20 VarianceEngine (5 candidates) |
| Evaluation methodology / benchmarks / ablations | S09 RNN vs DTW | S21 speakfrench (100k trials) |
| Data quality / building a dataset | S15 Zenodo datasets | S11 Multimodal sync |
| Learning something unfamiliar fast | S05 COVID vitals | S11 g.tec BCI integration |
| Crisis / urgent deadline | S05 COVID vitals | S12 Live concerts |
| Fixed-date delivery with many parties | S12 Live concerts | S10 MUSMET |
| Juggling priorities | S12 Live concerts | S10 MUSMET |
| Working with people outside your field | S11 g.tec + SAE Barcelona | S08 Forestpin auditors |
| Translating business needs into specs | S08 Forestpin | S02 Care-label QC |
| Stakeholder with unrealistic expectations | S02 Care-label QC | S08 Forestpin |
| Explaining technical work to non-experts | S19 MIDI Awards / demos | S07 MAS training seminars |
| Mentoring / teaching / raising the team's bar | S07 MAS CI/CD + training | S18 BSc supervision |
| Leadership without authority | S12 Live concerts | S07 MAS practice change |
| Failure / mistake / approach that didn't work | S16 SSIM → RNN pivot | S02 Care-label (scanner → camera → conveyor) |
| Changing your mind based on data | S16 SSIM → RNN pivot | S21 speakfrench (DTW lost to Wav2Vec2) |
| Rejection / setback | S23 Re-interview after "no hire" | S16 |
| Ambiguity / no clear spec | S01 Promptly | S20 VarianceEngine |
| Self-direction / initiative | S22 melodiq (closing a gap on purpose) | S15 Nebula |
| Open source / community | S15 Nebula + datasets | S19 Demos |
| Anomaly / risk detection | S08 Forestpin | S03 Fabric defects |
| Healthcare / safety-critical | S05 COVID vitals | S11 EEG pipeline |
| Generative AI / foundation models | S20 VarianceEngine | S21 speakfrench (Wav2Vec2) |
| Accessibility / education impact | S14 + P3c teaching/assistive thread | S18 |
| Why should we hire you | §2 opener for that sector + S01 + S09 | — |

---

## 2. "Tell me about yourself" — four openers (~90 seconds each)

Shape for every version: **present → two past proof points → why this role**. Close on the role, not on yourself.

### 2.1 Applied ML / ML Research Engineer (default)
> "I'm a machine learning research engineer with about ten years across industry and research, based in Toronto, a permanent resident, and available now. I build end-to-end ML systems: data in, model trained, deployed, and measured.
> I spent five and a half years at MAS Holdings, South Asia's largest apparel manufacturer, putting computer vision and IoT into production. One inspection system cut care-label checking from 15–20 minutes a label to 1–2 minutes a batch. I also built the alignment algorithm and the RIP integration for Promptly, which is now a commercial on-demand printing product with facilities in the US, Mexico, France and Sri Lanka.
> Then I did a PhD and postdoc at the University of Trento on real-time ML for time-series. My published system runs in 14 ms on a Raspberry Pi 4, 74 times faster than the baseline, in the Journal of the Audio Engineering Society this year.
> What I'm looking for is a team where the hard part is making ML work reliably in production, and that's what [role] is about."

### 2.2 Edge / embedded / on-device ML
Lead with the 14 ms / 31.4% CPU / RPi4 result, MIRaaS (where to split compute between edge and server), and Nebula's per-feature ARM latency benchmarks. MAS proof point: PLC-linked CV on the factory floor with a 5–6 s alert budget. Close: "I like problems where latency and power are the spec, not an afterthought."

### 2.3 Audio / music tech
Open with the guitar: "I've played guitar for over twenty years, Trinity Grade 8, fifteen-plus years in bands and sessions, and my PhD was teaching instruments to recognise what the player is doing in real time." Then JAES 74×, the smart guitar at McGill (F1 0.78), the MIDI Innovation Awards finalist, and four open datasets from 70+ musicians. Close on their product.

### 2.4 Industrial CV / manufacturing / IoT
Lead with MAS (V5 weighting): care-label QC (+300%), loom-side fabric inspection (−50% operators), sewing-floor IoT on three continents, Promptly. Then: "The PhD made me better at the part factories care about most: running reliably on small hardware in real time."

---

## 3. Stories

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

### S01 [Commercial Impact] Promptly — Two-Sided Prints on Finished Garments
**Source:** Knowledge graph §4.5.c, P16; Report #1405 — Crystal Fountains — Senior Software Developer
**S (Situation):** MAS/Twinery wanted on-demand direct-to-garment printing on *finished* garments. That meant a front and back print had to line up at the seams on a garment whose geometry changes every time it's laid down.
**T (Task):** Make two-sided prints align automatically, and connect the printer's software into the automated cell.
**A (Action):** Designed and prototyped the geometry-alignment algorithm: the camera captures the garment's geometry and the system calculates a per-side image warp so the prints meet at the seams (4–6 min per garment). Personally built the RIP (Raster Image Processor) integration that tied the printer into the automation loop. Consulted on the garment-flipping mechanism.
**R (Result):** Promptly became a commercial Twinery/MAS product with onshore facilities in the USA, Mexico, France and Sri Lanka. It's marketed as cutting production from ~90–180 days to 72 h–5 days, and Adore Me is a 5-year customer. It's the most commercially successful project you've been part of.
**Reflection:** The algorithm was the visible part, but the product only worked because the integration was solid. The unglamorous plumbing decides whether research ships.
**Best for questions about:** most impactful project, research → product, ambiguity, CV + hardware in one loop, "proudest achievement".
**Guardrails:** Never mention the patent: you're not a listed inventor. Algorithm details are under NDA, so say "calculated image warp from captured geometry" and stop there. Your roles were alignment algorithm, RIP integration, and mechanism consulting. Don't claim the whole product.

### S02 [Adoption & Iteration] Care-Label QC — Three Iterations to Production
**Source:** Knowledge graph P14; Report #656 — Reddit — Senior ML Infrastructure Engineer (as "MAS Holdings CV Deployment")
**S (Situation):** Care labels are multilingual and compliance-critical. Manual checking took 15–20 minutes per label.
**T (Task):** Automate verification so it was fast, trustworthy to operators, and compliant.
**A (Action):** Built OpenCV template + feature matching with an **explainable overlay**, so operators could see *why* a label failed instead of trusting a black box. Iterated the hardware three times: flatbed scanner → industrial camera → conveyor with PLC-driven reject. Kept all processing local for compliance. Added a human-in-the-loop fallback, CI/CD and code review so other teams could adopt it.
**R (Result):** 15–20 min/label → 1–2 min/batch; inspection time −99.5%; up to +300% operational efficiency.
**Reflection:** The first version worked technically but didn't fit the line. Operators adopted it once they could see the reasoning on the overlay. Trust was a feature I had to design, not a side effect of accuracy.
**Best for questions about:** driving adoption, human-in-the-loop, iterating with users, compliance constraints, quantified impact, early version that fell short.
**[fill in]:** One concrete moment from the floor, e.g. an operator objection or a QA lead who didn't trust it, and what you changed because of it. This turns it into a conflict/stakeholder story.

### S03 [Hard Real-Time CV] Loom-Side Fabric Defect Detection
**Source:** Knowledge graph P15
**S (Situation):** Structural fabric defects had to be caught at the loom, on rolls up to 60 inches wide, before the defect ran down the roll.
**T (Task):** Detect defects across the full width and alert within a 5–6 second budget.
**A (Action):** Designed a microscopic camera array with overlapping fields of view so the whole width was covered with no blind seams. Built the detection pipeline to fit the alert budget.
**R (Result):** In the pilot, the operators needed per loom fell by 50%.
**Reflection:** The latency budget came from the physics of the loom, not from an engineering preference. Starting from "how fast does the defect travel" set every design choice after that.
**Best for questions about:** latency constraints, CV system design, sensor layout, edge deployment in industry.
**Guardrails:** It was a pilot. Say "in the pilot".

### S04 [Reliability at Scale] Sewing-Floor IoT Across Three Continents
**Source:** Knowledge graph P24, §4.5.a–b; Report #656 — Reddit (as "MAS Holdings IoT Pipelines")
**S (Situation):** MAS had factories in South Asia, North America and Africa with heterogeneous sewing machines and no unified view of real-time productivity.
**T (Task):** Get reliable, real-time productivity data off mixed machine fleets at many distributed sites.
**A (Action):** Designed interfacing hardware for heterogeneous machines. Built real-time ingestion and ETL with quality checks and monitoring. Added repetitive-pattern tracking for operator efficiency, and changeover-optimization models predicting output, machine allocation and next-order layouts.
**R (Result):** A company-wide rollout supporting real-time monitoring and long-term capacity planning, at millions of IoT events per day across sites.
**Reflection:** Distributed sensor networks fail unpredictably. Design for partial failure and graceful degradation, not for the happy path.
**Best for questions about:** distributed systems, data pipelines, scaling, failure modes, time-series in production.
**Guardrails:** "Millions of events/day" is self-reported. Say it once and don't build on it. **[fill in]:** one specific failure (a site going offline, clock drift, a machine type that lied) and how the pipeline handled it.

### S05 [Crisis Delivery] COVID-19 Remote Vitals Monitoring
**Source:** Knowledge graph P23, §4.5.a
**S (Situation):** In 2020, hospital staff in Sri Lanka had to physically approach COVID patients to read their monitors, which exposed them to infection.
**T (Task):** Get vitals off existing bedside devices to a remote dashboard, fast, without replacing hospital equipment.
**A (Action):** Retrofitted SpO₂ meters and BP monitors with webcams and used image processing to digitize their displays, feeding a server dashboard for remote monitoring.
**R (Result):** Deployed across multiple hospital wards. It reduced healthcare-worker exposure, and the Government Medical Officers' Association (GMOA) of Sri Lanka recognised the work.
**Reflection:** Retrofitting what's already there beat a "proper" solution that would have arrived too late. In a crisis, deployability is the main requirement.
**Best for questions about:** urgency, learning fast, healthcare / safety-critical work, pragmatic engineering, social impact.
**[fill in]:** How long it took from idea to first ward, and one thing a clinician asked for that changed the design.

### S06 [Legacy / Vendor Integration] Aeoon Kyo DTG Printer + PLC
**Source:** Knowledge graph P17; Report #1405 — Crystal Fountains — Senior Software Developer (as "Promptly RIP + PLC Integration")
**S (Situation):** An industrial DTG printer came with closed RIP software and PLC-driven mechanics, and no API for running it inside an automated cell.
**T (Task):** Make the vendor software, PLC triggers and a vision step work as one closed loop, without modifying the vendor's machine.
**A (Action):** Reverse-engineered the PLC trigger points non-invasively, built RIP automation hooks, and coordinated three closed-loop subsystems in custom C++.
**R (Result):** The printer ran inside the automated workflow. This integration work fed directly into Promptly (S01).
**Reflection:** Documenting the vendor system's undocumented behaviour first saved every later integration.
**Best for questions about:** third-party/legacy systems, reverse engineering, hardware-software integration, C++ systems work, debugging without docs.

### S07 [Raising the Bar] MAS Practice Change, Training & Mentoring
**Source:** Knowledge graph §4.5, §13 (leadership row)
**S (Situation):** ML and CV work at MAS was spread across teams and factories with uneven engineering practice, and most of the group had no CV expertise.
**T (Task):** Get more teams building and adopting CV, and make what they built maintainable.
**A (Action):** Introduced CI/CD and code review, mentored engineers, ran group-wide seminars and hands-on CV training, and exhibited solutions at inter-company expos. Also represented the company at international trade shows to scout technology.
**R (Result):** The expos led to multi-factory deployments, and the practices outlasted individual projects.
**Reflection:** I raise the bar more through practice and training than through headcount. That's how I'd describe my leadership style as a senior IC.
**Best for questions about:** mentoring, leadership without a management title, knowledge transfer, influencing practice, teaching.
**[fill in]:** Rough numbers (how many people trained, how many engineers mentored) and one person whose work changed.

### S08 [Stakeholder Translation] Forestpin — Financial Anomaly Detection
**Source:** Knowledge graph §4.4
**S (Situation):** Forestpin builds forensic and audit-analytics software. Compliance and risk teams knew what "suspicious" looked like but couldn't express it as something a model could compute.
**T (Task):** Turn their detection needs into specs, then build and deploy the pipelines.
**A (Action):** Worked with compliance and risk stakeholders to define detection requirements and write technical specs. Built ML + statistical pipelines on large structured enterprise data, and SQL + Python backend scoring services for anomaly flagging and triage in production.
**R (Result):** Production scoring services for financial forensics, compliance monitoring and risk detection, with business and engineering aligned on what a flag meant.
**Reflection:** In anomaly detection the expensive error is a flag nobody can explain. Agreeing the definitions first mattered more than model choice.
**Best for questions about:** requirements gathering, non-technical stakeholders, anomaly detection, fintech, structured/tabular ML.
**Guardrails:** Short tenure (Aug 2020 – Feb 2021). If asked why, give the real reason in one line. **[fill in]** the reason, e.g. leaving to pursue the PhD, and confirm it's accurate before saying it.

### S09 [Performance & Benchmarks] Real-Time Audio Pattern Detection — 74× Faster (JAES 2026)
**Source:** Knowledge graph P1, J1; Report #656 — Reddit (as "JAES 2026 RNN vs DTW Baseline")
**S (Situation):** Smart musical instruments need to recognise what a musician is playing, live and polyphonic, on a Raspberry Pi–class device inside a ~30 ms window. The standard baseline, DTW, took over a second.
**T (Task):** Beat the baseline on both accuracy and latency on real embedded hardware.
**A (Action):** Designed 30 ms windows / 10 ms hop MFCC features into a stacked RNN. Built a rule-based synthetic-variation generator (~10k variations per pattern) to work around the lack of labelled data. Benchmarked against DTW with ablations on audio vs MIDI and pattern-set sizes 1/3/10, measuring accuracy, latency and CPU together.
**R (Result):** On a Raspberry Pi 4: 14 ms at 31.4% CPU, F1 0.76, vs DTW at 1038 ms, 48.9% CPU, F1 0.65. That's 74× faster and more accurate. Published in the Journal of the Audio Engineering Society, Mar 2026.
**Reflection:** Next time I'd formalize the benchmark harness earlier. It became the reusable asset, not the model.
**Best for questions about:** most technically challenging, optimization, evaluation methodology, limited labelled data, synthetic data, edge ML.
**Guardrails:** **Always F1 0.76. Never ">90% F1".**

### S10 [Pipeline Ownership] MUSMET — Full ML Pipeline, Research to Deployment
**Source:** Knowledge graph §4.1; Report #656 — Reddit (as "MUSMET Full ML Pipeline")
**S (Situation):** MUSMET is an EU Horizon EIC Pathfinder project (€3M, 12 partners including KTH, Politecnico di Torino and g.tec). It needed real-time pattern detection running on instruments, not just in papers.
**T (Task):** Own the full ML lifecycle: acquisition → DSP/feature engineering → training/eval → edge deployment → monitoring.
**A (Action):** Built each stage as a documented, reproducible component. Deployed on Raspberry Pi 4 with Elk Audio OS, as a VST plugin, with OSC output. Coordinated with academic and industry partners to harden research prototypes into components others could use.
**R (Result):** Real-time inference under 30 ms on edge-class devices (published: 14 ms / F1 0.76). Four peer-reviewed outputs in 2025, plus demos at Notte della Ricerca and the MUSMET kickoff.
**Reflection:** Pipeline reproducibility, not just model accuracy, is what survives handoff to other researchers and engineers.
**Best for questions about:** end-to-end ownership, production ML pipelines, research → production, working in a consortium.
**Guardrails:** You were a postdoc on the grant, not the PI.

### S11 [Cross-Discipline / Learning Fast] Multimodal Sync — Audio + EEG + MR Tracking × 4 Musicians
**Source:** Knowledge graph §4.1, P3b
**S (Situation):** Musical-metaverse experiments needed audio, BCI/EEG signals and mixed-reality head and hand tracking captured live and time-aligned, for four musicians at once.
**T (Task):** Build a real-time extraction and synchronization pipeline across very different devices, sample rates and clocks, with partners from other fields.
**A (Action):** Worked with g.tec medical engineering (BCI/EEG) and SAE Institute Barcelona. Learned the EEG side well enough to integrate it, and built a pipeline that captured and synchronized every per-device stream for 4 musicians at once.
**R (Result):** A working live multimodal capture pipeline for the MUSMET experiments.
**Reflection:** Most of the work was agreeing a shared time base and data contract with partners who think about signals differently. I now set that agreement up before any code.
**Best for questions about:** multi-stream time-series, sensor fusion, neurotech/medical signals, collaborating outside your field, learning an unfamiliar domain.
**[fill in]:** The sync method you used (hardware trigger, LSL, NTP/PTP, timestamp alignment) and the drift or jitter you achieved. Expect a technical follow-up here. The knowledge graph has no number for it, so have your own.

### S12 [Fixed-Date Delivery] MUSMET Live Multisensory Concerts
**Source:** Knowledge graph P5, P6, C2; Report #1407 — Kelluu — R&D Project Manager
**S (Situation):** Two live concerts combined three smart instruments, stage lights, a fogger, 10 Meta Quest 3 headsets and haptic smartphones, with 20 audience members and 6 performers as study participants.
**T (Task):** Deliver working shows on fixed dates, where a failure happens in front of an audience.
**A (Action):** Co-designed the shows and coordinated partners. Built the **Hot Licks Mapper**, a web patchbay routing instrument patterns to devices 1:1, 1:N, N:1 or N:N, editable live from a tablet over Wi-Fi. Ran lighting in QLC+. Rehearsed the failure paths, not just the show.
**R (Result):** Both concerts ran. Audiences rated lights and haptics as significantly more coherent than random (p < .05), and performer satisfaction was 9.33/10. Published at IEEE I3DA 2025.
**Reflection:** Rehearse the failure modes, not just the happy path.
**Best for questions about:** deadlines, multi-vendor coordination, live/real-time systems, juggling priorities, leading without authority.
**[fill in]:** One thing that broke in rehearsal or on the night, and the fallback you used.

### S13 [Hardware + Sensor Fusion] Smart Electric Guitar at McGill
**Source:** Knowledge graph §4.2, P4, C1
**S (Situation):** During a 4-month visit at McGill IDMIL/CIRMMT (Prof. Marcelo Wanderley), the question was whether a guitarist's physical gestures could become extra control alongside what they play.
**T (Task):** Build a self-contained instrument that detects gestures and musical patterns together, in real time.
**A (Action):** Mounted a BNO055 IMU on the headstock (I²C, 100 Hz) with a HiFiBerry DAC+ADC and a Raspberry Pi 4, self-powered on the guitar body. Trained a single LSTM-256 on a 1-second accelerometer buffer and fused it with audio pattern detection through a hierarchical finite-state machine (Idle → Pattern → Gesture). Profiled compute and power for edge feasibility. Ran a case study with 5 professional guitarists.
**R (Result):** P 0.79 / R 0.76 / F1 0.78 on a 500-event test corpus. Published at IEEE IS² 2025, and you performed with it in Piazza Duomo, Trento.
**Reflection:** A simple state machine for fusion beat a bigger end-to-end model here, because it was explainable to musicians and cheap on the device.
**Best for questions about:** sensor fusion, multimodal ML, prototyping hardware, short timelines, choosing simple over complex.

### S14 [User Research] Human-Centred Evaluation of Smart Instruments (UVPA Colombo)
**Source:** Knowledge graph §4.3, P7, C3
**S (Situation):** The detection systems worked in the lab, but it wasn't known whether musicians wanted them or how they'd use them.
**T (Task):** Find out how musicians perceive embedded pattern detection and what would make them adopt it.
**A (Action):** Ran a user study at the University of Visual and Performing Arts, Colombo, combining quantitative metrics with interviews.
**R (Result):** Concrete recommendations on usability, interpretability and adoption readiness. Published at IEEE I3DA 2025. The study also fed the teaching-tool and accessibility thread: detection as practice feedback, and pattern-triggered control as an aid for disabled musicians.
**Reflection:** Users found uses I hadn't designed for. Asking early changed what I built next.
**Best for questions about:** user research, product sense, listening to customers, accessibility/education, interpretability.
**[fill in]:** One finding that surprised you.

### S15 [Open Source & Data Quality] Nebula + Four Zenodo Datasets
**Source:** Knowledge graph §7, P12, P13; Report #1406 — MobilityData — Software Developer
**S (Situation):** There was no public benchmark data for live musical pattern detection, and no lightweight ARM-ready audio-feature library that published its latency.
**T (Task):** Build and publish reusable tooling and validated datasets.
**A (Action):** Designed and recorded four datasets (DoMP, DoPP, DoDP, DoDP2) with live musicians, using a shared `artistID_patternID_versionID` scheme and "perceptual equivalence" as the only constraint on variation, which makes them a worst-case benchmark. Wrote Nebula in C++17: time, spectral, cepstral, pitch and chroma features, with per-feature ARM/Raspberry Pi latency benchmarks and docs.
**R (Result):** 9,839 files from 70+ musicians, all with DOIs and used in peer-reviewed work. Nebula is public (13★).
**Reflection:** Benchmarks in the README drew more users than the feature list. Validation rules belong in code, not in a wiki.
**Best for questions about:** open source, data quality and collection, documentation, reproducibility, community.
**Guardrails:** Use the Zenodo file counts (4,392 / 2,276 / 994 / 2,177) and say "70+ musicians".

### S16 [Failure / Changing Course] When My Approach Hit Its Limits — SSIM and DTW → RNN
**Source:** Knowledge graph P8, P9, P10, C4, C6, C7
**S (Situation):** Early in the PhD you built training-free detectors: deterministic boundary checks (FRUCT 2020) and an SSIM-based matcher that treated note sequences like images (DAFx 2022, 95% detection on symbolic data). They worked, and you were invested in them.
**T (Task):** Move from symbolic MIDI to real polyphonic audio, with more patterns, on a Raspberry Pi.
**A (Action):** Benchmarked honestly as pattern sets grew. The results showed the template-style methods, DTW included, degrading as set size increased, while an RNN held at ~98% accuracy at 10 symbolic patterns (Audio Mostly 2024). You moved the main line of work to RNNs and solved their data problem with a synthetic-variation generator.
**R (Result):** The RNN line led to the JAES 2026 result (S09). The training-free work is still published and useful where there's no training data.
**Reflection:** I'd have found the scaling limit sooner if I'd tested at the target scale from day one. Now I benchmark at the size the system will really run at before I commit to an approach.
**Best for questions about:** failure, mistakes, changing your mind on evidence, sunk cost, research judgement.
**Delivery note:** Own the "I was attached to my method" part. That honesty is what makes it a credible failure story and not a humble-brag.

### S17 [Architecture Trade-off] MIRaaS — What Runs on the Edge vs the Server
**Source:** Knowledge graph P3, A2
**S (Situation):** Some music-analysis tasks are too heavy for an instrument-mounted device, but sending audio to a server adds network latency.
**T (Task):** Quantify when it pays to move MIR computation from the edge to a server.
**A (Action):** Built Music Information Retrieval as a Service: the edge device offloads MIR computation to a server over UDP, and you characterized latency end to end.
**R (Result):** Paper accepted at IEEE IS² 2026, which gives edge-vs-server decisions measured numbers instead of guesses.
**Reflection:** "Edge or cloud" is a measurement question, not a philosophy.
**Best for questions about:** system design, latency budgets, distributed inference, trade-offs, networking.
**[fill in]:** Your headline latency numbers from the paper before you use this in a technical round.

### S18 [Mentoring] Supervising Two BSc Theses
**Source:** Knowledge graph §4.1a
**S (Situation):** Undergraduate students at Trento wanted to build on the pattern-detection work.
**T (Task):** Guide them to finished theses that also moved the research forward.
**A (Action):** Supervised Leonardo Collizoli (*MIDI plugin for real-time musical pattern recognition*, Aug 2023) and Dennis Battisti (*Plugin implementation and GUI for real-time musical pattern detection*, Sep 2026). Each got a scoped, shippable piece of the system.
**R (Result):** Both theses completed. The work turned research code into usable plugins.
**Reflection:** Giving a student a component with a clear interface worked better than giving them an open research question.
**Best for questions about:** mentoring, delegation, scoping work for others, teaching.
**Guardrails:** No co-authored publications came from these. Don't imply there were.

### S19 [Communication] MIDI Innovation Awards Finalist + Live Demos
**Source:** Knowledge graph §9, §11
**S (Situation):** Real-time pattern detection is hard to explain in words and easy to understand when you see it.
**T (Task):** Get the work understood by musicians, industry judges and the public, not just reviewers.
**A (Action):** Built demos and videos ("Hot Licks"). Demoed at ISMIR 2023, SoundMIT, Audio Mostly 2024, ICT Days and Notte della Ricerca, and gave a talk at McGill.
**R (Result):** One of 15 finalists worldwide at the MIDI Innovation Awards 2023 (Prototypes & Non-Commercial Software; judges included Roger Linn and Jean-Michel Jarre), with coverage in Sound On Sound and MusicRadar.
**Reflection:** A 30-second demo beats a 10-minute explanation. I now build the demo early because it sharpens the research question too.
**Best for questions about:** explaining technical work, presenting, influencing, external visibility.

### S20 [Decision Under Uncertainty] VarianceEngine — Choosing an Architecture
**Source:** Knowledge graph §4.6
**S (Situation):** You wanted a model that takes one recorded performance and generates expressive variations (timing, dynamics, articulation, ornamentation), trained on your own DoPP dataset.
**T (Task):** Pick an approach that could actually work with a small dataset and two consumer GPUs.
**A (Action):** Wrote up and compared five candidates: mel-spectrogram diffusion, VQ-VAE + transformer prior, a retrieval baseline, symbolic transcription + transformer, and foundation-model fine-tuning. Chose LoRA fine-tuning of MusicGen-medium (rank 64, bf16, gradient checkpointing, separate learning rates for adapters and the new conditioner) with a custom audio-to-audio cross-attention conditioning head. Trained across an RTX 4090 + RTX 3090. Made deliberate feature choices, e.g. `chroma_stft` over `chroma_cqt` to avoid bass ringing, and pYIN over piptrack for its voicing confidence.
**R (Result):** Reached a checkpoint (step 1600, val loss 4.52) with sample variations. **Training is in progress and not yet evaluated.**
**Reflection:** Writing down why I rejected four options saved time later, because every "should I try diffusion?" doubt already had an answer.
**Best for questions about:** generative AI / foundation models, architecture decisions, working with limited compute, self-directed research.
**Guardrails:** Say "in progress" plainly. Don't present the val loss as a quality result.

### S21 [Rigorous Evaluation] speakfrench — 100,000-Trial Benchmark
**Source:** Knowledge graph §4.6
**S (Situation):** While learning French, you wanted pronunciation feedback that ran entirely in the browser, and you wanted to know which scoring method actually works.
**T (Task):** Compare methods fairly at a scale that gives a real answer.
**A (Action):** Wrote the DSP in JavaScript (radix-2 FFT → log-mel → MFCC). Benchmarked 6 methods across 3 families: DTW and cosine over MFCC, Gaussian log-likelihood and KL, and Wav2Vec2 embeddings. Used 10,000 sentences from FLEURS + MLS, 5 TTS voices, and 100,000 scored trials (50k matched / 50k mismatched).
**R (Result):** Wav2Vec2 XLSR-FR won with ROC-AUC 0.822 (EER 0.267, Cohen's d 1.155), vs the DTW-MFCC baseline at 0.599.
**Reflection:** DTW, the method I knew best, lost clearly. Running the comparison at scale is what kept me honest.
**Best for questions about:** evaluation design, metrics, learning on your own time, pretrained models, changing your mind on data.

### S22 [Closing a Gap on Purpose] melodiq — Learning the Data-Engineering Stack
**Source:** Knowledge graph §4.6
**S (Situation):** Job postings kept asking for Airflow, Snowflake and cloud data pipelines, and your experience there was lighter than your ML experience.
**T (Task):** Get real hands-on depth, not just a line on the CV.
**A (Action):** Built a personal audio-feature ETL: Airflow DAGs for raw-audio and GTZAN ingestion and feature extraction, S3 → Snowflake loading, Dockerized with docker-compose, with RDS + Snowflake infrastructure-as-code.
**R (Result):** A working pipeline (Feb–Mar 2026) and fluent answers on orchestration and warehouse loading.
**Reflection:** When I see a gap I'd rather build something small and real than read about it.
**Best for questions about:** initiative, self-learning, weakness → action, data engineering.
**Guardrails:** It has no training or serving layer. Don't call it an MLOps platform.

### S23 [Setback & Resilience] Invited Back After a "No Hire"
**Source:** `interview-prep/scinet-uoft-scientific-applications-ai-analyst.md`
**S (Situation):** You interviewed twice for a scientific-computing role. The search closed with "no suitable applicant" and the role was re-posted.
**T (Task):** Decide whether to try again, and if so, give them a reason to reach a different answer.
**A (Action):** Worked out the likely gap (classic HPC toolchain depth: MPI, Slurm, multi-node GPU), worked on it directly, prepared a getting-started tutorial outline for the new system, and re-applied through a referral.
**R (Result):** Invited back to interview. **[fill in]** the outcome when it's known.
**Reflection:** A rejection is information. The useful move is to find the specific gap and come back with evidence it's closed.
**Best for questions about:** rejection, resilience, responding to feedback, persistence, growth mindset.
**Guardrails:** Don't name SciNet when interviewing elsewhere ("a research-computing role"). Never use this story *at* SciNet: there, use the opener in its own prep file.

---

## 4. Hard questions — answer frames

| Question | Frame |
|---|---|
| **Biggest weakness** | Large-scale distributed training. "My largest training job is two GPUs, and my LLM work is applied, not pre-training research. I've been closing it on purpose: [multi-GPU / FSDP / Slurm work you've actually done]. My strength is the other end: making models fast and reliable on small hardware." Use S22 as proof that you close gaps. |
| **Second weakness (if pushed)** | "I'm strongest when I own a problem outright, so early on I tended to hold too much myself. Scoping work for two thesis students (S18) taught me to hand off components with clear interfaces." **[fill in]** only if this is true for you. |
| **What have you been doing since Jan 2026?** | "Independent research and open source: Nebula, LiveLaTeX on the VS Code Marketplace, a MIRaaS paper accepted at IS² 2026, Smart Drums in press at JAES, a generative model I'm fine-tuning on my own dataset, plus relocating to Canada." Confident, not apologetic. |
| **Why industry after a PhD?** | "I spent five and a half years in industry before the PhD. I went to research to get deep on real-time ML, and I'm going back because I want my work used." Cite S01 and S02 as what "used" means to you. |
| **Why leave MAS?** | **[fill in]**. Keep it to one line, forward-looking (MSc/PhD, research depth). |
| **Why only 6 months at Forestpin?** | **[fill in]**. One line. If it's the PhD, say so. |
| **Are you too academic / too senior / overqualified?** | Lead with the MAS outcomes and "I like shipping". Mention that you're immediately available and that you started your career on factory floors. |
| **Do you have LLM / GenAI experience?** | Be honest: applied and tool-level (RAG-level integration, LLM tooling daily including Claude Code, LoRA on MusicGen, Wav2Vec2 embeddings). Not an LLM researcher. Then S20. |
| **Do you want to manage people?** | "I'm a senior IC who raises the bar through practice and training." Then S07 and S18. Don't over-promise management appetite. |
| **Tell me about a conflict** | No conflict story is on record yet. Build one from S02 (operators or QA), S08 (compliance definitions) or S11 (partner data contracts) using a **real** disagreement: what each side wanted, what you proposed, the outcome, and what you'd do the same next time. **[fill in]** before your next behavioural round. |
| **Disagreed with your manager / supervisor?** | **[fill in]**. A good candidate shape is a research-direction disagreement settled with a benchmark (S16 style). Only use it if it happened. |
| **Salary expectations** | Ideal CAD 120k–150k base, flexible for a strong role with clear progression. Prefer to hear their band first ("What's the range budgeted for this role?"). |
| **Work authorization** | "Canadian permanent resident, no sponsorship needed, available immediately." |
| **French?** | "Basic, around A2, actively learning." Never claim bilingual. |

---

## 5. Guardrails — read before every interview

- **F1 = 0.76** for audio pattern detection. Never ">90% F1". Other valid figures: F1 0.78 (gesture fusion), ~98% (symbolic RNN at 10 patterns), 95% (SSIM).
- **Promptly:** alignment algorithm, RIP integration, mechanism consulting. **Never mention the patent.**
- **MAS** is one employer: Research Engineer, Jan 2015 – Jul 2020.
- **Verified numbers first** (14 ms, 74×, F1 0.76/0.78, p < .05), then self-reported industrial ones (+300%, −99.5%, −50%, millions of events/day).
- **MUSMET:** postdoc on the grant, not the PI.
- **VarianceEngine** is in progress and not evaluated. **melodiq** has no model layer.
- **Datasets:** 9,839 files, "70+ musicians".
- **Publications:** "10+ peer-reviewed". Google Scholar 27 citations, h-index 3.
- Don't name other companies you're interviewing with. Give a one-line truthful status if asked.

---

## 6. Questions to ask them (pick 3–5)

1. What does success look like in the first 6 and 12 months?
2. What's the hardest technical problem the team is stuck on right now?
3. How does a model get from a notebook to production here, and who owns each step?
4. What are the latency, compute or cost constraints the system lives under?
5. How do you measure whether a model is working once it's deployed?
6. What did the last person in this role do that you'd want more of, or less of?
7. How does the team decide between research bets and shipping work?
8. What are the next steps and the timeline?

---

## 7. Stories added by evaluations

New Block F stories from `/career-ops oferta` go below this line, in the format at the top of §3. Check §3 first: if a new story duplicates S01–S23, add its source line to the existing story instead of creating a copy.
