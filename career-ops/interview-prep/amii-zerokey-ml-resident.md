# Interview Prep — Amii × ZeroKey: Machine Learning Resident (12-month term)

**Job ID:** 1085 (career-ops, canonical) · **Applied:** 2026-08-26 · **Stage:** pre-screen
**Posting:** https://employmenthero.com/en-ca/jobs/position/alberta-machine-intelligence-institute-machine-learning-resident-client-zerokey-12-month-term-j1f03/
**Evaluation:** [1085 report](../archive/reports/1085-amii-2026-08-25.md) — 4.5/5
**Prepared:** 2026-09-24

---

## 0. Fix these before the call

Three things in what you sent could come up. Know your answer to each.

| # | Issue | What you submitted | What's actually true | What to do |
|---|---|---|---|---|
| 1 | **The F1 number** | Cover letter: "14ms on a Raspberry Pi 4 at over 90% F1" | The published JAES 2026 result is **F1 = 0.76 at 14 ms** (DTW baseline: F1 0.65 at 1038 ms). ">90% F1" is a retired number from old CVs. | Always say **0.76**. If they quote 90% back to you: *"That number came from older material. The peer-reviewed figure is F1 0.76 at 14 ms, against a DTW baseline of 0.65 at over a second. I'd rather you hold me to the published number."* Saying this yourself earns trust. Getting caught out loses it. |
| 2 | **Kalman filtering** | CV: "Kalman filtering, signal processing, and 3D spatial reasoning sit at the center of this work." Cover letter: "not adjacent to my background, it's the center of it." | Your knowledge graph shows **deep signal processing** and **IMU/motion sensing** but **no documented Kalman filter project**. (The BNO055 IMU on the McGill guitar does its sensor fusion on the chip.) | Decide now, honestly, what your Kalman experience is. Answer at that level and cover the basics in §6.1 before the technical round. Safe framing: *"Signal processing is my core. On state estimation, I know Kalman filters and the constant-velocity tracking model well. The IMU I used did its fusion on the chip, so for ZeroKey I'd be applying standard KF/EKF smoothing to position tracks, not inventing new estimators."* Only say the "know well" part if it's true. |
| 3 | **Phone number** | The submitted CV and cover letter list **+1 817 747 8598** (retired) | Current number: **+1 613 200 2030** | Confirm the recruiter has the 613 number, and put it in your follow-up email. |

Also: you applied to **four Amii residencies** (ZeroKey 1085, OpenCycle 1087/1169, Mobia 1089, Fillip Fleet 1090). Amii's talent team probably sees all four. Have a ranked answer ready (see §4, Q9).

---

## 1. What this call probably is

The Glassdoor ML Resident reviews and other candidate write-ups describe the same sequence:

1. **Pre-screen (this call), ~20 min**, with HR or a product manager. Covers your background, your motivation, and the role description. Reviewers call it "basic."
2. **Technical interview, ~60 min**, with an Amii scientist, and the client may attend. Reported topics: overfitting and underfitting, data handling, deep learning architectures, **RL and sequential decision-making**, **agentic AI**, and LLMs. One candidate said they got 3–4 RL questions even though RL was barely in the job description. **Expect RL.** Amii is an RL institute, and OmniVisor uses RL.
3. **Situational / behavioural interview.** Reported questions include how you'd run a social event, your favourite sports team, and how you'd judge a former colleague's behaviour. They're testing culture and team fit.
4. Timelines vary a lot: one review says 6 weeks, another 9 months. Silence after the final round has been reported, so follow up politely.

What the pre-screen checks: (a) can you explain your background clearly in two minutes, (b) do you actually want *this* residency, not just any job, (c) logistics: Edmonton, availability, work authorization, pay expectations, (d) whether a PhD with 10 years' experience will stay through a 12-month entry-level contract.

People named on the posting: **Xu Han, Machine Learning Scientist** and **Amor Provins, Product Owner, Advanced Technology**. If Amor joins a round, your examples can be less technical and more about outcomes.

### Technical interviewer: Xu Han (pronounced roughly "Shoo Hahn")
Named by Erika Bruneau at the pre-screen. He is almost certainly the "Xu, Machine Learning Scientist" quoted in the ZeroKey posting, so he likely scoped the project and would be the resident's Amii supervisor.
- **Role:** Machine Learning Scientist, **Advanced Technology** team, Amii (the same team as Amor Provins). Profile: https://www.amii.ca/people/xu-han
- **Background:** PhD in Mechanical Engineering, University of Illinois Chicago. Research on **AI to speed up scientific simulations of complex chemical processes in energy systems** (combustion, chemical kinetics, AI for science). 16 peer-reviewed papers; Amii's profile says 800+ citations, and Google Scholar now shows about 1,100.
- **Industry work before Amii:** custom AI for clients, including **computer vision for quality inspection** and **business-process automation with LLMs**.
- **What he says he cares about:** "novel AI approaches for under-explored industry applications with high-impact potential."

**How to use this:**
- **Lead with MAS quality inspection** (care-label QC with PLC reject, fabric defect detection). He has built the same kind of system, so you can talk as peers.
- **Physics and domain priors will land with him.** He works on AI for simulation, so framing a Kalman constant-velocity model as a physics prior, or synthetic data as simulation, fits how he thinks. Your rule-based synthetic-variation generator plays the role a simulator plays in his work. Expect questions on **why a model choice fits the physics of the data**, and on the "3D physical simulation" nice-to-have.
- **LLM automation → agentic side of the role.** He's done applied LLM automation, so expect practical questions on tool calling and how agents use model outputs, not LLM research.
- **Honest gaps he'll probably find:** 3D reconstruction and simulation, and formal Kalman work. Name them yourself, then show how you'd close them.
- **"Under-explored application" is his own phrase.** Use it: millimetre-accurate RTLS trajectories are an under-explored data source, and nobody has standard benchmarks for them yet. Mention you'd bring your dataset-and-benchmark habit (four Zenodo datasets).
- **Still prepare RL** (§6.2). It isn't his published area, but Glassdoor says Amii technical rounds include it.
- **Questions for him:** "How did you scope this project with ZeroKey, and what would success look like at month 12?" "Is there room to use physics-informed or simulation-based priors on the RTLS data?" "What did you learn from the CV-inspection projects that applies here?"
- Check his LinkedIn and Google Scholar (https://scholar.google.com/citations?hl=en&user=PEFl4WsAAAAJ; make sure the profile lists Amii) and skim one recent paper.

---

## 2. Amii — what to know

**What it is.** The Alberta Machine Intelligence Institute is one of Canada's **three national AI institutes**, with **Mila** (Montreal) and the **Vector Institute** (Toronto), under the Pan-Canadian AI Strategy that CIFAR runs. It's a non-profit based in downtown Edmonton and closely tied to the **University of Alberta**. It started in 2002 as the Alberta Ingenuity Centre for Machine Learning and rebranded as Amii in 2017. Its tagline is **"AI for Good and for All."**

**Who's there.**
- **Cam Linke**, CEO. His public message is that Canada's AI strategy needs *customers*, meaning companies adopting AI, not only research output. The residency program is that idea in practice.
- **Richard S. Sutton**, Chief Scientific Advisor. He won the 2024 ACM Turing Award with Andrew Barto for reinforcement learning, and co-wrote *The Alberta Plan for AI Research* (2022) with Michael Bowling and Patrick Pilarski.
- Fellows include **Michael Bowling** (poker AI: Cepheus, DeepStack), **Martha White** (RL), and **Patrick Pilarski** (RL for prosthetics; interesting to you because it's sensors plus real-time control of a physical device).
- Amii has run RL research for 20+ years. It's the institute's identity.

**Recent news (worth knowing, good small talk):**
- **National AI Literacy Initiative**, run with the Government of Canada, aims to reach **1 million learners** and **launched 21 Sep 2026** (three days ago). Google is a partner on AI literacy, announced at Upper Bound.
- **Government of Alberta: $50M over five years** (July 2026) to apply AI in public services and grow the economy.
- **Upper Bound 2026** (May, Edmonton): 11,000 attendees, 53% growth, billed as Canada's fastest-growing AI conference.

**How the residency works.** It's paid and full-time. You **report to an Amii Scientist** and meet regularly with the client team for knowledge transfer. You sit in a cross-functional team (ML research, project management, software engineering, product development). There's a **possible permanent role at the client** at the end, at the client's discretion. Pay is **"negotiated at time of offer."** Amii frames the program as being for "early-career professionals," which matters for §4, Q6.

**Why it matters to them:** Amii's industry arm succeeds when a client (ZeroKey) ends the term with a deployed model *and* the in-house skill to maintain it. Talk about **knowledge transfer, documentation, reproducible pipelines, and training people.** You have real examples: the MAS CV training seminars, CI/CD and code review at MAS, the MUSMET deployment docs, and two supervised BSc theses.

---

## 3. ZeroKey — what to know

**Basics.** Founded **2016**, HQ **Calgary** (3120 – 12 St. NE). **Matthew Lowe** is co-founder and CEO. Hugh McMillan is listed as co-founder and COO in third-party profiles (check LinkedIn). Series A led by **Brick & Mortar Ventures**, with **Asahi Kasei** and **Plug and Play**. Member of **NVIDIA Inception**. ISO 9001:2015. Customers include **more than 10% of the Fortune Global 500** (automotive, aerospace, advanced manufacturing, semiconductors), with deployments in 40+ countries. The Indo-Pacific (Korea, Japan, Taiwan) is a major market, plus defence customers in NATO-aligned countries.

**Their pitch (use their words):** *"The spatial data layer for Physical AI."* Software AI took off because every keystroke is recorded as data. A factory floor has nothing equivalent: human actions, tool motion and assembly steps are invisible to software. ZeroKey records them.

**Quantum RTLS (the hardware):**
- **Ultrasonic time-of-flight ranging**, not UWB or radio. Claimed accuracy **±1.5 mm in 3D**, versus about ±150 mm for UWB, about 1 m for BLE, about 3 m for Wi-Fi. They call it "100× more precise than anything else."
- Anchors about 20 m apart, **self-calibrating** (no manual surveying). Mobile trackers, wearables (badges and wristbands), PoE anchors, gateways, "Dot" nodes. Version 3.0 hardware now shipping.
- Handles **RF-hostile environments** (metal, machinery) where UWB suffers from multipath.
- **No cameras**, so no video-privacy problem. That matters for tracking workers.
- **35+ patents** (older sources say 24 or 30). Quantum RTLS launched in 2022, and growth since then has been steep.
- Revenue: hardware plus **per-device software licences**, plus a separate per-device **OmniVisor AI licence**.

**OmniVisor AI (the software this residency supports):**
- Launched **October 2025**. Described as "the first agentic intelligence engine that understands physical movement and process dynamics," with "a dedicated AI process engineer in every work cell."
- Built on **reinforcement learning plus LLMs**, with **AI-native tool calling and the Model Context Protocol (MCP)**. Model-agnostic, with native OpenAI support or a customer's own LLM.
- Published numbers: **10,000+ events/sec**, **<500 ms anomaly detection**, "95%+ accuracy," "50% faster setup."
- Users can ask in plain language ("Which lines had the most downtime yesterday?") and schedule "runnable tasks."
- Partner ecosystem: **Tulip Interfaces** (frontline operations platform; joint appearance at Hannover Messe 2026), VivaTech 2026, open API (api.zerokey.com).

**Real use cases to mention** (these are what "risky behaviour" and "non-compliant operations" mean in practice):
- **Bolt sequencing and torque validation**: checking the tool was at the right bolt, in the right order.
- **SOP validation on automotive assembly**: a tier-one supplier caught SOP violations as they happened and avoided thousands of defective vehicles.
- Bin picking and material verification. Luxury-goods traceability of precious metals.
- **Human–robot coordination, collision avoidance, AGV/AMR guidance, geofenced worker safety.**
- **Time-and-motion studies**, cycle-time analysis, worker heatmaps, inventory that "never got lost again."

### 3a. Ultrasound product, but a vision-heavy job description?

**What the job description actually says.** Vision and video appear only in the *qualifications*, never in the *responsibilities*:
- The required degree specialization list includes Computer Vision, alongside Spatial Intelligence, Physical AI and others.
- "Research or project experience in **one or more of**: computer vision, time series, video analysis, VR, motion sensing, pose estimation." This is an either/or list, and you already meet four of the six.
- Nice-to-haves: multimodal foundation models (VLMs/LLMs) and publications "especially in computer vision and 3D spatial intelligence."

The responsibilities and project description talk only about "millimeter-accurate positioning data and other observables," "spatial-temporal multimodal analysis," and risky-behaviour prediction. **The core data is RTLS trajectories, not video.**

**Why vision still shows up (my reading, not confirmed):**
1. **Vision is where the methods come from.** Pose estimation produces keypoint trajectories over time, and skeleton-based action recognition (e.g. ST-GCN) works on exactly that. An RTLS track (a few tags in 3D, mm accuracy, high rate) has the same structure as a sparse skeleton. People from CV/pose/video research are the natural hiring pool for "classify an action from 3D point trajectories."
2. **"Other observables" and "multimodal."** ZeroKey's "no cameras" claim is about how they *locate* things. It doesn't mean cameras never appear in a deployment. There's one verified case: the Tulip partnership paired Quantum RTLS with **Tulip Vision** cameras for bin tracking and photography. Tool, torque or MES events are other likely inputs.
3. **Ground-truth labelling (inference).** Video recorded during data collection is a common way to label position tracks ("this window = overhead reach"). Some video handling could be part of building datasets, even if cameras never run in production.
4. **VLMs in the agent layer (inference).** OmniVisor is LLM-based. Multimodal models could read floor plans, SOP documents with diagrams, or dashboards.
5. **Amii job descriptions reuse templates.** The Amii scientist on the project may come from CV (e.g. "Xu"), and the "spatial intelligence" wording is broad on purpose.

**How to use this:**
- It's upside for you, not a gap. You have **industrial CV** from MAS (care-label QC, fabric defect detection, image registration and warping for Promptly) *and* motion sensing and time-series work. Say: *"My CV background is industrial, not academic benchmarks, but the skill that transfers here is modelling motion as structured trajectories, and that's my PhD."*
- **Ask it outright** on the pre-screen or in round 2: *"The posting lists computer vision and video analysis. Is there a camera or vision stream in this project, for example for labelling ground truth or fusing with RTLS, or is it purely positioning data?"* It shows you read both the product and the job description closely.

---

## 4. Pre-screen answers

### Q1. "Tell me about yourself." (target ~90 seconds)

> I build real-time ML on physical sensor data and run it on edge hardware. I have about ten years of it, half in industry, half in research.
>
> I started at **MAS Holdings**, South Asia's largest apparel manufacturer, where I spent five and a half years on factory floors. I built computer-vision inspection systems wired into PLCs, and an **IoT system that tracked sewing productivity** across factories on three continents, including tracking operators' repetitive motion patterns for efficiency. So I've seen the problem ZeroKey solves from the factory side.
>
> Then I did a PhD at the University of Trento on **real-time pattern detection on embedded devices**: detecting temporal patterns in audio and motion streams on a Raspberry Pi in 14 milliseconds, **74 times faster** than the DTW baseline, published in the *Journal of the Audio Engineering Society*. At **McGill** I added motion sensing: a smart guitar with an IMU, fusing gesture detection with audio in real time. As a postdoc on an EU project, I built a pipeline that captured and **time-synchronized head and hand tracking, EEG and audio from four people at once**.
>
> This role combines both halves: spatial-temporal ML on noisy physical data, deployed at the edge, in manufacturing. I'm a Canadian PR, based in Toronto, available immediately, and happy to relocate to Alberta.

(Use "about ten years," and don't open with the PhD. The role is applied, so lead with the factory floor.)

### Q2. "Why Amii?"
- There's an institute whose whole job is getting research into real companies, and it happens to be the world's RL centre (Sutton, the Alberta Plan). OmniVisor is built on RL, so the scientific mentorship fits the product.
- You've worked the research-to-deployment path from both sides (MAS as the industry side, Trento/McGill as the lab side). Residencies are built on exactly that path.
- Optional, if it fits naturally: the AI Literacy launch this week and the $50M Alberta investment show Amii is growing its applied side, and that's where you want to be.

### Q3. "Why ZeroKey?"
- **The data is unusually good.** Millimetre-accurate 3D tracks at thousands of events per second are rare in industrial ML. Most factory data is noisy, sparse, and captured at a single point in time. With precise trajectories, action-level recognition (which bolt, what order, what posture) becomes realistic.
- **No cameras.** You can analyze worker motion without video surveillance, which helps both adoption and ethics. At MAS, adoption on the floor depended on trust.
- **The problem matches your PhD directly.** Detecting "this sequence of motions matches, or deviates from, the SOP" in real time on edge hardware is the same question as detecting "this sequence of notes or gestures matches a pattern."
- It's a Canadian deep-tech company with real Fortune-500 revenue, not a demo.

### Q4. "What do you know about the project?"
In one breath: *"Build production ML that runs live on Quantum RTLS position streams to flag risky behaviour: ergonomic risk, human–robot proximity, and non-compliant or out-of-sequence operations. It has to be fast enough for the edge and plug into OmniVisor's agentic layer, so the models run continuously and also answer on-demand questions from users."* Then ask: *"Is the first milestone anomaly detection, or classifying specific risk behaviours?"*

### Q5. "Walk me through the accomplishment in your cover letter." (the 74× result)
- **Situation:** Musicians needed pattern detection embedded in the instrument, with under 30 ms total latency and no cloud. DTW was the standard method and took about 1 s on a Raspberry Pi 4.
- **Action:** Built MFCC features from 30 ms windows, then a stacked-RNN detector trained on synthetic variations (a rule-based generator, about 10k variations per pattern, because labelled data was scarce). Benchmarked against DTW with ablations over pattern-set sizes, and published the benchmark method and four open datasets.
- **Result:** **14 ms, F1 0.76, 31% CPU**, versus DTW at 1038 ms, F1 0.65, 49% CPU. Peer-reviewed in JAES 2026.
- **Why I'm proud of it:** it was reproducible, not only fast. The benchmark harness turned out to be the reusable asset.
- **Link to ZeroKey:** SOP-sequence detection on RTLS tracks is the same problem with a different sensor.

### Q6. "You have a PhD and 10 years. Why an entry-level 12-month residency? Will you stay?"
This is the most important answer on this call. Say it plainly and with confidence:
> "I'm moving into physical and spatial AI. The residency gives me the best entry point: a real deployment, mentorship from Amii's scientists, and a route into ZeroKey itself. I'd rather take twelve months proving myself on a hard problem than join somewhere as a generalist. And the experience means I can start delivering from week one, not month four."

Then commit: *"I'm fully in for the twelve months."* Only say that if it's true, given your SciNet and eBay processes.

### Q7. "Location — you're in Toronto, and the role says Edmonton."
- *"Happy to relocate to Alberta."* Then ask: **"The role is listed in Edmonton but ZeroKey is in Calgary. Where would the resident sit, and how much time would be on-site at ZeroKey or at customer factories?"** You need that answer anyway.

### Q8. Availability and work authorization
- Available immediately. Canadian Permanent Resident, no sponsorship needed.

### Q9. "Are you interviewing elsewhere? We see you applied to other residencies."
Be honest and give a ranking. Suggested: *"Yes. I applied to a few Amii residencies because the model fits me, but ZeroKey and OpenCycle are my top two. They're the ones built on real-time sensor ML at the edge, which is my core. I'm also in late stages with a couple of Toronto roles, so I'd appreciate a sense of your timeline."* That's true, and it creates some gentle urgency.

### Q10. Pay expectations
- The posting says pay is "negotiated at time of offer." **Glassdoor estimates CA$72K–108K** for Amii ML Residents. Your normal target is **CA$120–150K**, so there's a gap.
- On a pre-screen, **get their band before giving a number**: *"I'm flexible given the conversion path. Could you share the range budgeted for this residency?"*
- If they insist on a number, give one you've already decided you'd accept, with reasons (PhD, 10 years, relocation to Alberta). Something like *"around the top of what you'd pay a PhD-level resident, roughly $100–110K, and I'm open to discussing it."* **Decide your minimum before the call**, and whether a relocation allowance matters to you.

### Q11. "What's a weakness / something you'd need to learn?"
Pick a real gap from the job description that doesn't disqualify you: *"3D reconstruction and physical simulation. My 3D work has been tracking and registration: XR head and hand tracking, projector-camera AR, image warping for alignment. Not reconstruction. I'd lean on the Amii scientists there and get up to speed quickly, the same way I picked up audio foundation-model fine-tuning this year."*

---

## 5. Requirements vs. your evidence (for the technical round)

| Requirement (JD) | Your evidence | Strength | Say this |
|---|---|---|---|
| PhD in ML/AI/related | PhD, Trento, 2025 | ✅ | — |
| Computer vision, time-series, video, VR, **motion sensing**, pose estimation (one or more) | Time-series (the PhD core); motion sensing (McGill IMU gesture, F1 0.78); VR/XR (MUSMET: 10 Quest 3 headsets, head and hand tracking sync); industrial CV (MAS) | ✅✅ | You meet four of the six. |
| Python, PyTorch, HF Transformers, sklearn | Python expert; published work in **TF/Keras**; PyTorch proficient; HF working knowledge (Wav2Vec2 in speakfrench, MusicGen LoRA in VarianceEngine) | ⚠️ | Show the recent PyTorch/HF work: *"My recent projects are in PyTorch: LoRA fine-tuning of MusicGen across two GPUs."* |
| **Build custom ML from scratch (e.g. a transformer)** | Custom stacked RNNs, SSIM-based matcher, custom audio-to-audio conditioning head (cross-attention) in VarianceEngine, radix-2 FFT/MFCC written from scratch in JS | ⚠️→✅ | Practise writing a transformer block from scratch (§6.3). They may ask you to sketch one. |
| **Kalman filtering**, signal processing, 3D spatial computing | DSP expert (S-transform, MFCC, onset detection); 3D: XR tracking sync, AR table, garment geometry warping; **no documented KF project** | ⚠️ | See §0 issue 2 and §6.1. |
| Linux, Git, clean code | Yes. C++17 library, CI/CD at MAS | ✅ | — |
| *Nice:* VLMs/LLMs and **AI agents** | Working knowledge: daily agentic tooling (Claude Code), LLM integration level | ⚠️ | Be honest: *"Applied level. I build with agents daily, not research level."* Know MCP (§6.4). ZeroKey uses it. |
| *Nice:* 3D spatial AI / reconstruction / physics simulation | Limited | ❌ | Name it as your learning area (Q11). |
| *Nice:* **real-world noisy data** | Everything you've done: live musicians, factory IoT, EEG | ✅✅ | Say it outright: *"Every dataset I've worked with was messy and physical."* |
| *Nice:* **quantization, low-latency edge deployment** | 14 ms on RPi4; CPU profiling; <30 ms budgets | ✅ (latency) / ⚠️ (formal quantization) | Know PTQ vs QAT, int8, ONNX Runtime/TensorRT (§6.5). |
| *Nice:* CI/CD, production ML, MLE skills | MAS production systems, Jenkins, Docker, Airflow | ✅ | — |
| *Nice:* publications | 10+ peer-reviewed (JAES, IEEE, ACM) | ✅ (not in CV/3D venues) | — |
| Client communication, presentations | Trade shows, CV training seminars, compliance stakeholder specs at Forestpin, EU consortium partners | ✅ | Good material for the behavioural round. |

**Your standout angle, not visible to most candidates:** you've been the factory engineer. At MAS you tracked **repetitive operator motion for productivity** and built **changeover and allocation prediction**. That's time-and-motion analytics, which is one of OmniVisor's own use cases. Most PhD applicants have never been on a factory floor.

---

## 6. Technical brush-up for round 2 (start now, don't cram it later)

### 6.1 Kalman filter: be able to write this out
- State for 3D position tracking (constant-velocity model): `x = [p_x, p_y, p_z, v_x, v_y, v_z]ᵀ`.
- **Predict:** `x̂⁻ = F x̂`, `P⁻ = F P Fᵀ + Q`, where `F` has `I` on the diagonal and `Δt·I` in the position–velocity block.
- **Update:** `K = P⁻Hᵀ(HP⁻Hᵀ + R)⁻¹`, `x̂ = x̂⁻ + K(z − Hx̂⁻)`, `P = (I − KH)P⁻`, with `H = [I 0]` (you measure position only).
- `Q` (process noise) is how much you trust the motion model. `R` (measurement noise) is how much you trust the sensor. ZeroKey's ±1.5 mm means `R` is small, so the filter mainly helps with **velocity and acceleration estimates** (inputs for ergonomics and risk) and **outlier and dropout handling**.
- **Innovation gating:** reject a measurement if its Mahalanobis distance `(z−Hx̂⁻)ᵀS⁻¹(z−Hx̂⁻)` exceeds a χ² threshold. Ultrasound multipath or occlusion produces outliers, so this is how you'd handle them.
- **EKF/UKF:** needed when the measurement is raw range or time-of-flight to anchors (non-linear `h(x)`). ZeroKey probably solves multilateration upstream, but mention that you know the difference.
- **RTS smoother:** for offline or near-real-time analysis, a backward pass gives cleaner trajectories for training labels.
- Your honest link: *"In signal-processing terms it's a recursive optimal filter. I've done a lot of spectral and temporal filtering, and state-space estimation is the same way of thinking applied to motion."*

### 6.2 RL (expect it, per Glassdoor)
- MDP (S, A, P, R, γ). Value function vs. Q-function. Bellman equation.
- TD learning vs. Monte Carlo. Q-learning (off-policy) vs. SARSA (on-policy). Policy gradient and REINFORCE. Actor-critic. PPO at a high level.
- Exploration vs. exploitation. Sparse rewards. Offline RL (important where you **can't explore on a real factory floor**).
- Sutton framing: *The Alberta Plan*, continual learning, the "Bitter Lesson" essay (general methods plus compute beat hand-built knowledge).
- **Link to OmniVisor:** RL for process optimization, e.g. scheduling, line balancing, or recommending corrective actions. Offline RL on logged RTLS trajectories is the realistic setting.

### 6.3 Transformer from scratch
- Scaled dot-product attention: `softmax(QKᵀ/√d_k)V`. Multi-head attention. Positional encoding (sinusoidal vs. learned; for irregularly sampled time series, time-embedding approaches such as Time2Vec).
- Block: LayerNorm → MHA → residual → LayerNorm → FFN → residual (pre-norm).
- Causal masking for streaming inference. **KV-cache** for low-latency streaming.
- Be ready to compare against your RNNs: *"RNNs gave me constant memory per step and tiny latency on an RPi, which is why I chose them. Transformers win on long-range context. For edge streaming on RTLS I'd compare a small causal transformer against a TCN and a GRU under the same latency budget."* That's a senior answer: you pick the model by benchmark under constraints.

### 6.4 Agentic AI and MCP (ZeroKey uses both)
- Tool calling: the LLM emits a structured call, the runtime runs it, and the result goes back into context.
- **MCP:** an open protocol that exposes tools, resources and prompts from servers to LLM clients. OmniVisor almost certainly exposes spatial queries (zones, dwell times, anomalies) as tools.
- Where your ML fits: *"The models I'd build become tools the agent calls: `detect_sequence_violation(cell, shift)`, `ergonomic_risk_score(worker_tag, window)`. The agent handles the language and orchestration, and the spatial-temporal models produce answers you can check."* This bridges the two halves of the job description (predictive models and agentic exploration).

### 6.5 Edge optimization and quantization
- PTQ (post-training quantization, calibration set, int8) vs. QAT (quantization-aware training). Per-channel vs. per-tensor scales. Static vs. dynamic quantization.
- Pruning, knowledge distillation, operator fusion. ONNX export → ONNX Runtime / TensorRT (Jetson, since ZeroKey is in NVIDIA Inception) / TFLite.
- Measure the latency budget end to end (sensor → features → inference → action), not model FLOPs. You did exactly this on the RPi4 (14 ms, 31% CPU).

### 6.6 Spatial-temporal ML on RTLS: your go-to design
If asked *"How would you detect risky behaviour from our data?"*, walk through this:

1. **Data:** per-tag streams (tag ID, x, y, z, t). Tags sit on workers (badge or wrist), tools, bins and robots. Plus context: work-cell geometry, SOP step definitions, and events from MES or torque tools.
2. **Pre-processing:** per-tag Kalman smoothing and gap filling, resampling to a fixed rate, coordinate frames per work cell.
3. **Features:** velocity, acceleration, **jerk**; zone entry, exit and dwell; **pairwise distances** (worker–robot, tool–bolt position); wrist height relative to shoulder-level zones for ergonomic reach and overhead work; path curvature; step-sequence tokens.
4. **Models, in increasing cost:**
   - Rules plus thresholds (geofences, proximity). This is the baseline you must beat.
   - **Sequence and template matching** against SOP (DTW, which is literally your PhD baseline) → **learned sequence models** (GRU/TCN/small transformer) for step recognition and out-of-order detection.
   - **Unsupervised anomaly detection** for the "unknown unknowns": autoencoder or forecasting-error methods, isolation forest on window features.
   - **Graph or multi-agent models** when interactions matter (worker–robot–tool): each tag is a node, edges carry distance and relative motion.
5. **Labels are scarce.** Use weak labels from SOP definitions and MES events, synthetic trajectories (your rule-based synthetic-variation generator is the same idea), active learning with process engineers.
6. **Evaluation:** event-level precision and recall (false alarms kill adoption on factory floors; say that from MAS experience), detection latency, CPU on target hardware.
7. **Deployment:** int8 on the edge gateway; <500 ms end to end (OmniVisor's published number); the model exposed as a tool for the agent.
8. **Privacy and trust:** worker-level data is sensitive, so aggregate by default and involve worker representatives. It's the camera-free advantage, and it still needs care.

---

## 7. Stories to have ready (behavioural round)

From `story-bank.md`, adapted to this role:

| Question type | Story | Hook for ZeroKey |
|---|---|---|
| Most impactful / proud of | JAES 74× RNN vs DTW | Same shape as sequence-compliance detection |
| Commercial impact / shipping | **Promptly** (alignment algorithm, RIP integration, flipping mechanism consulting; now shipping in the US, Mexico, France, Sri Lanka). **Never mention the patent.** | Hardware plus software plus vision in one closed loop in a factory |
| Adoption and trust on the floor | MAS care-label QC: human-in-the-loop, explainable overlay, PLC reject | False alarms and trust are what decide whether OmniVisor gets adopted |
| Multi-stream time sync | MUSMET: audio + EEG + head/hand tracking × 4 musicians (SAE Barcelona, g.tec) | Closest thing you've done to multi-tag 3D tracking |
| Fixed deadlines, many partners | MUSMET live concerts (10 Quest 3s, lights, haptics; p < .05) | Client-facing delivery on fixed dates |
| Anomaly / risk detection | Forestpin forensic anomaly scoring | "Risky behaviour" detection framed for stakeholders |
| Knowledge transfer / mentoring | MAS group-wide CV training; 2 supervised BSc theses; CI/CD and code review | Amii's knowledge-transfer requirement |
| Social event (asked on Glassdoor, seriously) | Scouts leader, Rotaract, organizing bands and concerts | Keep it light and concrete |

---

## 8. Questions to ask them

**Pre-screen interviewer: Erika Bruneau**, HR Business Partner, People & Culture, Amii (https://www.amii.ca/people/erika-bruneau). BCom in HR, MacEwan. Previously TD, Edmonton International Airport, Bureau Veritas. Ask her about process, logistics, the residency's structure and culture. Keep technical questions for round 2.

Priority questions for Erika:
1. What are the next steps after today, and what's the timeline?
2. The posting lists Edmonton but ZeroKey is in Calgary. Where would the resident be based, and how is time split between Amii and ZeroKey?
3. How is the residency structured day to day: who do residents work with, and how often do they meet with the Amii Scientist and the ZeroKey team?
4. How often do residents move into a permanent role with their client? What usually decides that?
5. What does onboarding look like in the first month?
6. What do the strongest residents have in common?
7. What professional development and community access do residents get (events, Upper Bound, training)?
8. Is there anything in my background you'd like me to clarify?
9. (Only if she raises pay) What's the range for this residency? Does it include benefits or relocation support?

Pick 3–4 for the pre-screen (keep the technical ones for round 2):

**Pre-screen:**
1. Where does the resident sit, Edmonton or Calgary, and how much time is on-site at ZeroKey or at customer factories?
2. What does the rest of the process look like, and what's the timeline?
3. What has made past ZeroKey or manufacturing residents successful, and how often do residents convert to a role at the client?
4. How is the team split: who is the Amii Scientist, and who on the ZeroKey side owns the project?

**Technical round:**
5. Which comes first: continuous detection (predefined risk behaviours) or the on-demand path where users ask questions?
6. What's the edge target: gateway hardware, a Jetson-class device, or on-premises servers? What's the latency budget?
7. What labels exist today? SOP definitions, MES and torque events, incident logs?
8. How does the RL in OmniVisor work today, and where would the resident's models fit next to it?
9. What does "production-ready" mean for ZeroKey at the end of 12 months?

---

## 9. Logistics checklist

- [ ] Confirm the recruiter has **+1 613 200 2030** (the submitted documents show the retired 817 number)
- [ ] Look up **Xu (ML Scientist)** and **Amor Provins (Product Owner, Advanced Technology)** on LinkedIn
- [ ] Watch or skim the **Augmented Ops podcast, Ep. 135 with Matt Lowe** (https://www.augmentedpodcast.co/135), the best source of ZeroKey's own vocabulary
- [ ] Have the submitted CV and cover letter open (`career-ops/archive/output/1085-amii-zerokey-ml-resident*.md`) so you know exactly what they read
- [ ] Decide your **minimum pay** and whether you need a relocation allowance
- [ ] Decide your honest **Kalman** answer (§0 issue 2)
- [ ] One-line status on SciNet / eBay, ready for the "other processes" question
- [ ] Thank-you email within 24 h. Mention one specific thing from the call and include the correct phone number.

---

## Sources

- Job posting (Employment Hero snapshot, 2026-08-25): `career-ops/.playwright-mcp/page-2026-08-25T18-29-00-772Z.yml`
- ZeroKey Quantum RTLS: https://zerokey.com/quantum-rtls/
- ZeroKey OmniVisor AI: https://zerokey.com/omnivisor-ai/
- ZeroKey company page: https://zerokey.com/our-company/
- ZeroKey Series A: https://zerokey.com/zerokey-closes-series-a-funding-round/
- OmniVisor launch (Business Wire, Oct 2025): https://www.businesswire.com/news/home/20251024925055/en/ZeroKey-Launches-OmniVisor-AI-A-New-Era-of-Intelligent-Factory-Operations
- Metrology News on OmniVisor (RL + LLM, MCP): https://metrology.news/zerokey-marries-3d-location-accuracy-with-ai-to-redefine-factory-measurement-intelligence/
- TechSoda profile (May 2026; business model, markets, 3.0 hardware): https://techsoda.substack.com/p/zerokey-bridging-the-physical-blind
- Tulip blog (use cases): https://tulip.co/blog/unlocking-spatial-intelligence-with-quantum-rtls/
- Augmented Ops podcast Ep. 135: https://www.augmentedpodcast.co/135
- Amii ML Resident interviews (Glassdoor): https://www.glassdoor.com/Interview/Amii-Canada-Machine-Learning-Resident-Interview-Questions-EI_IE4507580.0,11_KO12,37.htm
- Amii residencies: https://www.amii.ca/your-business/internships-residencies/
- Amii AI Literacy Initiative: https://www.amii.ca/updates-insights/amii-leads-national-ai-literacy-initiative
- Alberta $50M to Amii (Jul 2026): https://www.canhealth.com/2026/07/15/alberta-pumps-50-million-into-amii-its-ai-centre/
- Upper Bound 2026: https://www.globenewswire.com/news-release/2026/05/19/3297239/0/en/amii-fuels-canada-s-ai-momentum-as-upper-bound-opens-with-53-growth-and-11-000-global-attendees.html
- Cam Linke on Canada's AI strategy (BetaKit): https://betakit.com/amii-ceo-cam-linke-says-canadas-ai-strategy-requires-customers/
- Amii background, Sutton, and Fellows: `ai-job-search/company_research/amii.json`
