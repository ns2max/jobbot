# 408 — Baseten — Post-Training Research Scientist

**Date:** 2026-05-28
**URL:** https://jobs.ashbyhq.com/baseten/7c9d2bb0-ac03-4a3c-86c3-cf720cd314e8
**Archetype:** Research Scientist
**Score:** 2.8 / 5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A — Match con CV

**Moderate match on methodology; gap on domain.** Role involves pursuing open research problems at the intersection of post-training methodology and inference performance, building in-house post-training tooling, training diverse model architectures at scale, and collaborating with research engineering to translate findings to production.

**Alignment:**
- PhD in ML/signal processing + postdoc: meets "strong experience in ML, solid foundations in maths and CS"
- Benchmark-first research methodology: JAES 2026 (F1, ablations, 74× speedup quantification), DAFx 2022 (SSIM vs baselines) — rigorous evaluation is a direct match
- Research-to-production pipeline: MUSMET postdoc — prototyped novel algorithms, deployed to edge hardware
- Efficient model design under compute constraints: 14ms RPi4 inference — resource-constrained optimization is directly relevant to post-training for efficient inference
- Published research: 10 peer-reviewed publications

**Gaps:**
- **Domain gap (critical):** Post-training for LLMs (RLHF, RLVR, DPO, SFT, reward modeling) is the core domain. Nishal's research is entirely audio/MIR/signal processing — no NLP or LLM post-training work demonstrated.
- No transformer fine-tuning at scale
- No reward model or preference data work
- No GPU cluster scale work (Baseten trains diverse model architectures at scale — H100/A100 multi-node)

The general ML rigor maps well, but the specific domain (LLM post-training research) is absent from the profile.

**Score: 2.5 / 5**

---

## B — North Star Alignment

"Research Scientist" is a target archetype. The role's structure (open research, publish findings, translate to production) aligns well with the research arc. However, Baseten's post-training team works specifically on LLMs — the domain is language, not audio. The profile's publications and research are in MIR/audio. This creates a meaningful archetype fit but poor domain fit.

**Score: 3.0 / 5**

---

## C — Comp

$200K–$275K USD per year. In CAD: ~$275K–$380K. Top of market for research roles. However, this is a San Francisco hybrid role — US work authorization likely required for SF-based positions.

**Score: 4.5 / 5** (comp is excellent if accessible)

---

## D — Cultural Signals

Baseten is a Greylock-backed Series B focused on inference infrastructure and post-training. The post-training team is a newer high-investment function. Small, talent-dense research team. SF hybrid or in-office expected at that comp level.

**Score: 2.5 / 5** (location concern)

---

## E — Red Flags

- **[!] US work authorization likely required:** San Francisco hybrid at $200K–$275K USD — in-office expectation high. Canadian PR would need US sponsorship.
- **Domain gap (major):** LLM post-training research is a specific sub-field. Hiring managers will compare against candidates with RLHF/DPO/reward model publications. Audio ML PhD doesn't map cleanly.
- **Seniority bar:** "Research Scientist" at Baseten at this comp implies strong LLM post-training publication record.

**Score: 2.0 / 5**

---

## G — Posting Legitimacy

**Tier: High Confidence**

- Active on Ashby with stable URL
- Compensation disclosed ($200K–$275K) — signals real headcount budget
- Baseten's post-training team is publicly documented
- Multiple aggregators confirm active listing (startup.jobs, aijobs.com)

---

## Global Score: 2.8 / 5

**Recommendation: Against applying.** Two compounding blockers: (1) US work authorization required for SF-based role; (2) LLM post-training domain is not demonstrated in the profile. The research methodology rigor is genuine but insufficient to overcome both gaps simultaneously. Skip.

---

## Machine Summary

```yaml
num: 408
company: Baseten
role: Post-Training Research Scientist
archetype: Research Scientist
score: 2.8
location: San Francisco (hybrid)
work_auth_required: true
us_only: true
sf_onsite: true
comp_disclosed: true
comp_usd: "200K-275K"
verdict: against
key_gap: US work auth required (SF hybrid); LLM post-training domain absent from profile (audio/MIR PhD)
best_proof_point: Benchmark methodology (JAES 2026); efficient inference under compute constraints (14ms RPi4)
legitimacy: High Confidence
```
