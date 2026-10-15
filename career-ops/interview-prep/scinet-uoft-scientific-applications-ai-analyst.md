# Interview Prep: SciNet (U of T), Scientific Applications & AI Analyst — Round 2 (re-posted role)

**Req ID:** 50037 (re-post) · **Earlier req:** 47594 (posted 2026-04-23, the one you first interviewed for)
**Position number:** 00059302 on both postings → same funded seat, not a new role
**Dept:** SciNet, VP Research & Innovation · St. George campus · reports to the CTO (Daniel Gruner)
**Terms:** Full-time, 2-year grant term with possible renewal · USW Pay Band 18 · **$116,547 → $149,043** (annual steps)
**Your application:** CV `Nishal_Silva_AI_Analyst.pdf` (updated 2026-10-06), cover letter dated 2026-09-24, source = referral from a U of T employee
**Prepared:** 2026-10-11
**Not yet in either tracker** (career-ops `applications.md` / ai-job-search CSV). Only noted in the knowledge graph as "two interviews done, decision pending."

---

## 0. Read this first: what the situation tells you

**Facts**
- You had two interviews for req 47594. They told you (secretary, then Gruner by email) that they found no suitable applicant and would re-post.
- The re-post (50037, Aug 31) carries the **same position number**, and the aggregator text matches the April version (same summary, same "data analysis and ML libraries" and "computing hardware and networking" requirements). Check the JD text you saved in April against the one below. If anything changed, that's the clearest clue to what they were missing.
- Gruner emailed you himself. A CTO doesn't usually write to rejected candidates he never wants to see again. And they've now invited you back after reading a pool of new applicants.

**What it probably means (inference, not fact)**
In a failed university search, the committee looked at its finalists and decided none met the bar *on some specific dimension*. Re-inviting you means one of two things:
1. You were close, and they want to see whether the gap has closed, or how you'd close it.
2. The new pool wasn't better, so they're relaxing the bar toward what you already offer.

Either way, **this interview isn't a rerun of round one.** They already know your CV and your stories. What they don't know is the answer to *"is the thing that worried us last time still a problem?"*

**The likely worry, given this JD against your profile** (rank these yourself in §1.3 using what you actually got asked in rounds 1–2):

| Likely concern | Why | Your exposure |
|---|---|---|
| **Classic HPC depth**: MPI/OpenMP, Fortran, Slurm, compilers, parallel I/O | Essential quals: "Fortran, C, C++ under Linux", "serial, vector and parallel systems", "compilers, code optimization, file I/O". Gruner built Beowulf clusters for 20+ years, and the whole analyst team comes from that world. | **High.** C/C++/Python are strong. MPI, Fortran and Slurm aren't documented anywhere in your record. |
| **Cluster-scale GPU / distributed training** | The new system is meant for models with "hundreds of billions of parameters" (Minister Solomon). Users will need multi-node DDP/FSDP, NCCL, scheduling. | **Medium-high.** Your largest documented job is dual-GPU LoRA (RTX 4090 + 3090). Your edge work is the opposite end of the scale. |
| **Service orientation vs researcher identity** | The role is support, training and enabling other people's research. Your profile reads "researcher who ships his own systems." | **Medium.** You have real evidence (MAS training seminars, supervision, user studies), but you need to lead with it. |
| **8 years of "advanced scientific computing / large-scale data-driven computation"** | A literal reading favours people from physics/climate HPC backgrounds. | **Low-medium.** MAS IoT (millions of events/day) + PhD + postdoc adds up if you frame it as data-driven computation. |

**Strategy in one line:** Open by acknowledging the history, show concretely what you've done since round one on the gap, then show you think like a *service* analyst. Your question isn't "what can I build?" It's "how do I get 300 research groups productive on a new GPU machine?"

---

## 1. Similar cases and what actually worked

### 1.1 What the research found (said plainly)
No published case matches yours exactly (interviewed twice → told "no suitable applicant" → re-applied → re-interviewed → outcome reported). What exists are career-advice columns, HR process documents and forum anecdotes. The patterns are consistent, though.

**Why employers re-post and then re-consider a previous candidate**
- Ask a Manager (Alison Green) gives two reasons an employer re-considers someone it turned down for the same job: what they're looking for has changed, so you may fit now, or they've learned their ideal candidate doesn't exist and have become more flexible. Both fit "no suitable applicant" + re-post + re-invite.
- University failed-search procedure (UW–Madison HR toolkit): after a failed search, the hiring manager and committee review the start date, title, minimum salary, qualifications and position summary before re-posting. Here the position number and text look unchanged, which points to reason 2 (flexibility) or a fresh look at the same people, not a redesigned role.
- Other common reasons: the top choice declined and there was no strong runner-up, or funding was paused and restarted (Lady Unemployed; Ask a Manager). For a **grant-funded term position on a federal AI-compute grant** with fixed fiscal-year money ($40M in 2025-26, then $2.5M over two years for talent and operations), a hiring delay costs them real money. That works in your favour.

**Re-interview cases with an outcome**
- **Apple (Blind):** a candidate who missed out on a role was contacted directly by the same hiring manager when it re-opened. The manager said the earlier interview results were "still good," so the candidate wouldn't have to redo the full loop, but the manager still had to review the new applicants. *Lesson: earlier performance carries over. The second look is about what's changed.*
- **Ask a Manager, 2015:** a reader who had spoken with the company twice the previous summer saw the job re-posted. The advice was to tell the hiring manager directly about the earlier conversations, not to act like a new applicant. The column also lists why a company might want another conversation with a known candidate: new decision-makers need to meet you, they have open questions about your candidacy, the role changed, or they're comparing you with a late candidate.
- **Ask a Manager, 2010:** a reader was turned down, then contacted again by the same hiring manager about a second opening. A commenter from government explained that agencies sometimes must re-publish when too few eligible candidates came through the first screening. *That's close to U of T's USW posting rules, which can force a re-post for procedural reasons and not only because of you.*
- **Forum and career-site reports of people who converted on the second try** keep describing the same four moves:
  1. **Show new evidence, don't resend the same story.** "A weak re-application is uploading the same resume again and hoping for a different result." The people who converted added a skill, project or result since the last attempt.
  2. **Fix the specific thing that went wrong last time,** and sometimes say so: "last time I didn't answer X well; here's how I'd answer it now."
  3. **A light, direct touch with a previous interviewer** (one candidate messaged a former interviewer on LinkedIn to look out for the application). You already have a referral, and Gruner wrote to you, so the relationship exists.
  4. **Treat the earlier interviews as context the panel shares,** not something to hide.

**Where advice disagrees:** some forum posters read any re-post as "you were eliminated." In your case that reading is wrong: they re-invited you. The only reliable signal is what the employer actually does, and their action here is positive.

### 1.2 Your playbook, drawn from the above
1. **Name the history in the first two minutes** (script in §5.1). Calm, warm, no defensiveness.
2. **Bring one concrete "since we last spoke" item that targets the gap** (§4). A small, real artefact beats a broad claim: a working multi-GPU Slurm + torchrun job, an MPI exercise, a short tutorial you wrote for the new AI system.
3. **Don't repeat round-one stories in the same form.** They've heard them. Re-cut them for SciNet (enabling others, scale, I/O, training) and add one or two they haven't heard.
4. **Show you understand their problem right now:** a new sovereign AI system arriving, a user base that's mostly not AI-native, and a small analyst team that has to scale itself through training and documentation.
5. **Make it easy to say yes to someone they already know.** Lower the risk: "I can start immediately, I'm PR, I know the term is two years, and I've used the time since round one to close [gap]."

### 1.3 Debrief worksheet: fill this in before anything else
Write it from memory, honestly. It's the most valuable 30 minutes of this prep.

| | Round 1 | Round 2 |
|---|---|---|
| Who was on the panel (names, roles) | | |
| Questions you answered well | | |
| Questions where you hesitated, guessed or said "I haven't done that" | | |
| Technical topics they kept coming back to | | |
| Anything they said about the role you didn't know before | | |
| Your gut feel of the main doubt | | |

Then rank the concerns table in §0 using this. **Whatever goes in row 3 is your study list for §4.**

---

## 2. The role, decoded

### 2.1 The JD (req 50037)
**Purpose:** SciNet is installing a new AI capability, many high-performance GPUs funded through the **ISED Sovereign AI Compute** initiative. The analyst supports that platform and helps users with AI applications research and AI-assisted research in general. The work is senior IT services and **training** in GPU programming, data-science applications and scientific-computing workflows.

**Day-to-day:**
- Help users design, train and validate ML/DL models
- Large-dataset analysis: cleaning, transformation, feature engineering
- Deploy AI into production; integrate with existing software and infrastructure
- Monitor AI system performance; tune for efficiency, accuracy and scalability
- Help researchers adopt AI strategies for AI-assisted research

**Classification duties (USW boilerplate, but they'll ask about them):** analyse, recommend and design complex software architecture; write complex code; evaluate code for validity, compatibility and standards; deliver formal training; build relationships with stakeholders and partners; act as the expert resource for developers.

**Essential:** a bachelor's in CS/IT/engineering/quantitative science · **8+ years** of advanced scientific computing or large-scale data-driven computation · scientific numerical codes, **compilers, code optimization, file I/O, data management** · ML/data-analysis libraries · **excellent knowledge of computing hardware and networking** · **Fortran, C, C++ on Linux/Unix + R or Python** · able to program **serial, vector and parallel** systems · explain technical concepts to non-IT audiences · work across disciplines.
**Assets:** visualization; presentation and training skills.
**Traits:** goal-oriented, self-learner, proactive, problem-solver, self-directed.

### 2.2 SciNet: what to know
- **What it is:** U of T's advanced research computing centre, part of the national platform run with the **Digital Research Alliance of Canada**. It serves researchers across Canada in every discipline. Funded by ISED, Ontario and U of T.
- **Trillium** (launched **Aug 7, 2025**, replacing **Niagara** and **Mist**): **241,056 CPU cores + 252 GPUs** in a 63-node GPU subcluster, i.e. 4 GPUs per node. I believe these are NVIDIA H100s; confirm on docs.scinet.utoronto.ca. It was a $52M upgrade. In Dec 2025 Gruner said publicly that the system "pushes well beyond the scale of our previous generation."
- **The new AI system (why this job exists):** a **$42.5M** grant announced **Nov 28, 2025** (Minister of AI Evan Solomon). It comes from the **$2B Sovereign AI Compute Strategy**, delivered through the Alliance's **National AI Compute – Rapid Deployment** initiative: $40M in 2025-26 plus $2.5M over the next two years for **talent and operations** (likely what pays for this seat). Delivery and installation were targeted for H1 2026. It's framed around **data sovereignty** ("keeping Canadian data in Canada") and broad access: small universities, research hospitals, northern and Indigenous communities, and industry. Its scale target is training models in the hundreds of billions of parameters. I couldn't find a public name, GPU model or go-live date. **Ask them** (§7). That's a good question, not an ignorant one.
- **Other systems:** **Balam** (41× A100, run for U of T's **Acceleration Consortium**), **Rouge** (AMD GPU cluster), the **Teach** cluster (for courses), **S4H** secure enclave (sensitive or health data), JupyterHub, HPSS storage. VAST Data storage was reported in Dec 2025 (HPCwire), which matters for I/O conversations.
- **Training program** (central to this role): free courses, the **SciNet Certificate Program**, seminars and colloquia, and graduate courses co-developed with U of T: **PHY1610H** (Scientific Computing for Physicists), **MSC1090H** (Intro to Computational Biostatistics with R), **EES1137H** (Quantitative Applications for Data Analysis). Browse education.scinet.utoronto.ca. See which ML/DL courses exist now and who teaches them. Those people are likely panelists or close colleagues.
- **People:** Daniel Gruner, PhD (CTO) · Joseph Chen, PhD (Associate CTO, Hardware & Ops) · Applications Analysts: Yuxin Chang, Alexey Fedoseev, Leslie Groer, Yohai Meiron, Bruno Mundim, Mike Nolta, Jaime Pinto, Erik Spence, Ramses van Zon, James Willis · sysadmins, network/security, business officer. Mostly physics PhDs. That's the culture: rigorous, numerical, teaching-minded.

### 2.3 Daniel Gruner: how he thinks
- PhD in chemical physics (U of T). 20+ years in parallel computing, scientific modelling, software architecture, and running large Beowulf clusters and shared-memory machines.
- 2010 interview (Software Carpentry, third-bit.com): SciNet staff are HPC specialists, not a research group. Analysts **port user code** and write scientific software. His main concern is that **scientists who depend on HPC lack basic software-engineering training**: workflow planning, data management, development tools, version control, documentation. He wants staff who can engage users "at a higher level of understanding." He measures success by **better system utilization**, better-parallelized code and more efficient data handling.
- **How to use this:** talk about **utilization and enablement**, not only model accuracy. The AI system is expensive. Idle or badly used GPUs are the failure mode he cares about. Every story should end with *other people* getting more out of the machine.

---

## 3. Fit map: requirement → your evidence → gap → what to say

| JD requirement | Evidence (knowledge graph) | Gap | Say this |
|---|---|---|---|
| 8 yrs scientific / data-driven computation | MAS 5.5 yrs (IoT analytics, millions of events/day; production CV), PhD 4 yrs + postdoc 1 yr (real-time DSP/ML, datasets, benchmarks) | Not "HPC centre" years | "About ten years of data-driven computation, from factory-floor IoT pipelines to real-time numerical signal processing, all under hard compute budgets." |
| Numerical codes, compilers, optimization | **Nebula**: C++17, FFTW3, CMake, per-feature latency benchmarks on ARM. 74× speedup over DTW. CPU profiling on RPi4 (31.4% CPU). | Compiler flags/vectorization not documented | Talk about profiling first, then optimizing: measure, find the hotspot, pick an algorithm before micro-tuning. Mention `-O3 -march=native`, auto-vectorization reports, FFTW plans, only if you've actually used them. |
| File I/O, data management | Zenodo datasets (9,800+ recordings, frozen protocols); melodiq (Airflow, S3 → Snowflake); MAS ETL | Parallel filesystems | Small-files problem, sharding, HDF5/WebDataset, node-local scratch (§6.3). |
| ML libraries | TF/Keras (E), PyTorch (P), sklearn, HF (W), LoRA fine-tune of MusicGen | PyTorch should be the headline here; it's what users bring | Lead with PyTorch + HF + LoRA (VarianceEngine), not Keras. |
| Hardware & networking | Embedded HW, I²C, PLC, HiFiBerry; **MIRaaS** = UDP edge-to-server offload + latency characterization (IEEE IS² 2026) | Datacenter fabric: InfiniBand, RDMA, NCCL topology | MIRaaS shows you think in network latency budgets. Then show you know the datacenter vocabulary (§6.2). |
| Fortran | none | **Gap** | Honest (§5.3 Q). Fortran reads easily to a C programmer. Do the exercise in §4. |
| C/C++ under Linux, Python | C++17 (E), C (P), Python (E), Linux, shell | — | Strong. |
| Serial / vector / parallel | Real-time multi-stream pipelines (4 musicians × audio + EEG + XR); dual-GPU training | MPI/OpenMP/SIMD undocumented | Do §4 Day 2–3, then speak from real experience. |
| Training / presentation (asset) | MAS **group-wide CV seminars + hands-on training**; 2 BSc theses supervised; talks/demos; teaching-tool research | — | **Lead with this.** It's the asset they listed. |
| Non-IT audiences | User studies with musicians (20 + 6 participants; 5 guitarists); factory operators; compliance stakeholders (Forestpin) | — | "Most of my users were never engineers: musicians, factory operators, auditors." |
| Cross-disciplinary | Audio/music, neurotech (g.tec BCI), XR, manufacturing, finance, healthcare (COVID vitals) | — | Breadth is the point: the SciNet user base is every discipline. |
| Visualization (asset) | d3/topojson globe (Continuity), dashboards (COVID, IoT), Obsidian graph | Scientific viz (ParaView etc.) | Mention briefly. Don't oversell. |

**Honesty guardrails (from the knowledge graph):** F1 = **0.76** (never ">90%"). MAS is **one entry**, 2015–2020. Promptly = alignment algorithm + RIP integration + mechanism consulting, **never the patent**. LLM work is applied/tool-level. Don't claim MPI, Fortran or Slurm experience unless you've actually done it by interview day. Then say exactly what you did and when ("in the last two weeks I…"). They'll respect that more than an inflated claim.

---

## 4. Close the gap before the interview (prioritized plan)

Ask HR for the interview date, format (in person / video), length, panel names, and whether there's a **technical exercise or presentation**. Then compress or extend this plan.

**Day 1: SciNet + Alliance user environment (highest value per hour)**
- Read the SciNet docs for Trillium (docs.scinet.utoronto.ca): login vs compute nodes, filesystems (home/scratch/project), GPU job submission, software modules. Read the Alliance docs on **Python on clusters** (virtualenv + pre-built wheels, `pip install --no-index`; why conda is discouraged), **Apptainer** (HPC containers instead of Docker; rootless), **Lmod modules** (`module load StdEnv python cuda`), JupyterHub.
- You should be able to say, as if you've done it: "log in, `module load`, build a venv on the login node, submit with `sbatch`, stage data to node-local disk, checkpoint because jobs have wall-time limits."

**Day 2: Slurm + multi-GPU PyTorch, hands-on on your own 2 GPUs**
- Write a DDP training script launched with `torchrun --nproc_per_node=2`. Measure throughput on 1 vs 2 GPUs. Your 4090 + 3090 mix is a nice talking point: the slower card bounds DDP's synchronous step.
- Write the Slurm script you *would* submit on Trillium (template in §6.1), even if you can't run it.
- Learn: `NCCL_DEBUG=INFO`, `nvidia-smi dmon`, `torch.profiler`, **Nsight Systems (`nsys`)**, AMP/bf16, gradient accumulation, activation checkpointing.

**Day 3: MPI + OpenMP basics (enough to talk honestly with physicists)**
- `mpi4py`: hello world, `send/recv`, `allreduce`, scatter/gather. Run with `mpirun -n 4`.
- C + OpenMP: parallelize a loop with `#pragma omp parallel for reduction(+:sum)`. Know **MPI = distributed memory across nodes, OpenMP = shared memory threads within a node, CUDA = GPU, hybrid MPI+OpenMP is the classic HPC pattern.** Know that DDP's gradient sync *is* an MPI-style allreduce (NCCL ring/tree). That's the bridge between your AI world and their HPC world.
- Amdahl (strong scaling) vs Gustafson (weak scaling). Have one worked example ready.

**Day 4: Fortran reading + vectorization**
- Read and modify a small Fortran 90 program (array syntax, `do` loops, column-major order, `intent`, modules). Compile with `gfortran -O3`. Call it from Python via `f2py` (shows the integration angle).
- SIMD/vectorization: what `-O3 -march=native -fopt-info-vec` does, and why contiguous memory and stride matter (C row-major vs Fortran column-major).

**Day 5: Build your "since we last spoke" artefact**
Pick **one** and polish it:
- **(Best)** A 2-page **"Getting started: multi-GPU PyTorch on the new SciNet AI system"** tutorial, or a 45-minute workshop outline (§6.4), written in SciNet's documentation style. It shows training ability, GPU knowledge and that you're already thinking like a team member. Bring it printed or have it ready to screen-share. Offer it; don't force it.
- A GitHub repo: DDP + Slurm template + a scaling plot (1 vs 2 GPUs) + an MPI allreduce example, each with a README.
- A short profiling write-up: take a deliberately slow PyTorch dataloader pipeline, fix it (workers, pinned memory, sharded data), and show GPU utilization before and after.

**Ongoing:** LLM-for-research stack: vLLM serving, quantization (GPTQ/AWQ, 4-bit QLoRA), RAG over a lab's papers, Hugging Face hub offline use (compute nodes often have **no internet**, so pre-download models). Researchers will ask about this constantly.

---

## 5. Question bank with answer frames

### 5.1 The opener: they will ask some version of "why re-apply / what's changed?"
Have this under 60 seconds and rehearse it aloud:

> "Thank you for having me back. I appreciated Dr. Gruner's note when the search was paused. It was gracious, and it's part of why I re-applied. I came out of the earlier interviews more convinced this is the job I want. The new AI system is exactly where my background is useful: I've spent ten years making ML run efficiently on constrained hardware, and I've trained non-specialists to use it. Since we last spoke, I've worked deliberately on the HPC side, [specific: e.g. multi-GPU PyTorch under Slurm, MPI and OpenMP fundamentals, getting comfortable reading Fortran], and I've drafted what an onboarding tutorial for the new system could look like. I'd love to walk you through it if it's useful."

If they ask directly what you think was missing last time:
> "I suspect it was depth in the traditional HPC toolchain: MPI, Fortran, the scheduler side. That's fair. My strength is the AI side and working with users. Here's what I've done about the gap, and here's how I'd keep closing it on the job: the analyst team has decades of MPI expertise, and I'd bring the PyTorch, LLM and data-pipeline side that a GPU-first machine needs."

### 5.2 "Tell me about yourself" (SciNet cut, ~90 s)
Present: PhD in real-time ML, ten years across industry and research, Toronto-based PR, available now. Past, framed for SciNet: (1) **MAS:** production CV and IoT across factories on three continents, *and* I ran the group-wide CV training seminars, so I've always been the person who makes a tool usable by others. (2) **PhD/postdoc:** squeezing ML onto constrained hardware, 14 ms on a Raspberry Pi 4, 74× faster than the baseline (JAES 2026), plus multi-stream data pipelines with partners like g.tec. (3) **This year:** LoRA fine-tuning a music foundation model across two GPUs, open-source C++ tooling. Future: "I want to spend the next few years making a national GPU resource productive for researchers who aren't AI specialists. That's the job."

### 5.3 Technical / scenario questions (likely, given the JD and panel)

**Q: A researcher's PyTorch job on 4 GPUs is only 1.3× faster than on 1. How do you diagnose it?**
Frame: *measure before you guess.* (1) GPU utilization (`nvidia-smi dmon`); if it's low, they're **input-bound**: dataloader `num_workers`, `pin_memory`, JPEG/audio decode on CPU, thousands of small files on the shared filesystem → stage to node-local disk or shard (WebDataset/tar, HDF5). (2) Per-GPU batch too small → communication dominates → bigger batch or gradient accumulation; check the LR scaling. (3) Using `DataParallel` instead of `DistributedDataParallel`. (4) Communication path: `NCCL_DEBUG=INFO`, is it on NVLink/InfiniBand or falling back to TCP? (5) Profile one step with `torch.profiler`/`nsys`: compute vs dataloader vs allreduce. (6) Amdahl: serial parts like logging, validation on rank 0, checkpoint writes. Close with: "Then I'd write it up as a doc page so the next ten users don't hit it."

**Q: GPU out of memory when fine-tuning a large model.**
In order: bf16 mixed precision → activation (gradient) checkpointing → smaller micro-batch + gradient accumulation → parameter-efficient fine-tuning (LoRA; QLoRA 4-bit, which you've used on MusicGen-medium) → shard optimizer state and parameters (FSDP / DeepSpeed ZeRO-3) across GPUs → CPU offload as a last resort.

**Q: Back-of-envelope: what does full fine-tuning of a 70B model need?**
Mixed-precision Adam ≈ 16 bytes/param (bf16 weights 2 + bf16 grads 2 + fp32 master 4 + Adam m,v 8) → **≈1.1 TB** before activations → at least ~14 × 80 GB GPUs just for states, so FSDP/ZeRO-3 across multiple nodes, often plus tensor parallelism within a node. Versus **QLoRA**: 4-bit base ≈ 35–40 GB, so it can fit on one 80 GB GPU. Takeaway for users: "Most of you don't need full fine-tuning. Start with LoRA."

**Q: Explain MPI vs OpenMP vs CUDA to a biology grad student.**
Practice the analogy: OpenMP = more cooks in one kitchen sharing a fridge. MPI = several kitchens that phone each other with ingredients. CUDA = a kitchen of thousands of line cooks who can only do simple steps but all at once. Then: "Your PyTorch code already uses CUDA. Multi-GPU training uses an MPI-style 'everyone sums their gradients' step."

**Q: Strong vs weak scaling / Amdahl's law.**
Speedup = 1 / ((1−p) + p/N). With 95% parallel code, the maximum speedup is 20× no matter how many GPUs. Weak scaling (Gustafson) is why bigger problems use bigger machines efficiently. Tie it back: "I'd ask users for a scaling test before granting a large GPU allocation." Allocation efficiency is something the CTO cares about.

**Q: A user wants to run an LLM over sensitive interview transcripts / patient notes.**
Sovereignty is literally the funding rationale: run an open-weights model locally (vLLM / HF on the cluster). Data never leaves Canadian infrastructure. For regulated data, point them to **S4H** (the secure enclave) and their REB/data-agreement constraints. Don't send it to a commercial API.

**Q: How would you serve models for many users on a shared cluster?**
vLLM (continuous batching, PagedAttention KV cache), quantization to fit more per GPU, MIG partitioning for small models, scheduler integration (interactive partition vs batch), monitoring utilization, and a shared model cache so 50 users don't each download Llama.

**Q: Many small files are killing the filesystem.**
Metadata load on a parallel FS (GPFS/VAST): consolidate into tar shards / HDF5 / Zarr, read sequentially, stage to node-local scratch, avoid `ls` in tight loops, keep checkpoints few and large. Your Zenodo datasets (thousands of recordings) give you a real anchor.

**Q: Review this code (likely a slow Python loop or a C/Fortran snippet).**
Think out loud: correctness first, then complexity, then vectorize (NumPy broadcasting), then memory layout and access pattern, then parallelize. Mention testing (pytest) and version control. Gruner's 2010 concern was exactly this missing software discipline in scientists' code.

**Q: Have you used Fortran?**
> "Not professionally, and I won't pretend otherwise. I'm a strong C and C++ programmer, and since our last conversation I've been working through Fortran 90: array syntax, column-major layout, modules, calling it from Python with f2py. I can read and modify user codes now. Writing large new Fortran isn't where I'd add the most value to this role, and SciNet has deep expertise there already. I'd add the most on the GPU, PyTorch and LLM side, where the new system's users will be."
(Change the middle sentence to match whatever you actually did.)

**Q: Have you worked with MPI / Slurm / an HPC cluster?**
Same structure: what's true from the past (multi-device real-time pipelines, dual-GPU training, AWS ECS/EC2 batch jobs, Airflow scheduling), what you've done since (concrete), and how you'd keep ramping up (shadowing tickets, the SciNet certificate courses themselves).

**Q: How do you keep up with the field?**
Papers you read, Hugging Face releases, your own projects (VarianceEngine LoRA, speakfrench benchmark of 6 methods over 100k trials), daily AI-assisted coding with Claude Code. Note: assisting researchers with "AI-assisted research" is literally in the JD, and your workflow talk (14 slides on an AI-assisted research workflow) is direct evidence.

### 5.4 Behavioural (have one story per line)

| Question | Story (see §6) |
|---|---|
| Explaining something technical to non-experts | MAS training seminars / musician user studies |
| A user or stakeholder with unrealistic expectations | Care-label QC: iterated hardware 3 times with operators; compliance kept images on-site |
| Juggling many requests / priorities | MUSMET: multi-partner pipeline + live concert deadlines |
| Learning something unfamiliar fast | COVID vitals device / g.tec BCI integration / LoRA on MusicGen |
| Improving a system's efficiency | RNN vs DTW 74× / Nebula per-feature latency benchmarks |
| A mistake or failure | Pick a real one. Suggestion: an early design that didn't scale (e.g. DTW grew with pattern-set size) and how benchmarking caught it |
| Teaching / mentoring | 2 BSc theses (Collizoli 2023, Battisti 2026); MAS mentoring + CI/CD and code review |
| Working with researchers outside your field | g.tec + SAE Barcelona sync pipeline; Forestpin auditors |

### 5.5 Fit and logistics
- **"Why SciNet, not industry?"** You'd spend your time on the hardest version of the problem you like (getting ML to run efficiently), across every scientific domain, while teaching it. National-infrastructure mission, sovereign compute. You're in Toronto and want to stay.
- **"It's a two-year term."** "Understood and fine. Grant-funded terms are normal in research. I'd aim to make the role essential enough that renewal is easy." Only say this if it's true for you.
- **"Salary?"** It's Band 18 with a published scale ($116,547–$149,043). "I'm comfortable within the band. Given my PhD and experience I'd ask that placement reflect that, but I'm not going to make salary an obstacle." (USW starting step is usually fixed by policy. Don't push hard in the interview; negotiate at offer.)
- **"Other processes?"** Have a one-line, truthful answer. Don't bluff an offer.
- **Start date:** immediately.

---

## 6. Technical crib sheet

### 6.1 Slurm + torchrun multi-node template (know every line)
```bash
#!/bin/bash
#SBATCH --job-name=ddp-train
#SBATCH --nodes=2
#SBATCH --gpus-per-node=4
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=24
#SBATCH --time=04:00:00
#SBATCH --output=%x-%j.out

module load StdEnv python cuda      # exact module names: check SciNet docs
source $HOME/venvs/torch/bin/activate

export MASTER_ADDR=$(scontrol show hostnames $SLURM_JOB_NODELIST | head -n 1)
export MASTER_PORT=29500
export NCCL_DEBUG=WARN

srun torchrun \
  --nnodes=$SLURM_NNODES --nproc_per_node=4 \
  --rdzv_backend=c10d --rdzv_endpoint=$MASTER_ADDR:$MASTER_PORT \
  train.py --data $SCRATCH/shards --ckpt $SCRATCH/ckpt
```
Talking points: one launcher task per node, torchrun spawns one process per GPU; rendezvous on the first node; data on scratch (or staged to node-local disk); checkpoint regularly because of wall-time limits; `sacct`/`seff` to check efficiency afterwards.

### 6.2 Vocabulary to have ready
- **Interconnect:** InfiniBand (HDR/NDR), RDMA, GPUDirect RDMA, NVLink/NVSwitch inside a node; NCCL ring vs tree allreduce; topology-aware placement.
- **Parallelism for big models:** data (DDP), sharded data (FSDP / ZeRO 1-2-3), tensor, pipeline, sequence/context parallel; 3D parallelism (Megatron-LM, DeepSpeed).
- **Throughput metrics:** tokens/s, samples/s, **MFU** (model FLOPs utilization), GPU-hours per experiment.
- **Precision:** fp32 / tf32 / bf16 / fp16 / fp8 (Hopper Transformer Engine); loss scaling for fp16.
- **Inference:** KV cache, continuous batching, PagedAttention (vLLM), speculative decoding, quantization (GPTQ, AWQ, int8/4).
- **HPC basics:** login vs compute nodes, partitions/queues, fair-share, wall time, job arrays, interactive `salloc`, modules/Lmod, Apptainer, parallel FS (GPFS / Lustre / VAST), burst buffer / node-local NVMe, HDF5/NetCDF/Zarr, MPI-IO.
- **Profiling:** `nvidia-smi`, `nvtop`, Nsight Systems / Nsight Compute, `torch.profiler`, `py-spy`, `perf`, gprof, Valgrind/cachegrind, roofline model.

### 6.3 Data-pipeline I/O checklist (for users)
Shard (WebDataset tar / HDF5 / Parquet / Zarr) → read sequentially → stage to node-local disk per job → enough dataloader workers, pinned memory, prefetch → decode on GPU where possible (DALI) → few large checkpoints, async writes → never `pip install` or download models from compute nodes (no internet).

### 6.4 Workshop outline: "Deep learning on SciNet's AI system, from one GPU to many" (45–60 min)
1. Why GPUs, and when you *don't* need one (5 min)
2. Log in, modules, venv/Apptainer, data placement (10)
3. Single-GPU job: AMP, a correct dataloader, checkpoint/restart (10)
4. Scaling out: DDP with torchrun under Slurm, scaling test, reading efficiency with `seff` (15)
5. Big models: LoRA/QLoRA vs FSDP decision tree; serving with vLLM (10)
6. Responsible use: share GPUs, sovereign/sensitive data, citing the Alliance (5)
Hands-on: a notebook on the Teach cluster or JupyterHub. Exit survey → iterate (your user-study background).

---

## 7. Questions to ask them (choose 4–5; the first two matter most)
1. **"Looking back at the first search, what would the ideal person in this seat have that you didn't see? I'd like to know where to focus in my first six months."** Asked in a growth framing, this surfaces their real concern while you're still in the room to answer it.
2. "Where is the new AI system now: hardware, timeline to general availability, and which user communities do you expect first?"
3. "How will user support be split between this role and the existing applications analysts, especially for traditional HPC users moving into AI?"
4. "What does success look like at 6 and 12 months: tickets, training sessions delivered, utilization targets, onboarded groups?"
5. "Will this role develop new courses or certificate modules for AI? Is there an existing curriculum to extend?"
6. "How do you see LLM services fitting in: interactive inference endpoints for researchers, or batch-only?"
7. "Is there a path to renewal or conversion beyond the two-year term, and what usually decides it?"
8. "How does SciNet coordinate with the Alliance and other national sites on AI software stacks and documentation?"

---

## 8. Day-of checklist
- [ ] Fill in the §1.3 debrief before anything else
- [ ] Email HR: format, duration, panel names, any exercise or presentation, and accommodations if needed
- [ ] Re-read **the CV and cover letter you submitted** (CV 2026-10-06, cover letter 2026-09-24). Know every line, and check that the phone number reads **+1 613 200 2030**
- [ ] Compare the April and August JD texts if you saved the April one
- [ ] Rehearse aloud: opener (§5.1), "tell me about yourself" (§5.2), Fortran/MPI honesty answer, the 4-GPU diagnosis
- [ ] Artefact ready (§4 Day 5): printed copies (3–4) or a link
- [ ] Thank the referrer (a U of T employee) and tell them you've been re-invited. Ask, if appropriate, whether they know anything about format or panel
- [ ] Arrive early (St. George; check the building or room). Bring a notebook. Copies of your CV
- [ ] **Thank-you email within 24 h** to Gruner (and the panel if you have addresses). 4–5 sentences: thanks for having you back, one specific thing from the conversation, one-line reinforcement of your fit ("making the new system productive for non-AI researchers"), offer to send the tutorial or workshop outline if you didn't hand it over.

### Thank-you email draft
> Subject: Thank you, Scientific Applications & AI Analyst (50037)
>
> Dear Dr. Gruner,
>
> Thank you for meeting with me again today, and to [names] for their time. I especially enjoyed our discussion of [specific topic, e.g. how users will move from Trillium to the new AI system]. It reinforced how much I'd like to help researchers across disciplines get the most out of that machine. As mentioned, I've attached the short onboarding tutorial I drafted for multi-GPU PyTorch. I'd welcome any feedback on it.
>
> Best regards,
> Nishal Silva
> +1 613 200 2030

---

## 9. Sources
- Job posting, req 50037 (Inside Higher Ed mirror): https://careers.insidehighered.com/job/3546454/scientific-applications-and-ai-analyst/
- SciNet staff and training: https://scinethpc.ca/about-scinet
- New AI system announcement (2025-11-28): https://scinethpc.ca/?p=5083
- U of T News, $42.5M AI compute: https://www.utoronto.ca/news/ai-compute-infrastructure-u-t-receives-425-million-federal-investment
- BetaKit, federal AI compute commitment: https://betakit.com/feds-commit-42-5-million-to-expand-ai-compute-infrastructure-at-university-of-toronto/
- Trillium: https://scinethpc.ca/trillium/
- Daniel Gruner interview (2010): https://third-bit.com/2010/07/08/interview-scinet/
- Earlier SciNet analyst postings (2017, 2019) for role lineage: https://scinethpc.ca/?p=4474 · https://www.scinethpc.ca/?p=3181
- Re-post / re-consideration patterns: https://askamanager.org/2009/09/reapplying-for-job-you-were-rejected.html · https://askamanager.org/2009/05/can-i-reapply-after-being-rejected.html · https://www.askamanager.org/2010/08/what-does-it-mean-that-job-i.html · https://www.askamanager.org/2015/05/i-was-asked-to-interview-again-after-getting-an-offer-sticking-it-at-out-at-a-bad-new-job-and-more.html
- Failed-search procedure (UW–Madison): https://kb.wisc.edu/extension/117401
- Re-interview anecdote (Apple, Blind): https://www.teamblind.com/post/apple-re-interview-3saxvv2e
- Re-application advice: https://www.jobscan.co/blog/reapplying-for-job/ · https://ladyunemployed.com/5-reasons-employers-repost-job/
