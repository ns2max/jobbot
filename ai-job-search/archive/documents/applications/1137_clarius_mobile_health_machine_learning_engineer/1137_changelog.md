<!-- Job posting: https://clarius.com/career/co/research-development-rd/0D.17C/machine-learning-engineer/all/ -->

# 1137 Clarius Mobile Health — CV + Cover Letter Changelog (2026-09-03)

Pipeline: main-thread eval (70/100 Good Fit) → Fable draft (rebuilt from the 1131 V5 pair) → main-thread review + compile + verify. Codex exhausted until Oct 3.

## CV — `cv/1137_main_clarius_mobile_health_machine_learning_engineer.tex`
- **Variant V5 (Computer Vision / Industrial).** Tagline `Computer Vision & ML Engineer | Industrial Inspection, IoT & Edge Deployment` (byte-identical in cover). The role's #1 ask is deep learning + computer vision + production inference-speed optimization + software-engineering practice — the MAS industrial-CV / edge-deployment spine.
- Summary leads with taking ML models research-through-production on real hardware + the CI/CD/pytest discipline he introduced at MAS + the 14 ms / F1 0.76 / 74x inference result; **COVID-19 remote-vitals CV device (GMOA) pulled into the summary as the health bridge, with an explicit honest line that ultrasound imaging is a domain he would ramp on**.
- Competency groups relabelled toward the JD vocabulary: "Deep Learning & Computer Vision" (added the literal "deep learning"), "ML Engineering" (automated model retraining/evaluation/monitoring, failure diagnosis + root-cause, statistical validation), "Systems & Deployment" (inference-speed optimization for production, Python on Unix/Linux, ML data pipelines, "version control, testing and code review", ML technical-debt reduction). Docker + AWS promoted; Kubernetes + GCP downgraded to "familiarity".
- Projects trimmed to 4, health/CV-first: **the COVID vitals device is the lead project**; 95% SSIM kept and labelled symbolic-music training-free detection (not inspection — no conflation).
- MAS one entry Jan 2015-Jul 2020, 5 bullets; postdoc trimmed to 2; template `\newpage` not present; `\enlargethispage{3\baselineskip}` before the last section.
- **Grounding:** all numbers verified (14 ms / F1 0.76 / 74x / 31.4% CPU; 300% / 99.5% / 50%; 95% SSIM grounded KG §13/§16); MAS one entry; Promptly = geometry-alignment algorithm + RIP integration + mechanism consulting, **no patent**; English only; Claude Code named. Softened Fable's "moving models from research prototypes into production" (his MAS work wasn't formal research) to "taking model-based inspection from prototype to production".
- **Final: exactly 2 pages** (V5 budget). Page 1 ends with full Education, page 2 opens with the Experience heading — no orphaned titles. ATS text layer clean (0 cid/replacement, email + phone literal, single-ASCII-hyphen dates). Covered: computer vision, deep learning, production, deploy, inference speed, ML data pipelines, retrain, monitoring, TensorFlow, PyTorch, Python, Unix, C++, Docker, version control, testing, medical, ultrasound.

## Cover Letter — `cover_letters/1137_cover_clarius_mobile_health_machine_learning_engineer.tex`
- Plain `article`, 4 paragraphs, "Dear Hiring Manager,". **Exactly 1 page.**
- P1: research-to-production CV + software-engineering discipline + the JAES 2026 inference-speed result.
- P2: walks the posting's responsibilities in its own words (develop/train/deploy research + production; ML data pipelines; automate evaluation/retraining/monitoring; optimize model performance and inference speed for production; minimise ML technical debt; TensorFlow + PyTorch + C++).
- P3: why Clarius — from `company_research/clarius-mobile-health.json` (handheld wireless ultrasound making imaging accessible for the 25M who lack it; Clarius Intelligence AI; FDA-cleared MSK + OB AI models); connects the COVID vitals device + GMOA; **names ultrasound honestly as a new domain**, cites the manufacturing + financial-forensics cold-starts and the audio-to-ultrasound signal-transfer angle.
- P4: PR / no sponsorship / available immediately / Toronto-based, able to work remote-Canada or Vancouver hybrid. The 2-year term not dwelt on.

## Company research
- `company_research/clarius-mobile-health.json` written (Vancouver; handheld wireless ultrasound + Clarius Intelligence AI; FDA-cleared MSK tendon + OB fetal-biometrics AI models — verified via clarius.com/press search; PacifiCan CAD 3.4M / ~CAD 21.9M total; ~150 people; thrice Great Place to Work).

## Open flags for Nishal
- **Two-year fixed term** through Oct 2028 (stated strong likelihood of extension/permanent on meeting deliverables).
- **"Intermediate" level framing** — below his senior-IC target.
- **CAD 110,000-130,000** — at or just below the low end of his CAD 120-150k range.
- Ultrasound / medical-imaging domain is new; modern deep-CV segmentation/detection nets less demonstrated than his classical/industrial CV.
- Remote-Canada accepted — no relocation. No stated deadline.
