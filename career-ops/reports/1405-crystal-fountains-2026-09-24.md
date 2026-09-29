# Evaluation: Crystal Fountains (via NuBinary) — Senior Software Developer

**Date:** 2026-09-24
**URL:** https://jobs.ieee.org/job/x/f14adde5-5888941624/
**Archetype:** Solutions Architect (integrations) + Senior Software Engineer (C++/real-time) — hybrid, non-ML
**Score:** 3.4/5
**Legitimacy:** Proceed with Caution
**Verification:** JD read live on IEEE JobSite via Chrome 2026-09-24 (aggregated listing, posted 2026-09-19); original ATS/apply page not checked
**PDF:** pending

---

## A) Role Summary

| Field | Value |
|---|---|
| Archetype | Senior generalist software developer — systems integration + show-simulation tooling |
| Domain | Architectural water features (water/light/sound shows) — design, engineering, manufacturing |
| Function | Build + maintain: in-house app portfolio, "central nervous system" data/workflow integration (Java/Kotlin/REST), C# AutoCAD plugins with expert systems + LLMs, C++ Unreal Engine show-visualization plugins, DMX controller integration, remote commissioning support |
| Seniority | Senior IC, small team, reports to CTO |
| Remote | Not stated — assume onsite/hybrid at Vaughan office + factory. City rank 2 (GTA); ~35-45 min drive from Junction/High Park |
| Team size | "Small team" |
| Comp | Not listed (recruiter-posted via NuBinary) |
| TL;DR | A creative-tech integration job: tie ERP/SolidWorks/AutoCAD together, build Unreal show-sim plugins, and wire DMX fountain controllers. Strong on Nishal's C++ + real-time industrial + integration record, but no ML and comp is a real unknown. |

## B) Match with CV

Source of truth: `ai-job-search/input/knowledge-graph.md` (cv.md is a template).

| JD requirement | Evidence (KG) | Verdict |
|---|---|---|
| Degree in SE/CS or equivalent | PhD ICT (Trento), MSc Telecom & Electronic Eng., BEng Electronic Eng. — §3 | ✅ |
| Extensive experience in one of Java/C#/C++ | C++ = Expert: C++17 Nebula library, real-time engines, custom C++ closed-loop DTG printer control — §5.1, §4.5.c, §4.6 | ✅ strong |
| Moderate experience in two of Java/TS/C#/C++ | TypeScript/JS = Proficient (Hot Licks Mapper, web apps, speakfrench DSP in JS); C# = Working only; Java = none — §5.1 | ⚠️ one solid, one thin |
| Desktop + web apps and REST services | REST APIs (P), Node.js web apps (P), LiveLaTeX VS Code extension (shipped desktop-dev tooling) — §5.6, §4.6 | ⚠️ adequate, not deep |
| Integrate custom code with off-the-shelf business/engineering apps | Aeoon Kyo DTG printer: reverse-engineered PLC triggers + RIP automation hooks; Promptly RIP integration; software bots automating third-party software; Noyon Dentelle ERP lace search still in production — §4.5 | ✅ direct hit |
| Navigate and improve legacy code | Retrofitting heterogeneous sewing machines and legacy printer workflows at MAS — §4.5.b/c | ✅ adjacent |
| Mixed Linux/Windows | RPi/Elk Audio OS (Linux) deployments; Windows industrial PCs at MAS — §5.5 | ✅ |
| DMX/RDM protocols (helpful) | Ran stage lighting for two MUSMET live concerts; QLC+ lighting control (P) — QLC+ drives DMX — §4.1, §5.6 | ✅ adjacent (DMX via QLC+, RDM not evidenced) |
| AWS S3/EC2/Lambda/RDS (helpful) | AWS EC2/S3/ECS/MWAA/RDS (P); melodiq RDS + S3 pipelines — §5.6, §4.6 | ✅ |
| Test/troubleshoot real-time industrial HW/SW (helpful) | Care-label QC conveyor + PLC reject; loom-side camera arrays; 14 ms edge inference — §4.5, §4.1 | ✅ strong |
| C++ Unreal Engine plugins for show visualization | Unity + Meta XR SDK (W); audio VST/JUCE plugins; no Unreal — §5.6, §5.3 | ⚠️ gap |
| Expert systems + LLMs in C# AutoCAD plugins | LLM/RAG = Working level; no AutoCAD API work — §5.2 | ⚠️ gap |

### Gaps and mitigation

1. **Unreal Engine (nice-to-have to learn on the job).** Not a hard blocker: the JD asks for fast ramp-up on "novel languages, tooling and APIs". Mitigation: point to plugin work (VST/JUCE, Elk Audio OS, VS Code extension) and to the Unity/MR concert pipeline; a small UE5 C++ plugin (particle-based water jet preview driven by a timeline) would close it in a weekend.
2. **Java/Kotlin backbone (moderate).** He has none. Mitigation: frame REST/data-pipeline work (Airflow, Snowflake, SQL scoring services at Forestpin) as the transferable part; C++ → Java is a short hop. Say so plainly in the cover letter.
3. **C#/AutoCAD plugins (moderate).** C# is working-level. Mitigation: stress integration instincts (PLC/RIP/ERP hooks), not C# depth.
4. **No ML.** Not a gap for the job, but a North Star cost for Nishal (see C).

## C) Level and Strategy

- **Level detected:** Senior IC generalist under a CTO. Nishal is over-credentialed (PhD) but not over-qualified in the sense that matters: his MAS integration work is exactly this shape.
- **Sell senior without lying:** "I have spent ten years making hardware, industrial software and third-party tools talk to each other: printer RIPs, PLC triggers, ERP search, real-time audio on embedded Linux." Lead with Promptly (a globally deployed product he integrated) and the MUSMET concerts (lights, sound, MR headsets in one show).
- **If they downlevel:** fine if comp lands at or above ~CA$110K; ask for a written scope that includes the Unreal/visualization track (the part that keeps the creative-tech story alive).
- **Why take it:** music/show-tech + real-time systems + integration. **Why not:** leaves ML entirely; could make the ML-return narrative harder in 2-3 years.

## D) Comp and Demand

| Data point | Value | Source |
|---|---|---|
| Crystal Fountains self-reported salaries (all roles, small sample) | CA$58K-63K | [Glassdoor — Crystal Fountains Vaughan](https://www.glassdoor.com/Salary/Crystal-Fountains-Vaughan-Salaries-EI_IE1721930.0,17_IL.18,25_IC4035196.htm) |
| Software developer, Vaughan | CA$70K-169K | [CareerBeacon](https://www.careerbeacon.com/en/salaries/software-developer/vaughan_ontario) |
| Senior software developer, Toronto | avg CA$116K; P25-P75 CA$96K-144K | [Glassdoor Toronto](https://www.glassdoor.ca/Salaries/toronto-senior-software-developer-salary-SRCH_IL.0,7_KO8,33.htm) |

Comp is undisclosed and the only company-specific data point is low (likely dominated by non-engineering roles, but still a signal). **Ask the recruiter for the band before investing in a tailored application.** Demand: steady for senior generalists in the GTA; niche employer.

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---|---|---|---|
| 1 | Summary | ML research engineer framing | "Senior C++/Python engineer who integrates hardware, industrial software and creative tech — real-time systems, show tech, and ERP-grade integrations" | JD is integration-first, not ML |
| 2 | MAS entry | CV/ML metrics lead | Lead with Aeoon Kyo PLC + RIP hooks, Promptly RIP integration, Noyon ERP search, third-party automation bots | Mirrors "integrate custom code with off-the-shelf apps" |
| 3 | MUSMET entry | Pattern-detection metrics | Add the concert build: stage lights (QLC+/DMX), sound, 10 MR headsets, Hot Licks Mapper routing tool | Maps to water/light/sound shows + DMX |
| 4 | Projects | Research projects | Nebula (C++17), LiveLaTeX (shipped extension), melodiq (AWS/RDS) | Shows desktop/tooling shipping + AWS |
| 5 | Skills | ML-heavy | C++17, TypeScript, C# (working), REST, AWS, Linux/Windows, DMX via QLC+, PLC interfacing | ATS match |

LinkedIn top 5: headline add "real-time systems & integration"; feature Nebula + LiveLaTeX; add QLC+/DMX and PLC skills; add concert project with photos; recommendation from a MAS colleague on integration work.

## F) Interview Plan

| # | JD requirement | STAR+R story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Integrate with off-the-shelf apps | Promptly RIP + PLC integration | DTG printer vendor software was a closed loop | Tie printer workflow into the automation cell | Reverse-engineered PLC trigger points; built RIP hooks; coordinated 3 closed-loop subsystems in C++ | Product now deployed in US, Mexico, France, Sri Lanka | Document the vendor's undocumented behaviour first; it saved every later integration |
| 2 | ERP / data "single source of truth" | Noyon Dentelle lace archive + ERP search | Lace archive unsearchable | Digitize + make it findable from ERP | Built digitization + context-aware ERP search | Still in production use | Simple search over clean metadata beat clever matching |
| 3 | Show systems (water/light/sound) | MUSMET live concerts | Two concerts mixing lights, smoke, MR headsets, haptics | Make it run live with 20 audience + 6 performers | Built Hot Licks Mapper routing; ran lighting via QLC+ | Both shows ran; I3DA 2025 paper (p < .05) | Rehearse failure modes, not just the happy path |
| 4 | Real-time industrial troubleshooting | Care-label QC to conveyor + PLC reject | Manual care-label inspection | Automate reliably on the line | 3 iterations: flatbed → industrial camera → conveyor + PLC reject | −99.5% inspection time | Ship the simplest version first |
| 5 | Learn new tooling fast | Elk Audio OS / VST pipeline for MUSMET | New RT audio OS and plugin stack | Deploy detection as a live plugin | Learned Elk + VST + OSC and shipped it | 14 ms inference on RPi4 (JAES 2026) | Read the scheduler docs before optimizing code |
| 6 | Support away teams | MAS multi-factory rollouts | Deployments across sites | Keep remote sites running | Seminars, hands-on training, deployment docs | Multi-factory adoption | Training is part of the deliverable |

**Case study to present:** Promptly — integration of a vendor printer + PLC + vision alignment into a shipped product.
**Red-flag questions:** "Why leave ML?" → "I'm not leaving it; I'm choosing a place where real-time systems, integration and show tech meet — and your LLM-in-AutoCAD work is where ML shows up." "Why a PhD for this?" → the PhD was about real-time systems on constrained hardware; that is the job.

## G) Posting Legitimacy

**Assessment: Proceed with Caution**

| Signal | Finding | Weight |
|---|---|---|
| Posting freshness | Posted to IEEE JobSite 2026-09-19 (5 days); aggregated listing | Positive |
| Apply button / original page | Not verified (aggregated; original ATS not opened) | Neutral |
| Description quality | Very specific: named tools (SolidWorks, AutoCAD, Unreal, DMX/RDM), concrete roadmap, reporting line | Positive |
| Requirements realism | Consistent, generalist scope; no contradictions | Positive |
| Salary transparency | None; Glassdoor company data points low | Concerning |
| Recruiter intermediary | NuBinary recruits on behalf of the client (stated openly) | Neutral |
| Layoff / freeze news | None found | Neutral |
| Reposting | Not in scan-history | Neutral |

**Context:** A named-client recruiter posting with a detailed, idiosyncratic roadmap reads as a real opening. The caution is about comp, not legitimacy of the job.

---

## Keywords extracted
C++, Unreal Engine, plugins, C#, AutoCAD, Java, Kotlin, REST, TypeScript, desktop applications, web applications, ERP integration, SolidWorks, DMX, RDM, AWS S3, EC2, Lambda, RDS, Linux, Windows, legacy code, real-time industrial systems, simulation, visualization, LLM, expert systems

## Machine Summary
```yaml
id: 1405
company: Crystal Fountains (via NuBinary)
role: Senior Software Developer
score: 3.4
dimensions: {cv_match: 3.8, north_star: 3.0, comp: 2.5, culture: 3.5, red_flags: -0.2}
legitimacy: Proceed with Caution
location: Vaughan, ON (GTA) — city rank 2
recommendation: below 3.5 bar — apply only if the band is >= CA$110K and the non-ML move is intentional; ask recruiter for comp first
```
