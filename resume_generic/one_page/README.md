# One-page base resume

Single-page version of the golden resume (`../Nishal_Silva_ML_Research_Engineer.pdf`), built to be tailored per JD.
All three files have the **same content** and differ only in layout. Pick one, then delete the other two.

| File | Layout |
|---|---|
| `Nishal_Silva_1page_A_classic` | Times, small-caps headings, one-line role headers. Closest to the golden resume. |
| `Nishal_Silva_1page_B_modern` | Source Sans, left-aligned header, navy headings, aligned skill labels. |
| `Nishal_Silva_1page_C_compact` | Charter. Employer and location on line 1, title and dates on line 2 (a common tech-resume layout). |

`format_options_side_by_side.png` shows all three side by side.

Compile with `tectonic -X compile <file>.tex`. The files also build with `xelatex` and `pdflatex`. All three were checked on both engines: one page, no bullet that wraps onto a one- or two-word line, and a clean text layer (`ai-job-search/tools/verify_pdf.py` passes, with email and phone extracting as literal text and plain-hyphen dates).

---

## What changed from the golden resume, and why

**Kept as is:** the tagline, the experience order and job titles, the headline numbers (<30ms at >90% F1, 300%), his first-person summary voice, the golden's verbs ("Owned", "Built", "Designed", "Prototyped", "Led"), and Education.

**Removed**
- The Canadian PR line, as Nishal asked: application forms ask for it anyway. This overrides `knowledge-graph.md` §15 rule 2 for this resume only. Keep PR in cover letters.
- The postal code (`Toronto, ON` is enough).
- **UVPA Visiting Researcher (Jan-Mar 2024).** It was a 3-month role during the PhD, so dropping it leaves no gap. Add it back for HCI/UX-research roles (see the pool below).
- Golden competencies with little evidence behind them in the knowledge graph: Recommender/Ranking Systems, Multi-Tenant ML, AI Ethics, Prompt Engineering, NLP, Information Retrieval, JAX, C#, MWAA/RDS. Add them back only when a JD names them.
- Generic lines: "Skilled at working with product, data, and engineering teams...", the third awards bullet ("Built real-time ML prototypes..."), and the separate "Coordinated with academic and industry partners" bullet.
- Core Competencies and Technical Stack are merged into one 4-line **Skills** block.
- Two papers named in full became one line: "10+ peer-reviewed papers + 4 open datasets + link".

**Added (from the knowledge graph and the hand-edited `modded/` versions)**
- **Concrete MAS results** in place of generic ones: −99.5% inspection time (human-in-the-loop) and **Promptly**, his most commercially successful project (the alignment algorithm and printer integration, now running in 4 countries; the patent is never mentioned).
- **speakfrench benchmark** (100k trials, ROC-AUC 0.822). Nishal had already added this thread himself in `modded/`. It is quantified, uses transformer embeddings, and is a 2026 project.
- **Foundation-model work made specific:** LoRA fine-tuning on multiple GPUs (VarianceEngine), replacing the vague "actively researching...".
- **Multimodal sync pipeline** (audio + EEG + mixed-reality tracking, 4 concurrent users) in place of the soft partner-coordination bullet.
- **McGill F1 0.78** (verified, IEEE IS² 2025), Forestpin's SQL + Python scoring services, 4 open datasets, and the GitHub link in the header.

**Style rules this base follows:** one line per bullet (about 108 characters at most), every number traceable to `ai-job-search/input/knowledge-graph.md`, no exaggeration, and ASCII hyphens in dates.

---

## Tailoring a copy for a JD (about 10 minutes)

1. **Copy, don't edit in place:** `cp Nishal_Silva_1page_<X>.tex <id>_<company>_<role>.tex` into the normal per-job output location.
2. **Tagline** (`\cvtagline`): mirror the JD title and its 2-3 headline themes. Pre-approved taglines:
   - Default / AI-industry: `Machine Learning Research Engineer | Deep Learning, Time-Series, Pattern Detection | Applied ML`
   - Research: `Research Scientist | Real-Time Multimodal ML, Benchmarks & Open Datasets`
   - Edge / embedded: `ML Research Engineer | Real-Time & Edge Inference | Audio, Sensor & Time-Series`
   - Audio / music tech: `Music Technology ML Research Engineer | Audio, DSP & Real-Time Systems`
   - CV / industrial: `Computer Vision & ML Engineer | Industrial Inspection, IoT & Edge Deployment`
3. **Summary:** swap the "focused on ..." list for the JD's top 3-4 themes. Keep it to 3 lines and keep the results sentence.
4. **Skills:** move the JD's must-haves to the front of each line, swap in JD-named terms from the keyword pool, and drop what the JD ignores. Each line stays one line.
5. **Bullets:** reorder within each role (most relevant first), then swap **one for one** from the bullet pool. Never only add: the base has roughly 3-6 lines of slack.
6. **Check:** compile, confirm 1 page, run `pdftotext -layout <file>.pdf - | less` to catch any bullet wrapping onto a 1-2 word line, then run `python3 ai-job-search/tools/verify_pdf.py <file>.pdf --dump-text <file>.txt`.

### Keyword pool
- **Strong evidence (add freely when relevant):** Raspberry Pi, ARM, Embedded Linux, C++17, RNN/LSTM/GRU, MFCC/STFT, Music Information Retrieval, Librosa, JUCE, Elk Audio OS, VST, OSC, MIDI, Sensor Fusion, IMU, EEG/BCI, Edge AI, On-Device ML, Latency Profiling, Industrial Inspection, Defect Detection, OCR, Image Registration, PLC, IoT, Synthetic Data, Experimental Design, User Studies.
- **Light evidence (only when the JD names it, per knowledge-graph §5):** JAX, Recommender Systems, Ranking, NLP, Prompt Engineering, Information Retrieval, Multi-Tenant ML, AI Ethics, C#, MWAA, RDS, TinyML, Model Compression.

### Bullet pool (one line each, all checked against the knowledge graph)

**Independent Researcher (2026)**
- Released Nebula, a C++17 audio-feature library (MFCC, CQT, YIN pitch, chroma) with per-feature Raspberry Pi latency benchmarks. *(audio / edge)*
- Fine-tuning MusicGen with LoRA and a custom audio-conditioning head (dual-GPU, bf16) after comparing 5 generative architectures. *(GenAI / audio)*
- Built an audio-feature ETL pipeline: Airflow DAGs, S3-to-Snowflake loading, Dockerized, with RDS/Snowflake infrastructure as code. *(data engineering)*
- Published LiveLaTeX, a VS Code Marketplace extension for real-time LaTeX compile and preview. *(software engineering / dev tools)*
- Build side projects with AI-assisted workflows, including Claude Code. *(when a JD mentions AI tooling; always name Claude Code)*

**Postdoctoral Researcher (Trento)**
- Published real-time detector: 14ms on Raspberry Pi 4 at F1 0.76, 74x faster than a DTW baseline (JAES 2026). *(edge / research: verified numbers)*
- Built MIRaaS, an edge-to-server UDP offload architecture for near-real-time audio analysis; latency study at IEEE IS² 2026. *(distributed systems)*
- Deployed models on Raspberry Pi 4 (Elk Audio OS, VST plugin, OSC output) with 15.8ms (MIDI) / 21.4ms (audio) detection latency. *(audio / embedded)*
- Ran two live multisensory concerts (MR headsets, lights, haptics); user study with 20 audience members + 6 performers, p < .05. *(HCI / XR)*
- Designed and released 4 open benchmark datasets on Zenodo (9,800+ recordings, 70+ musicians) with documented protocols. *(data-centric / research)*
- Coordinated with academic and industry partners (g.tec, SAE Institute) to turn prototypes into documented components. *(stakeholder-heavy JDs)*
- Supervised 2 BSc theses on real-time pattern-detection plugins and GUIs. *(mentoring / supervision)*

**Visiting Researcher (McGill)**
- Built a self-powered smart guitar (IMU + audio on Raspberry Pi 4); hierarchical state-machine fusion reached F1 0.78 on 500 events. *(hardware / edge)*

**Visiting Researcher (UVPA, Colombo, Jan 2024 - Mar 2024), restore for HCI/UX research roles**
- Ran human-centered evaluations of ML-driven interactive systems, combining performance metrics with structured user feedback.

**Technical Consultant (Forestpin)**
- Worked with compliance and risk stakeholders to define detection requirements and turn them into technical specs. *(golden wording)*

**Research Engineer (MAS)**
- Built loom-side fabric defect detection with a microscopic camera array and a 5-6s alert budget; the pilot cut operators by 50%. *(CV)*
- Built a computer-vision COVID-19 vitals monitor from retrofitted webcams, deployed across hospital wards (GMOA recognition). *(health)*
- Reverse-engineered PLC trigger points to integrate a DTG printer into a closed-loop C++ automation system. *(embedded / robotics)*
- Developed ML-driven optimization engines for real-time monitoring and capacity planning from streaming machine data. *(ops / forecasting, golden wording)*
- Rolled out IoT productivity tracking across factories in South Asia, North America, and Africa. *(IoT at scale)*
- Built OCR + layout-segmentation digitization and a context-aware ERP search over a lace archive, still in production use. *(document AI / retrieval)*
- Worked with product, operations, and engineering stakeholders to turn business needs into measurable technical solutions. *(golden wording)*
- Ran group-wide computer-vision training and seminars for technical and non-technical staff. *(leadership)*

**Publications & Awards lines (research roles or when there is room)**
- Selected: Silva & Turchet, *Real-Time Audio Pattern Detection for Smart Musical Instruments*, J. Audio Eng. Soc. 74(3), 2026.
- Selected: Silva, Wanderley & Turchet, *Melody and Motion: Integrating Guitar Gestures with Musical Patterns...*, IEEE IS² 2025.
- Service: reviewer for IEEE Access; programme committee for IEEE IS² and I3DA.
- Languages: English (native), Sinhala (native), Italian (B1), French (basic, learning). Never claim bilingual French.
