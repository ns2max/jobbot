# Evaluation: Queen's University — Tier 2 CRC / Mitchell Chair — Supercomputing/HPC (Tenure-Track)

**Date:** 2026-09-24
**URL:** https://jobs.ieee.org/job/x/85995045/
**Archetype:** Assistant/Adjunct Professor (AI/ML) — HPC specialization
**Score:** 2.4/5
**Legitimacy:** High Confidence
**Verification:** JD read live on IEEE JobSite via Chrome 2026-09-24 (employer-direct posting, posted 2026-09-15); original ATS/apply page not checked
**PDF:** pending

---

## A) Role Summary

| Field | Value |
|---|---|
| Archetype | Tenure-track Assistant/Associate Professor as Tier 2 CRC or Mitchell Chair in supercomputing/HPC/extreme-scale systems |
| Domain | Academic — ECE, Smith Engineering |
| Function | Research program leadership, teaching, supervision, CRC nomination |
| Seniority | Assistant/Associate Professor; start Sep 1, 2027 |
| Remote | Kingston, ON — city rank 3; onsite |
| Comp | CA$150,000-200,000 |
| TL;DR | Funded HPC chair with reduced teaching. Nishal fits the professor archetype and the rank, but his research is real-time/embedded audio ML, not supercomputing systems (MPI, CUDA/HIP, SLURM, parallel I/O). |

## B) Match with CV

Source of truth: `ai-job-search/input/knowledge-graph.md` (career-ops `cv.md` is a template).

| JD requirement | Evidence (KG) | Verdict |
|---|---|---|
| PhD | PhD ICT, Trento 2025 (§3) | ✅ |
| Supercomputing systems background (SLURM, MPI/NCCL, OpenMP/CUDA/Kokkos, MPI+X, HDF5/Adios) | None evidenced; dual-GPU training for VarianceEngine only (§4.6) | ❌ hard gap |
| Deep expertise in an HPC research area | Edge/embedded latency research — the opposite end of the compute spectrum (§4.1) | ❌ |
| Edge systems ↔ supercomputers (listed example) | MIRaaS edge→server offloading (IEEE IS² 2026) (§4.1) | ⚠️ thin bridge |
| Publications, funding, research leadership | 10+ papers; EU EIC Pathfinder project member; no PI funding (§6, §4.1) | ⚠️ |
| Teaching + mentorship | 2 BSc theses supervised; seminars (§4.1a) | ⚠️ light |
| P.Eng eligibility | Probably eligible via PEO academic assessment (UK degrees) — confirm | ⚠️ |
| Tier 2 CRC: within 10 yrs of first independent appointment | Yes (none yet) | ✅ |

### Gaps and mitigation

1. **Research-area mismatch (hard).** Only credible angle is edge↔HPC continuum computing; thin.
2. **Funding record (moderate).** No PI grants.

## C) Level and Strategy

- **Level detected:** Assistant Professor.
- **Sell senior without lying:** "My work is the edge half of the edge-HPC continuum: real-time inference offloaded from embedded devices to servers."
- **If they downlevel:** n/a.

## D) Comp and Demand

| Data point | Value | Source |
|---|---|---|
| Posted band | CA$150K-200K | JD |
| Program | Mitchell Chair: 5 yrs of direct research support; reduced teaching | JD |

Comp is well above the ideal range. No extra search run (university/public-sector posting).

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---|---|---|---|
| 1 | Research statement | — | Edge↔HPC continuum computing for real-time ML | Only viable framing |
| 2 | CV | Industry CV | Academic CV: pubs, datasets, supervision, grants | Faculty format |
| 3 | Teaching | — | Signal processing + embedded ML courses | Dept fit |

LinkedIn: n/a.

## F) Interview Plan

| # | JD requirement | STAR+R story (S → T → A → R) | Reflection |
|---|---|---|---|
| 1 | Research program | JAES 2026 line of work (14 ms, F1 0.76, 74× faster) | Benchmark harness became the asset |
| 2 | Edge↔server | MIRaaS latency characterization (IS² 2026) | Network jitter dominates |
| 3 | Mentorship | Two BSc theses on real-time pattern detection plugins | Scope student projects to ship |

**Case study:** MIRaaS as the bridge to HPC.
**Red-flag questions:** "What is your HPC research?" — no strong answer; supports skipping.

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| Freshness | Posted 2026-09-15; start Sep 2027 (normal academic lead time) | Positive |
| Description quality | Very specific, funded program | Positive |
| Salary transparency | Band posted | Positive |
| Layoffs / freeze | n/a (university) | Neutral |
| Reposting | Not in career-ops scan-history | Neutral |

**Context:** Academic timelines are long by design.

---

## Keywords extracted
supercomputing, high performance computing, HPC, extreme-scale systems, MPI, NCCL, RCCL, OpenMP, CUDA, HIP, Kokkos, SLURM, HDF5, Adios, digital twins, AI infrastructure, Canada Research Chair, tenure-track, P.Eng

## Machine Summary
```yaml
id: 1414
company: Queen's University
role: Tier 2 CRC / Mitchell Chair — Supercomputing/HPC (Tenure-Track)
score: 2.4
dimensions: {cv_match: 2.0, north_star: 2.8, comp: 4.5, culture: 3.8, red_flags: -0.6}
legitimacy: High Confidence
location: Kingston, ON — city rank 3
recommendation: below 3.5 — skip (research-area mismatch)
```
