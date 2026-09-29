# Manual review instructions — for the claude.ai UI + Chrome workflow

Self-contained on purpose: the web UI session doing this review has no access to this repo's files. Everything the scoring needs is inlined below — you shouldn't need to open anything except this file, the job URLs, and the Claude UI.

**Status: ready.** All three discovery batches are scored. The list is final — see `needs-manual-review.md` in this same folder for the 72 postings and their URLs (⭐ marks the 11 strongest title-level matches, worth doing first if you don't want all 72).

## What happened

These postings are on job boards that render their content with JavaScript (Workday, Ashby, BambooHR, ADP, Taleo, UltiPro, WhatJobs redirects, Oracle Cloud HCM). The automated tools available to the PM session can't execute JavaScript, so it got a blank page instead of the actual job description for each one. It gave each a placeholder score (~40/100) based on the job title alone — not a real evaluation. This file is how those get a real one.

## How to review one posting

1. **Open the URL in Chrome.** Let the page fully load (these are slow, client-rendered pages).
2. **Copy the actual job description text** — the requirements, responsibilities, and any "who can apply" / work-authorization language. Skip nav/footer boilerplate.
3. **Paste this entire prompt into claude.ai**, filling in the two blanks:

```
Score this job posting against a candidate profile. Use the rubric and profile facts below exactly as given — don't substitute your own framework.

=== CANDIDATE PROFILE (relevant facts only) ===
- Canadian Permanent Resident, eligible to work anywhere in Canada without sponsorship, no hours/start-date constraint. Actively job-searching since mid-2025, available immediately.
- Languages: English (native/C2), Sinhala (mother tongue), Italian (B1), French (~A2, basic).
- PhD in Information Engineering and Computer Science (real-time/low-latency ML, embedded & edge inference, audio DSP, time-series pattern detection, RNNs), University of Trento 2021-2025. MSc Telecom/Electronic Eng, BEng Electronic Eng (Sheffield Hallam).
- Strong skills: real-time/low-latency ML, edge & embedded ML (Raspberry Pi, ARM), time-series/sequence modelling (RNN/LSTM/GRU), DSP & audio ML (MFCC, STFT, MIR), computer vision for industrial inspection (OpenCV), Python, C++17, TensorFlow/Keras, benchmark/dataset design, end-to-end ML pipelines, multimodal/sensor fusion (IMU, BCI/EEG, XR telemetry).
- Moderate skills: PyTorch, scikit-learn, anomaly detection, SQL, AWS (EC2/S3/ECS/MWAA/RDS), Docker, Airflow, Jenkins, ETL, REST APIs, JS/TS, MATLAB, C, VAE/diffusion generative prototypes.
- Weak/light-evidence skills (list only if the JD names them, score honestly): large-scale distributed training, LLM pre-training/foundation-model research, production RAG & prompt engineering, recommender/ranking systems, NLP, Kubernetes, MLflow, Snowflake, JAX.
- Career history: postdoc researcher (real-time audio+IMU ML, edge deployment, EU Horizon project); visiting researcher at McGill IDMIL/CIRMMT (smart guitar, IMU+audio fusion); technical consultant at Forestpin (financial forensics/anomaly detection ML); research engineer at MAS Holdings 2015-2020, ONE entry (industrial computer vision + IoT at manufacturing scale: care-label QC, loom-side inspection, direct-to-garment printing alignment algorithm + RIP integration — never mention a patent, he's not a listed inventor — COVID vitals CV device).
- Deal-breakers: roles requiring US-only work authorization; 5+ years large-scale distributed training/LLM pre-training; relocation outside Canada. Pure LLM-prompting/chatbot-integration roles with no ML-systems depth score moderate, not high (under-uses him).
- Career goals: senior/staff-track IC as ML Research Engineer or Applied Scientist building real-time/edge ML systems that ship; deepen audio ML/music-tech/multimodal time-series specialization or apply it to medical-signal/industrial/neurotech; Toronto-preferred Canadian team with real ownership.
- Energized by: real-time/edge inference under latency/compute/power budgets, end-to-end pipeline ownership, DSP/signal work, multimodal sensor fusion, benchmark/dataset design, hardware-in-the-loop, audio/creative-tools problems, systems that ship. Drained by: maintenance-dominated work, narrow no-ownership scope, pure LLM prompting with no systems depth, process-bound environments.

=== ELIGIBILITY GATE (run first, hard filter) ===
- Posting names a citizenship/PR requirement, or a security clearance gated on citizenship → FAIL, hard stop, quote the wording, do not score further.
- Posting explicitly welcomes international applicants/visa holders/sponsorship → PASS.
- Posting is silent on citizenship/residency → PROCEED but note as unverified.
- Location rule: anywhere in Canada (onsite/hybrid/remote/relocation-within-Canada) → PASS. Fully-remote role that hires Canada-based people, any HQ country → PASS. Onsite/hybrid outside Canada, or requires non-Canadian work authorization → FAIL. Remote role that excludes Canadian residents → FAIL.

=== LANGUAGE GATE (run second, hard filter for languages not on the list at all) ===
- Requires a language not listed above at all (e.g. "fluent German required") → FAIL, hard stop, quote the requirement.
- Requires a language listed above, but at a bar that plausibly exceeds the declared level (e.g. "fluent French" vs. his A2) → FLAG, don't fail — score normally but call this out explicitly.
- Requires a language at or below the declared level, or doesn't specify a level → PASS.

=== SCORING (only if both gates pass) — five dimensions, 0-100 each except Location ===
1. **Technical Skills Match**: 80-100 core requirements are primary skills; 60-79 most match with 1-2 learnable gaps; 40-59 partial match, real upskilling needed; 0-39 fundamental mismatch.
2. **Experience Match**: match on function/nature of work, not literal title. 80-100 direct domain+role match; 60-79 related/transferable; 40-59 adjacent, needs a case made; 0-39 unrelated.
3. **Behavioral/Culture Fit**: 80-100 strongly matches preferences above; 60-79 mixed but compatible; 40-59 friction areas; 0-39 mismatch. (Score honestly from the JD's tone/description; note you can't fully assess this without company research.)
4. **Location & Logistics**: PASS/FAIL per the gate above, not a 0-100 score.
5. **Career Alignment & Motivation**: 80-100 strongly aligned, clear growth; 60-79 good but partial fit; 40-59 doesn't build toward goals; 0-39 backwards step.

**Overall score = simple average of the four 0-100 dimensions** (Technical, Experience, Behavioral, Career Alignment — Location is pass/fail and doesn't enter the average, but a FAIL there overrides everything to a hard reject regardless of the average).

≥80/100 = recommend applying. Below that, still worth noting if close.

=== OUTPUT FORMAT — give me exactly this, nothing else ===
ID: <fill in from the table below>
Score: XX/100
Eligibility: PASS/FAIL/unverified
Language: PASS/FLAG/FAIL
Note: <one sentence — the strongest signal for or against, plus the biggest gap if any>

=== JOB POSTING TO SCORE ===
<PASTE THE JD TEXT YOU COPIED FROM CHROME HERE>
```

4. **Copy Claude's reply** (just the 5-line `ID/Score/Eligibility/Language/Note` block) and bring it back to this session, or save it somewhere you'll paste all of them from at once. Either works — one at a time or batched at the end.

## Job list

See `needs-manual-review.md` (same folder) — 72 postings, ID/company/role/platform/URL, ⭐-prioritized. Not duplicated here to avoid the two files drifting out of sync.
