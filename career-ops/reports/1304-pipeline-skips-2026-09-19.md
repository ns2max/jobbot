# Pipeline Triage — SKIP batch (2026-09-19 scan.mjs leads)

**Date:** 2026-09-19
**Context:** From tonight's `node scan.mjs` run (10 new offers). Fit-screened against Nishal's profile (real-time/embedded/edge ML, audio/DSP, computer vision, time-series/signal ML, benchmarking; PhD; Senior/Staff; ideal CAD $120-150K; Canada or worldwide-remote). None cleared the 3.5 bar for a full A-G evaluation.

**Verification:** unconfirmed (no browser tool available in this session) — titles/JD text pulled via WebFetch against each ATS API/page directly; Wealthsimple and Helm.ai are Ashby-hosted and returned JS-shell only (no JD body), scored on title + company signal alone and flagged for manual re-check.

**IDs:** 1304-1311 (originally drafted as 1136-1145, renumbered before merge — the jobbot workspace now runs one shared ID space across career-ops and ai-job-search; 1136-1145 collided with existing, already-applied ai-job-search tracker entries). Two of the ten new leads (Grafana Labs ×2) were skipped entirely by `merge-tracker.mjs` as already-tracked duplicates of existing #695/#696 — no new IDs needed for those. All 8 below are status `SKIP`.

---

| ID | Company | Role | URL | Score | Why SKIP |
|---|---|---|---|---|---|
| — | Grafana Labs | Staff Backend Engineer - Grafana App Platform | https://job-boards.greenhouse.io/grafanalabs/jobs/5988483004 | 2.0 | Pure Go backend/SaaS-multi-tenancy infra role, no ML/research/signal content at all. Already tracked as existing #696; merge-tracker correctly deduped, no new ID. |
| — | Grafana Labs | Staff Backend Engineer - Mimir Query, Databases | https://job-boards.greenhouse.io/grafanalabs/jobs/6146605004 | 2.0 | Same as above (distributed database/Kubernetes backend, Go); already tracked as existing #695. Also requires "USA time zones" despite Canada eligibility. |
| 1304 | Wealthsimple | Senior Software Developer, AI Platform | https://jobs.ashbyhq.com/wealthsimple/10e867d5-350d-4114-be79-898d4a755125 | 2.5 | JD unextractable (Ashby JS render, title/company only). "AI Platform" title reads as platform/infra engineering rather than applied ML research — flagged for a manual read, not a confident SKIP. |
| 1305 | League Inc | Senior or Staff Software Engineer, Backend | https://job-boards.greenhouse.io/leagueinc/jobs/6188428004 | 1.8 | Pure backend Go/Kubernetes/GCP/MongoDB platform role. No ML content. Toronto/remote-Canada location passes but domain is a total mismatch. |
| 1306 | Helm.ai | Machine Learning Engineer | https://jobs.ashbyhq.com/helm-ai/a9c443b8-4fc0-4444-afdd-298c25282533 | 3.4 | JD unextractable (Ashby JS render). Company does unsupervised perception for AV (adjacent to tracked #1118, previously discarded as expired) — plausible mid-fit on company signal alone. Worth a manual JD read before a final call; not dismissed on confidence. |
| 1307 | Waabi | Senior / Staff Software Engineer, AI Tooling | https://jobs.lever.co/waabi/2af36079-94fb-423d-a2b6-10b3a1ad5aa3 | 2.6 | Internal AI-tooling/DevEx role (LLM integration, prompt engineering, agent workflows for internal productivity) — not perception/robotics ML. Under-uses the PhD signal-processing background; closer to platform engineering. |
| 1308 | Waabi | Senior / Staff Software Engineer, ML-based Controls | https://jobs.lever.co/waabi/0614b22d-699e-4d08-9149-968e0b010bf4 | 3.6 | Real-time ML for physical/vehicle control systems (Python/C++/PyTorch), genuinely close to the real-time-embedded-ML profile; comp $241-320K USD is strong. Gap: no MPC/optimal-control/state-estimation track record — control theory is a specific, non-trivial specialization Nishal hasn't practiced. Closest of the 10 to the bar; worth a second look if the user wants to build a controls-adjacent story. |
| 1309 | Waabi | Staff Systems Engineer - Safety Methodologies | https://jobs.lever.co/waabi/cb383962-ad2d-40ab-93ce-e3aead4b3838 | 2.8 | Safety-case/statistical-validation methodology role for AV testing — shape is QA/safety-analyst, not ML engineering. Benchmark-methodology instinct transfers loosely but this isn't a modelling role. |
| 1310 | Fullscript | Senior Machine Learning Engineer | https://jobs.lever.co/fullscript/fbd252ba-c7c9-4be8-8f97-ac07acd4355a | 3.0 | LLM-powered clinical agent features (RAG, LangChain/LangGraph, OpenAI/Anthropic integration) for a healthcare platform. KG §2.5 explicit caution: "pure LLM-prompting/chatbot-integration roles... under-use him" — scored moderate not high per that rule, despite the medical-signal domain being loosely adjacent (COVID vitals device). |
| 1311 | Extreme Networks | Senior Full Stack Developer - Generative AI & Autonomous Agents | https://jobs.lever.co/extremenetworks/84d9b745-27d3-46f8-ad42-9305c868e932 | 2.0 | Full-stack Java/Angular/React/TypeScript role with a GenAI feature bolt-on. Not an ML/research role — frontend+backend generalist engineering. |

---

## Notes for the user

- Two of the eight scored (#1306 Helm.ai, #1304 Wealthsimple) returned no readable JD body — Ashby renders the description client-side and this session has no browser tool. Scores above are company/title-signal only; a manual open of the posting (or a future run with Playwright available) could move either one, especially Helm.ai given the company's domain fit.
- #1308 (Waabi ML-based Controls) is the strongest of the batch at 3.6 — still below the 4.0 apply bar, but closer than the rest by a clear margin.
- The Grafana Labs / League Inc / Extreme Networks results are scanner false positives on generic "Engineer" title matching — worth tightening `portals.yml`'s title filter for these three companies if this recurs.
- **ID assignment correction:** these were first drafted as 1136-1145 (career-ops' own next-available block) but that collided with 4 already-applied ai-job-search jobs (Eli Health, Amazon Alexa Smart Home, RBC Borealis, Tenstorrent) that had separately claimed those same numbers. Renumbered to 1304-1311, immediately after ai-job-search's own freshly-assigned block (1249-1303), before merging into the tracker. No already-applied job was touched.
