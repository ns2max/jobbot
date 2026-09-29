---
framework_version: 1.1.1
---

# Candidate Profile

<!-- Canonical source: input/knowledge-graph.md. This file is a working summary for /apply,
/scrape, /rank and /interview. When they disagree, the knowledge graph wins. -->

## Identity
- **Name:** Nishal Stanislaus Silva, PhD (preferred: Nishal)
- **Location:** Toronto, ON, Canada (Junction / High Park area)
- **Phone:** +1 613 200 2030 (older +1 817 number retired)
- **Email:** nishal.silva@hotmail.com (job search); ns2max@gmail.com (personal)
- **Website:** https://nishal.xyz
- **LinkedIn:** https://www.linkedin.com/in/nishal-silva
- **GitHub:** https://github.com/ns2max
- **ORCID:** https://orcid.org/0000-0003-0406-7459 · **Google Scholar:** user pdintvAAAAAJ
- **Status:** Canadian Permanent Resident, eligible to work anywhere in Canada without sponsorship
- **Availability:** Immediately (postdoc contract ended 31 Dec 2025)
- **Constraints:** Onsite Toronto / hybrid / remote-Canada all fine; open to relocation within Canada. No US-work-authorization-only roles.

### Languages

| Language | Level | Notes |
|----------|-------|-------|
| English | Native / C2 | All work and publications |
| Sinhala | Mother tongue | Use when a JD values South-Asian market/language coverage |
| Italian | B1 | Lived in Trento ~4 years; use for Italian/EU-linked employers |
| French | ~A2 | Basic, actively learning; only ever "basic / learning", never "bilingual" |

## Education

| Degree | Period | Institution | Key Topics |
|--------|--------|-------------|------------|
| PhD, Information Engineering and Computer Science | 2021-2025 (defended 31 Jan 2025) | University of Trento, Italy (DISI, CIMIL lab; supervisor Prof. Luca Turchet) | Real-time / low-latency ML, embedded & edge inference, audio DSP, time-series pattern detection, RNNs. Thesis: "Embedded Real-time Musical Pattern Detection for Smart Musical Instruments" |
| MSc, Telecommunication and Electronic Engineering | 2016-2018 | Sheffield Hallam University, UK | Thesis: "On Musical Onset Detection via the S-Transform" (Asilomar 2018) |
| BEng (Hons), Electronic Engineering | 2013-2014 | Sheffield Hallam University, UK | Thesis: "A Hand Gesture Controlled TV Remote" |
| Higher Diploma in Electronic Engineering | 2013 | SLIIT, Sri Lanka | Feeder programme for the SHU BEng |

## Professional Experience

### Postdoctoral Researcher - University of Trento (Jan 2025 - Dec 2025)
Trento, Italy
- Owned the full ML pipeline for streaming audio + IMU/gesture data: acquisition, DSP/feature engineering, training/eval, edge deployment (Raspberry Pi 4, Elk Audio OS, VST, OSC), monitoring. EU Horizon EIC Pathfinder project MUSMET.
- Real-time inference <30 ms on edge-class devices. Published system: 14 ms / F1 0.76 on RPi4 vs DTW 1038 ms / F1 0.65 (JAES 2026), 74x faster, 31.4% CPU.
- Designed benchmark suites (baselines + ablations: RNN vs DTW; audio vs MIDI; pattern-set sizes 1/3/10) quantifying accuracy-latency-CPU trade-offs.
- Built a real-time multimodal sync pipeline: audio + BCI/EEG (g.tec) + MR head/hand tracking, time-synchronized across 4 musicians simultaneously, with SAE Institute Barcelona.
- Built MIRaaS (Music Information Retrieval as a Service), a UDP edge-to-server offload architecture; latency-characterization paper accepted at IEEE IS2 2026.
- Co-designed and ran two live multisensory concerts (stage lights, smoke, 10x Meta Quest 3 MR headsets, haptic phones); user study 20 audience + 6 performers.
- 4 peer-reviewed outputs in 2025 + PhD thesis. Coordinated academic and industry partners; wrote reproducible pipelines and deployment docs. Supervised students (details pending, see below).

### Visiting Researcher - McGill University, IDMIL / CIRMMT (May 2024 - Aug 2024)
Montreal, Canada. Host: Prof. Marcelo M. Wanderley.
- Built a self-powered smart electric guitar: BNO055 IMU (I2C, 100 Hz) + HiFiBerry DAC+ADC + RPi4, instrument-mounted.
- Real-time gesture detection (single-LSTM-256 on a 1 s accelerometer FIFO) fused with audio pattern detection via a hierarchical finite state machine; 500-event corpus: P 0.79 / R 0.76 / F1 0.78 (IEEE IS2 2025).
- Compute/power profiling for edge feasibility; explored diffusion- and VAE-based synthetic audio for low-label regimes.

### Visiting Researcher - University of Visual and Performing Arts (Jan 2024 - Mar 2024)
Colombo, Sri Lanka.
- User study of musicians' perception and use cases of smart musical instruments with embedded pattern detection (IEEE I3DA 2025).
- Human-centred evaluation: quantitative metrics + interviews, producing usability and adoption recommendations.

### Technical Consultant - Forestpin (Pvt) Ltd (Aug 2020 - Feb 2021)
Colombo, Sri Lanka. Forensic / audit-analytics software company.
- Designed and deployed ML + statistical pipelines for financial forensics, compliance monitoring and risk detection on large structured enterprise datasets.
- Built SQL + Python backend scoring services for anomaly flagging and triage in production.
- Translated compliance-stakeholder requirements into technical specs.

### Research Engineer - MAS Holdings (Pvt) Ltd (Jan 2015 - Jul 2020)
Colombo, Sri Lanka. South Asia's largest apparel manufacturer. **One CV entry** (internally: MAS Technology Services 2015-2017, MAS Pixel 2018-2019, MAS Digital Excellence 2020).
- End-to-end ML and computer-vision systems for manufacturing at scale; camera, sensor and IoT streams integrated into production workflows; operational efficiency up to +300%.
- Automated multilingual care-label QC (OpenCV template + feature matching, explainable overlay, conveyor + PLC reject); inspection time cut 99.5%.
- Loom-side fabric structural-defect detection with a microscopic camera array; pilot cut operators 50%.
- Promptly on-demand direct-to-garment printing: designed the geometry-alignment algorithm (camera-captured garment geometry to per-side image warp), personally built the RIP (Raster Image Processor) integration, consulted on the flipping mechanism. Now a Twinery/MAS commercial product with facilities in the US, Mexico, France and Sri Lanka. **Never mention the patent - Nishal is not a listed inventor.**
- Real-time ingestion and ETL for high-frequency IoT and operational time-series across sites in South Asia, North America and Africa; C++/Python inference engines on embedded hardware.
- COVID-19 remote vitals CV device deployed across hospital wards (GMOA recognition). Mentored engineers; introduced CI/CD and code review; delivered group-wide CV training.

### Internships
- Communication Engineering Intern - Arthur C. Clarke Institute for Modern Technologies, Sri Lanka (Jan - Aug 2013). Automated railway-gate control for Sri Lanka Railways; radio comms; IoT water-tank prototype.
- Marketing Research Intern - Nielsen Lanka, Colombo (Sep - Dec 2010).

### Student supervision (BSc theses, University of Trento)
- **Leonardo Collizoli** - BSc thesis, "MIDI plugin for real-time musical pattern recognition", University of Trento, Aug 2023
- **Dennis Battisti** - BSc thesis, "Plugin Implementation and GUI for Real-Time Musical Pattern Detection", University of Trento, Sep 2026

## Independent Projects
- **Nebula** - C++17 audio-feature-extraction library with per-feature ARM/Raspberry Pi latency benchmarks (13 stars). Time-domain, spectral, time-frequency, cepstral, pitch and chroma features. github.com/ns2max/nebula
- **LiveLaTeX** - published VS Code Marketplace extension (`ns2max.livelatex`), real-time LaTeX compile/preview via Tectonic
- **speakfrench** - client-only French pronunciation-scoring webapp (no backend, GitHub Pages-ready). Custom radix-2 FFT -> log-mel -> MFCC in JS. Benchmarked 6 scoring methods across 3 families (deterministic DTW/cosine-MFCC, probabilistic Gaussian log-likelihood/KL, deep learning Wav2Vec2 XLSR-FR/EN-base) at scale: 10,000 sentences (FLEURS + MLS French), 5 TTS voices, 100,000 scored trials. Best: Wav2Vec2 XLSR-FR, ROC-AUC 0.822, EER 0.267, vs DTW-MFCC baseline ROC-AUC 0.599. Aug 2026.
- **melodiq** - personal audio-feature ETL pipeline: Airflow DAGs for raw-audio and GTZAN dataset ingestion and feature extraction, S3-to-Snowflake loading, Dockerized, with RDS/Snowflake infrastructure-as-code. Feb-Mar 2026.
- **VarianceEngine** - generative model producing expressive musical variations from a single ground-truth performance recording, trained on the DoPP dataset. Evaluated 5 candidate architectures (mel-diffusion, VQ-VAE + transformer prior, retrieval baseline, symbolic transcription + transformer, foundation-model fine-tune) before choosing LoRA fine-tuning of MusicGen-medium with a custom audio-to-audio conditioning head; dual-GPU training (RTX 4090 + 3090). In progress, checkpointed but not yet evaluated. May 2026.
- **poetry2music** (in progress) - multilingual (English/Italian/French/Sinhala) annotated poetry corpus for poetic-structure-to-music research: IPA + phonetic-feature annotation pipeline (espeak-ng, panphon), prosody/rhyme/meter analysis, schema-validated records, Obsidian-vault graph visualization. Phase 1 gold set: 13 poems annotated, scaling toward ~1000. Started Sep 2026, ongoing.
- **Side projects (2026):** d3/topojson filming-locations globe with a crossover engine; Ontario G1 practice app. All built with AI-assisted workflows including **Claude Code**.
- Independent researcher, Colombo (2020-2021): wrote the FRUCT 2020 paper with KTH and Trento before starting the PhD.

## Technical Skills

### Programming & ML
- **Python** (expert): TensorFlow, Keras, PyTorch, scikit-learn, Librosa, SciPy, NumPy, Pandas
- **C++17** (expert): real-time audio engines, PLC integration, the Nebula library
- **C** (proficient), MATLAB/Octave (proficient), JavaScript/TypeScript (proficient), Shell (proficient), C# (working), LaTeX (expert, XeLaTeX)
- Architectures built: stacked RNNs (LSTM/GRU/SimpleRNN), single-LSTM gesture classifiers, CNNs on symbolic matrices, multi-network binary ensembles, DTW baselines, SSIM-based training-free matching, VAE + diffusion prototypes
- Lighter evidence (list only when a JD names them): JAX, HuggingFace Transformers, ONNX, AWS SageMaker, LLMs, RAG, prompt engineering, recommender/ranking, NLP

### Signal / Audio Processing (expert)
DSP, STFT, MFCC/LFCC/PLP/GFCC, S-transform, CQT, chroma, onset/beat tracking, YIN pitch, MIR, symbolic music, MIDI modelling, Elk Audio OS, JUCE, VST, OSC

### Computer Vision (expert, industrial)
OpenCV (template + feature matching, segmentation, warping/registration, corner detection), OCR + layout segmentation, microscopic/industrial camera arrays, projector-camera AR, explainable defect overlays

### Embedded / Edge / IoT (expert)
Raspberry Pi (production), Arduino, PIC, STM32, BNO055 IMU / I2C, HiFiBerry, PLC interfacing, sensor retrofits, low-latency inference budgeting, ARM CPU profiling

### Data / Cloud / MLOps
AWS (EC2, S3, ECS, MWAA, RDS), SQL, ETL pipelines, Docker, Airflow, Jenkins, Git, pytest, CI/CD, REST APIs, Node.js; Kubernetes/MLflow/Snowflake (working knowledge)

### Domain Expertise
Smart musical instruments / Internet of Musical Things, real-time pattern detection, industrial CV & IoT for manufacturing, financial anomaly detection, medical-signal / neurotech data engineering, HCI & user studies

### Research Skills
Experimental design, benchmark & dataset design (4 public datasets, 70+ musicians), ablations, statistical evaluation, user studies/interviews, technical writing (10+ papers), peer review, grant-funded project execution

## Publications
10+ peer-reviewed items + PhD thesis, plus 2 in press/accepted. Google Scholar: 27 citations, h-index 3. Venues: JAES, IEEE IS2, IEEE I3DA, ACM Audio Mostly, DAFx, IEEE Asilomar, FRUCT. Full list with DOIs: knowledge-graph.md §6. Selected:
1. Silva, N. & Turchet, L. (2026). Real-Time Audio Pattern Detection for Smart Musical Instruments. J. Audio Eng. Soc. 74(3). https://doi.org/10.17743/jaes.2022.0250
2. Silva, N. & Turchet, L. (2026, in press). Smart Drums: Comparing Audio and MIDI in Embedded Real-Time Drum Pattern Recognition. J. Audio Eng. Soc.
3. Silva, N. & Turchet, L. (2026, accepted). Music Information Retrieval as a Service (MIRaaS). IEEE IS2 2026.
4. Silva, N., Wanderley, M. & Turchet, L. (2025). Melody and Motion. IEEE IS2 2025. https://doi.org/10.1109/IS264627.2025.11284634
5. Silva, N. & Turchet, L. (2024). Real-Time Pattern Recognition of Symbolic Monophonic Music. ACM Audio Mostly 2024. https://doi.org/10.1145/3678299.3678329

## Datasets (open access, Zenodo)
- DoMP - 4,392 monophonic MIDI recordings, 40 musicians (10.5281/zenodo.10818617)
- DoPP - 2,276 polyphonic audio recordings, 44.1 kHz/24-bit, 20 musicians (10.5281/zenodo.14497998)
- DoDP - 994 drum-pattern MIDI recordings, 10 drummers (10.5281/zenodo.14497974)
- DoDP2 - 2,177 drum-pattern MIDI recordings, artist-level style templates (10.5281/zenodo.18395007)

## Awards
- MIDI Innovation Awards 2023 - Finalist ("Hot Licks"; Prototypes & Non-Commercial Software; Sound On Sound + MusicRadar coverage)
- GMOA recognition (Sri Lanka, 2020) - COVID-19 remote vitals monitoring deployment
- EU MUSMET funding (as postdoc, not PI), 2025

## Academic Service
- Reviewer: IEEE Access; Journal of the National Science Foundation of Sri Lanka
- Programme committee / reviewer: IEEE IS2; IEEE I3DA; Colloquio di Informatica Musicale

## References
Not managed in this repo. If a posting explicitly requires references, tailor the CV/cover letter
at that point; Nishal runs the request process manually. Likely referees: Prof. Luca Turchet (PhD
supervisor / postdoc PI, University of Trento), Prof. Marcelo M. Wanderley (McGill host).
