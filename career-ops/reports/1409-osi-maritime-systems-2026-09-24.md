# Evaluation: OSI Maritime Systems — Software Engineering - Systems Test Engineer P3

**Date:** 2026-09-24
**URL:** https://jobs.ieee.org/job/x/f14adde5-5879457773/
**Archetype:** Software V&V / systems test (defence) — non-ML
**Score:** 2.3/5
**Legitimacy:** High Confidence
**Verification:** JD read live on IEEE JobSite via Chrome 2026-09-24 (aggregated listing, posted 2026-09-11); original ATS/apply page not checked
**PDF:** pending

---

## A) Role Summary

| Field | Value |
|---|---|
| Archetype | Systems test engineer for naval ECDIS navigation software (ECPINS Warship) |
| Domain | Defence marine navigation software |
| Function | Test: plan, write procedures, execute V&V, defects, lab builds, customer acceptance on ships |
| Seniority | Intermediate-senior (P3), 4-6 yrs |
| Remote | Burnaby, BC — city rank 3; onsite lab work; ship/site travel |
| Comp | Not posted |
| TL;DR | Real-time naval navigation software testing under ISO 9001 with a mandatory security clearance. Real-time systems knowledge transfers; the role, domain and clearance do not suit Nishal's direction. |

## B) Match with CV

Source of truth: `ai-job-search/input/knowledge-graph.md` (career-ops `cv.md` is a template).

| JD requirement | Evidence (KG) | Verdict |
|---|---|---|
| Degree CS/SE/EE/Math | PhD ICT; BEng/MSc electronic eng. (§3) | ✅ |
| 4-6 yrs software environment; real-time interfaces to external systems | Real-time audio/IMU/OSC pipelines; PLC/RIP interfaces (§4.1, §4.5.c) | ✅ |
| ISO 9001 software process | Not evidenced | ❌ |
| Testing on Windows + Linux; 2D/3D graphics, TCP/IP, UDP | Linux/Windows deployments; MIRaaS over UDP; OSC (§4.1, §5.5) | ✅ |
| Test plans/procedures/reports | Benchmark suites, ablations, user-study protocols (§5.7) | ⚠️ research-style, not formal V&V |
| Security clearance required | None; PR — naval programs often need Secret, which is slower/harder for non-citizens | ⚠️ eligibility risk |
| Marine navigation knowledge (asset) | None | ❌ |

### Gaps and mitigation

1. **Clearance (possible blocker).** Confirm the level with OSI before anything else.
2. **Formal V&V / ISO 9001 (moderate).** Mitigation: frame benchmark/ablation rigour as test design; learn IEEE 829-style docs.
3. **Career direction (soft).** A test-engineering move away from ML/research.

## C) Level and Strategy

- **Level detected:** P3 intermediate; under-uses PhD.
- **Sell senior without lying:** "I design measurement before I build — every system I've shipped had a benchmark harness first."
- **If they downlevel:** Not recommended to pursue at a lower band.

## D) Comp and Demand

| Data point | Value | Source |
|---|---|---|
| Posted comp | None | JD |
| Hiring activity | ~17-18 open roles in Canada; Glassdoor career-opportunity rating 3.0/5 | [Glassdoor — OSI jobs](https://www.glassdoor.ca/Jobs/OSI-Maritime-Systems-Jobs-E22719.htm) |

No comp data for this title; mid-level test roles in Vancouver typically sit below the ideal band.

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---|---|---|---|
| 1 | Summary | ML research | Real-time systems engineer with measurement-first testing practice | Test role |
| 2 | MUSMET | Model metrics | Latency characterization (MIRaaS over UDP), benchmark suites | Real-time + networking |
| 3 | Skills | ML stack | Linux/Windows, TCP/UDP, test procedures, Python/C++ | ATS |

LinkedIn: minimal change; not a priority target.

## F) Interview Plan

| # | JD requirement | STAR+R story (S → T → A → R) | Reflection |
|---|---|---|---|
| 1 | Real-time interfaces | MIRaaS: offloaded MIR over UDP, latency characterized → IEEE IS² 2026 | Measure tail latency, not averages |
| 2 | Test design | JAES RNN vs DTW ablation matrix (set sizes 1/3/10) | Pre-register the protocol |
| 3 | Customer acceptance | COVID vitals device installed in hospital wards | Field conditions rewrite specs |

**Case study:** MIRaaS latency characterization.
**Red-flag questions:** "Why test after a PhD?" — no strong answer; supports skipping.

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| Freshness | Posted 2026-09-11 (13 days) | Positive |
| Description quality | Detailed duties, stack, clearance | Positive |
| Salary transparency | Not posted | Neutral |
| Layoffs / freeze | None found; active hiring | Positive |
| Reposting | Not in career-ops scan-history | Neutral |

**Context:** Defence employer with steady hiring.

---

## Keywords extracted
systems test, verification and validation, test plans, test procedures, ECDIS, real-time systems, TCP/IP, UDP, Windows, Linux, 2D/3D graphics, ISO 9001, SDLC, defect tracking, security clearance, customer acceptance

## Machine Summary
```yaml
id: 1409
company: OSI Maritime Systems
role: Software Engineering - Systems Test Engineer P3
score: 2.3
dimensions: {cv_match: 2.8, north_star: 1.8, comp: 2.5, culture: 3.0, red_flags: -0.5}
legitimacy: High Confidence
location: Burnaby, BC — city rank 3
recommendation: below 3.5 — skip
```
