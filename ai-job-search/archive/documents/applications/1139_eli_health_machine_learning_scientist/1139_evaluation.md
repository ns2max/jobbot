<!-- Job posting: https://jobs.ashbyhq.com/eli/dd8575a8-60e0-472f-a8b9-6f7a6478699d -->

# Job Fit Evaluation — 1139

**Role:** Machine Learning Scientist (on-site Applied ML Scientist)
**Company:** Eli Health (Engineering / ML team)
**Location:** Montreal, QC — in-person
**Deadline:** none stated · **Comp:** not disclosed
**Evaluated:** 2026-09-03 (main-thread; Opus subagent hit a 529) · triage rank_score 79 · /apply Step 1 score **80/100**

## Eligibility Gate: PASS (unverified)
Posting states no citizenship, PR, clearance, or work-authorization requirement. Nishal is a Canadian PR, eligible anywhere in Canada without sponsorship, available immediately (postdoc ended Dec 2025). Low-risk startup; worth confirming nothing on their careers page gates it, but nothing in the ad does.

## Language Gate: PASS
No French requirement stated as a job condition. The only language wording is "communicate findings to technical and non-technical stakeholders" and "produce clear, reproducible Python code". Eli is an anglophone startup (US FDA-registered product, English posting, async English workflows). Nishal: English Native/C2. No flag — his ~A2 French is irrelevant here.

## Scored Dimensions

| Dimension | Score | Notes |
|-----------|-------|-------|
| Technical Skills (30%) | 80 | The role is "scientific problem solving and applied ML, not ML infrastructure": explore data-generating processes; develop/evaluate ML, **signal-processing**, and statistical models; feature engineering, model selection, validation, error analysis; identify confounding, data leakage, measurement variability, distribution shift; design experiments to resolve uncertainty; classical ML and DL when appropriate; reproducible Python beyond notebooks. Direct hits: signal processing (his expertise — DSP, STFT, MFCC, S-transform), evaluation under domain shift and benchmark/ablation design (frozen protocols, RNN-vs-DTW, pattern-set sizes), production-failure diagnosis and monitoring (postdoc + MAS deployed systems), anomaly detection (Forestpin), Python (expert). Gaps: classical-statistics depth (he leans DL/signal over pure statistician — has Youden's-index thresholding, p-value user studies, but not a heavy inferential-stats track record); biochemical/assay-chemistry domain (saliva hormone sensing) is new; PyTorch is secondary to TF/Keras. |
| Experience Match (25%) | 80 | Functionally close: "turn imperfect real-world data into robust, reproducible analyses and models" and "stay connected to how models behave in the real world, diagnose failures, drive new analyses" is the postdoc + MAS pattern — owned the full ML pipeline on noisy streaming sensor data, designed the benchmarks that told real improvements from metric noise, shipped systems with monitoring; Forestpin was anomaly detection on messy structured enterprise data. Medical-signal adjacency: the COVID-19 remote-vitals CV device deployed across hospital wards (GMOA recognition). Gap: no consumer-diagnostics or biochemistry background; "production" for him has meant embedded devices and a factory floor, not an at-home health platform; publication venues are audio/DSP, not health. 5+ yrs professional experience (excl. internships): clears it (~11 total, 5+ ML-centric). |
| Behavioral Fit (15%) | 86 | Near-bullseye. "<25 people, high-performing", "drive their own work, think creatively about open-ended problems, solve proactively", "autonomy and space", async-first, "everything you do results in tangible impact and shapes the company's trajectory", "mission-driven — improve lifelong health at scale". The signature question they hire for — "given the data and the problem, what can we conclude with confidence, what remains uncertain, what should we do next" — is research rigor stated as a job requirement, which is exactly his instinct (benchmarks, ablations, negative results, honest uncertainty). Mild friction: on-site requirement against his stated flexibility (he would relocate); a pure-science role has less of the hands-on systems/hardware/edge-latency building he most enjoys. |
| Location | PASS | Montreal, QC — Canadian; relocation within Canada is acceptable per profile, and Montreal is a bonus (McGill IDMIL/CIRMMT ties). The role is explicitly **in-person** ("on-site Applied ML Scientist", "office and R&D facilities are in Montreal") even though the wider team is distributed — so this is a real relocation from Toronto, not a hybrid. |
| Career Alignment (30%) | 78 | Up: Applied ML Scientist IC title at the right level; medical-signal / wearables / continuous-monitoring is a stated target sector for him (he drafted cold outreach to Oncoustics on an audio-to-ultrasound transfer pitch); research-to-product loop with real ownership; small mission-driven team. Down: much less real-time / edge / audio (his highest-fit area); "not ML infrastructure" means less of the end-to-end systems building he thrives on; early-stage startup risk; comp undisclosed (Series A, likely equity-weighted, may sit below the CAD 120-150k benchmark); no explicit publication scope. |

**Overall: 80/100** (0.30·80 + 0.25·80 + 0.15·86 + 0.30·78 = 24 + 20 + 12.9 + 23.4)

## Verdict: Strong Fit

## Key Strengths
- Signal-processing + statistical-modelling on noisy real-world sensor data is his core: DSP expert, benchmark/ablation design with frozen protocols, evaluation under domain shift.
- The "is this improvement real or just a better metric" discipline is how he already works: designed baseline-and-ablation suites (RNN vs DTW; audio vs MIDI; pattern-set sizes 1/3/10) that quantified accuracy-latency-CPU trade-offs, and kept a written record of experiments including negative results.
- Production-failure diagnosis and monitoring: owned deployed edge ML with monitoring in the postdoc; shipped CV/IoT systems into live manufacturing at MAS with a human-in-the-loop adjudication path; Forestpin anomaly scoring services in production.
- Medical-signal adjacency: COVID-19 remote-vitals CV device deployed across hospital wards (GMOA recognition); medical-signal / neurotech / wearables ML is a target sector.
- Strong Python (expert), reproducible tested pipelines (pytest, CI/CD), clear technical writing (10+ peer-reviewed papers), communication with non-ML domain experts (12-partner EU consortium, group-wide training at MAS).
- Behavioral match to a small autonomous mission-driven team is as strong as any role in the pipeline.
- Eligibility clean; open to relocating to Montreal (McGill CIRMMT bonus).

## Gaps to Address
- **Classical / inferential statistics depth:** frame the statistical-evaluation record (Youden's-index thresholding, p-value user studies, ablation design, uncertainty quantification in benchmarks) honestly; acknowledge that formal experimental-design and inferential-stats rigor at assay scale is an area to deepen.
- **Biochemistry / assay-chemistry / consumer-diagnostics domain:** entirely new; frame the manufacturing and financial-forensics domain ramps as precedent for learning a new applied field fast, and the COVID vitals device as the closest prior health-signal work.
- **PyTorch:** secondary to TF/Keras — the posting says "common ML/data science libraries" without naming a framework, so lead with TF/Keras depth + scikit-learn + the signal-processing stack.
- **Less real-time/edge/audio than his highest-fit roles:** the role is deliberately science-over-infra; position that as a fit (he wants method autonomy and open-ended problems) rather than a gap, but note internally it under-uses his systems/hardware strength.
- **On-site Montreal + startup comp:** real relocation from Toronto against a Series A comp band that may be below target; worth a direct conversation.

## Cover Letter — Special Instructions
None stated. Standard 4-paragraph structure. Worth echoing their signature question ("what can we conclude with confidence, what remains uncertain, what should we do next") as the through-line, since that framing is exactly how he approaches a problem.

## Recommendation
Apply — Strong Fit, and one of the best behavioral matches in the pipeline. Lead with the noisy-sensor-data signal-processing record and the benchmark/ablation rigor that separates real improvements from metric noise; frame the medical-signal domain (COVID vitals device) as the adjacency and be honest that assay chemistry is new. Confirm the on-site Montreal relocation and the comp band before submitting.

## Company Research Checklist
- [x] Website — Hormometer (at-home saliva cortisol monitoring, cartridge + app, minutes to result); ~6 yrs R&D, 2,000+ iterations, women's lifelong hormonal health framing.
- [x] Media — Series A CAD 17M led by BDC Capital Thrive Venture Fund; total ~CAD 28M; Accelia Capital + Telus Global Ventures earlier; US FDA-registered; CES 2025 Best of Innovation in Digital Health.
- [x] LinkedIn — founded 2019, co-founders CEO Marina Pavlovic Rivas + CTO Thomas Cortina; small team.
- [ ] Reviews — no Glassdoor sample found; rely on the posting's culture description + interview questions.
- [x] Written to `company_research/eli-health.json`.
