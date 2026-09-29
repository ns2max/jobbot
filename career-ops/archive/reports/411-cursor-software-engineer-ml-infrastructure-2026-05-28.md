# 411 — Cursor — Software Engineer, ML Infrastructure

**Date:** 2026-05-28
**URL:** https://jobs.ashbyhq.com/cursor/c66cde5e-9cb6-4a2e-a330-9323e1edf2a9
**Archetype:** Senior / Staff ML Engineer
**Score:** 2.5 / 5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A — Match con CV

**Poor match.** Role is large-scale compute and storage infrastructure for ML: GPU cluster management, distributed training throughput, Infiniband/RoCE networking, Slurm/Ray scheduling, bare-metal Linux at thousands of nodes. This is ML platform / HPC infrastructure, not applied ML.

**Alignment:**
- Python, TypeScript: present in stack
- Docker, Kubernetes: present
- Infrastructure-as-code (Kubernetes): partial match
- Distributed systems: conceptual exposure from MUSMET pipeline + MAS Holdings ETL
- Linux: standard in the stack

**Gaps:**
- No GPU cluster management or HPC infrastructure experience
- No Infiniband, RoCE, or bare-metal GPU networking
- No Slurm / Ray scheduler operations
- No Nvidia Blackwell/Hopper hardware experience
- No Rust or Golang (explicitly listed alongside Python and TypeScript)
- No workload scheduling systems at thousands of nodes
- Location: SF or NY in-person — US work authorization required

**Score: 1.5 / 5**

---

## B — North Star Alignment

"Senior / Staff ML Engineer" is a target archetype, but this role is GPU cluster infrastructure engineering — not applied ML, model development, or research. Significant trajectory mismatch.

**Score: 1.5 / 5**

---

## C — Comp

No salary disclosed. SF-based infra role at a $2B ARR company: likely $200K–$350K USD. Strong comp but inaccessible due to location.

**Score: 3.0 / 5**

---

## D — Cultural Signals

Same as 409/410: flat, high-density, fast-moving, SF/NY in-person. Infrastructure role at Cursor is very specialized and high-stakes — any cluster downtime blocks all model training.

**Score: 2.0 / 5**

---

## E — Red Flags

- **[!] US work authorization required:** SF or NY in-person — Canadian PR ineligible without sponsorship. Score capped at 2.5.
- **Skills gap (major):** No GPU cluster, HPC, or distributed storage infrastructure experience. Rust/Golang not in stack.
- **Trajectory mismatch:** Infrastructure role diverges from ML research/applied target.

**Score: 1.0 / 5**

---

## G — Posting Legitimacy

**Tier: High Confidence**

- Active on Cursor careers page (cursor.com/careers/software-engineer-ml-infrastructure) and Ashby board
- Specific hardware requirements (Blackwell, Hopper, Infiniband) confirm real active hiring
- Cursor is actively expanding training capacity

---

## Global Score: 2.5 / 5

**Recommendation: Against applying.** US work authorization required + major skills gap on GPU cluster infrastructure. Three independent reasons not to apply (location, skills, trajectory). Skip.

---

## Machine Summary

```yaml
num: 411
company: Cursor
role: Software Engineer, ML Infrastructure
archetype: Senior / Staff ML Engineer
score: 2.5
location: San Francisco / New York (in-person)
work_auth_required: true
us_only: true
sf_onsite: true
comp_disclosed: false
comp_usd_estimate: "200K-350K"
verdict: against
key_gap: US work auth required (SF/NY in-person); no GPU cluster/HPC/Infiniband infrastructure experience; no Rust/Golang
best_proof_point: Docker/Kubernetes; distributed data pipelines (MAS Holdings)
legitimacy: High Confidence
```
