# Evaluation: Perplexity AI — Member of Technical Staff (Backend/Infrastructure Engineer, Search)

**Date:** 2026-08-20
**URL:** https://jobs.ashbyhq.com/perplexity/dd80ab52-34bd-42af-aa5e-6283b7e6c194
**Archetype:** Senior/Staff ML Engineer (infra-heavy) — secondary: Solutions Architect (AI/ML)
**Score:** 2.7/5
**Legitimacy:** Proceed with Caution
**PDF:** not generated — score below 3.5 threshold
**Verification:** unconfirmed (batch mode) — extracted via Ashby posting API (`api.ashbyhq.com/posting-api/job-board/perplexity`), WebFetch could not render the JS job page directly.

---

## A) Role Summary

| Field | Value |
|---|---|
| Archetype detected | Senior/Staff ML Engineer (infra) — owns backend systems behind Perplexity's latency-sensitive search stack |
| Domain | Distributed backend infrastructure for search serving/retrieval (Rust, Go, AWS, Kubernetes) |
| Function | Build + operate — full lifecycle from architecture to production ops |
| Seniority | Senior (no explicit level in title; "MTS" generalist band, requirements read mid-senior) |
| Remote | **Onsite — Belgrade** (primary), secondary offices London, Berlin. No remote or Canada option stated. |
| Team size | Not disclosed |
| TL;DR | A backend infra role on Perplexity's search team, onsite in Belgrade/London/Berlin — strong technical overlap with the candidate's real-time systems background, but a hard location mismatch against the Canada-based, no-relocation-support profile. |

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|---|---|---|
| Cloud infra, distributed systems, automation | "Owned full ML pipelines... data acquisition... deployment with monitoring" (Postdoc, Trento); AWS/Kubernetes/Docker in Technical Stack | Moderate |
| Linux internals, performance analysis, production debugging | "<30ms latency at >90% F1... reproducible pipelines" (Postdoc) demonstrates latency-constrained engineering, but not Linux-kernel-level work | Weak-moderate |
| Latency-sensitive, high-throughput backend systems | "<30ms real-time inference" (Professional Summary); "improved operational efficiency by up to 300%" (MAS Holdings) — real-time discipline transfers, but not at Perplexity's QPS scale | Moderate |
| Fluency in Rust, Go, C++, or Java | Technical Stack lists Python, C++, C, JavaScript, MATLAB, C# — no Rust/Go | **Gap** |
| CI/CD, release tooling | "established code review and CI/CD practices" (MAS Holdings) | Strong |

**Gaps:**
1. **Rust/Go fluency** — hard requirement, listed first in "Requirements." Candidate's systems languages are C/C++/Python/C#. **Hard blocker** — no adjacent experience to point to; a 2-week Rust refresher would not close a "fluency" bar for a live-service infra team.
2. **Search/retrieval at billions-of-pages scale** — nice-to-have per JD, but candidate's largest data-scale work (MAS Holdings IoT pipelines, MUSMET streaming) is not comparable to web-scale search infra. Mitigation: frame streaming multi-dimensional data pipelines as transferable systems-design experience, not a scale claim.
3. **Location** — onsite Belgrade/London/Berlin, no remote/Canada path disclosed. **Hard blocker** per profile policy (non-Canadian onsite, no relocation support noted).

## C) Level and Strategy

1. **Level detected:** Senior IC generalist infra band; requirements (5+ yrs implied by depth, Rust/Go fluency) suggest mid-to-senior, not entry MTS.
2. **"Sell senior without lying":** Lead with the <30ms/>90% F1 real-time pipeline work and the 300% throughput win at MAS Holdings as evidence of shipping under hard latency/scale constraints — reframe as "constrained systems engineering," not language-specific tenure.
3. **"If they downlevel me" plan:** Not applicable — the Rust/Go gap is the blocker here, not seniority. Even at a lower level, the language mismatch remains.

## D) Comp and Demand

| Source | Data | Note |
|---|---|---|
| Glassdoor | Perplexity AI MTS avg. ~$147K/yr (45 salaries, US) | Base-only figure, likely light on equity |
| Levels.fyi | Perplexity SWE total comp $200K–$507K+ | Wide range reflects level/equity variance; MTS-specific band not isolated |
| jobsbyculture.com | Perplexity 2026 TC estimate $180K–$450K+ | Directionally consistent with Levels.fyi |

No Belgrade/EMEA-specific comp band found — SF/US figures above are not directly transferable to a Belgrade-based role, which will pay materially below US bands. **Red flag:** role requires onsite presence in Belgrade, London, or Berlin — none is Canada, and no relocation/visa support is mentioned. Per profile policy, this is an auto-flag; candidate is a Canadian PR with no stated intent to relocate to Serbia/UK/Germany.

## E) Customization Plan

Not generated — score below 3.5 threshold. If the candidate wants to pursue despite the location mismatch (e.g., open to Berlin/London relocation), top priorities would be: (1) add a Rust learning-in-progress line, (2) reframe MUSMET/MAS work around latency-under-load rather than dataset scale, (3) drop signal-processing framing in favor of "systems reliability engineer."

## F) Interview Plan

Not generated — score below 3.5 threshold.

## G) Posting Legitimacy

**Assessment:** Proceed with Caution

| Signal | Finding | Weight |
|---|---|---|
| Posting age | `publishedAt` = 2025-03-07 — this posting is ~17 months old as of 2026-08-20 | Concerning |
| Apply button | Live on Ashby board (job still listed in active board API response) | Positive |
| Description quality | Specific tech stack (Rust, Go, AWS, K8s), clear responsibilities/requirements split | Positive |
| Requirements realism | Consistent, no contradictions | Positive |
| Company hiring signals | CEO on record (Mar 2026) saying company is not freezing hiring, aiming to expand cautiously; broader AI-sector layoff wave (165K+ roles cut in 2026 YTD) is context, not company-specific | Neutral |
| Reposting pattern | Not previously seen in `scan-history.tsv` under a different URL | Neutral |

**Context Notes:** A 17-month-old still-open MTS infra req at a fast-scaling company (Perplexity has been aggressively hiring MTS roles broadly, per the wider job-board pull) is plausible as a rolling/evergreen infra req rather than a single-seat ghost listing — many AI labs keep senior infra reqs open continuously. Still, the age is the single most concerning data point; worth confirming activity via LinkedIn before investing significant prep time.

---

## Keywords extracted

Rust, Go, distributed systems, cloud infrastructure, Linux internals, Kubernetes, AWS, observability, CI/CD, capacity planning, performance profiling, incident response, search serving, retrieval, high-QPS, containers, infrastructure as code, systems programming, production debugging, low-latency backend
