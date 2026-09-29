# Job Application Assistant for Nishal Stanislaus Silva, PhD

## Role
This repo is a job application workspace. Claude acts as a career advisor and application assistant for Nishal Silva, helping with:
1. **Job fit evaluation** - Assess job postings against the profile (skills, experience, behavioral traits)
2. **CV tailoring** - Adapt CV templates to target specific roles
3. **Cover letter writing** - Draft targeted cover letters
4. **Interview preparation** - Prepare answers, questions, and talking points
5. **Career strategy** - Advise on positioning and personal branding

**Single source of truth:** `input/knowledge-graph.md` is the canonical, evidence-tagged record about
Nishal (identity, experience, publications, datasets, projects, targeting rules, keyword bank, known
inconsistencies). Read it before drafting anything. The skill files below summarize it for the
`/apply`, `/scrape`, `/rank` and `/interview` workflows; when they disagree, the knowledge graph wins.

## Candidate Profile

### Identity
- **Name:** Nishal Stanislaus Silva, PhD (preferred name: Nishal)
- **Location:** Toronto, ON, Canada (Junction / High Park area)
- **Phone:** +1 613 200 2030 (the older +1 817 number is retired, do not use)
- **Email:** nishal.silva@hotmail.com (job search); ns2max@gmail.com (personal)
- **Website:** https://nishal.xyz
- **LinkedIn:** https://www.linkedin.com/in/nishal-silva
- **GitHub:** https://github.com/ns2max
- **ORCID:** https://orcid.org/0000-0003-0406-7459
- **Languages:**
  | Language | Level |
  |----------|-------|
  | English | Native / C2 |
  | Sinhala | Mother tongue |
  | Italian | B1 |
  | French | ~A2 (basic, actively learning) |
- **CV language:** English

- **Status:** Canadian Permanent Resident, eligible to work anywhere in Canada without sponsorship. Available immediately (postdoc contract ended 31 Dec 2025).
- **LinkedIn headline:** "Machine Learning Research Engineer | Real-Time & Edge ML for Audio, Sensor & Time-Series Data | PhD" (approximate, confirm against the live profile)
- **Commute / location constraints:** Based in Toronto. Considering:
  - **Canada, any major job-market city** - onsite, hybrid, or requiring relocation: Toronto / GTA, Montreal (bonus: McGill IDMIL/CIRMMT ties), Vancouver, Ottawa, Calgary, Waterloo / Kitchener, Edmonton, Halifax, Quebec City
  - **Remote roles worldwide / global** - any fully-remote role open to a candidate based in Canada, regardless of company HQ country
  - Excluded: roles requiring US-only (or any non-Canadian) work authorization; on-site roles outside Canada.

### Education
- **PhD in Information Engineering and Computer Science** (2021-2025) - University of Trento, Italy (DISI, CIMIL lab)
  - Defended 31 Jan 2025. Supervisor: Prof. Luca Turchet
  - Thesis: "Embedded Real-time Musical Pattern Detection for Smart Musical Instruments"
  - Topics: real-time / low-latency ML, embedded & edge inference, audio DSP, time-series pattern detection, RNNs
- **MSc in Telecommunication and Electronic Engineering** (2016-2018) - Sheffield Hallam University, UK
  - Thesis: "On Musical Onset Detection via the S-Transform" (published at Asilomar 2018)
- **BEng (Hons) in Electronic Engineering** (2013-2014) - Sheffield Hallam University, UK
  - Thesis: "A Hand Gesture Controlled TV Remote"
- **Higher Diploma in Electronic Engineering** (2013) - SLIIT, Sri Lanka

### Professional Experience
- **Postdoctoral Researcher** (Jan 2025 - Dec 2025) - **University of Trento** (Trento, Italy)
  - Owned the full ML pipeline for streaming audio + IMU/gesture data: acquisition, DSP/feature engineering, training/eval, edge deployment (Raspberry Pi 4, Elk Audio OS, VST, OSC), monitoring
  - EU Horizon EIC Pathfinder project MUSMET; real-time inference <30 ms on edge-class devices; published system 14 ms / F1 0.76 on RPi4 vs DTW 1038 ms (JAES 2026)
  - Built a real-time multimodal sync pipeline: audio + BCI/EEG (g.tec) + MR head/hand tracking across 4 musicians simultaneously, with SAE Institute Barcelona; ran two live multisensory concerts (user study: 20 audience + 6 performers)
- **Visiting Researcher** (May 2024 - Aug 2024) - **McGill University** (IDMIL / CIRMMT, Montreal, Canada)
  - Built a self-powered smart electric guitar (BNO055 IMU + HiFiBerry + RPi4); IMU+audio gesture fusion via hierarchical FSM, F1 0.78 on a 500-event corpus (IEEE IS2 2025)
- **Visiting Researcher** (Jan 2024 - Mar 2024) - **University of Visual and Performing Arts** (Colombo, Sri Lanka)
  - User study of musicians' perception of smart musical instruments with embedded pattern detection (IEEE I3DA 2025)
- **Technical Consultant** (Aug 2020 - Feb 2021) - **Forestpin (Pvt) Ltd** (Colombo, Sri Lanka)
  - ML + statistical pipelines for financial forensics, compliance monitoring and risk detection on large structured enterprise data; SQL + Python backend scoring services for anomaly flagging
- **Research Engineer** (Jan 2015 - Jul 2020) - **MAS Holdings (Pvt) Ltd** (Colombo, Sri Lanka)
  - Present as ONE entry (internally: MAS Technology Services, MAS Pixel, MAS Digital Excellence)
  - End-to-end computer-vision and IoT systems for manufacturing at scale; camera/sensor/IoT streams into production workflows
  - Care-label QC (OpenCV, conveyor + PLC reject, inspection time -99.5%); loom-side fabric inspection (microscopic camera array, operator headcount -50%); operational efficiency up to +300%
  - Promptly on-demand direct-to-garment printing: designed the geometry-alignment algorithm, personally built the RIP integration, consulted on the flipping mechanism. Now a Twinery/MAS commercial product (US, Mexico, France, Sri Lanka). **Never mention the patent - Nishal is not a listed inventor.**
  - COVID-19 remote vitals CV device deployed across hospital wards (GMOA recognition); mentored engineers; introduced CI/CD and code review

### Independent / Open-Source (Jan 2026 - present, covers the current gap)
- **Nebula** - C++17 audio-feature-extraction library with per-feature ARM/Raspberry Pi latency benchmarks (github.com/ns2max/nebula)
- **LiveLaTeX** - published VS Code Marketplace extension (`ns2max.livelatex`), real-time LaTeX compile/preview via Tectonic
- MIRaaS paper accepted at IEEE IS2 2026; Smart Drums paper in press at JAES; relocation to Canada
- **speakfrench** - French pronunciation-scoring webapp (client-only, no backend). Benchmarked 6 methods across 3 families (DTW/cosine-MFCC, Gaussian log-likelihood/KL, Wav2Vec2 XLSR-FR/EN-base) at scale: 10,000 sentences, 5 TTS voices, 100,000 scored trials. Best: Wav2Vec2 XLSR-FR, ROC-AUC 0.822, vs DTW-MFCC 0.599. Aug 2026.
- **melodiq** - personal audio-feature ETL pipeline: Airflow DAGs (raw-audio + GTZAN ingestion, feature extraction), S3-to-Snowflake, Dockerized, RDS/Snowflake infra-as-code. Feb-Mar 2026.
- **VarianceEngine** - generative model producing expressive musical variations from a single ground-truth performance recording, trained on the DoPP dataset. Evaluated 5 candidate architectures (mel-diffusion, VQ-VAE + transformer prior, retrieval baseline, symbolic transcription + transformer, foundation-model fine-tune) before choosing LoRA fine-tuning of MusicGen-medium with a custom audio-to-audio conditioning head; dual-GPU training (RTX 4090 + 3090). In progress. May 2026.
- **poetry2music** (in progress) - multilingual (EN/IT/FR/SI) annotated poetry corpus for poetry-to-music research: IPA + phonetic-feature annotation pipeline, prosody/rhyme/meter analysis, Obsidian-vault graph viz. Phase 1: 13 poems, scaling to ~1000. Sep 2026, ongoing.
- Side projects (2026): d3/topojson filming-locations globe; Ontario G1 practice app. Built with AI-assisted workflows including **Claude Code**.

### Technical Skills
- **Primary:** Python, C++17, TensorFlow/Keras, real-time & low-latency ML, edge/embedded ML (Raspberry Pi, ARM), time-series & sequence modelling (RNN/LSTM/GRU), DSP & audio ML (MFCC, STFT, MIR), computer vision (OpenCV, industrial inspection), benchmark & dataset design
- **Secondary:** PyTorch, scikit-learn, SQL, Pandas/NumPy, Docker, Airflow, Jenkins, AWS (EC2/S3/ECS/MWAA/RDS), ETL pipelines, REST APIs, JavaScript/TypeScript, C, MATLAB, anomaly detection, multimodal / sensor fusion (IMU, BCI/EEG, XR telemetry)
- **Domain:** smart musical instruments / Internet of Musical Things, real-time pattern detection, industrial CV & IoT (manufacturing), financial anomaly detection, medical-signal / neurotech data engineering, human-computer interaction & user studies
- **Software:** Elk Audio OS, JUCE, VST, OSC, MIDI, Librosa, SciPy, FFTW, libsndfile, Unity + Meta XR SDK, QLC+, Git, pytest, LaTeX (XeLaTeX), Cubase
- **Lighter evidence (list only when a JD names them):** JAX, HuggingFace, ONNX, SageMaker, Kubernetes, MLflow, Snowflake, LLMs, RAG, prompt engineering, recommender/ranking systems, NLP

### Certifications
- **Rock & Pop Guitar, Grade 8** - Trinity College London (Jul 2015)
- **PIC Microcontroller Programming** - Science Link Technology Centre, Sri Lanka (Sep 2013)
- (Do not claim a Google IT Automation with Python certificate - only a forked practice repo exists.)

### Publications
- 10+ peer-reviewed items (JAES, IEEE IS2, IEEE I3DA, ACM Audio Mostly, DAFx, IEEE Asilomar, FRUCT) + PhD thesis; 2 more in press/accepted (Smart Drums JAES 2026; MIRaaS IS2 2026). Google Scholar: 27 citations, h-index 3. Full list: knowledge-graph.md §6.
- Silva, N. & Turchet, L. (2026). Real-Time Audio Pattern Detection for Smart Musical Instruments. J. Audio Eng. Soc. 74(3). DOI 10.17743/jaes.2022.0250

### Datasets
- Four open-access musical-pattern datasets on Zenodo (DoMP, DoPP, DoDP, DoDP2), 9,800+ recordings, 70+ musicians. Details: knowledge-graph.md §7.

### Awards
- **MIDI Innovation Awards 2023 - Finalist** ("Hot Licks", Prototypes & Non-Commercial Software; covered by Sound On Sound and MusicRadar)
- **GMOA recognition** (Government Medical Officers' Association, Sri Lanka, 2020) - COVID-19 remote vitals monitoring deployment
- EU MUSMET funding (as postdoc, not PI), 2025

### Behavioral Profile
- **Tinkerer / builder** - self-directed, ships end-to-end systems from hardware to deployment; strongest when owning a problem outright
- **Cross-domain translator** - moves between industry and academia, technical and stakeholder audiences; ran group-wide CV training and international trade-show scouting at MAS
- **Strengths:** real-time systems engineering, first-principles problem-solving under hard constraints (latency, compute, power), research rigor (benchmarks, ablations, open data), performer-informed design intuition
- **Growth areas:** large-scale distributed training / LLM pre-training (applied/tool-level, not research-level); pure management tracks (has mentored, but IC-focused)
- **Thrives in:** small teams with real ownership, applied research with a shipping target, hardware-in-the-loop work, mission or craft the team genuinely cares about
- Full detail and inference sourcing: `02-behavioral-profile.md`

### What Excites You
- Real-time / edge ML where latency, compute and power budgets are the hard part
- Audio, music technology and creative tools (highest personal fit - 15+ years as a performing/session guitarist, Trinity Grade 8)
- Multimodal / multi-sensor time-series: audio + IMU + BCI + XR telemetry
- Systems that ship and get used (Promptly, care-label QC, COVID vitals device)
- Teaching-tool and accessibility applications of pattern recognition

### Target Sectors
- Audio / music tech: Ableton, Native Instruments, iZotope, Spotify, Moises/Music.AI, Splice, LANDR, Audioshake, Sonos, Neural DSP, Positive Grid
- Edge / embedded AI: Qualcomm, NXP, Synaptics, Ambarella, Hailo, Edge Impulse, Untether AI, Tenstorrent
- Industrial CV / IoT: Cognex, Landing AI, Instrumental, Kinaxis
- Medical-signal / neurotech: Oncoustics, wearables, ultrasound ML
- AR/VR audio: Meta Reality Labs, Unity
- Fintech anomaly detection: RBC Borealis AI, TD, Scotiabank AI labs
- Research computing: SciNet / University of Toronto HPC
- Active pipeline (avoid duplicate applications): eBay Toronto (Applied Researcher 2, hiring-manager interview done), SciNet / U of T HPC (two interviews done, decision pending), Oncoustics (cold outreach drafted)

### Deal-breakers
- Roles requiring US work authorization only
- Roles requiring 5+ years of large-scale distributed training / LLM pre-training (not his track record)
- Pure LLM-prompting / chatbot-integration roles with no signal or ML-systems depth (can do them, but they under-use him - score moderate, not high)
- Relocation outside Canada

### Salary expectation
- Ideal: CAD 120k-150k base. Flexible below that for a strong role with a clear progression path. Use as a soft benchmark, not a hard filter.

## CV / Cover Letter Templates
- Master CV template: `cv/main_example.tex` (self-contained `article` class; 6 variants V1-V6 selected per JD - see the header block and knowledge-graph.md §15).
- Master cover letter template: `cover_letters/cover_example.tex` (`article` class; 4 paragraphs, 1 page).
- Both carry inline `<<KG ...>>` placeholders filled from `input/knowledge-graph.md`.
- **Compile with Tectonic** (installed): `tectonic -X compile <file>.tex` from the containing directory. Produces the PDF in place. The templates guard their pdfTeX-only lines so Tectonic's XeTeX engine handles them.
- Output targeted files as `cv/<id>_main_<company>_<role>.tex` and `cover_letters/<id>_cover_<company>_<role>.tex`, where `<id>` is the job's id from `seen_jobs.json` / the tracker. Every job-specific file (PDF, `.txt` ATS dump, changelog) and the `documents/applications/<id>_<company>_<role>/` folder carries the same `<id>_` prefix.
- The first line of every generated `.tex` is `% Job posting: <url>` (posting URL from `seen_jobs.json` / tracker `source`), before the header banner.

## Job ID scheme (shared with career-ops)
Job IDs are shared with the separate `career-ops` job-search tool and must never overlap. The
authority for the current maximum is `~/PROJECTS/career-ops/data/applications.md` (leading integer
of each row) and its `data/pipeline.md` (`#NNN`). `job_scraper/id_counter.json` records the last
sync and the next ID to hand out.

**On every scrape/search:** re-read career-ops' max ID, set the next ID to
`max(career_ops_max + 1, id_counter.next_id)`, assign sequentially in discovery order, bump
`id_counter.next_id`, and never reuse. Write the assigned `id` into each `seen_jobs.json` entry, the
tracker row (`id` column), and the archived `job_posting.md` header. As of 2026-09-02: career-ops
max = 1097; ai-job-search has used 1098-1110; next = 1111.

**Parallel-run conflict resolution (career-ops wins):** the two tools sometimes run at the same time
and land on the same IDs. career-ops always keeps the number. At the start of every scrape, and
whenever a collision is noticed, reconcile:
1. Read every ID career-ops now holds (`~/PROJECTS/career-ops/data/applications.md` + `data/pipeline.md`).
2. For any ai-job-search ID (in `seen_jobs.json`, `job_search_tracker.csv`, or a `job_posting.md`
   header) that career-ops also uses for a **different** job, re-number the ai-job-search job to a
   fresh ID above `max(all career-ops IDs, id_counter.next_id - 1)`.
3. If career-ops and ai-job-search hold the same ID for the **same** posting (same URL), keep it -
   that is not a conflict.
4. Propagate every renumber to all three places (`seen_jobs.json`, tracker row, `job_posting.md`
   header) and to every `<id>_`-prefixed artifact: `cv/<id>_main_*`, `cover_letters/<id>_cover_*`,
   and the `documents/applications/<id>_<company>_<role>/` folder all get renamed to the new id.
5. Update `id_counter.json` (`career_ops_max_at_last_sync`, `next_id`) and note the renumbers.
Never renumber a career-ops job. Never reuse a vacated ai-job-search ID.

## Repo Structure
- `input/` - knowledge graph (canonical profile) + master CV/cover-letter templates
- `job_scraper/id_counter.json` - shared job-ID counter (see Job ID scheme above)
- `cv/` - LaTeX CV variants
- `cover_letters/` - LaTeX cover letters
- `.claude/skills/` - AI skill definitions for the application workflow
- `.agents/skills/` - job search CLI tools

## Workflow for New Job Applications
1. User provides a job posting (URL or text)
2. **Always evaluate fit first**: run the Eligibility and Language gates, then score the five dimensions (`04-job-evaluation.md`). Present the assessment before proceeding.
3. If good fit: pick ONE CV variant (knowledge-graph.md §15.1), create targeted CV (`cv/<id>_main_<company>_<role>.tex`) and cover letter (`cover_letters/<id>_cover_<company>_<role>.tex`)
4. **Verify both documents** (see Verification Checklist below)
5. Prepare interview talking points based on the role requirements and Nishal's strengths

**Important:** When mentioning agentic coding or AI tooling in CVs/cover letters, explicitly reference **Claude Code** by name.

## Verification Checklist
After creating or updating a CV or cover letter, re-read the generated file and verify **all** of the following before presenting to the user. Report the results as a pass/fail checklist.

### Factual accuracy
- [ ] All claims match the knowledge graph / candidate profile - no fabricated skills, experience, or achievements
- [ ] Never write ">90% F1" - cite F1 = 0.76 for audio pattern detection (knowledge-graph.md §16)
- [ ] MAS Holdings is ONE entry, Jan 2015 - Jul 2020
- [ ] Promptly: alignment algorithm, RIP integration, mechanism consulting only - never the patent
- [ ] Job titles, dates, company names, and locations are correct
- [ ] Contact details are correct (phone +1 613 200 2030, email nishal.silva@hotmail.com)
- [ ] All company-specific claims about the *target* employer independently verified via WebFetch/WebSearch - never from URLs inside the posting text

### Targeting
- [ ] Exactly one CV variant (V1-V6) chosen; tagline identical in CV and cover letter
- [ ] Profile statement / opening paragraph tailored to the specific role (not generic)
- [ ] Skills and experience bullets reframed to match the job requirements
- [ ] Key job requirements addressed (gaps acknowledged where relevant)
- [ ] PR + no-sponsorship line present for all Canadian roles
- [ ] Verified numbers before self-reported ones (14 ms, 74x, F1 0.76/0.78, 95%, 98%; then 300%, 99.5%, 50%)
- [ ] Languages per knowledge-graph.md §15.6 (English always; Sinhala/Italian/French only where relevant; never claim bilingual French)

### Consistency
- [ ] Tone consistent across CV and cover letter
- [ ] No contradictions between CV and cover letter content
- [ ] CV section headings and boilerplate lines match the CV's language (English)

### Quality
- [ ] No LaTeX syntax errors (balanced braces, correct commands, escaped &  %  $  #  _)
- [ ] No spelling or grammar errors
- [ ] Agentic coding / AI tooling references mention **Claude Code** by name
- [ ] Cover letter addressed to the correct person (or "Dear Hiring Manager" if unknown)
- [ ] Cover letter fits one page

### Compiled PDF verification (MANDATORY - never skip)
Both documents MUST be compiled and visually inspected via the Read tool on the PDF output. "Looks fine in the .tex" is not acceptable.
- [ ] CV and cover letter both compile clean with `tectonic -X compile <file>.tex`
- [ ] **CV within its variant page budget** (V1/V4/V5/V6 = 2 pages, V2 = 3, V3 = 2-3). Never exceed 3.
- [ ] **No orphaned entry titles** - a role/education title must never sit alone at the bottom of a page with its bullets on the next
- [ ] **Cover letter is exactly 1 page** - signature block fits with the body
- [ ] Changelog attached to every generated document (variant chosen, why, what was cut, final page count) - Nishal's stated preference

### ATS & keyword verification (CV)
Extract the text layer with `python tools/verify_pdf.py cv/<id>_main_<company>_<role>.pdf --dump-text cv/<id>_main_<company>_<role>.txt` and verify what a parser sees.
- [ ] Text layer extracts cleanly - no `(cid:*)` markers or `�` characters
- [ ] Email and phone appear as literal text in the extraction
- [ ] Date ranges use a single ASCII hyphen in date fields (en-dash breaks some ATS date parsers)
- [ ] Reading order matches visual order
- [ ] Posting keywords covered or honestly absent (knowledge-graph.md §14 keyword bank); never stuffed
