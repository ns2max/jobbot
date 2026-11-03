# SciNet Company Crash Course: The Organization, Its Work and Its People

**Companion to:** `scinet-uoft-scientific-applications-ai-analyst.md` (strategy, fit, questions) · `scinet-uoft-technical-concepts.md` (HPC/AI concepts) · `scinet-uoft-trillium-crash-course.md` (using Trillium)
**Prepared:** 2026-10-16 · **Reading time:** about 35–45 minutes (§0 and §13 alone take 5 minutes)
**What this adds:** the company knowledge, so you can talk about SciNet like an insider: where it came from, what it runs, who pays for it, who uses it, what's happening there *right now* (2026), who the people are, and what they value.

**Confidence markers.** Unmarked facts come from SciNet, U of T, Alliance, BetaKit, HPCwire/VAST or university news sources (listed at the end). *(verify)* = one secondary source, dated, or my inference. **Staff listings on scinethpc.ca can be stale.** Check the team page the day before.

---

## 0. SciNet in 90 seconds (memorize)

> SciNet is the **University of Toronto's supercomputing centre**, a unit under the **Vice-President, Research & Innovation**. It grew out of a **2005 consortium of U of T and its ten affiliated hospitals** and opened its first systems in **2008–09**. It's one of the **five national host sites** of the **Digital Research Alliance of Canada**, so it serves researchers **across the whole country**, not just U of T. Accounts are free to eligible Canadian researchers, and the big allocations come through the Alliance's annual competition (RAC). Funding comes from **ISED (federal), Ontario and U of T**. In Ontario it partners with **SHARCNET and CAC under Compute Ontario**.
>
> Its flagship is **Trillium**: built by Lenovo, launched **7 Aug 2025**, **241,056 CPU cores + 252 NVIDIA H100s**, about 34 PF peak, about 1.7 MW, **29–30 PB of all-flash VAST storage**. It replaced **Niagara** (2018) and **Mist** (2020). SciNet also co-manages **Killarney**, Vector Institute's national AI cluster at U of T, and runs **Balam** (Acceleration Consortium), **Rouge** (AMD), **Teach**, the **S4H** secure enclave, **HPSS** tape archive and **Open OnDemand**.
>
> **This job exists because** on **28 Nov 2025** the federal Minister of AI, Evan Solomon, announced **$42.5M** (Sovereign AI Compute Strategy, delivered by the Alliance's *National AI Compute – Rapid Deployment* initiative) for a **new AI system hosted and operated by SciNet**. It's mostly **NVIDIA GPUs**, co-located with Trillium, and reportedly **triples its GPU capacity**. The pitch is **sovereignty** ("keeping Canadian data in Canada") plus **broad access**. SciNet has about a dozen PhD-level analysts, mostly physicists, led by CTO **Daniel Gruner**. Their culture is **rigorous, teaching-first and focused on utilization**.

---

## 1. Identity, structure and money

### 1.1 What SciNet is (and isn't)
- **A service centre, not a research group.** Staff are HPC specialists who **run machines, port and optimize user codes, and teach**. Gruner's framing (2010, still accurate): analysts engage users "at a higher level of understanding" and success = **better system utilization**. A vendor case study quotes him describing SciNet as a **not-for-profit organization focused exclusively on the advancement of science**.
- **Org home:** a unit in U of T's **VPRI portfolio**. VPRI org charts from Feb and Mar 2026 list **Daniel Gruner, CTO, SciNet**. The VP Research & Innovation is **Leah Cowen** (pictured at the Nov 2025 AI announcement).
- **Users:** national. Any qualified researcher at a Canadian university can get an account. BetaKit's Trillium story names users "from the **University of Victoria** to **Memorial University**." Every discipline: physics, astro, climate, chemistry, bio/health, engineering, social science and, increasingly, AI.
- **Not to be confused with** USDA's **SCINet** (US agriculture) or **SCinet** (the SC conference network). Search results mix them up constantly.

### 1.2 How the money flows (be able to explain this)
| Source | What it funds | Example |
|---|---|---|
| **Federal (ISED) via the Alliance** | National compute infrastructure + operations | ~$52M Trillium (Oct 2024 announcement, with Ontario + Compute Ontario matching); $42.5M AI system (Nov 2025) |
| **Ontario + Compute Ontario** | Provincial match, regional coordination | Part of Trillium's $52M; a $95.4M joint U of T + Waterloo package (Waterloo got ~$43M for **Nibi**, Graham's replacement) |
| **U of T** | Host institution, facility, staff home | Data centre, VPRI unit |
| **Partners / projects** | Dedicated systems | Acceleration Consortium (**Balam**), AMD donation (**Rouge**), ATLAS Tier-2 (CERN/WLCG) |

**Allocations:** compute is "free at point of use." A default allocation (`def-<PI>`) goes to any PI. Large shares go through the Alliance's annual **Resource Allocation Competition (RAC)** (`rrg-…`), with priority set by fair-share. Usage reports live in **CCDB**.

### 1.3 The Ontario layer
**Compute Ontario** coordinates Ontario's ARC consortia: **SciNet** (U of T), **SHARCNET** (Waterloo/Western-led, now running **Nibi**), **CAC** (Centre for Advanced Computing, Queen's). Joint output you should know about: the **Compute Ontario Colloquium** (§7). Its CEO was **Ranil Sonnadara** (appointed 2021) *(verify current)*.

---

## 2. Timeline (2005 → 2026)

| Year | Event |
|---|---|
| **2005** | U of T + its 10 affiliated hospitals form the consortium that becomes SciNet |
| **2008** | Data-centre renovation starts (Aug). IBM deal billed as "Canada's most powerful supercomputer." **TCS** (Tightly Coupled System, IBM Power) installed Nov, friendly users Dec |
| **2009** | **GPC** (General Purpose Cluster, IBM iDataPlex, ~30k cores) arrives. Both open to all Canadian researchers in Aug 2009 |
| **2012** | GPC runs its **10-millionth job** |
| **2013** | **SciNet Certificate Program** launched |
| **2017** | TCS switched off (29 Sep). GPC reduced. Lenovo selected for Niagara |
| **2018** | **Niagara** (Lenovo, ~60k cores, homogeneous, built for large parallel jobs) debuts at **#53 on TOP500** (June) |
| **2020** | Niagara expanded to **80,640 cores**. **Mist** GPU cluster opens 12 Feb (54 nodes × 4 **V100**, IBM Power9; also refreshed the SOSCIP GPU platform) |
| **2021** | **Rouge** (AMD donation: 20 nodes, 160 **MI50**). **Alliance** replaces Compute Canada as national body |
| **2023** | **Balam** (41 × A100) for the Acceleration Consortium. Compute Ontario Colloquium starts (Jan) |
| **Oct 2024** | **$52M** to replace Niagara, about 3× its raw compute. The name **Trillium** first appears in coverage |
| **2025** | Niagara cut to 50% and Mist to 35% to free power for Trillium acceptance. **Killarney** (Vector + SciNet, PAICE) available **9 Jun**. **Trillium launched 7 Aug**. **$42.5M AI system** announced **28 Nov**. **VAST** storage selection publicized Dec |
| **2026** | Research results from Trillium (ocean, stellar mixing). 4-day datacentre shutdown (Jun). Cooling and filesystem incidents (Jul). **3-day Trillium shutdown in Sep "for integrating an expansion into the cooling system."** Switch incident 26 Sep. AI system due "H1 2026" (no public go-live found as of mid-Oct) |

**Talking point:** SciNet has been through **three full generations** (TCS/GPC → Niagara/Mist → Trillium) and each transition was a big **user migration** project. The AI system is the next one, and that's this role.

---

## 3. What they run today

### 3.1 Trillium (flagship, national)
- **Built by Lenovo Canada.** Direct liquid cooling: the docs refer to "Trillium **Neptune** nodes," Lenovo's warm-water cooling line *(verify)*.
- **CPU:** 1,224 nodes × 2 × 96-core **AMD EPYC 9655 "Zen 5"** = 192 cores/node, **whole-node scheduling**.
- **GPU:** **63 nodes × 4 NVIDIA H100 SXM 80 GB** (252 GPUs), 96 cores/node. Scheduled per GPU (¼ node) or whole node. Separate GPU login node.
- **Storage:** about **29–30 PB VAST all-NVMe** for home, scratch and project, as a single performance tier. Previously ~18 PB **GPFS + a separate flash burst buffer** for small-file I/O, which ran 7+ years.
- **Scale:** ~34 PF peak, ~1.7 MW. Located in an undisclosed GTA facility (BetaKit was asked not to reveal it, citing **~$200M of hardware**). Jobs 15 min–24 h.
- **The VAST story is a great conversation hook.** Gruner, Dec 2025: *"With VAST, we no longer have to juggle different storage tiers or bolt on burst buffers just to keep up with demanding I/O."* The point: one storage system has to serve **traditional HPC codes and AI workloads side by side**, and AI data loaders (many small random reads) were what made burst buffers necessary in the first place.

### 3.2 Killarney (co-managed with Vector; very relevant)
- Part of **PAICE** (Pan-Canadian AI Compute Environment: CIFAR + Amii/Mila/Vector + the Alliance). **Located at U of T, managed by the Vector Institute and SciNet**, available since **9 Jun 2025**.
- **Standard tier:** 168 Dell nodes × 4 **L40S** (672 GPUs). **Performance tier:** 10 Dell XE9680 × 8 **H100 SXM** (80 GPUs). InfiniBand HDR. 1.7 PB VAST.
- Access: Vector-affiliated PIs / CIFAR AI Chairs, and researchers in AI programs or applying AI methods.
- **Why it matters for you:** SciNet already has hands-on experience running a dedicated *AI* cluster for AI-native users. The new system is likely aimed at the broader, non-AI-native researcher base. Ask about the difference (§12).

### 3.3 Other systems
| System | What | Users |
|---|---|---|
| **Balam** | 41 × NVIDIA A100 (2023) | U of T **Acceleration Consortium** (self-driving labs, AI for materials/chemistry; $200M CFREF, the largest federal research grant to a Canadian university; director **Alán Aspuru-Guzik**) |
| **Rouge** | 20 nodes × 8 AMD **MI50** (ROCm), AMD donation 2021 | All U of T members |
| **Teach** | Teaching cluster (+ Teach OnDemand) | Courses and workshops |
| **S4H** | Secure enclave for sensitive data (health, proprietary). Stated compliance with **CMMC 2.0 Level 2** (contingent on audit) | U of T members. Ties to the hospital-network origins |
| **HPSS** | Tape-backed archive, ~**90 PB** | Cold data. Globus-accessible |
| **Open OnDemand** | `ondemand.scinet.utoronto.ca`: JupyterLab, VS Code, RStudio in-browser | Interactive users |
| **ATLAS Tier-2** | CERN LHC grid site (WLCG), managed by **Leslie Groer** | Particle physics |

### 3.4 The new AI system (why this job exists)
- **Announced:** Fri **28 Nov 2025** by **Evan Solomon** (Minister of AI and Digital Innovation). **$42.5M**. Funded by the **Canadian Sovereign AI Compute Strategy**, delivered via the **Alliance's National AI Compute – Rapid Deployment** initiative (up to **$40M in FY2025-26**, a call issued to the **seven** institutions currently hosting national compute). U of T's award is the largest confirmed. The earlier guide notes $2.5M over two years for **talent and operations**, which likely funds this seat.
- **What:** "largely" new **NVIDIA GPUs** + some storage, **co-located with Trillium**, reportedly **tripling** Trillium's GPU capacity *(single source; verify)*. GPU model and system name **not public** as of mid-Oct 2026.
- **Timeline:** "delivered and installed in **H1 2026**" (SciNet). BetaKit said spring 2026. I found **no public go-live notice**. Note the **Sep 2026 cooling-system expansion**. The AI system needing more cooling is my **inference** *(verify)*, and it makes an excellent question.
- **Solomon's framing:** model training "at a very large scale" and a **secure multitenant platform for data-intensive research**. *"Countries that control their own compute will have control of their own future."*
- **The Alliance's sovereign AI vision** (ai.alliancecan.ca): **equitable national access** to compute, data, tools *and training*. Publicly owned infrastructure that keeps "Canadian data and research **off foreign clouds**." Pillars include **Canada's first "AI Factory"** integrating AI compute with ARC systems, and a national data platform. Separately, ISED's **$705M Sovereign Compute Infrastructure Program (SCIP)** is the bigger, longer-term track.

**What it means for the role (say this):** the hardware is the easy part. The value comes from **getting hundreds of research groups, most of them not AI-native, to use expensive GPUs well**: onboarding, docs, workshops, fixing data loaders, sizing jobs properly, and moving people off one-GPU notebooks onto properly scheduled multi-GPU jobs. **Utilization is the metric.**

---

## 4. The national landscape (where SciNet sits)

```
            ISED — Canadian Sovereign AI Compute Strategy ($2B, Dec 2024)
       ┌────────────┬───────────────────────────┬─────────────────────────┐
  AI Compute     Public infrastructure ($1B)    AI Compute Access Fund
  Challenge      ├─ SCIP ($705M, long-term)     ($300M, SMEs)
  ($700M,        └─ near-term upgrades (~$200M)
  e.g. Cohere)        └─ Alliance "Rapid Deployment" ($40M FY25-26) ──► U of T/SciNet $42.5M
                                       │
               Digital Research Alliance of Canada (CEO: Dr. Michael Schull, since 1 Dec 2025)
     ┌────────────┬─────────────┬──────────────┬──────────────┬──────────────┐
   Fir (SFU)   Nibi (Waterloo/  Rorqual      Narval         Arbutus        TRILLIUM
   (Cedar      SHARCNET)        (Calcul      (Calcul        (UVic cloud)   (U of T/SciNet)
   successor)  (Graham succ.)   Québec, 2025) Québec)
                                       │
     PAICE (CIFAR + Vector/Mila/Amii): Killarney (Vector + SciNet, U of T)
                                       · TamIA (Mila, Laval) · Amii cluster (Alberta)
     Ontario layer: Compute Ontario → SciNet · SHARCNET · CAC
```

- **2024–25 refresh:** four of the national systems were replaced: Cedar→**Fir**, Graham→**Nibi**, Béluga→**Rorqual** (137k cores, 324 GPUs), Niagara/Mist→**Trillium**. Trillium is the **largest CPU system** and is designed for **big, tightly coupled parallel jobs** (Niagara's tradition: "do the really big jobs," in Gruner's words to BetaKit).
- **Alliance leadership:** **Dr. Michael Schull** became CEO on 1 Dec 2025 (from **ICES**, Ontario's health-data institute, which is interesting given the health and sensitive-data angle). Predecessors: George Ross (interim) and Nizar Ladak.
- **Why Trillium is different** is literally the title of **Ramses van Zon's** Compute Ontario colloquium (6 May 2026). Its themes, from the Trillium crash course: whole-node scheduling, home read-only on compute nodes, all-flash VAST, H100 GPU subcluster. Mentioning that you watched it would land well *(only if you actually watch it)*.

---

## 5. The science: what users do on SciNet

Have **two or three of these ready**. Citing a user's science shows you care about the *research*, not just the hardware.

1. **Global ocean modelling (Peltier group, U of T Physics).** A next-generation **MITgcm** global ocean simulation building to **1/96° (~1 km)** horizontal resolution, billed as the **highest-resolution realistic global ocean model** to date. Collaborators: **Dimitris Menemenlis** (NASA JPL) and **Kayhan Momeni** (who gave the Jan 14, 2026 colloquium). They plan to **openly release all configurations, tools and outputs**. One group reportedly needed **~50,000 cores** at once. *Hook:* "That's the 'really big jobs' philosophy, and the open-release plan is the same open-science instinct behind my Zenodo datasets."
2. **New stellar mixing process (UVic, Nature Astronomy, early 2026).** Led by **Simon Blouin**, group of **Falk Herwig** (UVic, ARC director). Using the **PPMstar** code, they showed **rotation amplifies internal-gravity-wave mixing in red giants by over 100×**, helping solve a ~50-year puzzle about carbon isotope ratios. Herwig: *"We were able to discover a new stellar mixing process **only because of** the immense computing power of the new Trillium machine… the computationally most intensive stellar convection and internal gravity wave simulations performed to date."* (They also used TACC.)
3. **Particle physics:** the **ATLAS Tier-2** site for CERN's LHC grid.
4. **AI for discovery:** **Acceleration Consortium** self-driving labs on **Balam**. AI + robotics for molecules and materials (they report a candidate cancer drug in about 30 days).
5. **Health / sensitive data:** the hospital-consortium roots, the **S4H** enclave and an Alliance CEO from ICES. *Hook for you:* your COVID vitals and BCI/EEG work means you've dealt with sensitive human-subject data.

**What this tells you about the user base:** mostly **simulation-heavy physical scientists** with deep MPI/Fortran/C++ codes, plus a fast-growing group of researchers who now want to **add ML** (surrogate models, emulators, LLM-assisted analysis). The AI analyst serves **both**: helping the simulation folks adopt AI, and helping AI folks use HPC well.

---

## 6. Operations reality in 2026 (shows you've been paying attention)

- **Power and cooling are the binding constraint.** Trillium uses ~1.7 MW. In 2025 Niagara was cut to 50% and Mist to 35% just to free power for Trillium's acceptance testing.
- **2026 events** (SciNet status pages): planned **4-day full datacentre shutdown (June)** · **cooling problems + filesystem issues (late July)** · planned **3-day Trillium compute shutdown (September) to integrate a cooling-system expansion** · a **switch problem on 26 Sep**, fixed the same morning, but some jobs died ("resubmit").
- **Why it matters:** analysts deal with the user side of every outage: communicating it, helping people resubmit, and making the case for **checkpointing**. *Line:* "Your September cooling expansion reads like making room for the AI system. Is that right?" Ask it as a question, not a claim.

---

## 7. Training and outreach (a core part of this role)

- **SciNet Certificates (since 2013):** **Scientific Computing**, **High Performance Computing** and **Data Science** (36+ credit-hours of data-science courses). Credits come from completing SciNet courses.
- **Course catalogue** (`education.scinet.utoronto.ca`, also branded *scinet.courses*): codes like **HPC101**, **DAT1xx**. Historic staples: OpenMP, MPI, CUDA, Advanced Parallel Scientific Computing, Hadoop, scalable R/Python, databases, visualization, ML.
- **Grad courses co-taught with U of T:** **PHY1610H Scientific Computing for Physicists** (Ramses van Zon: best practices, C++, optimization, ODE/PDE/Monte Carlo/MD, a bit of parallel), **MSC1090H** (computational biostatistics with R), **EES1137H** (quantitative data analysis).
- **AI/ML teaching that already exists:** **DAT112, neural network programming in Python** (Erik Spence; 6 weeks, online, Tue/Thu, switches to Keras from class 3). DAT111 intro to NNs (2018 summer school). Spence's colloquium "**A comparison of neural network frameworks**" (Jan 2023). *Implication:* the deep-learning curriculum looks Keras-era and single-GPU. **The gap the AI system creates: PyTorch-first, multi-GPU (DDP/FSDP), LLM fine-tuning/inference, containers, data pipelines.** That's exactly the workshop outline in the strategy guide §6.4.
- **2025–26 offerings seen:** "**Python on Trillium and Open OnDemand**" (van Zon, 27 Oct 2025) · **SCMP213 Open OnDemand on Trillium** (Apr 2026) · **intro to containers (Oct 2026)** · **scaling up your HPC work (Dec 2026)** · an R data-analysis grad course starting Jan 2027 · SciNet staff teaching a Python-parallel session at the **International HPC Summer School (IHPCSS) 2026** (Perth).
- **Compute Ontario Colloquium:** Wednesdays at 12:00 on Zoom (weekly/bi-weekly), since **Jan 2023**, run jointly by CAC, SciNet and SHARCNET. Recent: **Momeni, ocean modelling on Trillium (14 Jan 2026)** · **van Zon, "Why the Trillium Cluster is Different" (6 May 2026)** · Willis on **SWIFT** (Oct 2023).
- **Gruner** is described in SC conference bios as SciNet's "main supporter and believer" in its education efforts. **Training isn't a side duty here. It's the CTO's passion.**

---

## 8. The people

**Caveat:** compiled from scinethpc.ca staff listings, U of T org charts, conference bios and course pages. Titles may be dated. Don't call anyone by a title you haven't confirmed.

### 8.1 Leadership
| Person | Role | Background | How to connect |
|---|---|---|---|
| **Daniel Gruner, PhD** | **CTO** (confirmed on VPRI org charts, Feb/Mar 2026) | PhD chemical physics (U of T). 20+ years of parallel computing, scientific modelling, software architecture. Ran large **Beowulf** clusters and shared-memory machines. Helped build the facility that houses Trillium | Utilization, enablement, teaching, software-engineering habits for scientists (version control, data management, documentation). He emailed you personally. |
| **Joseph Chen, PhD** | **Associate CTO, Hardware & Operations** | Formerly SciNet sysadmin. Before that, parallel-cluster admin at U of T's **Institute for Aerospace Studies (UTIAS)** | Networking, hardware, power/cooling, the GPU install. Your MIRaaS network-latency work + hardware background |
| **Scientific Director** | *(unconfirmed)* | One directory lists **Hugh Couchman** (McMaster astrophysicist, SHARCNET founder) *(verify)*. W. Richard Peltier co-authored the 2019 Niagara paper and has long been SciNet's flagship user. Older sources call him founding scientific director *(verify)* | Don't name a scientific director unless confirmed |

### 8.2 Applications analysts (your future peers)
| Person | Background (as listed) | Likely angle in an interview |
|---|---|---|
| **Ramses van Zon, PhD** | PhD theoretical physics (Utrecht). Postdocs at Rockefeller (non-equilibrium stat-mech) and U of T Chemical Physics (glassy systems, **molecular dynamics**). Teaches **PHY1610**. Ran the Python-on-Trillium workshop and the "Why Trillium is different" colloquium | Software best practice, C++, Python environments on clusters, teaching. Probably the most likely technical panelist on user-facing questions |
| **Erik Spence, PhD** | Applications analyst. Teaches **DAT112 neural networks** and NN-framework comparisons | Your closest peer on AI teaching. Be generous about building *on* his courses, not replacing them |
| **Mike Nolta, PhD** | PhD physics (**Princeton**) | Cosmology/numerical background *(verify)*. Rigorous technical questions |
| **Bruno Mundim, PhD** | PhD physics (UBC). RIT and **Albert Einstein Institute**. Computational astrophysics (numerical relativity) | Large parallel codes, MPI, scaling |
| **Yohai Meiron, PhD** | PhD physics. **N-body** simulations, black holes. Extensive **GPU computing**. Helped run a GPU cluster during his postdoc at **Peking University** | GPU programming and GPU-cluster operations. Likely to probe CUDA depth |
| **James Willis** | Contributor to **SWIFT** (task-parallel gravity + SPH cosmology code, strong-scaling past 100k cores). Gave a SWIFT colloquium (Oct 2023) | Task-based parallelism, performance engineering |
| **Leslie Groer** | Manages the **ATLAS Tier-2** facility. Leads the Alliance's **Subatomic Physics National Team** (grid computing for HEP) | Grid/high-throughput workflows, national-team collaboration |
| **Yuxin Chang, PhD** | PhD **Electrical & Computer Engineering** (U of T) | Possibly the closest to your engineering background *(verify focus)* |
| **Alexey Fedoseev** | Applications analyst (no bio found) | — |
| **Jaime Pinto** | **Storage analyst** / scientific programmer. Aeronautical engineering + CS. Previously IT at **SickKids** and **Mount Sinai** research environments | Storage, filesystems, VAST, data management |

**The pattern:** about 8 of 10 are **physics PhDs** (stat-mech, astro, cosmology, relativity) who became HPC specialists. They value **numerical rigor, honest answers and teaching**. **What you add that they lack:** production ML/DL engineering (PyTorch, LoRA fine-tuning, data pipelines, MLOps), real-time/edge performance discipline, AI-assisted research workflows, and a lot of experience with non-technical users. **Pitch yourself as complementary, not as replacing anyone's expertise.**

### 8.3 Names from the funding and political side (recognize, don't name-drop)
- **Evan Solomon:** federal Minister of AI and Digital Innovation (announced the $42.5M)
- **Leah Cowen:** U of T VP Research & Innovation (SciNet's VP)
- **Timothy Chan:** U of T Associate VP & Vice-Provost (quoted on the Trillium funding: infrastructure "critical for our community and for the Canadian research community at large")
- **Michael Schull:** Alliance CEO (since Dec 2025) · **Gail Murphy:** Alliance vice-chair (at the Nov 2025 event) *(verify)*
- **Alán Aspuru-Guzik:** Acceleration Consortium director (Balam's users)

---

## 9. Culture and values: what they reward

1. **Utilization over hype.** Expensive hardware sitting idle or used badly is the failure. Talk about *GPU-hours well spent*, not about model accuracy.
2. **Teaching as the main lever.** A dozen analysts can't hand-hold thousands of users, so they scale through courses, certificates, docs and colloquia.
3. **Big, tightly coupled science.** Niagara and Trillium were designed for the largest parallel jobs in the country. They're proud of that ("the really big jobs").
4. **Software-engineering hygiene for scientists:** version control, reproducible environments, data management, documentation (Gruner's long-standing theme).
5. **Open science and national service:** free access, national allocation, results like the open ocean-model release.
6. **Rigor and honesty:** physicists spot hand-waving instantly. "I haven't done that, but here's how I'd find out" beats bluffing.
7. **Pragmatic, vendor-neutral engineering:** IBM → Lenovo, NVIDIA + AMD (Rouge), GPFS → VAST. They pick what serves the workload.

---

## 10. Connect your story to SciNet (talking points)

| SciNet reality | Your evidence | One-liner |
|---|---|---|
| New AI system, mostly non-AI-native users | MAS group-wide CV seminars + hands-on training. Supervised 2 BSc theses | "I've taught ML to engineers who'd never trained a model. That's most of your incoming GPU users." |
| Utilization is the metric | Per-feature latency + CPU profiling on ARM (14 ms at 31.4% CPU) | "I measure before I optimize, at any scale. Idle H100s are a profiling problem." |
| HPC + AI on one storage system (VAST story) | Zenodo datasets (9,800+ recordings), ETL (Airflow/S3/Snowflake) | "Small-file I/O is the classic AI-on-HPC pain point. I'd teach packing and staging from day one." |
| 24 h wall time, outages in 2026 | VarianceEngine: resumed multi-GPU LoRA from checkpoint | "Checkpoint/restart isn't optional here. I'd make it the first thing in every template." |
| Open science (ocean model release) | 4 public datasets, frozen protocols, open code | "I build things for other people to reuse. That's the same instinct." |
| Sensitive/health data (S4H, ICES-linked CEO) | COVID vitals, EEG/BCI human-subject data | "I've handled human-subject data under ethics constraints." |
| Physics-PhD culture | PhD + JAES/IEEE peer review, ablations, baselines | "I'd push every user toward baselines, frozen test sets and ablations." |
| Keras-era DL courses | PyTorch + HF + LoRA, Claude Code workflow talk | "I'd love to extend DAT112 into PyTorch multi-GPU and LLM fine-tuning, building on what Erik has." |

---

## 11. Smart, company-informed questions (pick 3–4)

1. "Where is the new AI system now? Installed, in acceptance, or still being procured? And was September's cooling expansion part of preparing for it?"
2. "How will access work: through the RAC like Trillium, a separate AI allocation, or something closer to Killarney's model? Who do you expect the first users to be?"
3. "SciNet already co-manages Killarney with Vector. What did you learn there about AI users that you'd do differently on the new system?"
4. "What does success look like for this role after a year? GPU utilization, number of groups onboarded, courses delivered?"
5. "Would you want the analyst to extend DAT112 toward PyTorch, multi-GPU training and LLM fine-tuning, or build a separate AI track in the certificate program?"
6. "Moving to VAST removed the burst buffer. Have you seen AI-style small-file I/O stress it on Trillium's GPU nodes yet?"
7. "Is the new system meant to support sensitive data, along the lines of S4H, given the sovereignty framing?"

---

## 12. Numbers cheat sheet

| Fact | Number |
|---|---|
| Consortium origin | 2005 (U of T + 10 hospitals) |
| First systems | TCS 2008, GPC 2009 |
| Niagara | 2018, #53 TOP500, ~60k → 80,640 cores |
| Mist | 2020, 54 × 4 V100, Power9 |
| Trillium launch | **7 Aug 2025** |
| Trillium cores / GPUs | **241,056 / 252 H100** (63 nodes × 4) |
| Trillium node | 192 cores (2 × 96 Zen 5); GPU node 96 cores |
| Trillium peak / power | ~34 PF / ~1.7 MW |
| Storage | ~29–30 PB VAST all-flash (was ~18 PB GPFS + burst buffer) |
| HPSS archive | ~90 PB |
| Trillium funding | ~$52M (Oct 2024) |
| AI system funding | **$42.5M (28 Nov 2025)**, H1 2026 target |
| Alliance Rapid Deployment | up to $40M FY2025-26 |
| Sovereign AI Compute Strategy | $2B (Dec 2024): $700M challenge / $1B public infra (incl. $705M SCIP) / $300M access fund |
| Killarney | 672 L40S + 80 H100, U of T, Vector + SciNet, Jun 2025 |
| Balam / Rouge | 41 A100 / 160 MI50 |
| Certificates | 3 kinds, since 2013 |

---

## 13. Self-quiz (cover the right column)

| Question | Answer |
|---|---|
| Who does SciNet report to? | U of T VP Research & Innovation (Leah Cowen) |
| Who builds Trillium? | Lenovo |
| What did Trillium replace? | Niagara (CPU) and Mist (GPU) |
| Name the five other national systems | Fir, Nibi, Rorqual, Narval, Arbutus |
| Which AI cluster does SciNet co-manage? | Killarney, with Vector (PAICE) |
| What changed in storage, and why? | GPFS + burst buffer → single-tier VAST, so one system can serve HPC and AI I/O |
| Who announced the AI money, and how much? | Evan Solomon, $42.5M, 28 Nov 2025 |
| Which program delivers it? | Alliance National AI Compute – Rapid Deployment (Sovereign AI Compute Strategy) |
| Two Trillium science highlights? | Peltier 1/96° MITgcm ocean model; UVic red-giant stellar mixing (Nature Astronomy) |
| Who teaches the neural network course? | Erik Spence (DAT112) |
| Who teaches PHY1610? | Ramses van Zon |
| What's the Alliance CEO's background? | Michael Schull, formerly ICES (health data) |
| What is S4H? | Secure enclave for sensitive data |
| What happened in Sep 2026? | 3-day shutdown to integrate a cooling expansion, plus a switch incident on the 26th |

---

## 14. Verify before you walk in (15 minutes)

- [ ] **scinethpc.ca/news**: any AI-system update (name, GPU model, go-live) since mid-Oct
- [ ] **Team page**: current analysts and titles; whether a Scientific Director is listed
- [ ] Whether the "triples GPU capacity" figure appears in an official source
- [ ] **education.scinet.utoronto.ca**: current AI/ML courses and who teaches them
- [ ] Optional: skim the recording or slides of van Zon's "Why the Trillium Cluster is Different" (May 2026) and Momeni's ocean talk (Jan 2026)

---

**Sources:**
[SciNet home](https://scinethpc.ca/) · [About SciNet](https://www.scinet.utoronto.ca/about-scinet/) · [SciNet staff](https://scinethpc.ca/?p=88) · [History of SciNet](https://scinethpc.ca/?p=939) · [Trillium](https://scinethpc.ca/trillium/) · [Mist](https://scinethpc.ca/mist/) · [Our Systems](https://scinethpc.ca/our-systems) · [Compute services](https://scinethpc.ca/compute-services/) · [HPSS](https://www.scinethpc.ca/?p=3285) · [New AI System Coming to SciNet](https://scinethpc.ca/news/new-ai-system-coming-to-scinet/) · [U of T: $42.5M AI compute](https://www.utoronto.ca/news/ai-compute-infrastructure-u-t-receives-425-million-federal-investment) · [Alliance: AI compute at U of T](https://www.alliancecan.ca/en/latest/news/the-government-of-canada-celebrates-the-investment-in-new-ai-compute-infrastructure-at-the-university-of-toronto) · [BetaKit: $42.5M](https://betakit.com/feds-commit-42-5-million-to-expand-ai-compute-infrastructure-at-university-of-toronto/) · [BetaKit: inside the GTA facility](https://betakit.com/inside-the-gta-facility-housing-one-of-canadas-most-powerful-supercomputers/) · [U of T: $52M upgrade](https://www.utoronto.ca/news/u-t-receives-52-million-upgrade-scinet-supercomputer) · [Academica: $95.4M U of T + Waterloo](https://academica.ca/top-ten/the-alliance-on-compute-ontario-invest-over-95-4m-into-u-of-t-uwaterloo-computing-infrastructure) · [VAST: SciNet customer story](https://www.vastdata.com/customers/scinet) · [insideHPC: VAST selected by SciNet and SHARCNET](https://insidehpc.com/2025/12/vast-data-selected-by-scinet-and-sharcnet-in-canada/) · [Niagara paper (arXiv)](https://ar5iv.arxiv.org/html/1907.13600) · [TCS decommissioned](https://scinethpc.ca/news/tcs-decommissioned/) · [Trillium ocean modelling](https://scinethpc.ca/news/trillium-pushes-the-limits-of-global-ocean-modelling/) · [Trillium stellar mixing](https://scinethpc.ca/news/trillium-enables-discovery-of-a-new-stellar-mixing-process/) · [UVic: supercomputers solve astronomical problem](https://news.uvic.ca/2026/supercomputers-solve-astronomical-problem/) · [SciNet status messages](https://docs.scinet.utoronto.ca/index.php/Previous_messages) · [Alliance: Killarney](https://docs.alliancecan.ca/wiki/Killarney) · [Alliance: PAICE](https://alliancecan.ca/en/services/advanced-research-computing/pan-canadian-ai-compute-environment-paice) · [Alliance: accelerated AI investments](https://alliancecan.ca/en/initiatives/accelerated-ai-investments) · [Alliance: sovereign AI vision](https://ai.alliancecan.ca/) · [Alliance: Schull named CEO](https://alliancecan.ca/en/latest/news/alliance-board-names-dr-michael-schull-next-ceo) · [ISED: Sovereign AI Compute Strategy](https://ised-isde.canada.ca/site/ised/en/node/271) · [Calcul Québec: Rorqual](https://www.calculquebec.ca/en/?p=6871) · [SciNet certificate program](https://www.scinethpc.ca/?p=1664) · [Data Science certificate](https://scinethpc.ca/news/announcing-scinets-data-science-certificate-program/) · [DAT112 (Spence)](https://education.scinet.utoronto.ca/course/info.php?id=1274) · [Ramses van Zon](https://pages.scinet.utoronto.ca/~rzon/index.html) · [Compute Ontario colloquium (May 2026)](https://education.scinet.utoronto.ca/course/info.php?id=1403) · [Acceleration Consortium $200M](https://news.engineering.utoronto.ca/self-driving-labs-200-million-federal-grant-powers-ai-driven-materials-discovery-for-clean-energy-advanced-manufacturing-and-more/) · [VPRI org chart (Mar 2026)](https://research.utoronto.ca/sites/default/files/2026-03/Workflow_OrgChart-VPRIExec_20260304.pdf) · [Compute Ontario CEO (2021)](https://news.mcmaster.ca/ranil-sonnadara-to-lead-compute-ontario/)
