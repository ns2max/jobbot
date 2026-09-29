# Postings that couldn't be evaluated — need manual read in Chrome

**Status: the original 72 rows below are RESOLVED** — a manual review pass on 2026-09-20 (via Claude cowork) read most of them directly on their company/ATS pages and scored them; results are in `manual-review-results.md`, already merged into `seen_jobs.json`. Rows are kept here as a historical record, not renumbered. **33 NEW postings were added below (2026-09-20, second pass)** from a later discovery batch (IDs 1440-1618) — these are the ones still genuinely open for manual review. 105 total rows in this file; 33 are live, the rest already handled.

All returned a blank/template page, got rate-limited, or were blocked (403) before the automated tools could read the actual job description — no Playwright/browser tool is available in this environment. Open these directly in Chrome, read the JD, and score with `manual-review-instructions.md`.

⭐ = title-level strong specialty match (edge/embedded/DSP/audio/CV/FDE) — worth prioritizing if you don't want to do all of them.

**Not in this list (already resolved, no Chrome needed):** #1298 ServiceNow (confirmed expired), #1331 IBM (hard eligibility FAIL — "PhD graduates are not eligible for this program"), #1351 LVT (hard eligibility FAIL — US-work-authorization only, otherwise would've been a strong technical match), #1371 NBC Universal (expired), #1383 Lumenalta (404). Also now resolved from the second pass: #1501 IBM (same PhD-ineligible clause as #1331), #1570 SAP (mis-tagged Canada result, actually Bangalore India onsite), #1572 Samsara (Remote-US only, no Canada), #1577 jobgether/Lever (404), #1602 BCE/Bell (closed), #1614/#1615 FairwAI (unpaid student fellowships, not real roles), plus 10 duplicates of already-tracked postings found under new IDs (#1477, #1480, #1505, #1510, #1520, #1538, #1568, #1592, #1597, #1616 — see their `seen_jobs.json` notes for which ID each duplicates).

| ID | Company | Role | Platform | URL |
|----|---------|------|----------|-----|
| 1369 | ⭐ Aerovect | Senior Staff Software Engineer, Perception | Ashby | https://jobs.ashbyhq.com/AeroVect/5bc8532b-0cf1-4115-895e-327e31d16b0f |
| 1377 | ⭐ FabStation | Senior Computer Vision Engineer, Real-Time 3D Tracking | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__140300747__7103 |
| 1381 | ⭐ protege | Forward Deployed Engineer, Audio | Ashby | https://jobs.ashbyhq.com/protege/2d001d2f-40a0-428d-96cb-114323c38cd8 |
| 1389 | ⭐ alsglobal | Machine Learning Engineer | Workday | https://alsglobal.wd103.myworkdayjobs.com/External/job/Montreal-Quebec-Canada/Machine-Learning-Engineer_R9121 |
| 1392 | ⭐ docebo | Founding Forward Deployed Engineer | Ashby | https://jobs.ashbyhq.com/docebo/273845bc-2e43-4e48-99fe-815ff6188d8a |
| 1413 | ⭐ GE Vernova | Senior Staff Embedded Software Developer - DSP / Développeur logiciel embarqué senior – DSP F/H | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/senior-staff-embedded-software-developer-dsp-d%C3%A9veloppeur-logiciel-embarqu%C3%A9-senior-senior-staff-%E2%80%93-dsp-f-h-at-ge-vernova-4459654880 |
| 1422 | ⭐ Microchip Technology Inc. | Principal DSP Firmware Engineer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/principal-dsp-firmware-engineer-at-microchip-technology-inc-4449920657 |
| 1423 | ⭐ Microsoft | Applied Scientist - CoreAI Voice Agent | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/applied-scientist-coreai-voice-agent-at-microsoft-4469513968 |
| 1426 | ⭐ Octasic | Wireless Communications Systems Developer (SDR / Protocols / Embedded) | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/wireless-communications-systems-developer-sdr-protocols-embedded-at-octasic-4454179447 |
| 1431 | ⭐ SearchLabs | Computer Vision Engineer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/computer-vision-engineer-at-searchlabs-4467783528 |
| 1436 | ⭐ Waste Robotics | Developpeur(euse) Vision Senior | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/developpeur-euse-vision-senior-at-waste-robotics-4467576725 |
| 1280 | Hyatt | Sr. Machine Learning Engineer (Canada - Remote) | Taleo | https://hyatt.taleo.net/careersection/1/jobdetail.ftl?job=CHI015575&lang=en |
| 1282 | Okta | Staff Machine Learning Engineer, SecureAI | Okta careers page | https://www.okta.com/company/careers/opportunity/8208359?gh_jid=8208359 |
| 1285 | Royal Bank of Canada | Senior Machine Learning Software Engineer | Workday | https://rbc.wd3.myworkdayjobs.com/RBCGLOBAL1/job/401-GEORGIA-ST-WVANCOUVER/Senior-Machine-Learning-Software-Engineer_R-0000186441 |
| 1286 | Synechron | AI / ML Engineer | Workday | https://synechron.wd1.myworkdayjobs.com/SynechronCareers/job/MDC--Montreal/AI---ML-Engineer_JR1043328 |
| 1289 | priceline | Machine Learning/GenAI Engineering Manager | Workday | https://priceline.wd1.myworkdayjobs.com/Priceline/job/Toronto/Machine-Learning-GenAI-Engineering-Manager_R5823 |
| 1290 | Royal Bank of Canada | Senior Machine Learning Engineer | Workday | https://rbc.wd3.myworkdayjobs.com/RBCGLOBAL1/job/RBC-CENTRE-155-WELLINGTON-ST-WTORONTO/Senior-Machine-Learning-Engineer_R-0000186948-1 |
| 1292 | Artificial.Agency | Senior Machine Learning Engineer | Ashby | https://jobs.ashbyhq.com/artificial.agency/c6da058c-32a0-4dba-938a-b29c9823691c |
| 1296 | Ciklum | Senior AI/Machine Learning Engineer | Oracle Cloud HCM | https://ialmme.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/ciklum-career/job/4644 |
| 1299 | Okta | Staff Machine Learning Engineer, Generative AI (Auth0) | Okta careers page | https://www.okta.com/company/careers/opportunity/8139696?gh_jid=8139696 |
| 1300 | ZoomInfo | Senior Machine Learning Engineer | ZoomInfo | https://www.zoominfo.com/careers?gh_jid=8537816002 |
| 1301 | The Agency Fund | AI/ML Engineer | Ashby | https://jobs.ashbyhq.com/the%20agency%20fund/7250e7d0-993e-4df1-8c7e-4ab3cbde9930 |
| 1302 | Synthesia | Machine Learning Engineer - Roleplay Sessions | Ashby | https://jobs.ashbyhq.com/synthesia/637a0f3b-fd23-409a-b66b-917d1411d56e |
| 1303 | Cleveland Clinic | Staff/Senior Machine Learning Scientist | Workday | https://ccf.wd1.myworkdayjobs.com/ClevelandClinicCareers/job/Remote-Location/Staff-Senior-Machine-Learning-Scientist_353997 |
| 1337 | inetco | Senior Machine Learning / AI Engineer | BambooHR | https://inetco.bamboohr.com/careers/46 |
| 1338 | Socket.dev | Director & Principal Engineer, AI/ML & MLOps Platform | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__144705904__7103?geoID=6399 |
| 1339 | Socket.dev | Director & Principal AI/ML Platform Engineer | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__144705785__7103?geoID=6399 |
| 1341 | Katalyst Data Management | Senior AI/ML Engineer | ADP | https://workforcenow.adp.com/mascsr/default/mdf/recruitment/recruitment.html?ccId=19000101_000001&cid=bac9de56-9737-42ae-8a5c-ec456daa802e&jobId=9201205095504_1&lang=en_US |
| 1342 | Katalyst Data Management | AI/ML Engineer | ADP | https://workforcenow.adp.com/mascsr/default/mdf/recruitment/recruitment.html?ccId=19000101_000001&cid=bac9de56-9737-42ae-8a5c-ec456daa802e&jobId=9201205090285_1&lang=en_US |
| 1343 | Ernst & Young Advisory Services | AI and Data - Manager - AI/ML Engineer | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__142359052__7103?geoID=847 |
| 1344 | Vancity | Senior Machine Learning Engineer | UltiPro | https://recruiting.ultipro.com/van5000vcscu/JobBoard/a46cbdaaca2c49b68d2be0ceaafa0e25/OpportunityDetail?opportunityId=69c2b79d-4c89-4bf4-9ced-a332ab7cdc20 |
| 1345 | Workday (the company itself) | Machine Learning Engineer | Workday | https://workday.wd5.myworkdayjobs.com/Workday/job/Canada-BC-Vancouver/Machine-Learning-Engineer_JR-0109545-1 |
| 1346 | lululemon | Staff AI/ML Engineer — GenAI & Scalable AI Platform (Onsite) | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__138299989__7103?geoID=6399 |
| 1347 | Agile Electromagnetics Inc. | Machine Learning Engineer | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__140253070__7103?geoID=4247 |
| 1350 | Runway | Senior/Staff Product Engineer | Ashby | https://jobs.ashbyhq.com/runway-ml/0feb8680-6573-458b-b00d-98aea86a94f5 |
| 1354 | Expertshub.ai | AI Engineer | PowerToFly | https://powertofly.com/jobs/detail/2581090 |
| 1361 | Cohere | Member of Technical Staff, Pre-Training Data | Ashby | https://jobs.ashbyhq.com/cohere/859e2e47-02fb-4afe-bb8a-e83bf4d8c265 |
| 1362 | Cohere | Senior Member of Technical Staff, Synthetic Data | Ashby | https://jobs.ashbyhq.com/cohere/2df2da3c-fb69-4d4d-b3c9-077b3df2ba3d |
| 1363 | Cohere | Site Reliability Engineer, Inference Infrastructure | Ashby | https://jobs.ashbyhq.com/cohere/8b6696e1-f1c4-4010-bde9-3cec1340a2a6 |
| 1364 | Cohere | Forward Deployed Engineer, Infrastructure Specialist (North America) | Ashby | https://jobs.ashbyhq.com/cohere/be48aafc-9610-4ebd-8414-a0722a3cd59a |
| 1365 | d-Matrix | Sr. Staff, ML Researcher - LLM Algorithmic Optimization | Ashby | https://jobs.ashbyhq.com/d-matrix/59e6acf8-2d7c-4aa0-a2af-aa9f27d4d31e |
| 1366 | Outsiders Fund | ML Ops Engineer - Data Pipelines & Perception Tooling | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__140574594__7103 |
| 1367 | Artificial.Agency | AI Engineer | Ashby | https://jobs.ashbyhq.com/artificial.agency/31e14e65-ea3c-425d-adf0-875857e65b0a |
| 1368 | AeroVect Technologies Inc. | Software Engineer, ML Ops | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__140499558__7103 |
| 1370 | Palitronica Inc. | MLOps & Data Engineer — Build & Scale AI Pipelines | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__141206096__7103 |
| 1373 | ODAIA | Lead ML Engineer: Production AI & Big Data | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__140696930__7103 |
| 1375 | Roche | Applied AI Scientist, Cheminformatics | Workday | https://roche.wd3.myworkdayjobs.com/roche-ext/job/Mississauga/Applied-AI-Scientist--Cheminformatics_202608-121627 |
| 1376 | OpenSpace | Sr. Computer Vision Engineer | careers page shell | https://www.openspace.ai/careers |
| 1378 | Implant Genius | Senior Data Scientist / GenAI / 3D CV / Photogrammetry | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__140498880__7103 |
| 1379 | Mundo AI | Member of Technical Staff | Ashby | https://jobs.ashbyhq.com/mundo-ai/651413ef-5e0f-4aca-8a4a-f2595476fb34 |
| 1380 | Veeda AI | Member of Technical Staff - ML Data | Ashby | https://jobs.ashbyhq.com/veeda-ai/cff4c53f-b4b6-43c8-9437-40d66cefa263 |
| 1384 | apella | Senior Machine Learning Engineer, Forecasting | Ashby | https://jobs.ashbyhq.com/apella/b4cd6537-f32f-4d1a-9b78-1857b1009488 |
| 1386 | wynd-labs | Machine Learning Engineer | Ashby | https://jobs.ashbyhq.com/wynd-labs/a148c710-7685-4184-9be8-c4d46a0a8f04 |
| 1387 | payabli | Staff Machine Learning Engineer | Ashby | https://jobs.ashbyhq.com/payabli/cd2074e4-b45b-454d-a9f4-8608cc024804 |
| 1388 | inferact | Member of Technical Staff, Inference | Ashby | https://jobs.ashbyhq.com/inferact/ef7198da-ad0a-4c02-963f-6250a15e3534 |
| 1391 | yuja | AI Engineer | BambooHR | https://yuja.bamboohr.com/careers/494 |
| 1393 | Render | Forward Deployed Engineer | Ashby | https://jobs.ashbyhq.com/render/b29de212-fcca-4b5d-8640-a165b23d5d6c |
| 1395 | decodahealth | Forward Deployed Engineer | Ashby | https://jobs.ashbyhq.com/decodahealth/22de9ee6-b411-463e-87c0-b8c3ded62028 |
| 1397 | Magical | AI Forward Deployed Engineer | Ashby | https://jobs.ashbyhq.com/magical/55801f62-d42b-4c68-87ba-01c483ba4459 |
| 1398 | Unit8 SA | Senior Forward Deployed Engineer (Hybrid, Canada) | Workable | https://apply.workable.com/j/6E5DB3FE0F |
| 1399 | Artefact | Senior Forward Deployed Engineer (Gemini Enterprise) | Greenhouse (form-only) | https://job-boards.greenhouse.io/artefact/jobs/8716939002 |
| 1406 | Cerebras | Staff Software Engineer, GPU Inference | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/staff-software-engineer-gpu-inference-at-cerebras-4466314167 |
| 1407 | Ciena | Principal SerDes System/DSP Design Engineer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/principal-serdes-system-dsp-design-engineer-at-ciena-4369562263 |
| 1408 | Cohere | Senior Software Engineer, GPU Infrastructure (HPC) | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/senior-software-engineer-gpu-infrastructure-hpc-at-cohere-4404281841 |
| 1409 | Cresta | Senior Forward Deployed Engineer (AI Agent) | Greenhouse (form-only) | https://job-boards.greenhouse.io/cresta/jobs/4595480008 |
| 1410 | Deloitte | Ingénieur ou ingénieure de recherche en IA | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/ing%C3%A9nieur-ou-ing%C3%A9nieure-de-recherche-en-ia-at-deloitte-4463828390 |
| 1411 | Doppel | Forward Deployed Engineer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/forward-deployed-engineer-at-doppel-4438115994 |
| 1412 | Electronic Arts (EA) | MLOps Developer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/d%C3%A9veloppeur-se-op%C3%A9rations-li%C3%A9es-%C3%A0-l%E2%80%99apprentissage-automatique-mlops-developer-at-electronic-arts-ea-4465933701 |
| 1416 | Index Exchange | Senior Machine Learning Engineer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/senior-machine-learning-engineer-at-index-exchange-4407622665 |
| 1417 | Jesta I.S. | Senior MLOps Developer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/senior-mlops-developer-d%C3%A9veloppeur%C2%B7euse-mlops-senior-at-jesta-i-s-4466600164 |
| 1418 | L'Oréal | MLOps Developer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/mlops-developer-at-l-or%C3%A9al-4460621092 |
| 1420 | Manulife | Machine Learning Engineer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/machine-learning-engineer-at-manulife-4454925313 |
| 1421 | Meta | SWE, Systems ML (Frameworks/Compilers/DL-Kernels) | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/software-engineer-systems-ml-frameworks-compilers-dl-kernels-ing%C3%A9nieur-logiciel-sp%C3%A9cialis%C3%A9-en-apprentissage-automatique-des-syst%C3%A8mes-%E2%80%93-cadres-compilateurs-noyaux-d-apprentissage-profond-at-meta-4458495244 |
| 1425 | NVIDIA | DL Performance Software Engineer - LLM Inference | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/dl-performance-software-engineer-llm-inference-at-nvidia-4450018115 |
| 1427 | ProteinQure | Research Software Engineer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/research-software-engineer-at-proteinqure-4468285604 |
| 1428 | RBC | Senior ML Engineer, ML Platform - GFT | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/senior-ml-engineer-ml-platform-gft-at-rbc-4454037841 |
| 1429 | RBC | Lead ML Platform Engineer | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__145588770__7103 |
| 1430 | SCIENTIFIC GAMES | Senior Machine Learning Engineer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/senior-machine-learning-engineer-at-scientific-games-4453483087 |
| 1432 | SecurityScorecard | Senior Forward Deployed Engineer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/senior-forward-deployed-engineer-at-securityscorecard-4463090100 |
| 1433 | Skip | Senior Machine Learning Engineer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/senior-machine-learning-engineer-at-skip-4417228191 |
| 1434 | Syntrace | Applied AI Engineer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/applied-ai-engineer-at-syntrace-4469506430 |
| 1435 | TD | AI/ML Platform Engineer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/ai-ml-platform-engineer-at-td-4465329807 |
| 1437 | Xanadu | Quantum Architecture Research Software Developer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/quantum-architecture-research-software-developer-at-xanadu-4462426699 |
| 1438 | Arcadia | Forward Deployed Engineer | LinkedIn (rate-limited) | https://ca.linkedin.com/jobs/view/forward-deployed-engineer-at-arcadia-4467237710 |
| 1439 | 11x | Forward Deployed Engineer [REMOTE - Canada] | gem.com ATS | https://jobs.gem.com/11x-ai/am9icG9zdDo7tWh-PewL-ku53L0cC2FB |

### Second pass (2026-09-20) — 33 new rows, genuinely open

| ID | Company | Role | Platform | URL |
|----|---------|------|----------|-----|
| 1469 | Assembler AI | Senior Backend Engineer — Real-Time Vision Cloud | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__145134498__7103?geoID=4&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1470 | ⭐ IBM Computing | Senior Real-Time AI Infrastructure Engineer | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__144801608__7103?geoID=3531&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1567 | Stripe | Machine Learning Engineer | Stripe careers page (listing shell only, no JD resolved) | https://stripe.com/jobs/search?gh_jid=8014859&utm_source=freehire.me |
| 1569 | kadence | Machine Learning Data Engineer | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__145325456__7103?geoID=4&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1574 | Jobtailor | Applied Data Scientist/Engineer | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__144537397__7103?geoID=6225&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1575 | TD Bank | AI2 Applied Machine Learning Scientist (Graduate) | Workday | https://td.wd3.myworkdayjobs.com/TD_Bank_Careers/job/Toronto-Ontario/AI2-Applied-Machine-Learning-Scientist---Associate_R_1506714-1?utm_source=freehire.me |
| 1576 | Autodesk | Senior Data Scientist | Workday | https://autodesk.wd1.myworkdayjobs.com/Ext/job/Toronto-ON-CAN/Senior-Data-Scientist_26WD99752-1?utm_source=freehire.me |
| 1579 | vectorinstitute | Associate Software Developer, Machine Learning | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__142937123__7103?geoID=6225&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1580 | Tenova | R&D Engineer- Data Scientist | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__145284048__7103?geoID=3775&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1583 | SimpliCity Digital Inc | Applied AI Engineer (JavaScript, Remote in Canada) | Workable | https://apply.workable.com/j/599E79DC83?utm_source=freehire.me |
| 1585 | Forward Financing | Staff Applied AI Engineer | Ashby | https://jobs.ashbyhq.com/forward%20financing/63049e18-d7c8-48ea-8fea-d052f8aa7241?utm_source=freehire.me |
| 1586 | morningstar | Senior Software Engineer- Applied AI | Workday | https://morningstar.wd5.myworkdayjobs.com/morningstar/job/Toronto/Senior-Software-Engineer--Applied-AI_REQ-058502?utm_source=freehire.me |
| 1587 | OpenHouse.ai | Hybrid Data & Integration Engineer — AI-Driven Homebuilding | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__145371799__7103?geoID=847&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1588 | ODAIA | Lead ML Platform Engineer | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__145777276__7103?geoID=847&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1589 | ⭐ Teledyne (FLIR) | Senior Firmware Engineer | Workday | https://flir.wd1.myworkdayjobs.com/flircareers/job/Canada---Richmond-BC/Senior-Firmware-Engineer_REQ36559?utm_source=freehire.me |
| 1590 | Huawei Technologies Canada | Research Engineer - AI Data Security | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__142241923__7103?geoID=6551&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1591 | Elastic | Senior Security Research Engineer, SONAR | Elastic careers page | https://jobs.elastic.co/jobs?gh_jid=8130114&gh_jid=8130114&utm_source=freehire.me |
| 1594 | Citi | (Python) AI Engineer - Vice President | Workday | https://citi.wd5.myworkdayjobs.com/2/job/Mississauga-Ontario-Canada/XMLNAME--Python--AI-Engineer---Vice-President_26992058?utm_source=freehire.me |
| 1595 | AMD | Agentic AI / Data Engineer - DC GPU | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__145234330__7103?geoID=7029&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1598 | Vanguard | Senior AI/ML Scientist | Workday | https://vanguard.wd5.myworkdayjobs.com/vanguard_external/job/Toronto-Canada/Senior-AI-ML-Scientist_182067-1?utm_source=freehire.me |
| 1599 | RBC | Data Scientist and AI Engineer, Autonomous AI Agents | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__145529449__7103?geoID=6225&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1600 | PowerToFly | Lead Backend Engineer for AI at Thomson Reuters | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__144496442__7103?geoID=6225&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1601 | Computrition, Inc. | Experienced Backend Engineer with AI-Focused Expertise | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__144498726__7103?geoID=6747&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1603 | Royal Bank of Canada | Principal Data Science and AI Engineer | Workday | https://rbc.wd3.myworkdayjobs.com/RBCGLOBAL1/job/TORONTO-Ontario-Canada/Principal-Data-Science-and-AI-Engineer_R-0000187083?utm_source=freehire.me |
| 1604 | Royal Bank of Canada | Data Scientist and AI Engineer, Autonomous AI Agents (likely same as #1599, unconfirmed) | Workday | https://rbc.wd3.myworkdayjobs.com/RBCGLOBAL1/job/TORONTO-Ontario-Canada/Data-Scientist-and-AI-Engineer-Autonomous-AI-Agents--LLMs-and-Deep-Learning-_R-0000187024-1?utm_source=freehire.me |
| 1605 | Uncover (Nexxa) | Backend Engineer for AI Infrastructure | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__144494869__7103?geoID=6225&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1606 | Engg | Backend AI Engineer | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__145049067__7103?geoID=6225&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1608 | Mission.dev | AI Infrastructure Engineer | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__145590026__7103?geoID=4&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1609 | HRB | Backend Engineer for AI Applications | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__142652659__7103?geoID=6399&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1610 | ⭐ GFL Environmental Inc. | Senior Data Engineer — Real-Time AI & Data Platform | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__144533696__7103?geoID=6412&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |
| 1611 | Bank of Montreal | Lead Cloud Software Developer (AWS / AI / Real Time Payment Systems) | Workday | https://bmo.wd3.myworkdayjobs.com/External/job/Toronto-ON-CAN/Lead-Cloud-Software-Developer----AWS---AI---Real-Time-Payment-Systems-_R260019528-1?utm_source=freehire.me |
| 1612 | Aptiv | Member of Technical Staff – OS Kernel | Workday | https://aptiv.wd5.myworkdayjobs.com/APTIV_CAREERS/job/CAN-Kanata-2-ON---WR/Member-of-Technical-Saff---OS-Kernel_J000701242-1?utm_source=freehire.me |
| 1613 | Citibank (Switzerland) AG | Gen AI Solutions Python Developer | WhatJobs redirect | https://en-ca.whatjobs.com/pub_api__cpl__144503399__7103?geoID=3775&utm_campaign=publisher&utm_medium=api&utm_source=freehire.me |

## After you review one

Use the rubric and prompt template in `manual-review-instructions.md`. Two options once you've read a posting:
1. **Score it yourself** and tell me the result — I'll write it into `seen_jobs.json` (fit score + note) so it shows up correctly in the unified tracker instead of the placeholder.
2. **Paste the JD text back to me** — I'll run the same 5-dimension evaluation on it that the rest of the batch got.

Either way, give me the ID so I can match it up. You don't need to do all 72 — the ⭐ ones are the best use of your time if you want to triage.
