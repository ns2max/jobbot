# 404 — Cohere — Senior ML Systems Engineer, Frameworks & Tooling

**Date:** 2026-05-28
**URL:** https://jobs.ashbyhq.com/cohere/c99e61c9-ed92-426d-9711-188dfc0f729f
**Archetype:** Senior / Staff ML Engineer
**Score:** 3.2 / 5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A — Match con CV

**Partial match.** The role centers on building and owning the training framework for frontier-scale LLM training: distributed training abstractions (FSDP/ZeRO, data/tensor/pipeline parallelism), multi-node cluster optimization (GB200/H200), and developer tooling. This is deep ML systems / HPC infrastructure — not applied ML or inference.

**Alignment:**
- PyTorch, JAX, Docker, Kubernetes, distributed systems: present in stack
- C++ production engineering at MAS Holdings: relevant
- MLOps and CI/CD practices: present
- Multi-node cluster orchestration (Slurm, Ray, Kubernetes): Kubernetes yes, Slurm not demonstrated

**Gaps:**
- No direct LLM training framework experience (DeepSpeed, Megatron, Triton kernels)
- No CUDA/NCCL performance debugging track record
- No contributions to PyTorch/JAX internals or open-source ML frameworks
- No HPC-scale cluster work (GB200, H200 multi-node)
- Publications at top-tier ML venues listed as nice-to-have — Nishal's publications are audio/MIR, not ML systems

This is a highly specialized infra role. The profile has strong production ML and systems instincts but is missing the specific LLM training infra stack Cohere needs.

**Score: 2.5 / 5**

---

## B — North Star Alignment

Target archetypes are Senior/Staff ML Engineer and ML Research Engineer. This role is neither: it is an ML systems / HPC infrastructure role that supports model training but doesn't involve applied ML, model development, or research. The day-to-day would be framework internals, GPU cluster debugging, and distributed training abstractions — a useful adjacent skill set but not the trajectory Nishal is targeting.

**Score: 2.5 / 5**

---

## C — Comp

No salary disclosed. Cohere offers remote-flexible work, full health/dental, mental health budget, 6 weeks vacation, 100% parental leave top-up (6 months). For a Senior/Staff ML Systems Engineer at a frontier AI company, market rate is $170K–$220K CAD equivalent. Cohere's Canadian presence (Toronto HQ) is a positive. Remote-eligible.

**Score: 3.5 / 5** (no disclosed comp, assume competitive given Cohere's scale)

---

## D — Cultural Signals

Cohere is a frontier AI company, Series D+, building enterprise LLM products. Strong engineering culture. Remote-flexible with offices in Toronto, SF, London, NY, Paris. No US work auth requirement — Cohere is Canadian-HQ'd, eligible for Canadian PR candidates.

No red flags on culture. Role posted as fully remote. Cohere has had some turbulence in 2024–2025 (leadership changes, refocusing on enterprise) but is well-funded and relevant.

**Score: 3.5 / 5**

---

## E — Red Flags

- **Skill mismatch (major):** Role requires deep LLM training framework experience (DeepSpeed, Megatron, Triton, NCCL debugging) that Nishal does not have. Applying without this risks a fast rejection.
- **Career trajectory mismatch:** Moving into ML systems infrastructure at this stage would be a lateral-to-downward move from an applied ML / research trajectory.
- No US work auth issues (Cohere is Canadian).

**Score: 2.5 / 5**

---

## G — Posting Legitimacy

**Tier: High Confidence**

- Active on Ashby job board as of search date
- Specific technical requirements (GB200/300, FSDP/ZeRO, NCCL) indicate a real open headcount, not a ghost posting
- Cohere has a known LLM training team
- Posted within last 30 days based on aggregator data ("1 month ago")

---

## Global Score: 3.2 / 5

**Recommendation: Against applying.** Strong skill mismatch on the core requirement (LLM training framework internals). The production ML background is adjacent but not sufficient. Applying here would be a stretch that Cohere's team will quickly identify. Not aligned with target trajectory.

---

## Machine Summary

```yaml
num: 404
company: Cohere
role: Senior ML Systems Engineer, Frameworks & Tooling
archetype: Senior / Staff ML Engineer
score: 3.2
location: Remote (global, Cohere is Canadian-HQ)
work_auth_required: false
us_only: false
sf_onsite: false
comp_disclosed: false
comp_estimate_cad: "170K-220K"
verdict: against
key_gap: No LLM training framework internals (DeepSpeed, Megatron, NCCL debugging, CUDA kernels)
best_proof_point: MAS Holdings C++ real-time systems; Kubernetes/Docker MLOps
legitimacy: High Confidence
```
