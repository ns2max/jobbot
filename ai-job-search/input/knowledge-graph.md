# Knowledge Graph — Nishal Stanislaus Silva, PhD

<!--
PURPOSE: Single source of truth about Nishal for AI job-search agents (fit scoring, CV/cover-letter
tailoring, outreach drafting). Read this file instead of the individual CV variants.
STRUCTURE: Sections 0–3 = who/what/where. Sections 4–12 = evidence (experience, publications, projects,
datasets, code, talks, service, awards). Sections 13–16 = agent-facing guidance (targeting rules,
keyword bank, proof points, known inconsistencies).
CONFIDENCE TAGS: [verified] = confirmed against a public source (DOI, DBLP, Crossref, Zenodo, CIMIL lab
page, IRIS thesis record, GitHub, MIDI Awards press). [self] = from Nishal's own CVs/site/chats, not
independently checked. [flag] = conflicting or stale — see §16 before using.
LAST FULL REFRESH: 2026-09-03
-->

---

## 0. ONE-PARAGRAPH SUMMARY (for agents that read only one block)

Nishal Silva is a Toronto-based Machine Learning Research Engineer (PhD, University of Trento, Jan 2025) with ~10 years across industry and academia. His specialty is **real-time / low-latency ML on embedded and edge hardware** — audio, sensor and time-series pattern detection deployed on Raspberry Pi–class devices (14 ms inference, 74× faster than a DTW baseline, published in JAES 2026). Before the PhD he spent ~5.5 years at MAS Holdings (Sri Lanka's largest apparel manufacturer) building production computer-vision and IoT systems (care-label QC: −99.5% inspection time; loom-side fabric inspection: −50% operator headcount; algorithm design, RIP integration and mechanism consulting for **Promptly**, MAS/Twinery's on-demand direct-to-garment printing product now deployed in the US, Mexico, France and Sri Lanka) and ~6 months at a fintech (Forestpin) doing anomaly detection for financial forensics. He has 10+ peer-reviewed publications (JAES, IEEE IS², IEEE I3DA, DAFx, Audio Mostly, Asilomar, FRUCT), four open datasets on Zenodo, an open-source C++17 audio-feature library (Nebula), and was a MIDI Innovation Awards 2023 finalist. He is a **Canadian Permanent Resident (no sponsorship needed)**, open to onsite Toronto, hybrid, remote-Canada, or relocation within Canada. He is also a Trinity College London Grade 8 guitarist with 15+ years as a performing/session musician — relevant for music-tech, creative-tools and human-AI-interaction roles.

---

## 1. IDENTITY & CONTACT

| Field | Value | Tag |
|---|---|---|
| Full name | Nishal Stanislaus Silva, PhD | verified |
| Preferred name | Nishal | self |
| Primary job-search email | nishal.silva@hotmail.com | self |
| Personal email | ns2max@gmail.com | self |
| Institutional email | nishal.silva@unitn.it (postdoc ended Dec 2025 — may lapse) | flag |
| Phone | +1 613 200 2030 (current; the +1 817 number on older CVs is retired — do not use) | verified by Nishal |
| Location | Toronto, ON, Canada (postal M6P 1Z2 — Junction / High Park area). Earlier stated Brampton. | self |
| Website | https://nishal.xyz (also https://nish.al → same site; repo: github.com/ns2max/ns2max.github.io) | verified |
| LinkedIn | https://www.linkedin.com/in/nishal-silva | verified |
| GitHub | https://github.com/ns2max (28 repos) | verified |
| ORCID | https://orcid.org/0000-0003-0406-7459 | verified |
| ResearchGate | https://www.researchgate.net/profile/Nishal-Silva-3 | verified |
| Google Scholar | https://scholar.google.com/citations?user=pdintvAAAAAJ | verified (exists; not fetchable) |
| DBLP | https://dblp.org/pid/211/7639.html | verified |
| X / Twitter | @nishal9999 | verified (via GitHub) |
| Instagram | @nishal91 (personal), @a.man.goes.to.places (photography) | verified (site) |
| Telegram | t.me/ns2max | verified (site) |
| Handle used everywhere | ns2max | verified |
| Nationality / origin | Born and raised in Colombo, Sri Lanka | self |
| Work authorization | **Canadian Permanent Resident — eligible to work anywhere in Canada without sponsorship** | self |
| Languages | English — native / C2 · Sinhala — mother tongue · Italian — B1 · French — ~A2 (classroom study, ongoing) | verified by Nishal |
| Availability | Immediately available (postdoc contract ended Dec 2025; job-searching in Canada since mid-2025) | self |

---

## 2. JOB-SEARCH TARGETING (what to look for)

### 2.1 Target role titles (in rough priority order)
1. Machine Learning Research Engineer / ML Engineer (applied)
2. Applied Scientist / Applied Researcher / Research Scientist (industry)
3. Edge AI / Embedded ML / On-device ML Engineer
4. Audio ML / Music Technology / DSP Engineer (highest personal fit)
5. Computer Vision Engineer (industrial inspection, manufacturing, retail analytics)
6. Time-series / Signal-processing ML (IoT, sensor analytics, medical signals, ultrasound, wearables)
7. Solutions Architect / Tech Lead for real-time ML systems
8. Research Software Engineer / Scientific Computing (e.g., HPC centres)

### 2.2 Geography & work mode
- Base: Toronto, ON. Onsite Toronto ✔, hybrid ✔, remote-Canada ✔, relocation within Canada ✔ (Vancouver, Montreal, Ottawa, Waterloo all acceptable).
- Canada strongly preferred (PR status). Non-Canadian remote roles only if they hire Canadian residents.
- Montreal has a bonus signal: existing ties to McGill IDMIL/CIRMMT (Prof. Marcelo Wanderley).

### 2.3 Seniority
- PhD + 10 yrs total experience (≈5.5 yrs industry pre-PhD + 4 yrs PhD + 1 yr postdoc). Target: Senior / Staff-track IC, or Research Engineer II/III. Not targeting management-only roles, but has mentored engineers and set CI/CD & code-review practice at MAS.

### 2.4 Companies / sectors already identified as strong fits (from prior sweeps)
- Oncoustics (ultrasound signal ML — audio→ultrasound domain-transfer pitch; cold outreach drafted)
- eBay Toronto — Applied Researcher 2, Search Ranking & Monetization (hiring-manager interview completed)
- SciNet / University of Toronto HPC — two in-person interviews completed; decision pending as of late Aug 2026
- Waabi, Qualcomm Canada, RBC Borealis AI, Music.AI
- Natural fits by sector: audio/music tech (Ableton, Native Instruments, iZotope, Spotify, Moises/Music.AI, Splice, Landr [Montreal], Audioshake, Sonos), edge/embedded AI (Qualcomm, NXP, Synaptics, Ambarella, Hailo, Edge Impulse, Untether AI [Toronto], Tenstorrent [Toronto]), industrial CV/IoT (Cognex, Landing AI, Instrumental, Kinaxis, manufacturing automation), medical signal ML (Oncoustics, wearables, ultrasound), AR/VR/metaverse audio (Meta Reality Labs, Unity), fintech anomaly detection (RBC, TD, Scotiabank AI labs, Borealis).

### 2.5 Deal-breakers / low-fit signals
- Roles requiring US work authorization only.
- Pure LLM-prompting / chatbot-integration roles with no signal/ML-systems depth (he can do them but they under-use him; fit score should be moderate, not high).
- Roles requiring 5+ yrs of large-scale distributed training / LLM pre-training — not his track record (be honest: LLM/RAG experience is applied/tool-level, not research-level).

---

## 3. EDUCATION & CERTIFICATIONS

| Credential | Institution | Location | Date | Notes | Tag |
|---|---|---|---|---|---|
| PhD, Information Engineering and Computer Science | University of Trento (DISI) | Trento, Italy | Defended 31 Jan 2025 | Programme "Informatica e telecomunicazioni", Cycle XXXVII (started late 2021). Supervisor: Prof. Luca Turchet. Lab: CIMIL (Creative, Intelligent & Multisensory Interactions Lab). Thesis: *Embedded Real-time Musical Pattern Detection for Smart Musical Instruments*. Thesis PDF: https://iris.unitn.it/retrieve/handle/11572/445071/913389/PhDthesis_NishalSilva.pdf | verified |
| MSc, Telecommunication and Electronic Engineering | Sheffield Hallam University | Sheffield, UK | Aug 2018 (thesis Dec 2017) | Thesis: *On Musical Onset Detection via the S-Transform* → published at Asilomar 2018 + arXiv 1712.02567 | verified |
| BEng (Hons), Electronic Engineering | Sheffield Hallam University | Sheffield, UK | Mar 2014 | Thesis: *A Hand Gesture Controlled TV Remote* (2014) | self |
| Higher Diploma in Electronic Engineering | Sri Lanka Institute of Information Technology (SLIIT) | Sri Lanka | 2013 | Feeder programme for the SHU BEng | self |
| Rock & Pop Guitar, Grade 8 | Trinity College London | — | Jul 2015 | Highest grade in the Trinity Rock & Pop syllabus | self |
| PIC Microcontroller Programming | Science Link Technology Centre | Sri Lanka | Sep 2013 | | self |
| Google IT Automation with Python (practice repo forked) | Coursera/Google | — | — | Only evidence is a forked practice repo; do not claim certificate unless confirmed | flag |

---

## 4. PROFESSIONAL EXPERIENCE (complete, reverse-chronological)

### 4.1 Postdoctoral Researcher — University of Trento, Italy · Jan 2025 – Dec 2025 [self; CIMIL page confirms role]
Project: **MUSMET — "Musical Metaverse made in Europe: an innovation lab for musicians and audiences of the future"**, EU Horizon EIC Pathfinder Open, grant 101184379, €3.0 M, Feb 2025 – Jan 2029, coordinated by University of Trento with 12 partners incl. KTH, Politecnico di Torino, g.tec, Somnium Space [verified via CORDIS].
- Owned the full ML pipeline for streaming audio + IMU/gesture data: acquisition → DSP/feature engineering → training/eval → edge deployment (Raspberry Pi 4, Elk Audio OS, VST plugin, OSC output) → monitoring.
- Real-time inference services at <30 ms latency on edge-class devices. Published system: 14 ms / F1 0.76 on RPi4 vs DTW 1038 ms / F1 0.65 [verified, JAES 2026]. (Older CVs say ">90% F1" — retired; use 0.76.)
- Designed benchmark suites (baselines + ablations: RNN vs DTW; audio vs MIDI; pattern-set sizes 1/3/10) to quantify accuracy–latency–CPU trade-offs.
- Built the "Smart Drums" study: DTW vs stacked RNN (LSTM-256 → GRU-128 → SimpleRNN-256) on MIDI and MFCC audio; RNN 15.8 ms (MIDI) / 21.4 ms (audio) vs DTW 366 / 1132 ms [self; JAES paper in press].
- Built **MIRaaS** (Music Information Retrieval as a Service): offloads MIR computation from edge devices to a server over UDP; latency characterization paper accepted at IEEE IS² 2026 [verified via CIMIL].
- Co-designed and ran two live multisensory concerts (stage lights, smoke, 10× Meta Quest 3 MR headsets, haptic smartphones) with 20 audience + 6 performer participants; built the **Hot Licks Mapper** routing tool.
- Built a **real-time multimodal data extraction & synchronization pipeline** for musical-metaverse experiments: music/audio + BCI (EEG) signals + head- and hand-tracking from mixed-reality headsets, captured live and time-synchronized across **4 musicians simultaneously** (4 × the full set of per-device streams). Done in partnership with **SAE Institute Barcelona** and **g.tec medical engineering** (MUSMET consortium partner). [self] → strong evidence for multi-sensor time-series alignment, neurotech/BCI data engineering, and XR telemetry work.
- Researched **pattern recognition as a teaching tool** (real-time detection accuracy as practice feedback — e.g., green/red light when a phrase is played correctly) and **as an assistive aid for disabled musicians** (pattern-triggered control replacing manual controllers). [self] → relevant to music-education, accessibility and assistive-tech roles.
- 4 peer-reviewed outputs in 2025 (2× I3DA, 1× IS², JAES accepted) + PhD thesis; demos at Notte della Ricerca (MUSE Trento) and the MUSMET kickoff.
- Coordinated with academic + industry partners; wrote deployment docs and reproducible pipelines.
- Dates confirmed by Nishal: 1 Jan 2025 – 31 Dec 2025. (Website still shows "Research Assistant, Mar 2025 – present" — needs updating.)

### 4.1a Student supervision [self, provided by Nishal 2026-09]
Two BSc theses supervised at the University of Trento:
- **Leonardo Collizoli** — BSc thesis, *MIDI plugin for real-time musical pattern recognition*, University of Trento, Aug 2023.
- **Dennis Battisti** — BSc thesis, *Plugin Implementation and GUI for Real-Time Musical Pattern Detection*, University of Trento, Sep 2026.
Both directly on the smart-instrument pattern-detection line. No resulting co-authored publication recorded. Use for JDs naming mentorship/supervision; the Student Supervision block in `cv-template.tex` can now be populated (V2 and any supervision-naming JD).

### 4.2 Visiting Researcher — McGill University (IDMIL / CIRMMT), Montreal, Canada · May 2024 – Aug 2024 [self]
Host: Prof. Marcelo M. Wanderley.
- Built a smart electric guitar: BNO055 IMU on the headstock (I²C, 100 Hz) + HiFiBerry DAC+ADC + RPi4, self-powered, mounted on the guitar body.
- Real-time gesture detection (single-LSTM-256 on 1-s accelerometer FIFO) fused with audio pattern detection via a hierarchical finite state machine (Idle → Pattern → Gesture). 500-event test corpus: P 0.79 / R 0.76 / F1 0.78 [verified, IS² 2025 paper].
- Case study with 5 professional guitarists on the functional-to-theatrical gesture continuum.
- Compute/power profiling for edge feasibility; explored diffusion- and VAE-based synthetic audio data for low-label regimes [self].
- Presented to the cross-institutional McGill + UniTrento team.

### 4.3 Visiting Researcher — University of Visual and Performing Arts (UVPA), Colombo, Sri Lanka · Jan 2024 – Mar 2024 [self]
- Comprehensive user study of musicians' perception and use cases of smart musical instruments with embedded pattern detection → published as *User-Centered Evaluation of SMIs…* (I3DA 2025) [verified].
- Human-centred evaluation methodology: quantitative metrics + interviews → usability/adoption recommendations.

### 4.4 Technical Consultant — Forestpin (Pvt) Ltd, Colombo, Sri Lanka · Aug 2020 – Feb 2021 [self]
Forestpin = forensic analytics / audit-analytics software company.
- Designed and deployed ML + statistical pipelines for financial forensics, compliance monitoring and risk detection on large structured enterprise datasets.
- Built SQL + Python backend scoring services for anomaly flagging and triage in production.
- Translated compliance-stakeholder requirements into technical specs.

### 4.5 MAS Holdings group, Sri Lanka · Jan 2015 – Jul 2020 (5.5 yrs; three internal entities) [self]
MAS Holdings = South Asia's largest apparel/intimates manufacturer (Victoria's Secret, Nike, lululemon supplier). **On all job materials present this as ONE entry: "Research Engineer — MAS Holdings (Pvt) Ltd, Colombo, Jan 2015 – Jul 2020"** (confirmed by Nishal). The three-entity breakdown below is for background-check accuracy and for choosing which bullets to surface.

**4.5.a Software Research Engineer — MAS Digital Excellence, Battaramulla · Jan 2020 – Jul 2020**
- COVID-19 remote vitals: CV device digitizing sphygmomanometer / SpO₂ readings via retrofitted webcams; deployed in multiple hospital wards; dashboard for remote monitoring; recognized by the Government Medical Officers' Association (GMOA) of Sri Lanka.
- Company-wide IoT rollout tracking real-time sewing productivity across factories in South Asia, North America and Africa.
- Machine-changeover optimization system: predicting output, sewing-machine allocation and next-order layouts.
- Retail CV pilot: customer-behaviour "hot-spot" detection for product placement; vision-based label "order retrieval" system.

**4.5.b Research Engineer — MAS Pixel, Battaramulla · Jan 2018 – Dec 2019**
- Large-scale IoT productivity analytics from sewing-machine data; designed interfacing hardware for heterogeneous machines; repetitive-pattern tracking for operator efficiency.
- Image-processing QA for digital textile printing (print real-estate optimization).
- Minimal-data corner-detection algorithm enabling multiple automated measurement systems.
- CV + ML care-label QC system (see Project P10) — iterated from flatbed scanner → industrial camera → conveyor + PLC reject.
- Software bots automating third-party software; represented company at international trade shows scouting tech.

**4.5.c Technical Consultant — MAS Technology Services, Colombo 02 · Jan 2015 – Dec 2017**
- AR projection table for garment/print prototyping (lead designer & developer).
- CV segmentation/classification programs feeding document-processing bots (tech-pack digitization: OCR + layout segmentation, pre-LLM).
- Loom-side fabric structural-defect detection with a microscopic camera array (pilot; −50% operators).
- Garment detection/segmentation/classification in stock photography.
- **Promptly (Prompt.ly)** — on-demand direct-to-garment printing on *finished* garments. Nishal's role: (a) designed and prototyped the geometry-alignment algorithm (camera-captured garment geometry → calculated image warp so two-sided prints align at the seams; 4–6 min per garment; details under NDA); (b) **personally built the RIP (Raster Image Processor) integration** that tied the printer workflow into the automation loop; (c) **consulted on the garment flipping mechanism**. Do NOT mention the patent — Nishal is not a listed inventor. **Nishal's most commercially successful project**: Promptly is now a Twinery (MAS innovation arm) product with onshore facilities in the USA, Mexico, France and Sri Lanka, marketed as cutting production timelines from ~90–180 days to 72 h–5 days with 99% water and 80% energy savings; Adore Me cited as a 5-year customer. [self + verified product pages]
- Aeoon Kyo DTG printer integration: reverse-engineered PLC trigger points + RIP automation hooks; three closed-loop subsystems coordinated in custom C++.
- Lace archive digitization + context-aware ERP search for Noyon Dentelle — still in production use.
- Ran seminars and hands-on CV training across the group; exhibited solutions at inter-company expos → multi-factory deployments.

Aggregate MAS claims used on CVs [self]: operational efficiency up to +300% (care-label throughput); inspection time −99.5%; operator headcount −50% (fabric QC pilot); millions of IoT events/day across distributed sites; C++/Python real-time inference on embedded/IoT hardware; mentored engineers; introduced CI/CD and code review.

### 4.6 Independent / open-source (used on some CVs to cover the Jan 2026 → present gap) [self]
- **Nebula** — C++17 audio-feature-extraction library with per-feature latency benchmarking for ARM/Raspberry Pi (13 ★, 1 fork). Features: time-domain (ZCR, RMS, tempo, envelope), spectral (centroid, bandwidth, contrast, harmonicity, formants), time-frequency (STFT, mel/Bark/ERB, CQT, modulation spectrogram), cepstral (MFCC, LFCC, PLP, RASTA-PLP, GFCC, GTCC, PNCC + deltas), pitch (YIN F0, vibrato), chroma/tonal (key, chord, tonal centroid). Deps: FFTW3, libsndfile, CMake. [verified]
- **LiveLaTeX** — published VS Code extension (publisher `ns2max`, v0.1.0): real-time LaTeX compiler and preview powered by Tectonic. https://marketplace.visualstudio.com/items?itemName=ns2max.livelatex [verified]
- **speakfrench** — client-only French pronunciation-scoring webapp (no backend, GitHub Pages-ready). Custom radix-2 FFT → log-mel → MFCC in JS (`js/dsp.js`). Benchmarks 6 scoring methods across 3 families: deterministic (DTW over MFCC, cosine similarity of mean MFCC), probabilistic (diagonal-Gaussian log-likelihood, Gaussian symmetric-KL), deep learning (Wav2Vec2 XLSR-FR / EN-base embeddings via transformers.js). At-scale evaluation: 10,000 sentences (FLEURS + MLS French corpora), 5 edge-tts voices, 100,000 scored trials (50k matched / 50k mismatched). Best method: Wav2Vec2 XLSR-FR, ROC-AUC 0.822, EER 0.267, Cohen's d 1.155 — vs. DTW-MFCC baseline ROC-AUC 0.599. Aug 2026. [self]
- **melodiq** — personal audio-feature ETL pipeline: Airflow DAGs for raw-audio and GTZAN genre-dataset ingestion, feature extraction, and S3-to-Snowflake loading; Dockerized (docker-compose), with RDS + Snowflake infrastructure-as-code (DDL generation). No model-training/serving layer built. Feb–Mar 2026. [self]
- **VarianceEngine** — generative model that takes a single ground-truth performance recording and produces N expressive variations (timing, dynamics, articulation, harmonic ornamentation), trained on his own DoPP dataset (2,276 recordings, 20 performers, 176 patterns — see §7). Documented and compared 5 candidate architectures before choosing one: mel-spectrogram diffusion, VQ-VAE with a conditional transformer prior, a retrieval baseline (chroma/pitch-matched retrieval + pitch-shift/time-stretch alignment), symbolic transcription + autoregressive transformer, and fine-tuning a pre-trained audio foundation model — selected **LoRA fine-tuning of MusicGen-medium** (rank 64, dual learning rates for the new conditioner vs. LoRA adapters, bf16, gradient checkpointing) with a custom audio-to-audio conditioning head (cross-attention on a ground-truth audio embedding, not the stock text conditioning), trained across two GPUs (RTX 4090 + RTX 3090). Dataset-analysis stage used librosa `chroma_stft` (chosen over `chroma_cqt` to avoid bass-register ringing on dense polyphony) and pYIN (chosen over piptrack for its voiced/unvoiced confidence score, avoiding f0 hallucination on chords). Reached a checkpoint (step 1600, val loss 4.52) and produced sample generated variations; training in progress, not yet evaluated. May 2026. [self]
- **poetry2music** (in progress, not yet committed to git) — multilingual (English/Italian/French/Sinhala) annotated poetry corpus for poetic-structure-to-music research: phonetic IPA annotation (espeak-ng) + panphon feature-vector tallies, prosody/rhyme/meter analysis, JSON-schema-validated records (`SCHEMA.md`), Obsidian-vault graph visualization of shared attributes across poems. Phase 1 gold set: 13 poems annotated (target ~40–60), with a documented pipeline to scale to ~1000. Started Sep 2026. [self]
- Independent researcher, Colombo, 2020–2021: wrote the FRUCT 2020 paper with KTH (Fischione) and Trento (Turchet) before joining the PhD.

### 4.7 Internships
- Communication Engineering Intern — Arthur C. Clarke Institute for Modern Technologies, Katubedda, Sri Lanka · Jan – Aug 2013 (confirmed; website shows Oct 2013–Mar 2014 and needs correcting). Automated railway-gate control section for Sri Lanka Railways; radio comms devices; IoT water-tank prototype; exhibitor.
- Marketing Research Intern — Nielsen Lanka, Colombo · Sep–Dec 2010. Credit-card usage research for major banks; call-centre.

---

## 5. TECHNICAL SKILLS (with evidence depth)

Depth scale: **E** = expert / core, shipped & published; **P** = proficient, used in production or research; **W** = working knowledge / listed on CV without a public artifact.

### 5.1 Languages
Python (E) · C++ (E — C++17 library, real-time engines, PLC integration) · C (P) · MATLAB/Octave (P — MSc work) · JavaScript/TypeScript (P — Hot Licks Mapper, web apps) · C# (W) · Shell (P) · Assembly, VHDL (W, undergrad) · LaTeX (E — CVs in XeLaTeX)

### 5.2 ML / DL
TensorFlow + Keras (E — all published RNN work) · PyTorch (P) · scikit-learn (P) · JAX (W) · HuggingFace Transformers (W) · ONNX (W) · AWS SageMaker (W)
Architectures actually built: stacked RNNs (LSTM/GRU/SimpleRNN), single-LSTM gesture classifiers, CNNs on symbolic matrices, multi-network binary ensembles, DTW baselines, SSIM-based training-free matching, VAE + diffusion prototypes for synthetic audio, rule-based synthetic-variation generators.
Listed but shallow evidence: LLMs, RAG, prompt engineering, recommender/ranking systems, NLP (treat as W).

### 5.3 Signal / audio processing (E)
DSP, STFT, MFCC/LFCC/PLP/GFCC, S-transform (Stockwell), CQT, chroma, onset/beat tracking, YIN pitch, SSIM/bicubic interpolation repurposed to sequences, Librosa, SciPy, FFTW, libsndfile, JUCE, Elk Audio OS, VST, OSC, MIDI (note/velocity/pitch-bend modelling), music information retrieval, symbolic music.

### 5.4 Computer vision (E, industrial)
OpenCV (template + feature matching, segmentation, warping/registration, corner detection), OCR + layout segmentation, microscopic/industrial camera arrays, projector-camera AR, explainable defect overlays. Commercial CV suites: Cognex VisionPro, HALCON, ViDi, IC Imaging Control (W).

### 5.5 Embedded / edge / IoT (E)
Raspberry Pi (production deployments), Arduino, PIC, STM32, FPGA (W), BNO055 IMU / I²C, HiFiBerry, PLC interfacing, sensor retrofits, low-latency inference budgeting (30 ms window), CPU profiling on ARM, self-powered instrument-mounted compute.

### 5.6 Data / cloud / MLOps
AWS EC2/S3/ECS/MWAA/RDS (P), Snowflake (W), SQL (P), Pandas/NumPy (E), ETL pipelines (P), Docker (P), Kubernetes (W), MLflow (W), Airflow (P), Jenkins (P), Git (E), pytest/unit testing (P), CI/CD (P), REST APIs (P), Node.js web apps (P), Unity + Meta XR SDK (W — MR headsets in concerts), QLC+ lighting control (P).

### 5.7 Research skills
Experimental design, benchmark & dataset design (4 public datasets, 70+ musicians), ablations, statistical evaluation (Youden's index thresholding, p-value user studies), user studies/interviews, technical writing (10+ papers), peer review, grant-funded project execution.

### 5.8 Creative / other
Guitar (Trinity Grade 8), vocals, studio/session recording, Cubase, BIAS FX, NAM captures; Photoshop, After Effects, Lightroom, SketchUp; landscape/travel photography.

---

## 6. PUBLICATIONS (complete; verified where a DOI exists)

### 6.1 In press / accepted
| # | Title | Authors | Venue | Status | Tag |
|---|---|---|---|---|---|
| A1 | Smart Drums: Comparing Audio and MIDI in Embedded Real-Time Drum Pattern Recognition | Silva, Turchet | Journal of the Audio Engineering Society | **In press (2026)** — submitted Nov 2025, accepted. Website still says "in review" under an older title; update it. | verified by Nishal |
| A2 | Music Information Retrieval as a Service (MIRaaS): Latency Characterization of an Edge-to-Server Architecture for Near-Real-Time Audio Analysis | Silva, Turchet | 7th IEEE International Symposium on the Internet of Sounds (IS² 2026) | Accepted | verified (CIMIL) |

### 6.2 Published
| # | Title | Authors | Venue | Date | DOI / URL | Cites | Tag |
|---|---|---|---|---|---|---|---|
| J1 | Real-Time Audio Pattern Detection for Smart Musical Instruments | Silva, Turchet | J. Audio Eng. Soc. 74(3) | 6 Mar 2026 | 10.17743/jaes.2022.0250 · https://aes.org/publications/elibrary-page/?id=23129 | 0 | verified |
| C1 | Melody and Motion: Integrating Guitar Gestures with Musical Patterns for Extended Control in Live Performance and Metaverse Applications | Silva, Wanderley, Turchet | IEEE 6th Int. Symp. on the Internet of Sounds (IS² 2025), pp. 1–9 | 29 Oct 2025 | 10.1109/IS264627.2025.11284634 | 0 | verified |
| C2 | Interactive IoMusT-Based Concerts: Real-Time Pattern Recognition and Audience Experience | Silva, Boem, Turchet | IEEE I3DA 2025 | 10 Sep 2025 | 10.1109/i3da65421.2025.11202042 | 0 | verified |
| C3 | User-Centered Evaluation of Smart Musical Instruments with Embedded Real-Time Pattern Detection | Silva, Turchet | IEEE I3DA 2025 | 10 Sep 2025 | 10.1109/i3da65421.2025.11202088 | 1 | verified |
| T1 | Embedded Real-time Musical Pattern Detection for Smart Musical Instruments (PhD thesis) | Silva | University of Trento, IRIS 11572/445071 | 31 Jan 2025 | https://iris.unitn.it/handle/11572/445071 | — | verified |
| C4 | Real-Time Pattern Recognition of Symbolic Monophonic Music | Silva, Turchet | Audio Mostly 2024 (ACM) | 18 Sep 2024 | 10.1145/3678299.3678329 | 4 | verified |
| D1 | Demo of a Smart Musical Instrument-Based Real Time Pattern Detection System (demo paper, pp. 552–554) | Silva, Turchet | Audio Mostly 2024 (ACM) | 18 Sep 2024 | 10.1145/3678299.3678359 | 0 | verified |
| C5 | Towards an Internet of Musical Things (IoMusT) Ecosystem: Multi-Sensory Performances Enabled Through AI-Based Smart Musical Instruments | Silva | 11th Int. Conf. on Arts & Humanities (ICOAH) | Mar 2024 | — | — | self |
| C6 | A Structural Similarity Index Based Method to Detect Symbolic Monophonic Patterns in Real-Time | Silva, Turchet | 25th Int. Conf. on Digital Audio Effects (DAFx20in22), Vienna | Sep 2022 | https://dafx2020.mdw.ac.at/proceedings/papers/DAFx20in22_paper_18.pdf | — | verified |
| C7 | Towards Real-Time Detection of Symbolic Musical Patterns: Probabilistic vs. Deterministic Methods | Silva, Fischione, Turchet | 27th FRUCT Conf., pp. 238–246 | Sep 2020 (proceedings); CVs say Apr 2021 | https://ieeexplore.ieee.org/document/9211010 | — | verified (flag on date) |
| C8 | On Musical Onset Detection via the S-Transform | Silva, Weeraddana, Fischione | 52nd Asilomar Conf. on Signals, Systems & Computers, pp. 1080–1085 | Oct 2018 | 10.1109/ACSSC.2018.8645367 | — | verified |
| P1 | On Musical Onset Detection via the S-Transform (preprint) | Silva, Weeraddana | arXiv 1712.02567 | Dec 2017 | https://arxiv.org/abs/1712.02567 | — | verified |
| T2 | On Musical Onset Detection via the S-Transform (MSc thesis) | Silva | Sheffield Hallam University | Dec 2017 / Jan 2018 | — | — | self |
| T3 | A Hand Gesture Controlled TV Remote (BEng thesis) | Silva | Sheffield Hallam University | Aug/Oct 2014 | — | — | self |

Earlier submitted-but-superseded titles seen on a 2025 CV (do not cite as publications): "Real-Time Polyphonic Audio Pattern Detection on Smart Musical Instruments" (submitted to IEEE T-HMS → became J1) and "Performer-Audience Multi-sensory Interactions: An IoMusT Performance Ecosystem…" (submitted to IJHCS → became C2).

### 6.3 Bibliometrics
- **Canonical (Google Scholar, per Nishal): 27 citations, h-index 3.** Use these on materials.
- Secondary: ResearchGate 7 items, 616 reads, 14 citations; Crossref DOI cites C4 = 4, C3 = 1 (Sep 2026) [verified].
- Counting rule for CVs: "10+ peer-reviewed publications" = J1, C1–C8, D1 (10) + thesis; "3 publications in 2025" = C1, C2, C3.

### 6.4 Co-authors / network
| Person | Role | Relationship | Tag |
|---|---|---|---|
| Luca Turchet | Assoc. Prof., Univ. of Trento; head of CIMIL; MUSMET coordinator; pioneer of the IoMusT concept | PhD supervisor, postdoc PI, co-author on 9 papers | verified |
| Marcelo M. Wanderley | Professor, McGill IDMIL/CIRMMT | McGill host; co-author C1; ongoing connection | verified |
| Carlo Fischione | Professor, KTH Royal Institute of Technology | Co-author C7, C8 (pre-PhD collaboration) | verified |
| Pradeep Chathuranga Weeraddana | Professor, Univ. of Moratuwa (formerly KTH) | MSc collaborator, co-author C8/P1 | verified |
| Alberto Boem | Researcher, Univ. of Trento (CIMIL) | Co-author C2 (concerts) | verified |

---

## 7. DATASETS (open access, Zenodo)

| ID | Name | Modality | Zenodo page stats (canonical) | Paper-level description | DOI | Tag |
|---|---|---|---|---|---|---|
| DoMP | Dataset of Monophonic Patterns | MIDI, monophonic, piano + guitar | 4,392 files, 40 performers, 333 pattern families, mean 13.2 versions/pattern | 40 musicians (20 keys, 20 guitar; 7 nationalities; age 18–43), 10 patterns × 10 takes each = 4,000; Fishman TriplePlay tracker; mean 20.45 notes/pattern; 26.5% contain pitch bends | 10.5281/zenodo.10818617 | verified DOI |
| DoPP | Dataset of Polyphonic Patterns | WAV audio, 44.1 kHz / 24-bit (confirmed; datasets.html wrongly says 48 kHz/16-bit), polyphonic | 2,276 files, 20 performers, 176 patterns, mean 5.2 s; 89.3% variation pairs chroma-sim > 0.9 | 20 musicians (10 keys, 10 guitar; age 26–55), 10 patterns × 10 takes = 2,000; RME Fireface UFX / Zoom U-24; mean 7.4–8.4 s | 10.5281/zenodo.14497998 | verified DOI |
| DoDP | Dataset of Drum Patterns v1 | MIDI, GM drums | 994 files, 77 patterns, mean 12.9 versions; **cite 10 drummers** (confirmed; Zenodo/datasets.html say 8 — needs correcting) | 10 drummers, Yamaha DTX-432k, 1,000 recordings, 75% in 4/4 | 10.5281/zenodo.14497974 | verified DOI |
| DoDP2 | Dataset of Drum Patterns v2 | MIDI, GM drums, uniform 96 tpb | 2,177 files, 10 performers, 100 patterns, mean 21.8 versions; 194 artist-template files (patternID −1) for style anchors / zero-shot | 20 drummers total across DoDP+DoDP2 used in Smart Drums paper (2,000 instances, MIDI + 48 kHz/24-bit audio) | 10.5281/zenodo.18395007 | verified DOI |

Shared design: `artistID_patternID_versionID` naming, unified artist-ID namespace, live musicians, expressive variation with "perceptual equivalence" as the only constraint → worst-case benchmark for live pattern detection; also positioned for expressive-variation modelling, groove analysis, style transfer and music generation.

**Citation rule (confirmed by Nishal): agents cite the Zenodo file counts** — DoMP 4,392 · DoPP 2,276 · DoDP 994 · DoDP2 2,177 = **9,839 files from 80 performer-slots (40 + 20 + 10 + 10; "70+ musicians" is the safe phrasing)**. Use the paper round numbers only when quoting a specific paper's experiment.

---

## 8. PROJECTS (portfolio; P-IDs referenced elsewhere)

### 8.1 Music tech / audio ML (PhD + postdoc)
| ID | Project | Key facts | Output |
|---|---|---|---|
| P1 | Real-Time Polyphonic Audio Pattern Detection ("Hot Licks" audio) | 30 ms windows / 10 ms hop, MFCC → stacked RNN; synthetic training variations (~10k per pattern) from rule-based generator; RPi4: 14 ms, 31.4% CPU, F1 0.76 vs DTW 1038 ms, 48.9% CPU, F1 0.65 | J1, demo video https://youtu.be/gkOqfOT8zXM |
| P2 | Smart Drums: audio vs MIDI drum pattern recognition | DTW vs stacked RNN at set sizes 1/3/10; RNN 15.8 ms (MIDI) / 21.4 ms (audio); Elk Audio OS VST + OSC | A1 |
| P3 | MIRaaS — MIR as a Service | UDP edge→server offload of MIR computation; latency characterization | A2 |
| P3b | Multimodal musician-telemetry sync pipeline | Real-time extraction + synchronization of audio, BCI/EEG (g.tec), and MR-headset head/hand tracking across 4 musicians; partnership with SAE Barcelona + g.tec (MUSMET) | Internal / MUSMET deliverable |
| P3c | Pattern recognition for teaching & accessibility | Detection-accuracy feedback for practice; pattern-triggered control as an aid for disabled musicians | Research thread (C2 performer feedback, C3) |
| P4 | Gesture Detection for Electric Guitar | IMU + audio fusion via HFSM; F1 0.78 on 500 events; 5-guitarist case study; metaverse avatar mapping | C1 |
| P5 | Multisensory IoMusT Concerts | 3 SMIs (guitar/keys/drums) → OSC → server → Varytec/Stairville lights (QLC+), AF-180 fogger, 10× Quest 3 (Unity), haptic phones (Node.js + Vibration API); lights & haptics rated significantly more coherent than random (p < .05); performer satisfaction 9.33/10 | C2, video https://youtu.be/axEHkdnxFB8 |
| P6 | Hot Licks Mapper | Web patchbay for 1:1, 1:N, N:1, N:N routing of SMI patterns to devices; live edits from tablet over Wi-Fi; multi-subnet device addressing | C2 |
| P7 | User-centred SMI evaluation | User study (UVPA Colombo) on musicians' perception of embedded pattern detection | C3 |
| P8 | DTW vs RNN for symbolic patterns + DoMP | RNN ~98% accuracy at 10 patterns; DTW degrades with set size; rule-based synthetic-variation generator | C4, D1 |
| P9 | SSIM-based training-free pattern detection | 4-attribute note representation (pitch, bend extrema, velocity, duration); MM = SSIM(pitch)+0.2·SSIM(amp)+0.2·SSIM(bend)+0.3·SSIM(dur); bicubic resize for variable length; 95% detection on human, synthetic and JKUPDD sets | C6 |
| P10 | Early foundations: probabilistic vs deterministic | MIDI matrix representation; deterministic boundary-check vs single-NN, multi-NN, CNN, RNN; smart cajón prototype | C7; MIDI Awards 2023 finalist |
| P11 | Musical Onset Detection via S-Transform | Frequency-adaptive S-transform band splitting + periodicity scoring; beats Ellis 2007 spectral baseline, approaches Klapuri 2006, O(N log N), no training; Ballroom (698) + Songs (465) datasets | C8, P1, T2 |
| P12 | Nebula | C++17 audio-feature library w/ ARM latency benchmarks | GitHub |
| P13 | Datasets DoMP/DoPP/DoDP/DoDP2 | see §7 | Zenodo |

### 8.2 Computer vision / industrial (MAS)
| ID | Project | Key facts |
|---|---|---|
| P14 | Automated Care-Label QC | Multilingual label verification; OpenCV template + feature matching, explainable overlay; 3 iterations (scanner → camera → conveyor + PLC reject); 15–20 min/label → 1–2 min/batch; +300% efficiency; fully local processing for compliance |
| P15 | Loom-side Fabric Defect Detection | Microscopic camera array, overlapping FOV across 60-in rolls, 5–6 s alert budget; pilot cut operators 50% |
| P16 | **Promptly** — Seamless Two-Sided DTG Prints on Finished Garments | Alignment algorithm (camera-captured geometry → per-side image warp; 4–6 min per garment; NDA); RIP integration built personally; consulted on flipping mechanism. No patent claim. Became Twinery/MAS's commercial on-demand printing product (US, Mexico, France, Sri Lanka facilities; 72 h–5 day turnaround; Adore Me customer). Most commercially successful project Nishal has been part of. https://twinery.com/solution/promptly/ |
| P17 | Aeoon Kyo DTG Printer Integration | Non-invasive PLC trigger extraction + RIP automation hooks; 3 closed-loop subsystems in C++ |
| P18 | Tech-Pack Digitization | Pre-LLM OCR + layout segmentation of physical garment blueprints → searchable archive |
| P19 | Lace Archive & ERP Search (Noyon Dentelle) | Flatbed + microscopic capture preserving relief; designer metadata tagging; context-aware search in ERP; still in use |
| P20 | AR Print-Prototyping Table | Projector + camera; project designs onto physical garments |
| P21 | Retail Customer-Behaviour CV pilot & Smart Retail Racks | Hot-spot detection for product placement; sensor-equipped racks (details TBD) |
| P22 | Garment segmentation/classification in stock photos; corner-detection for automated measurement; digital-print QA |

### 8.3 IoT / health
| ID | Project | Key facts |
|---|---|---|
| P23 | COVID-19 Remote Vitals Monitoring | Retrofitted SpO₂ meters + BP monitors with webcams + image processing → server dashboard; multiple hospital wards; GMOA recognition |
| P24 | Sewing-floor IoT productivity analytics | Multi-continent rollout; machine-interface hardware; changeover/allocation prediction |

### 8.4 Side projects (2026, demonstrate breadth & AI-tool fluency)
- Continuity — interactive d3/topojson globe of film/TV filming locations with a crossover engine (Haversine, 50 km, ±12-month in-universe window).
- speakfrench — French pronunciation-scoring webapp; benchmarks DTW/Gaussian/Wav2Vec2 methods at scale (100k trials, best ROC-AUC 0.822). See §4.6 for detail.
- melodiq — personal audio-feature ETL pipeline (Airflow, S3, Snowflake). See §4.6.
- VarianceEngine — generative model for expressive musical-variation generation, LoRA fine-tune of MusicGen on the DoPP dataset (in progress). See §4.6.
- poetry2music (in progress) — multilingual annotated poetry corpus for poetry-to-music research. See §4.6.
- Ontario G1 interactive practice app.
- 14-slide talk on his personal AI-assisted workflow (Claude-driven job search, LaTeX CV pipeline, graphical-abstract generation with Python/CairoSVG).
- Independent research interests listed on CV: pose-estimation for athlete technique correction; retail stock-maintenance CV; foundation-model music generation and synthetic musical-variation generation.

---

## 9. TALKS, DEMOS, PERFORMANCES

| Date | Event | Location | Contribution |
|---|---|---|---|
| Sep 2025 | Notte della Ricerca — MUSE science museum | Trento | Demo: SMI controlling peripheral devices |
| 2025 | MUSMET kickoff meeting | Univ. of Trento | Mixed-reality demo for SMIs & the Musical Metaverse |
| 2025 | Live performance | Piazza Duomo, Trento | Performed with the gesture-sensing smart guitar |
| Oct 2024 | Multisensory concert | Univ. of Trento | Two live concerts with SMIs, lights, MR, haptics (video) |
| Sep 2024 | Audio Mostly 2024 | Univ. of Milan | Paper + demo (D1) |
| Sep 2024 | ICT Days | Univ. of Trento | Demo |
| May 2024 | McGill University | Montreal | Talk: Real-time musical pattern detection |
| May 2024 | Univ. of Trento | Trento | IoMusT performance ecosystem demo (video https://youtu.be/jfm5L3DYIcc) |
| Oct 2023 | ISMIR 2023 | Politecnico di Milano | Demo |
| Oct 2023 | SoundMIT Synth Expo | Turin | Demo |
| Sep 2023 | Univ. of Trento | Trento | MIDI-based real-time monophonic detection demo (video https://www.youtube.com/watch?v=eTnmlujcvMU) |
| 2023 | MIDI Innovation Awards finalist video | online | "Hot Licks – Software Prototype" https://www.youtube.com/watch?v=8VTNe8P3gmo ; livestream https://www.youtube.com/watch?v=Qt0FJQ9V9sk |

---

## 10. ACADEMIC SERVICE

- Journal reviewer: IEEE Access; Journal of the National Science Foundation of Sri Lanka.
- Programme committee / reviewer: IEEE International Symposium on the Internet of Sounds (IS²); International Conference on Immersive and 3D Audio (I3DA); XXIII Colloquio di Informatica Musicale (CIM).

---

## 11. AWARDS & RECOGNITION

| Award | Year | Detail | Tag |
|---|---|---|---|
| MIDI Innovation Awards — Finalist, "Hot Licks" | 2023 | Category: Prototypes & Non-Commercial Software Products; 15 finalists worldwide; judges incl. Roger Linn, Jean-Michel Jarre, Pedro Eustache, Nina Richards, Michele Darling; covered by Sound On Sound and MusicRadar | verified |
| GMOA recognition (Government Medical Officers' Association, Sri Lanka) | 2020 | COVID-19 remote vitals monitoring deployment | self |
| TNL Onstage 2009 — winning band "Five Minutes Apart" (guitarist) | 2009 | Major Sri Lankan band competition | self |
| YES FM All Starz 2008 — runner-up band "The Purple People" (bass) | 2008 | | self |
| EU MUSMET funding (as postdoc, not PI) | 2025 | EIC Pathfinder Open, €3 M consortium | verified |

---

## 12. MUSIC, CREATIVE & COMMUNITY PROFILE (use for music-tech, creative-tools and culture-fit framing)

- Guitarist since age 14 (20+ years); vocalist; Trinity College London Rock & Pop Grade 8 (2015).
- 15+ years playing in bands, studio/session guitarist, freelance guitar instructor, YouTube cover guitarist; involved in award-winning and commercially successful Sri Lankan acts.
- Gear: Ibanez RGA7 (Seymour Duncan Sentient/Pegasus), BIAS FX, Neural Amp Modeler captures; DAW: Cubase. Deep interest in amp modelling / neural audio effects — a credible bridge to companies like Neural DSP, IK Multimedia, Positive Grid, Line 6.
- Volunteer guitarist for community music programmes (Toronto).
- Landscape/travel photographer (@a.man.goes.to.places); ran a photography blog; created promotional material for employers.
- Leadership/community: Phase-1 trained Scout leader; Rover Scout; Sri Lanka representative at the World Scout Jamboree, Essex, UK (year not stated on CV; the Essex jamboree was 2007); Sergeant-at-Arms, Rotaract Club of SLIIT; President/Editor of the UN Youth Association at St. Peter's College Colombo (Model UN delegate); Interact Club officer.
- Inspirations he cites: Arthur C. Clarke, Star Wars/Star Trek/Knight Rider — self-described tinkerer since childhood.
- Italian B1 (lived in Trento ~4 years); French ~A2 via classroom study — relevant for Montreal/Quebec roles and bilingual-preferred federal or Ottawa postings; building French and Italian pronunciation-trainer apps.

---

## 13. PROOF POINTS BY CLAIM (paste-ready evidence)

| Claim | Evidence | Tag |
|---|---|---|
| Sub-30 ms real-time inference on edge hardware | J1: 14 ms on RPi4 at 31.4% CPU; A1: 15.8/21.4 ms; MUSMET services <30 ms | verified / self |
| 74× faster than baseline | J1: 14 ms vs 1038 ms DTW | verified |
| Detection accuracy | **Cite F1 = 0.76** for audio pattern detection (J1). Other published figures: F1 0.78 (gesture+pattern fusion, C1), ~98% accuracy (symbolic RNN at 10 patterns, C4), 95% detection (SSIM, C6). Do NOT use the ">90% F1" headline from older CVs. | verified by Nishal |
| Training-free ML | SSIM method, 95% detection (C6); S-transform beat tracker, no training (C8) | verified |
| Benchmark & dataset design | 4 Zenodo datasets, 70+ musicians; RNN-vs-DTW ablations at set sizes 1/3/10 | verified |
| Multimodal ML (audio + IMU) | C1: HFSM fusion, F1 0.78 | verified |
| Multi-stream time-series synchronization / neurotech data eng. | MUSMET pipeline: audio + BCI + XR tracking, 4 musicians live, with SAE Barcelona & g.tec | self |
| Commercial product impact | Promptly (MAS/Twinery) — alignment algorithm, RIP integration and mechanism consulting for a globally deployed on-demand printing product (never cite the patent) | self + verified product pages |
| Education / accessibility applications | Pattern recognition as practice feedback and as assistive control for disabled musicians | self |
| Generative / synthetic data | Rule-based variation generator (C4, J1); VAE/diffusion prototypes at McGill | verified / self |
| Human-in-the-loop & user studies | C2 (20 audience + 6 performers, p < .05), C3 (musician study), C1 (5-guitarist case study) | verified |
| Production CV at industrial scale | MAS: +300% efficiency, −99.5% inspection time, −50% operators, ERP lace search still live | self |
| IoT at scale | MAS sewing-floor IoT across South Asia, N. America, Africa; "millions of events/day" | self |
| Financial anomaly detection | Forestpin: SQL+Python scoring services for forensic analytics | self |
| Healthcare deployment | COVID vitals CV device in hospital wards; GMOA recognition | self |
| Hardware/firmware depth | PLC reverse-engineering (P17), IMU/I²C, HiFiBerry, Arduino/PIC/STM32, railway-gate control intern | self |
| Open-source | Nebula (13 ★), JKUPDD mirror, real_time_patt | verified |
| Leadership & mentoring | MAS: mentored engineers, CI/CD + code review, group-wide CV training seminars, multi-factory deployments; student supervision during PhD/postdoc (details pending, §4.1a) | self |
| EU-funded research | MUSMET (EIC Pathfinder, 101184379) | verified |
| Peer-reviewed track record | 10 peer-reviewed items + 2 in press/accepted; 5 venues (JAES, IEEE IS², IEEE I3DA, ACM Audio Mostly, DAFx, IEEE Asilomar, FRUCT) | verified |
| Award recognition | MIDI Innovation Awards 2023 finalist (Sound On Sound, MusicRadar coverage) | verified |

---

## 14. ATS / KEYWORD BANK

**Core:** machine learning, deep learning, real-time inference, low-latency, edge AI, embedded ML, on-device ML, TinyML, Raspberry Pi, ARM, model optimization, latency profiling, benchmarking, ablation studies, time-series, sequence modelling, RNN, LSTM, GRU, pattern recognition, anomaly detection, signal processing, DSP, audio ML, music information retrieval, MIR, MFCC, STFT, onset detection, beat tracking, symbolic music, MIDI, OSC, JUCE, Elk Audio OS, VST, multimodal learning, sensor fusion, IMU, gesture recognition, human-computer interaction, HCI, user studies, computer vision, OpenCV, industrial inspection, defect detection, OCR, image registration, PLC, IoT, ETL, data pipelines, AWS, Docker, Airflow, CI/CD, Python, C++17, TensorFlow, Keras, PyTorch, scikit-learn, SQL, synthetic data, VAE, diffusion models, generative AI, datasets, open science, Zenodo, peer-reviewed, JAES, IEEE, ACM, EU Horizon, EIC Pathfinder, metaverse, mixed reality, Meta Quest, Unity, haptics, smart musical instruments, Internet of Musical Things, IoMusT, Internet of Sounds, BCI, EEG, neurotech, g.tec, XR telemetry, head/hand tracking, data synchronization, multi-stream alignment, music education, assistive technology, accessibility, on-demand manufacturing, direct-to-garment, Promptly, Twinery.

**Secondary (listed, lighter evidence):** JAX, HuggingFace, ONNX, SageMaker, Kubernetes, MLflow, Snowflake, LLM, RAG, prompt engineering, NLP, recommender systems, ranking, transfer learning, model compression, C#, MATLAB, FPGA, VHDL.

---

## 15. FRAMING RULES FOR AGENTS

1. **Pick ONE variant from the matrix below and do not mix rows.** The variant fixes the tagline, section order, competency group names, the third Technical Stack line, publication count and page target. `cv-template.tex` carries the same matrix inline with per-section instructions; this table is the summary.

| # | Variant | When | Tagline | Distinctive structure | Pages |
|---|---|---|---|---|---|
| V1 | AI-Industry (**default**) | Applied/product ML at a company | Machine Learning Research Engineer \| Deep Learning, Time-Series, Pattern Detection \| Applied ML | Groups: ML Engineering / Domain Expertise / Research & Leadership. Stack leans Kubernetes, MLflow, REST, ONNX, SageMaker, LLM/RAG, recommender & ranking | 2 |
| V2 | AI-Research | Research scientist, applied scientist, national lab | Research Scientist \| Real-Time Multimodal ML, Benchmarks & Open Datasets | Full publications + datasets + peer review + talks + supervision; drop Portfolio; ML/AI line leads with JAX, HuggingFace, PyTorch | 3 |
| V3 | Edge/Embedded | On-device ML, TinyML, real-time systems, silicon | ML Research Engineer \| Real-Time & Edge Inference \| Audio, Sensor & Time-Series | Groups: ML Engineering / Edge & System Optimization / Research Engineering. Third stack line = Edge & Systems (RPi, Embedded Linux, JUCE, Elk, ARM profiling). Keeps Projects | 2–3 |
| V4 | Music-Tech | Audio ML, MIR, instruments, creative tools | Music Technology ML Research Engineer \| Audio, DSP & Real-Time Systems | **Portfolio & Demos moves up** to just after the summary; **Education moves down** near the end; 4 publications incl. the PhD thesis; keep the guitarist line; Trinity Grade 8 may join Education | 2 |
| V5 | CV/Industrial | Inspection, manufacturing, robotics, retail | Computer Vision & ML Engineer \| Industrial Inspection, IoT & Edge Deployment | **Inverts the bullet weighting**: MAS gets 4–5 bullets, postdoc drops to 2. Third stack line = Computer Vision. Projects drawn from §8.2 | 2 |
| V6 | Generic | Speculative applications, recruiters, vague JDs | Research Engineer \| Real-Time ML, DSP & Time-Series \| Music Technology | Competencies as **one flat comma list, no group headings**; Education sits *before* the stack | 2 |
2. Always state PR status + no sponsorship near the top for Canadian roles.
3. Quantify with the verified numbers first (14 ms, 74×, F1 0.76/0.78, 95%, 98%), then the self-reported industrial numbers (300%, 99.5%, 50%). Never use ">90% F1".
4. For LLM-heavy JDs, position honestly: strong ML-systems engineer who uses LLM tooling daily (AI-assisted workflows, RAG-level integration) — not an LLM researcher.
5. For fintech/anomaly JDs, foreground Forestpin + MAS IoT analytics; for healthcare/medical-signal/neurotech JDs, foreground COVID vitals, the BCI + XR synchronization pipeline (g.tec), and the audio→ultrasound domain-transfer narrative (used for Oncoustics). For product/manufacturing-tech JDs, lead with Promptly as the commercial-impact story. For ed-tech, music-education or accessibility JDs, use the teaching-tool / disabled-musician research thread.
6. Languages on materials: English (native) always; Sinhala when a JD values South-Asian market/language coverage; Italian (B1) for Italian/EU-linked companies; French (~A2) only as "basic / actively learning" — never claim bilingual for Quebec or federal postings. For Montreal roles, mention the McGill IDMIL/CIRMMT connection; for Toronto HPC/scientific-computing roles, mention SciNet interviews are already in progress (avoid duplicate applications).
7. Employment gap since Jan 2026: cover with "Independent Research & Open-Source (Jan 2026 – present): Nebula (C++17 audio-feature library), LiveLaTeX (VS Code extension on the Marketplace), MIRaaS paper (IS² 2026), Smart Drums paper (JAES, in press), relocation to Canada."
8. **The variant sets the length; the JD can override it.** V1/V4/V5/V6 = 2 pages, V2 = 3, V3 = 2 unless the JD asks for publications.Extend to 3 pages only when the role rewards a full academic record (research scientist, postdoc, faculty, national lab, or any posting that asks for a publication list, teaching record, or evidence of supervision). At 3 pages add: the full publication list (§6, including theses and in-press items), the full Datasets section (§7), Scientific Committee & Peer Review (§10), Talks & Demos (§9), and Student Supervision (§4.1a). At 2 pages cut those, fold the datasets into a single Highlights line, and keep 3 bullets per role. Never exceed 3 pages; if it overflows, cut Talks before Publications. `cv-template.tex` tags every section [CORE] or [EXTENDED] accordingly.
9. Writing style Nishal wants in generated materials: concise, technically precise, no fluff, copy-paste-ready, stay within the original CV's scope and length, attach a changelog to revisions.

---

## 16. KNOWN INCONSISTENCIES / ITEMS TO CONFIRM WITH NISHAL

All inconsistencies resolved with Nishal on 2026-09-03. Canonical values:

| Item | Canonical value |
|---|---|
| Phone | +1 613 200 2030 (the +1 817 number is retired) |
| Postdoc dates | 1 Jan 2025 – 31 Dec 2025 |
| Smart Drums (A1) | JAES 2026, in press |
| Audio pattern-detection accuracy | F1 = 0.76 (never ">90% F1") |
| LiveLaTeX | Published VS Code Marketplace extension (ns2max.livelatex) |
| MAS Holdings | One CV entry: Research Engineer, Jan 2015 – Jul 2020 |
| Dataset sizes | Zenodo file counts (4,392 / 2,276 / 994 / 2,177) |
| Citation metrics | Google Scholar: 27 citations, h-index 3 |
| Languages | English native (C2) · Sinhala mother tongue · Italian B1 · French ~A2 |
| ACCIMT internship | Jan – Aug 2013 |
| DoPP audio format | 44.1 kHz / 24-bit |
| DoDP v1 performers | 10 drummers |
| FRUCT paper | FRUCT 2020 (proceedings Sep 2020) |
| JAES J1 | Mar 2026, Vol. 74 No. 3 |
| Wanderley | Co-author on C1 (gesture paper) only |
| Location | Toronto, ON |

**Open data gap:** none outstanding. (§4.1a Student Supervision filled 2026-09.)

**Salary expectation (provided 2026-09):** ideal CAD 120k–150k base; flexible below for a strong role with clear progression. Soft benchmark, not a hard filter.

**Website fixes owed (nishal.xyz):** cv.html postdoc dates & ACCIMT dates; publications.html Smart Drums → "in press" with final title; datasets.html DoPP format (44.1 kHz/24-bit) and DoDP performer count (10).

---

## 17. SOURCE INDEX

- Personal site & repo: https://nishal.xyz (index, about, cv, research, publications, datasets, demos pages; docs/Nishal_Silva_Research_Engineer.pdf; docs/cv_nishal4.pdf)
- DBLP: https://dblp.org/pid/211/7639.html
- Crossref API query on author "Nishal Silva"
- CIMIL people & publications: https://www.cimil.disi.unitn.it/people/ · https://www.cimil.disi.unitn.it/publications/
- IRIS thesis record: https://iris.unitn.it/handle/11572/445071
- AES e-library: https://aes.org/publications/elibrary-page/?id=23129
- CORDIS MUSMET fact sheet: https://cordis.europa.eu/project/id/101184379
- MIDI Innovation Awards 2023 coverage: https://www.soundonsound.com/news/midi-innovation-awards-finalists-announced · https://www.musicradar.com/news/midi-innovation-awards-2023
- GitHub: https://github.com/ns2max · https://github.com/ns2max/nebula
- ResearchGate: https://www.researchgate.net/profile/Nishal-Silva-3
- Zenodo DOIs: 10.5281/zenodo.10818617, 14497998, 14497974, 18395007
- Project docs: cv-long.md, cv-ai-industry.md, cv-musictech.md, cv-ai-research.md, cv-generic.md, publications-list.md, projects-list.md, coverletter.md (job-search project)
- Prior chat context (memory): job-search targets, Smart Drums paper, MIRaaS, side projects, writing preferences
