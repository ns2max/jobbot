# Jumio: Senior Machine Learning Engineer (Computer Vision / Biometrics), Montreal

## Company Dossier, Role Breakdown and Recruiter-Screen Prep

**Candidate:** Nishal Silva, PhD · **Job ID:** 1112 (career-ops) · **Applied:** 2026-10-17 · **Stage:** recruiter phone screen\
**Posting:** https://job-boards.greenhouse.io/jumio/jobs/4709657005 (live on the Greenhouse API, checked 2026-10-21)\
**Submitted documents:** `archive/resumes/1112_jumio_senior-machine-learning-engineer.pdf` and `archive/cover-letters/1112_jumio_senior-machine-learning-engineer.pdf`\
**Prepared:** 2026-10-25

> **How to read this.** Part 1 explains the company. Part 2 explains the job and the work. Part 3 covers salary. Part 4 is the call itself. If you only have 15 minutes, read the **Quick-Start page** below and then §4.4 (likely questions).

---

## Quick-Start (one page)

1. **The company.** Jumio is a private, PE-backed identity-verification company headquartered in Sunnyvale, CA, founded in 2010. People photograph an ID and take a selfie. Jumio checks the ID is real, reads it, confirms the person is live, and matches the face to the ID. Customers include banks, fintech, crypto, gaming and airlines. It's had a lot of leadership change: a **new CEO, Mark Lorion, since April 2026**.
2. **The job.** You'd be a CV engineer on the **Montreal Biometrics team**, building and benchmarking face models (detection, image quality, recognition), running Airflow data pipelines, and making models fast (quantization, distillation, ONNX/TensorRT) on AWS. The posting says outright that **you'll ramp up on biometrics**, so face experience isn't expected.
3. **Your hook.** *Production camera CV + benchmarking across operating conditions + low-latency inference.* Your MAS work (checking printed labels against reference artwork, OCR, layout segmentation) is the closest thing you have to Jumio's document-verification core.
4. **Salary.** Expect about **CAD $135K–$160K base** at Senior, probably around $150K. Ask for their band first. If pressed: "**$150K–$165K base, depending on level and total package.**"
5. **Say your gap first:** "I haven't done face biometrics; your posting frames this as ramping up on the domain, which is why I applied to this req."
6. **Ask the recruiter:** how this role is levelled against the two Staff/Senior biometrics openings; the band; next steps; hybrid policy and relocation; whether the team works in English.
7. **Fix before the technical rounds:** your CV says ">90% F1", but the published figure is **F1 0.76**. Always say 0.76.

---

# PART 1: THE COMPANY

## 1.1 Snapshot

| Item | Detail |
|---|---|
| Legal name | Jumio Corporation (private) |
| Founded | 2010, Palo Alto, by Daniel Mattes |
| Headquarters | Sunnyvale, California |
| Other locations | Vienna and Linz (Austria, the original R&D base); **Montreal (AI Labs, since 2018)**; London; India (remote engineering, Jumio India Pvt Ltd); Lenexa, Kansas (current robotics/ML research posting) |
| Employees | Not disclosed. Estimates range from ~610 (Tracxn, May 2026) to ~1,500 (PitchBook). Safe phrasing: "several hundred to about a thousand." |
| Revenue | Not disclosed. Third-party estimates conflict ($50M–$264M), so don't quote a number. |
| Owners / backers | **Centana Growth Partners** (owner since 2016), **Great Hill Partners**, **Millennium Technology Value Partners** |
| Last major raise | $150M growth investment, March 2021 |
| Scale claims (jumio.com) | 1B+ transactions processed; 5,000+ supported ID document types; 300+ patents and applications; 30M+ identities in the "Identity Graph"; ~120 transactions per second |
| Category | Identity verification (IDV) / eKYC / AML: "identity intelligence" |
| Values | **IDEAL**: Integrity, Diversity, Empowerment, Accountability, Leading Innovation |

## 1.2 History

| Year | Event | Why it matters to you |
|---|---|---|
| 2010 | Founded by Daniel Mattes in Palo Alto. Early backers included Andreessen Horowitz and Eduardo Saverin (Facebook co-founder). | Started as card/ID scanning for mobile payments ("Netverify"). |
| 2015 | Mattes resigned after a board investigation. The company restated its 2013–2014 results. | Background only. **Don't bring this up.** |
| 2016 | Chapter 11 bankruptcy (March). Bought by **Centana Growth Partners** (May). **Stephen Stuut** became CEO. | This is the start of the "new Jumio." |
| 2018 | **Jumio AI Labs Montreal** opened (7 staff, targeting 30 by end of 2019) for production ML: data extraction, fraud detection, risk scoring, face recognition speed and accuracy. | **This is your team's origin.** |
| 2019 | The SEC charged the former CEO and CFO over the 2013–14 revenue overstatement. Both settled. | Background only. |
| 2020 | Bought **Beam Solutions'** AML transaction-monitoring platform. **Robert Prigge** was CEO. | Moved from ID checks toward full compliance ("KYX platform"). |
| 2021 | **$150M** growth investment (March). Announced the **4Stop** acquisition (KYB/KYC data hub, 650+ data sources), completed Jan 2022. **Bala Kumar** joined as product/tech leader. | Platform era: orchestration and risk signals. |
| 2023 | Laid off **100+** staff (January, confirmed by the company). A BIPA biometric-privacy suit tied to Binance survived a motion to dismiss. | Industry-wide downturn; biometric privacy is a live legal risk. |
| 2025 | **Jumio Liveness Premium** launched (June) against deepfakes and injection attacks. **ISO/IEC 30107-3 Level 2** PAD conformance via the iBeta lab (October). | Biometrics is the flagship, and the face models are core IP. |
| Jan 2026 | Robert Prigge left. **Bala Kumar** became President and interim CEO. | Leadership change. |
| Apr 2026 | **Mark Lorion** (former CEO of Tempo Software) named CEO on Apr 27. Kumar stays as President and Chief Product & Technology Officer. **Jumio Watch** launched. | A new CEO brought in for growth. |
| 2026 | Q2: Trinsic partnership (digital IDs from 60+ countries), selfie.DONE expanded in LATAM. Q3 (released Oct 21): **selfie.DONE rolled out globally**, 30+ new customers. Leader in the QKS SPARK Matrix for the third year in a row. | Reusable biometric identity is the growth bet. |

## 1.3 What Jumio sells

| Product | What it does | ML / CV inside (★ = likely your team's work) |
|---|---|---|
| **ID Verification** | User photographs a passport, licence or ID card. Jumio classifies it, checks it's authentic, and extracts the data. | Document detection and classification across 5K+ ID types; tamper/forgery detection; OCR, MRZ and barcode reading; capture-quality checks (blur, glare, cropping) |
| **Selfie Verification / Biometrics** | Confirms the person holding the ID is the real owner. | ★ face detection; ★ face image quality; ★ **1:1 face match** (selfie ↔ ID photo); ★ **age estimation**; ★ checks for a **sleeping person**, **multiple people**, **face morphing** |
| **Liveness / Liveness Premium** | Proves a live human is present, not a photo, screen, mask or deepfake. Premium adds **randomized colour sequences / active illumination**. | ★ presentation-attack detection (PAD); deepfake and injection-attack detection; ISO 30107-3 Level 2 conformant |
| **selfie.DONE** | Reusable identity: a returning verified user just takes a selfie, no ID scan. Rolled out globally Q3 2026. | ★ face recognition against stored templates, which needs very low false-match rates; template security |
| **Jumio Identity Graph / Cross-Transaction Risk** | 30M+ known identities, used to score reputation and block repeat fraudsters. | ★ **1:N face search**, so vector DBs and ANN search (a listed nice-to-have); graph-based risk models |
| **Jumio Watch** (Apr 2026) | Continuous risk monitoring after onboarding. | Risk models, anomaly detection |
| **Jumio Smart** | Positioned as contextual identity intelligence across the customer lifecycle. | Orchestration and risk scoring |
| **Risk Signals, AML Screening, Gov't DB / Address checks, Doc Proof, Video Verification, Authentication, Fastfill, Jumio Go** | Data and compliance add-ons: sanctions/PEP screening, database checks, proof of address, re-authentication, form auto-fill. | Mostly data and rules; Doc Proof and Fastfill use OCR |
| **Jumio Platform (KYX)** | Orchestration, rules engine, analytics, AI risk scoring that ties everything together. | Platform engineering |

**Distribution:** web and mobile SDKs (iOS/Android), so some models run **on the device** for capture guidance. Server-side processing runs on **AWS**, and AWS is also a listed partner. Other partners include Microsoft, Oracle and Sift.

## 1.4 How one verification works, and where your models sit

```
User opens a bank or crypto app  →  Jumio SDK (mobile/web)
  1. CAPTURE      camera guidance on-device: is the document in frame? blur? glare?   ← on-device CV (CoreML/LiteRT)
  2. DOCUMENT     classify ID type → authenticity / tamper checks → OCR, MRZ, barcode  ← document CV
  3. SELFIE       face detection → face image quality gate → liveness / PAD            ← ★ Biometrics team
  4. FACE MATCH   embed selfie + ID portrait → 1:1 similarity → threshold decision     ← ★ Biometrics team
  5. EXTRA CHECKS age estimation, morph detection, multiple faces, sleeping person    ← ★ "face attributes"
  6. RISK         Identity Graph 1:N search (repeat fraudster?), risk signals, AML     ← ANN search + risk models
  7. DECISION     approve / reject / human review → customer gets the result via API
```

**What "quality assessment" in the JD means:** step 3's quality gate decides whether the selfie (or the ID portrait) is good enough to match on. A bad gate causes false rejects for real users (lost revenue) or lets attacks through. It's the same problem as your MAS quality overlay: decide automatically whether an image is usable.

**What "benchmarking across datasets and operating conditions" means:** measuring match and liveness error rates across phones and cameras, lighting, ID types, countries, ages, skin tones and attack types, and proving there's no demographic bias. It's commercially and legally essential.

## 1.5 Customers and industries

- **Industries:** financial services and banking, fintech and payments, BNPL, **crypto**, **gaming and sports betting**, **travel and airlines**, sharing economy and mobility, telcos, healthcare, education, public sector, retail.
- **Customers named on jumio.com:** Webull, United Airlines, Alaska Airlines (travel-document verification in its app), Stanleybet (says onboarding takes half the time), Personal Pay. Binance has been reported as a client (named in the 2023 BIPA case).
- **Buyers care about:** pass rates for genuine users (conversion), fraud caught, speed (seconds per verification), global document coverage, certifications (ISO 30107-3), regulatory compliance, and price per verification.

## 1.6 Market and competitors

| Competitor | One-line position |
|---|---|
| **Onfido** (owned by Entrust since 2024) | Closest historical rival: document + selfie IDV with a strong AI story |
| **Veriff** | Estonian IDV, strong in video and fraud intelligence |
| **Persona** | Developer-friendly, configurable identity platform; fast-growing |
| **Socure** | US identity graph and risk scoring; heavily funded |
| **Incode** | Biometrics-first IDV with on-device focus |
| **AU10TIX** | Document forensics at scale (Israeli) |
| **Sumsub, Trulioo, IDnow, Mitek, HyperVerge, Shufti Pro** | Global and regional IDV/KYC players |

**Market dynamics:**
1. **Deepfakes and injection attacks** are the main 2025–26 threat, and liveness is the battleground.
2. **Reusable identity and digital IDs** (mobile driver's licences, EU digital identity wallets) could reduce document scans, which is why Jumio pushes selfie.DONE and the Trinsic partnership.
3. **Consolidation** (e.g., Entrust buying Onfido).
4. **Pricing pressure** from cheaper regional vendors.

Jumio positions itself as the premium, enterprise, global-coverage option.

## 1.7 Leadership

| Person | Role | Note |
|---|---|---|
| **Mark Lorion** | CEO (since Apr 27, 2026) | Former CEO of Tempo Software (Atlassian ecosystem). An operator/growth CEO. Some press spells it "Lorian," so check jumio.com. |
| **Bala Kumar** | President, Chief Product & Technology Officer | Joined 2021; interim CEO Jan–Apr 2026. **Engineering, including Biometrics, reports up to him.** |
| Board / owners | Centana, Great Hill, Millennium | PE ownership means growth targets, efficiency pressure, and an eventual exit (sale or IPO). |

The Montreal hiring manager isn't named publicly. Ask the recruiter for the name, then look the person up on LinkedIn before the technical round.

## 1.8 Montreal: Jumio AI Labs

- Opened Aug 2018 as Jumio's second AI centre after Vienna. Early coverage emphasised **face recognition speed and accuracy**, data extraction and fraud detection.
- In 2026 all three Montreal openings are CV/biometrics roles (§2.1), so **Montreal is the biometrics/CV hub**.
- Remote ML hiring also happens in India and Austria, so expect collaboration across time zones (Montreal ↔ Vienna ↔ India).
- Office address and hybrid policy aren't public. **Ask on the call.**

## 1.9 Culture and employee sentiment

| Signal | Reading |
|---|---|
| Glassdoor overall | ~3.9–4.2 / 5; ~75–79% would recommend (325–338 reviews, Sept 2026) |
| Culture & values | 3.9 / 5, **down ~6%** year-on-year |
| Work-life balance | 3.9 / 5, down ~4%; reviewers say it "varies dramatically by team" |
| Positives | Easy access to top management, interesting technical problems, global team |
| Negatives | **Repeated layoff waves** (100+ confirmed Jan 2023; reviewers describe more waves 2023–2025), doubts about transparency, slow or ghosted hiring communication (Jumio has publicly acknowledged this) |

**What this means for you:**
- This is a real company with a real product and strong biometrics IP, but expect PE-style cost discipline.
- A CV/biometrics team that is **actively hiring three roles** is a good sign: it's an area they're investing in.
- Still, ask about team stability and roadmap (§4.6).

## 1.10 Legal and regulatory context (useful vocabulary; don't lead with it)

- **Biometric privacy law** shapes the work: GDPR Art. 9 (biometrics are special-category data); **Quebec Law 25** plus the requirement to declare biometric databases to the **CAI**; Illinois **BIPA** (Jumio faced a 2023 BIPA suit over Binance users); Texas and Washington biometric laws; the **EU AI Act** (remote biometric identification is high-risk).
- **Consequences for engineering:** data minimisation, retention limits, consent tracking, and careful sourcing of training data. That's why the JD mentions **synthetic data** and "privacy, security and compliance."
- **Standards they sell against:** ISO/IEC 30107-3 (PAD, Level 2 achieved Oct 2025), ISO/IEC 19795 (performance testing), ISO/IEC 29794-5 (face image quality), and NIST FRTE/FATE evaluations.

---

# PART 2: THE ROLE

## 2.1 Three Montreal reqs, and where you sit

| Req | Title | Bar | You |
|---|---|---|---|
| **4709657005 (yours)** | Senior Machine Learning Engineer | 5+ yrs ML with a CV focus. **"Ramp up on the biometrics domain."** Contribute, collaborate, mentor. | ✅ |
| 4685786005 | Senior MLE – (Biometrics), "MLE IV" | **3+ yrs biometrics/face analysis**. *Lead* face recognition. Staff/Senior. | ❌ |
| 4713201005 | MLE – (Computer Vision), "MLE IV" | Staff/Senior, deep face recognition, **practical** fairness mitigation, multi-GPU scaling | ❌ |

**Interpretation:** the team hires face-recognition leads through the IV reqs and strong CV engineers through yours. Your level is probably **MLE III / Senior**, and the posting says the level is "determined after interviews," so there's upside. You'd likely work **under or alongside an MLE IV/Staff lead** who owns the face-recognition architecture.

## 2.2 Likely team shape (inferred, not confirmed)

- **Biometrics / Computer Vision team, Montreal:** probably 5–15 ML engineers. It may have a manager or Head of Biometrics, Staff/IV leads per area (recognition, liveness/PAD, attributes), and Senior/mid engineers like this role.
- **Partner teams:** data engineering (the Bangalore Biometrics data-engineer posting suggests the data pipeline is shared with India), the platform/SDK teams that ship models to mobile, the fraud/risk ML team (India "MLE IV – Fraud"), product managers, and compliance/legal.
- **Customers of your models:** the Jumio Platform API (server, AWS) and the mobile/web SDKs (on-device).

## 2.3 What you'd actually do, JD line by line

| JD line | What it means day to day | Your nearest experience |
|---|---|---|
| *Design and develop CV models and pipelines: face detection, quality assessment, recognition* | Train and fine-tune face detectors (RetinaFace/SCRFD-style), quality regressors (score which selfies are usable) and embedding models (ArcFace-style losses). Write the preprocessing: alignment, cropping, normalisation. | MAS: garment detection/segmentation, defect detection, quality overlays; template + feature matching |
| *Benchmarking across datasets and operating conditions* | Build evaluation harnesses: FNMR at a fixed FMR, DET curves, APCER/BPCER for liveness, breakdowns by device, lighting, ID type, country, age and skin tone. Write the reports that go to product and compliance. Compare against NIST-style protocols. | **Your strongest match:** JAES benchmark suites, ablations, worst-case datasets (DoMP/DoPP/DoDP), F1 vs latency vs CPU trade-off studies |
| *Train and optimise with PyTorch / TF / JAX* | GPU training on AWS. Experiment tracking. Hyper-parameter sweeps. Probably mostly PyTorch. | TF/Keras (expert), PyTorch (proficient), dual-GPU LoRA training (VarianceEngine) |
| *End-to-end pipelines; Airflow for data ingestion and cleaning* | DAGs that pull production samples (with consent and retention rules), de-duplicate, label or pseudo-label, balance demographics, version datasets, and trigger training and evaluation. | MAS real-time ingestion + ETL; melodiq Airflow → S3 → Snowflake; MWAA on CV |
| *Low-latency inference: quantization, distillation, TensorRT/ONNX; deploy on AWS* | Export to ONNX, build TensorRT engines (FP16/INT8 calibration), distil large teachers into small students, measure p50/p95 latency and cost per verification, and package for serving (likely containers on ECS/EKS/SageMaker). | 14 ms on RPi4 (74× faster), ARM profiling, OS scheduling, ONNX, compression |
| *Mentor ML engineers; technical best practices* | Code and design reviews, evaluation standards, onboarding docs. | MAS CI/CD + code review + CV training; 2 BSc theses supervised |
| *Fairness & ethics awareness* | Demographic-differential analysis; dataset balancing; maybe synthetic faces to fill gaps. | Performer-diversity dataset design; user studies (new territory for faces) |
| Nice-to-haves: ANN/vector DB, GANs/diffusion synthetic data, CoreML/LiteRT, privacy | 1:N search for selfie.DONE and the Identity Graph; synthetic faces; on-device capture models | VAE/diffusion synthetic data (McGill); edge deployment; C++ |

## 2.4 Likely first-6-month projects (best guesses)

1. **Onboarding (weeks 1–4):** learn the face pipeline, evaluation sets and metrics. Reproduce the current model's benchmark numbers. Ship one small improvement or fix.
2. **Face quality model:** improve the quality gate to cut false rejects on real users, for example on low-light or older-phone captures. Measure by pass-rate lift at constant fraud.
3. **Benchmark harness and fairness report:** extend evaluation to new datasets and conditions, and automate the demographic breakdowns in Airflow.
4. **Inference optimisation:** distil or quantize a recognition or liveness model for lower latency and GPU cost. Possibly a mobile/on-device variant for capture guidance.
5. **Data pipeline:** ingestion and cleaning DAGs; balanced training-set curation; maybe synthetic-data experiments.
6. **Support selfie.DONE scale-up:** template matching at low false-match rates, and 1:N search behaviour as reuse grows globally.

## 2.5 A plausible week

- **Experiments (~40%):** run training jobs on AWS GPUs, analyse error cases ("why does FNMR spike on this ID type in this region?"), and keep an experiment log.
- **Engineering (~30%):** Airflow DAGs, evaluation code, ONNX/TensorRT export, CI tests, reviewing peers' PRs.
- **Collaboration (~20%):** stand-ups, a weekly ML review with Vienna/India colleagues, syncs with product (pass rates, customer escalations) and sometimes compliance (fairness reports).
- **Mentoring and documentation (~10%):** design docs, onboarding notes, review feedback.
- **Occasional:** production escalations (a customer reports a spike in false rejects), and red-team results from new attack types (a new deepfake tool).

## 2.6 Tech stack you'd likely touch

| Area | Likely tools |
|---|---|
| Languages | **Python** (main), some C++ for performance or SDK hand-off |
| Training | **PyTorch** (most likely), TensorFlow for legacy models, maybe JAX |
| CV libraries | OpenCV, Pillow, albumentations; face libraries (InsightFace-style detectors and ArcFace losses) |
| Data / orchestration | **Airflow** (maybe AWS MWAA), S3, SQL; dataset versioning |
| Cloud | **AWS**: EC2 GPU instances, SageMaker, EKS/ECS, S3 |
| Inference | **ONNX, TensorRT**, quantization (PTQ/QAT), distillation; Triton-style serving is possible |
| Mobile | CoreML, LiteRT (formerly TFLite) for on-device models |
| Search | FAISS / Milvus-type ANN for 1:N |
| MLOps | Docker, CI/CD, experiment tracking (MLflow / W&B-type), Git |

## 2.7 How your work would be judged

| Metric | Meaning |
|---|---|
| **FNMR @ FMR** (e.g., FNMR at FMR = 1e-4 or 1e-6) | Genuine users wrongly rejected, at a fixed rate of impostors wrongly accepted. Recognition's headline metric. |
| **APCER / BPCER** | Liveness: attacks wrongly accepted / genuine users wrongly rejected |
| **Demographic differentials** | Max/min ratio of FMR or FNMR across groups. Lower is fairer. |
| **Pass rate / conversion** | Business view: how many genuine users get through on the first try |
| **Latency (p95) and cost per verification** | Inference speed and GPU dollars |
| **Robustness** | Performance on new devices, new attack types, and new countries' IDs |

## 2.8 Fit, gaps and a ramp plan

| Area | Fit | How to close the gap |
|---|---|---|
| Production camera CV | ✅ strong | Lead with it |
| Benchmarking / evaluation rigour | ✅ signature strength | Lead with it |
| Low-latency inference | ✅ strong (CPU/ARM) | Learn TensorRT specifically (below) |
| Pipelines / Airflow / AWS | ✅ proficient | Be accurate about scale |
| Mentoring | ✅ | MAS stories |
| **Face recognition / biometrics** | ❌ new | The JD expects you to ramp. Self-study below. |
| PyTorch depth | ◑ proficient | Do the mini-project in PyTorch |
| Multi-GPU training at scale | ◑ dual-GPU only | Read up on DDP; don't overclaim |
| Formal fairness analysis | ◑ conceptual | NIST IR 8280 + the RFW dataset |

**Two-week self-study before the technical rounds (high return):**
1. **Read:** ArcFace (Deng et al., CVPR 2019); RetinaFace; one face-quality paper (CR-FIQA or MagFace); NIST IR 8280 (demographic effects) summary; the ISO/IEC 30107-3 metrics overview.
2. **Mini-project (2–3 evenings), and mention it in the technical round:** take a pretrained ArcFace model (e.g., InsightFace), evaluate 1:1 verification on LFW plus **RFW (Racial Faces in the Wild)**, and report FNMR at fixed FMR per demographic group. Then export to ONNX, quantize to INT8, and report the accuracy-vs-latency trade-off. This covers recognition, benchmarking across conditions, fairness and optimisation in one artefact, in your own JAES style.
3. **TensorRT basics:** run the ONNX → TensorRT engine flow once (FP16 and INT8 calibration) on any NVIDIA GPU you have (your RTX 4090 works).

---

# PART 3: SALARY

## 3.1 Data

| Source | Scope | Figure (CAD unless noted) |
|---|---|---|
| Glassdoor.ca: Jumio "Senior ML Engineer" | Jumio, small sample | **Total pay $145K–$182K, median $164K** |
| Glassdoor.ca: Jumio ML Engineer (all levels) | Jumio, 7–9 salaries | **Average base ~$140K** |
| Glassdoor: Jumio ML Engineer, Montreal | 9 salaries, Oct 2026 | 25th–75th percentile **$90K–$164K** (junior and senior mixed) |
| Glassdoor estimate on open Jumio Montreal senior roles | Model estimate | $125K–$181K |
| Levels.fyi: Jumio SWE, Canada | June 2025, tiny sample | Median total comp ~$181K |
| Payscale: Senior MLE, Montréal 2026 | All employers | Base $98K–$143K (average $115K) |
| JobRise: Senior AI Engineer, Montréal 2026 | All employers | $130K–$165K |
| US H-1B wages, Jumio MLE (2025) | US, **USD** | $112K–$148K USD (cross-check only) |
| Dreamwork "$280K–$430K" | Unverified aggregator | **Ignore** (looks like a US big-tech band on the wrong role) |

Quebec has no pay-transparency law, so there's no posted range. Montreal pays about 5–15% less than Toronto, and Quebec tax is higher. As a private, PE-backed company, Jumio likely pays base + annual bonus, possibly stock options (illiquid), and benefits. Don't expect RSUs.

## 3.2 Estimate

| Where you land | Base | Total (base + bonus) |
|---|---|---|
| Below Senior ("MLE III") | $120K–$135K | $130K–$150K |
| **Senior (most likely)** | **$135K–$160K** | **$145K–$180K** |
| Pulled up to Staff/"MLE IV" | $160K–$185K | $175K–$210K |

**Target about $150K base.** Your private floor is about $135K at Senior (don't say it).

## 3.3 Scripts

- **First ask:** "The posting says the level is set after the interviews. What range do you have budgeted for this role?"
- **If pushed:** "For senior computer-vision ML roles in Montreal I'm targeting around **$150K to $165K base**, depending on level and the full package: bonus, equity and relocation. I'm flexible for the right fit, and this is a strong one."
- **If their band is lower:** "That helps, thanks. Where would someone with a PhD, five years of production CV and published low-latency inference work sit in that band? And can the level be revisited after the technical rounds?"
- **If they ask your current salary:** "My last role was an EU-funded postdoc in Italy, so it isn't comparable. I'm benchmarking against the market for this role."
- **Package items to ask about:** bonus target %, equity type, RRSP match, benefits, **relocation (Toronto → Montreal)**, hybrid days, start date.

---

# PART 4: THE RECRUITER CALL

## 4.1 What the call is

**Format:** 20–30 minutes with a talent-acquisition partner. No deep technical questions.

**What they're checking:**
1. Fit to the req: production CV at Senior level (they may re-check your two screening-question answers).
2. Logistics: PR and no sponsorship (say it in the first minute), Montreal relocation, availability, French.
3. Comp alignment.
4. Motivation.
5. Communication.

**The process afterwards (thin evidence; confirm on the call):**
- A 2021 review: HR call → two technical rounds with light live coding (pandas, SQL, TensorFlow; looking up syntax allowed), plus project walkthroughs and design-choice discussion.
- Prep sites describe about 4 rounds over 3–5 weeks (screen → technical deep dive → take-home → live coding). Unverified.
- Jumio has acknowledged ghosting candidates in the past. Follow up after 7 business days.

## 4.2 Pitch: 60 seconds ("Tell me about yourself")
> "I'm a machine learning engineer with about ten years across industry and research, and the thread is computer vision under real constraints.
>
> I spent five years at MAS Holdings, South Asia's largest apparel manufacturer, building production camera systems. One was an automated label-inspection system that checked printed labels against reference artwork. It cut inspection time by 99.5% and tripled throughput. Others included fabric-defect detection with a microscopic camera array, and OCR and layout segmentation to digitize garment documents.
>
> Then a PhD and postdoc at the University of Trento on real-time ML on edge hardware. My published detector runs in 14 milliseconds on a Raspberry Pi 4, 74 times faster than the baseline, and much of that work was building benchmark suites across datasets and operating conditions.
>
> So this role lines up closely: CV models, benchmarking across conditions, and optimising inference on AWS. I'm a Canadian PR in Toronto, available immediately, and I know Montreal well from a research stint at McGill in 2024."

**Extensions for the 2-minute version:**
- End-to-end pipeline ownership at the postdoc (acquisition → deployment → monitoring).
- Four public benchmark datasets on Zenodo.
- Airflow + AWS.
- Mentoring: CI/CD, code review, 2 BSc theses.
- Promptly's alignment algorithm became a commercial product in 4 countries. (Never mention the patent.)

## 4.3 The bridge sentence (use it once)
> "Your capture → document → selfie pipeline maps closely to systems I've built: template verification of printed material, OCR and layout segmentation, image quality gating, and fast inference on edge hardware. Faces are the new part, and the posting frames this role as exactly that ramp."

## 4.4 Likely questions and answers

**Q1. Why Jumio?**
> "Three reasons. First, it's computer vision where errors have real consequences, which is the kind of problem I like: fraud prevention and access to financial services. Second, the work is what I'm best at: benchmarking across operating conditions and getting latency down. Third, the push toward continuous identity and reusable credentials like selfie.DONE means the face models run far more often, so robustness and efficiency matter even more. And it's in Montreal."

**Q2. Why go back to industry?**
> "I went from industry to research on purpose, to get deeper tools: rigorous benchmarking, real-time inference, publishing. My best work has been systems that shipped, like the label inspection and Promptly. I want to be close to production again."

**Q3. What have you done since December 2025?**
> "My postdoc ended and I moved to Canada. Since then I released Nebula, an open-source C++17 feature library with latency benchmarks. I got papers through at JAES and IEEE IS² 2026. I built an Airflow → S3 → Snowflake pipeline, and I'm fine-tuning a generative model across two GPUs. I've been selective in the job search."

**Q4. No face biometrics. Why you?** ← *Rehearse this one out loud.*
> "That's right, and your posting frames this role as ramping up on the biometrics domain, which is why I applied to this req and not the Staff biometrics one. What transfers directly: production detection and classification pipelines, quality assessment, benchmarking across datasets and conditions, and inference optimisation. I've changed domains before and delivered: I took SSIM, a computer-vision metric, and applied it to music sequences in a published method. I'm already working through the face-recognition literature, ArcFace, face quality, and the NIST demographic studies, so the face-specific parts will take weeks, not months."
(Only say the last sentence if you've started the §2.8 reading.)

**Q5. Production CV and hands-on experience (re-checking your application answers).**
- **Deployed:** care-label QC (scanner → camera → conveyor with PLC reject); fabric defects at the loom; COVID-19 vitals monitoring (camera reading medical device displays, deployed across hospital wards).
- **Detection/segmentation:** garment detection/segmentation; defect detection.
- **OCR / document image analysis:** tech-pack digitization; label verification.
- **Image quality:** defect and quality overlays.
- **Real-time perception:** microscopic camera array with a 5–6 s alert budget; 14 ms edge inference.

**Q6. PyTorch / AWS / Airflow depth?**
> "My published models are TensorFlow/Keras, and my current work is in PyTorch, including a recent dual-GPU LoRA fine-tune. AWS: EC2, S3, ECS, MWAA, RDS. Airflow for ingestion and feature DAGs."
Don't claim production-scale SageMaker/EKS or large multi-GPU clusters.

**Q7. TensorRT / quantization / distillation?**
> "My optimisation work is on CPU/ARM: profiling, architecture and OS scheduling, plus ONNX export and compression. TensorRT is the same discipline on NVIDIA: calibration, layer fusion, FP16/INT8 measured against accuracy. That's a quick ramp."

**Q8. Fairness?**
> "My datasets were built for performer diversity, 70+ musicians across nationalities, ages and instruments, and I evaluated across those groups. For faces, I know the frame: false-match and false-non-match rates per demographic group at a fixed threshold, with data balancing and synthetic data to close gaps. I'd want to learn Jumio's process. It's part of the integrity piece."

**Q9. Relocation and timeline?**
> "Yes, Montreal is my top-choice city. I can move within about 4–6 weeks of an offer. What's the hybrid expectation?"

**Q10. French?**
> "Basic, about A2, and I'm actively taking classes. I work in English. I learned Italian to B1 while living in Trento, so I build languages up once I'm living in them."
Never claim bilingual. Ask whether the team works in English.

**Q11. Other interviews?**
> "Yes, later stages with a couple of Toronto organizations, but Jumio is a top choice for fit and Montreal. If timelines get tight, I'll let you know."

**Q12. What level?**
> "Senior. I've led production CV systems, set engineering practices and mentored engineers. Happy for the technical rounds to decide, and I'd ask that Staff stays open if they support it."

**Q13. Mentoring / technical bar?**
MAS: introduced CI/CD and code review, and ran group-wide CV training that led to multi-factory deployments. *"Standards only stick if you pair them with the first few reviews yourself."*

## 4.5 Fix before the technical rounds

| Issue | Submitted | True | What to do |
|---|---|---|---|
| **F1** | CV summary: "**>90% F1**" (from the golden resume). Cover letter: "F1 0.76". | Published JAES 2026: **F1 0.76 at 14 ms** (DTW baseline 0.65 at 1038 ms) | Always say 0.76. If challenged: *"That's from older material. The peer-reviewed figure is F1 0.76 at 14 ms. Hold me to the published number."* |
| "300% efficiency" | CV | Care-label throughput: 15–20 min per label → 1–2 min per batch | Be able to explain exactly what it measured |
| "AI Ethics" competency | CV | No formal fairness project | Use the Q8 framing |
| Contact details | +1 613 200 2030 / nishal.silva@hotmail.com | ✅ | Nothing to do |

## 4.6 Questions to ask (pick 4–5; first two are essential)
1. **"How is this role levelled relative to the Staff/Senior biometrics openings, and what's the band?"**
2. **"What are the next steps and timeline? Is there a take-home or live coding?"**
3. "Who's the hiring manager, and how big is the Montreal CV/biometrics team?"
4. "What would success in the first six months look like: detection, quality or recognition?"
5. "What's the hybrid policy, and is there relocation support?"
6. "Does the team work in English?"
7. "How does work split between Montreal, Vienna and India?"
8. "With selfie.DONE going global, are biometrics models moving more on-device, or staying server-side on AWS?"
9. (Carefully, if rapport is good) "With the new CEO this year, how has the biometrics roadmap changed? Is the team growing?"

## 4.7 Biometrics vocabulary (for credibility; don't lecture)
- **1:1 verification** (selfie ↔ ID) vs **1:N identification** (Identity Graph, duplicate search → ANN / FAISS / Milvus).
- **FMR/FNMR** (or FAR/FRR), DET curves, ISO/IEC 19795.
- **PAD / liveness:** ISO/IEC 30107-3, APCER/BPCER, iBeta Level 1/2; passive vs active liveness. Jumio achieved Level 2 in Oct 2025.
- **Injection attacks** (deepfake fed through a virtual camera, bypassing the real one) are *outside* ISO 30107-3's scope. **Morphing** attacks blend two faces into one ID photo.
- **Models:** RetinaFace/SCRFD (detection); ArcFace/CosFace (margin losses); MagFace (quality from embedding norm).
- **Face image quality (FIQA):** ISO/IEC 29794-5; SER-FIQ, CR-FIQA.
- **Fairness:** NIST IR 8280; RFW / BUPT-Balancedface datasets; NIST FRTE (formerly FRVT) and FATE.
- **Privacy:** GDPR Art. 9; Quebec Law 25 + CAI; BIPA; EU AI Act.
- **Optimisation:** PTQ vs QAT; distillation; ONNX → TensorRT FP16/INT8; CoreML and LiteRT on-device.

## 4.8 Checklist
**Before:**
- [ ] Reread the submitted CV and cover letter.
- [ ] Say the 60-second pitch out loud twice.
- [ ] Rehearse Q4 and the salary scripts out loud.
- [ ] Check the CEO's name spelling on jumio.com.
- [ ] Keep §3.2 and §4.6 in front of you.
- [ ] Quiet room, phone charged.

**During:**
- PR, no sponsorship and immediate availability in the first minute.
- Get their band before giving a number.
- Write down: the recruiter's name, the band, next steps, the hiring manager's name, hybrid policy, timeline.

**After:** send a thank-you the same day (below). If you hear nothing for 7 business days, check in politely. Update tracker #1112.

> Subject: Thank you — Senior Machine Learning Engineer (Montreal)
>
> Hi [Name],
>
> Thank you for the conversation today. I enjoyed learning more about the Biometrics team and [one specific thing they said]. The role is a strong match for the work I enjoy most: production computer vision, benchmarking across operating conditions and low-latency inference. I'm excited about ramping up on the biometrics side.
>
> I look forward to the next steps.
>
> Best regards,
> Nishal Silva, PhD · +1 613 200 2030 · nishal.silva@hotmail.com

## 4.9 Story bank (for the technical rounds)

| JD pillar | Story | Number | Reflection |
|---|---|---|---|
| CV pipeline shipped | Care-label QC: template + feature matching, explainable overlay, 3 iterations | −99.5% inspection time, +300% throughput | The version that shipped was the simplest of the three |
| Benchmarking | JAES: RNN vs DTW across set sizes 1/3/10, audio vs MIDI, CPU budget | 14 ms vs 1038 ms; F1 0.76 vs 0.65 | Pre-register the evaluation protocol |
| Low latency | MUSMET edge deployment on RPi4 | 14 ms, 31.4% CPU | The biggest win was OS scheduling: look at the whole stack |
| Pipelines | MAS IoT ingestion + ETL; melodiq Airflow → S3 → Snowflake | Millions of events/day | Data-quality checks kept it reliable |
| Mentoring | MAS CI/CD + code review + training; 2 BSc theses | Multi-factory rollout | Pair new standards with the first reviews yourself |
| Commercial impact | Promptly: alignment warp + RIP integration | Live in 4 countries | Algorithms only matter once integrated into the machine |
| Synthetic data | McGill VAE/diffusion; VarianceEngine LoRA MusicGen | — | Validate synthetic data against real data |

---

## Sources

**Company**
- Wikipedia: https://en.wikipedia.org/wiki/Jumio
- TechCrunch (2016 bankruptcy): https://techcrunch.com/2016/03/21/identity-verification-startup-jumio-files-for-bankruptcy-will-sell-assets-to-early-backer-eduardo-saverin
- Beam Solutions acquisition: https://www.jumio.com/about/press-releases/jumio-acquires-beam-solutions-aml-platform/ · https://www.helpnetsecurity.com/2020/10/01/jumio-beam-solutions/
- 4Stop acquisition: https://businesswire.com/news/home/20211207005310/en/Jumio-Acquiring-4Stop-Redefining-the-End-to-End-Identity-Platform
- 2023 layoffs: https://www.biometricupdate.com/202301/jumio-downsizes-as-identity-verification-providers-respond-to-economic-climate
- Bala Kumar interim CEO: https://www.jumio.com/about/press-releases/bala-kumar-president-interim-ceo/
- Mark Lorion CEO: https://www.businesswire.com/news/home/20260427323482/en/Jumio-Announces-Mark-Lorion-as-Chief-Executive-Officer · https://www.fintechfutures.com/job-cuts-new-hires/jumio-names-mark-lorion-ceo
- Q2 2026: https://www.biometricupdate.com/202607/jumio-expansion-beyond-biometric-onboarding-roots-yields-q2-growth · https://www.morningstar.com/news/business-wire/20260721162029/jumio-accelerates-the-shift-to-identity-intelligence-with-strong-q2-2026-growth
- Q3 2026: https://www.financialcontent.com/article/bizwire-2026-10-21-jumio-drives-global-leadership-in-digital-trust-and-identity-intelligence-in-q3-2026
- Products and claims: https://www.jumio.com/ · https://www.jumio.com/technology/live-detection/
- Liveness Premium: https://www.businesswire.com/news/home/20250618472801/en/Jumio-Launches-Premium-Liveness-Detection-Solution-for-Superior-Protection-Against-Deepfakes-and-Injection-Attacks
- ISO 30107-3 Level 2: https://www.jumio.com/about/press-releases/iso-iec-level-2-compliance/
- Awards and analyst recognition: https://www.jumio.com/about/press-releases/liveness-premium-gold-2026-cybersecurity-excellence-awards/ · https://www.prnewswire.com/news-releases/jumio-positioned-for-third-consecutive-year-as-the-leader-in-the-2026-spark-matrix-for-identity-capture-and-verification-solutions-302854028.html
- Montreal AI Labs: https://www.jumio.com/about/press-releases/artificial-intelligence-ai-labs-montreal/ · https://www.biometricupdate.com/201808/jumio-opens-new-montreal-ai-facility-for-research-into-facial-recognition-speed-and-accuracy · https://www.theglobeandmail.com/business/article-silicon-valleys-jumio-launches-artificial-intelligence-lab-in
- Size estimates: https://tracxn.com/d/companies/jumio/__n_v3Ht0SWd-Yl-76hYL_8HHaij8GvNxHSXOTsZWKnT8 · https://pitchbook.com/profiles/company/51697-00
- Competitors: https://hyperverge.co/blog/jumio-competitors/ · https://www.au10tix.com/blog/jumio-competitors-best-8-jumio-alternatives/
- Culture: https://www.glassdoor.co.uk/Reviews/Jumio-Reviews-E868408.htm · https://www.comparably.com/companies/jumio

**Role**
- Greenhouse board API (all three Montreal reqs, checked 2026-10-21): https://boards-api.greenhouse.io/v1/boards/jumio/jobs
- Interview reviews: https://www.glassdoor.sg/Interview/Jumio-Interview-E868408-RVW71149376.htm · https://dataford.io/interview-guides/jumio/machine-learning-engineer

**Salary**
- https://www.glassdoor.ca/Salary/Jumio-Machine-Learning-Engineer-Montreal-Salaries-EJI_IE868408.0,5_KO6,31_IL.32,40_IM990.htm
- https://www.glassdoor.ca/Salary/Jumio-Machine-Learning-Engineer-Salaries-E868408_D_KO6,31.htm
- https://www.glassdoor.ca/Salaries/montreal-qc-senior-machine-learning-engineer-salary-SRCH_IL.0,11_IM990_KO12,44.htm
- https://next.levels.fyi/companies/jumio/salaries/software-engineer
- https://www.payscale.com/research/CA/Job=Senior_Machine_Learning_Engineer/Salary/0f5f0caf/Montr%C3%A9al-QC
- https://jobrise.io/fr/blog/salaire-ai-engineer-montreal-2026/
- https://www.ellis.com/visa-sponsors/jumio-corporation/salaries

*Inferred content is labelled as such (team shape, first projects, weekly mix, stack). Confirm these on the call.*
