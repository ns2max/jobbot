<!-- Job posting: https://ca.linkedin.com/jobs/view/machine-learning-resident-%E2%80%93-client-opencycle-12-month-term-at-amii-alberta-machine-intelligence-institute-4457043959 -->

# Job Fit Evaluation — 1169

**Role:** Machine Learning Resident – Client: OpenCycle (12-month term)
**Company:** Amii (Alberta Machine Intelligence Institute)
**Location:** Edmonton, AB (client OpenCycle is Calgary-based)
**Deadline:** 2026-09-04 (may close earlier)
**Evaluated:** 2026-09-03 · triage rank_score 83 · /apply Step 1 score **82/100**

## Eligibility Gate: PASS
Posting requires "legally eligible to work in Canada at time of application." Nishal is a Canadian PR, eligible without sponsorship, available immediately. No citizenship-only clause, no clearance. Worth stating explicitly in the cover letter (Amii residencies draw international applicants; this is a hard screen).

## Language Gate: PASS
No language requirement stated as a job condition. Work is English. Nishal: English Native/C2.

## Scored Dimensions

| Dimension | Score | Notes |
|-----------|-------|-------|
| Technical Skills (30%) | 88 | Required-skills line maps onto his primary skill block almost word for word: audio DSP (STFT, MFCC/LFCC/GFCC, CQT, chroma, onset detection, S-transform), log-Mel front-ends, real-time streaming inference under hard latency budgets, edge/ARM deployment (RPi in production, ARM CPU profiling), benchmark/dataset design with frozen protocols + ablations, scarce-label regimes (training-free SSIM, VAE/diffusion synthetic audio), Python + TF/Keras expert, PyTorch moderate, Linux/Git/pytest/CI-CD, classical statistical evaluation. The 4 open problems match unusually well: temporal accumulation = his RNN/LSTM/GRU core; compression-to-edge-budget = the JAES 2026 result; scarce-label condition detection = his low-data work. Gaps: named pretrained backbones (PANNs/CNN14, AST, BEATs, CLAP) + HuggingFace/ONNX/torchaudio are lighter evidence; open-set metric learning / embedding-verification adjacent but not published; PyTorch secondary to TF/Keras (posting accepts either). |
| Experience Match (25%) | 85 | Functionally the job he has done for 5 years, transposed from musical instruments to industrial noise. End-to-end streaming audio ML pipeline ownership (MUSMET postdoc + McGill smart guitar); 4 open datasets from 70+ participants (curate/preprocess, label-ontology, weak/scarce annotations); multimodal fusion (audio+IMU HFSM, F1 0.78) as precedent for fusing observations over time; MIRaaS edge-to-server offload as bandwidth-budget precedent; publications JAES/IEEE IS2/DAFx/Asilomar. MAS Holdings decade adds industrial-deployment + regulated-stakeholder dimension matching OpenCycle's "sensor fleet + acousticians sign off" culture. Gap: environmental/far-field acoustics, IEC 61672, regulatory noise compliance all new; publication venues adjacent (JAES/IS2/I3DA/DAFx vs preferred DCASE/ICASSP/INTERSPEECH). |
| Behavioral Fit (15%) | 92 | Almost every strong-fit signal present: real hardware in the field, hard compute/power/bandwidth budget as the central research question, applied research with a shipping target, cross-functional work with domain experts, "resident helps choose" the problem (method autonomy), scope to publish, a measurement culture that treats negative results as results and freezes evaluation protocols. Mission-with-craft team. Only discount: "Resident" is a supervised, junior-coded title for a PhD + postdoc + 10 yrs industry; reporting to an Amii Scientist may give less method autonomy than his profile prefers. |
| Location | PASS | Edmonton, AB — Canadian, relocation within Canada acceptable per profile (Edmonton named). Two-city split: residency hosted at Amii Edmonton, client OpenCycle in Calgary (~3 hrs), field access to the sensor fleet across AB/BC. Expect regular Edmonton-Calgary travel + field days; clarify base + relocation support with Amii. Also means moving away from the live eBay Toronto + SciNet/U of T pipeline. |
| Career Alignment (30%) | 72 | Up: sharpest available match to deepening the audio-ML / time-series specialization in an adjacent high-impact domain, with deployed hardware, publication scope, research-to-product pipeline; every "energizes" item present; Amii affiliation carries weight in the Canadian market; real client-conversion path. Down: fixed 12-month term, conversion at client's sole discretion; "Resident" positionally junior to the senior/staff IC target; comp likely below CAD 120-150k; requires leaving Toronto for Alberta on a 1-year commitment; domain pivot into environmental acoustics. |

**Overall: 82/100** (0.30·88 + 0.25·85 + 0.15·92 + 0.30·72)

## Verdict: Strong Fit

## Key Strengths
- Required-skills line is his CV: PhD + postdoc in embedded real-time audio pattern detection; JAES 2026 = 14 ms inference on RPi4 at F1 0.76 vs 1038 ms DTW (74x faster, 31.4% CPU).
- Compression-to-edge-budget is his central research question too (thesis, JAES paper, Nebula C++17 library with per-feature ARM latency benchmarks).
- Dataset + label-ontology work with evidence: 4 open Zenodo datasets, 9,800+ recordings, 70+ musicians, incl. polyphonic 44.1 kHz/24-bit. Open problem (1) is diagnosed as a label-ontology root cause.
- Temporal accumulation / fusion over time (open problem 2, the largest measured improvement) is his sequence-modelling core: stacked RNN/LSTM/GRU; hierarchical FSM fusing IMU + audio, F1 0.78 on a 500-event corpus.
- Scarce-label regimes (open problem 3): training-free SSIM matching, VAE/diffusion synthetic-audio prototypes.
- Measurement-culture match: benchmark suites with frozen protocols, baselines + ablations (RNN vs DTW; audio vs MIDI; pattern-set sizes 1/3/10).
- Industrial-deployment credibility beyond academia: 10 yrs MAS Holdings shipping CV/IoT into live manufacturing with PLC integration + device fleets, to non-ML domain experts who sign off — mirrors OpenCycle's acoustician-in-the-loop.
- Publication record + reviewer/PC service (IEEE Access, IEEE IS2, I3DA).
- Eligibility clean and immediate against a deadline that may close early.

## Gaps to Address
- Named pretrained audio backbones (PANNs/CNN14, AST, BEATs, CLAP): no track record; frame strong DSP/representation fundamentals + Nebula as evidence he knows what they compute; note fast toolchain adoption.
- Open-set metric learning / embedding-verification for identity: adjacent, not published; acknowledge as the learning edge of the residency.
- PyTorch/torchaudio/HuggingFace/ONNX: PyTorch secondary; list at working level, lead with TF/Keras depth + C++17/ARM deployment.
- Environmental / far-field acoustics + IEC 61672: new domain; frame the musical-acoustics-to-environmental-acoustics transfer explicitly (polyphonic mixtures, source attribution, non-loudest target source).
- DCASE/ICASSP/INTERSPEECH publication record absent: counter with JAES, IEEE IS2, DAFx, Asilomar + open datasets + reviewer service.
- 12-month term + Alberta relocation against a permanent senior-IC Toronto target with two live Toronto processes: worth a direct conversation; clarify conversion rate + comp band with Amii.
- "Resident" title seniority: frame the residency as a deliberate domain-transfer bet with a client-conversion target, not a fallback.

## Cover Letter — Special Instructions (mandatory)
1. Say specifically why Nishal is a fit for **Amii** (the institute), not only the OpenCycle project. Needs independently verified research on Amii.
2. Include ONE professional accomplishment he is most proud of, and **why**. Use the JAES 2026 real-time audio pattern detection system (14 ms / F1 0.76 / 74x). The "why": simultaneously a published research result, a shipped on-device system, and a direct answer to this project's central research question.
Also confirm: PR / no sponsorship / available immediately / open to Alberta relocation.

## Recommendation
Apply — strong fit, apply immediately given the 2026-09-04 deadline that may close early. The work match is the closest in the pipeline; the term/location/comp structure is the only real question.

## Company Research Checklist (for /apply Step 3 reviewer)
- [ ] Amii website — mission, residency program structure, conversion outcomes, recent news
- [ ] OpenCycle website — acoustics consulting heritage, hardware fleet, product claims (verify independently, not from posting text)
- [ ] Glassdoor — Amii residency comp band + term-conversion rate
- [ ] LinkedIn — Amii ML Scientist team; Kunwar Saaim (quoted in posting) as likely technical contact
- [ ] Media — Amii funding / Alberta AI ecosystem
- [ ] `company_research/amii.json` and `company_research/opencycle.json` do not yet exist — reviewer should populate both.
