<!-- Job posting: https://clarius.com/career/co/research-development-rd/0D.17C/machine-learning-engineer/all/ -->

# Job Fit Evaluation — 1137

**Role:** Machine Learning Engineer (R&D, special 24-month project)
**Company:** Clarius Mobile Health
**Location:** Remote, Canada (Vancouver BC hybrid preferred; remote-Canada considered) — **no relocation required**
**Type:** Temporary / Intermediate · two-year fixed-term through Oct 2028 (strong likelihood of extension/permanent)
**Comp:** CAD 110,000 - 130,000
**Deadline:** none stated
**Evaluated:** 2026-09-03 (main thread) · triage rank_score 72 · /apply Step 1 score **70/100**

## Eligibility Gate: PASS
No citizenship, PR, or clearance requirement. Canadian PR, eligible anywhere in Canada without sponsorship, available immediately. Remote-Canada is explicitly accepted, so no relocation.

## Language Gate: PASS
English only. Nishal: English Native/C2.

## Scored Dimensions

| Dimension | Score | Notes |
|-----------|-------|-------|
| Technical Skills (30%) | 74 | Direct: Python + Unix/Linux mastery; **TensorFlow and PyTorch both required** and both held (TF primary, PyTorch secondary); software-engineering best practices (version control, testing, code quality) - pytest, CI/CD, code review, all his; ML data pipelines (MAS real-time ingestion + ETL, postdoc pipeline); "automate model retraining, evaluation, and monitoring in production" (postdoc deployment monitoring); "optimize model performance and inference speed for production deployment" is his signature (14 ms on RPi4, 74x speedup); C++ (preferred) - expert. Docker + AWS held; Kubernetes + GCP light. Gaps: "deep expertise in deep learning and computer vision" - he has strong classical/industrial CV (OpenCV, template + feature matching, registration) but modern deep-CV architecture depth (segmentation/detection nets for medical imaging) is lighter; medical ultrasound imaging is a new domain; "building scalable web applications" is light. |
| Experience Match (25%) | 72 | "Development, training, and deployment of ML models in both research and production settings" with "strong software engineering practices" is the postdoc + MAS pattern - research-to-production ML with engineering discipline. Medical-signal adjacency: the COVID-19 remote-vitals CV device deployed across hospital wards (GMOA). 3+ yrs industry ML: clears comfortably. Gaps: no ultrasound / medical-imaging domain experience; the role is partly maintenance-flavoured ("improve and maintain ML tools", "address and minimize ML technical debt", "automate ML tasks"). |
| Behavioral Fit (15%) | 63 | Positives: 150-person company, "talented, innovative, highly collaborative", thrice Great Place to Work, a genuinely high-impact mission (25M professionals lack imaging access). Friction: a real maintenance / ML-technical-debt / tooling-upkeep component that is a partial drain for a builder who prefers owning new systems end to end; a two-year fixed term; "Intermediate" level framing. |
| Location | PASS | Remote, Canada accepted (or Vancouver hybrid). No relocation - remote-Canada is fine per profile. |
| Career Alignment (30%) | 68 | Up: medical-imaging / ultrasound ML is a stated target sector (medical-signal / wearables; he drafted an audio-to-ultrasound domain-transfer pitch for Oncoustics); research-to-production ML with an inference-speed-optimization emphasis (his strength); a mission he would value. Down: two-year fixed term (extension likely, not guaranteed); "Intermediate" level is below his senior-IC target; CAD 110-130k sits at or just below the low end of his CAD 120-150k range; the maintenance / tech-debt component under-uses him. |

**Overall: 70/100** (0.30·74 + 0.25·72 + 0.15·63 + 0.30·68 = 22.2 + 18.0 + 9.45 + 20.4)

## Verdict: Good Fit

## Key Strengths
- Optimizing model performance and inference speed for production is his signature: 14 ms on a Raspberry Pi 4 at 31.4% CPU, F1 0.76, 74x faster than the DTW baseline (JAES 2026).
- Research-to-production ML with software-engineering discipline: postdoc owned the full pipeline (acquisition to deployment to monitoring); MAS shipped CV/IoT into live manufacturing with CI/CD and code review he introduced.
- TensorFlow + PyTorch both held; Python + Unix/Linux + C++17 expert; ML data pipeline design and ETL.
- Computer vision: OpenCV template/feature matching, image registration and warping, industrial inspection (99.5% inspection-time cut, 50% operator reduction).
- Medical-signal adjacency: COVID-19 remote-vitals CV device deployed across hospital wards (GMOA recognition); an audio-to-ultrasound domain-transfer pitch already drafted (Oncoustics).
- Remote-Canada accepted - no relocation; PR; available immediately.

## Gaps to Address
- **Deep / modern CV architecture depth for medical imaging:** his CV strength is classical + industrial; segmentation / detection nets for ultrasound are a ramp-up. Frame the deployed-CV + inference-optimization record as the base and be honest that ultrasound imaging is new.
- **Ultrasound / medical-imaging domain:** entirely new; precedent for learning an applied field cold (apparel manufacturing, financial forensics) + the COVID vitals device as the closest prior health work; the audio-to-ultrasound signal-transfer framing is a genuine angle.
- **Kubernetes / GCP / scalable web applications:** light - mention Docker + AWS as held, the rest as familiar.
- **Fixed-term + Intermediate + comp band:** two-year term, sub-senior framing, CAD 110-130k at/below the low end of target - for Nishal to weigh; extension-to-permanent is stated as a strong likelihood.

## Cover Letter — Special Instructions
None stated. Standard 4 paragraphs. Lead with inference-speed optimization + research-to-production ML discipline; use the medical-signal adjacency (COVID vitals device) and the audio-to-ultrasound signal-transfer angle for the "why Clarius" paragraph; be honest that ultrasound imaging is new; note remote-Canada / no-relocation and immediate availability.

## Recommendation
Apply - Good Fit. Medical-imaging ML is a target domain, it is remote-Canada with no relocation, and the inference-optimization + research-to-production emphasis maps well to his strengths. Weigh the two-year fixed term, the "Intermediate" framing, and the CAD 110-130k band (low end of range) before prioritizing it over the stronger fits.

## Company Research Checklist
- [x] Website — handheld wireless app-connected ultrasound; "Clarius Intelligence" AI (anatomical guidance, automated measurements, imaging optimization, voice controls); ~150 people; mission = accessible imaging (25M lack access).
- [x] Media — multiple FDA-cleared AI models shipped (MSK tendon ID/measurement; OB AI fetal biometrics for resource-limited care; veterinary AI); PacifiCan CAD 3.4M (Mar 2024), ~CAD 21.9M total raised; ThinkSono partnership; May 2026 "rivals traditional ultrasound systems" claim.
- [x] Comp + term — disclosed in posting (CAD 110-130k, two-year fixed-term through Oct 2028).
- [x] Written to `company_research/clarius-mobile-health.json`.
