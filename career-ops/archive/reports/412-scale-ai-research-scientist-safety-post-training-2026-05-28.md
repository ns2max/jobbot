**Date:** 2026-05-28
**URL:** https://job-boards.greenhouse.io/scaleai/jobs/4696595005
**Archetype:** ML Research Engineer / Applied Scientist (Safety Post-Training)
**Score:** 2.5/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A — Match con CV

**Alignment: Moderate-Low (capped by work auth)**

Positive signals:
- Post-training pipelines: Nishal has full ML pipeline ownership (MUSMET postdoc), but this is LLM post-training (RLHF, DPO, GRPO) — not his domain. No LLM fine-tuning experience on record.
- Published ML research: 10 peer-reviewed publications, including JAES 2026 and DAFx 2022 — strong research track record.
- "Minimum 3 years addressing sophisticated ML problems": 10+ years across MAS Holdings, MUSMET postdoc, Forestpin.
- Benchmark/evaluation design: Deep methodology (F1, SSIM, ablations) directly maps to "evaluations revealing unsafe model behaviors."
- Experimental design and ablation methodology: core proof point from PhD and postdoc.

Gaps:
- No LLM post-training experience (RLHF, DPO, GRPO, PPO) — this is the core of the role.
- No safety/interpretability/alignment research background.
- No generative AI (LLM-scale) publications at NeurIPS/ICLR/ICML.
- Mechanistic interpretability, red-teaming, adversarial evaluation: zero evidence.
- The "Safety" framing (AI control, agent robustness, deception) is entirely outside current profile.

**CV match score: 2.5/5**

---

## B — North Star Alignment

Closest archetype: ML Research Engineer / Applied Scientist.

This role sits at the intersection of LLM safety research and post-training engineering — a niche where Nishal has none of the specific sub-domain expertise. The research rigor transfers (benchmark design, experimental methodology, publications), but the content area (LLM alignment, RLHF, safety) is orthogonal to the MIR/audio/embedded ML trajectory.

Not a North Star match. The role requires deep LLM alignment expertise that doesn't appear in cv.md or knowledge-graph.md.

**North Star score: 2.0/5**

---

## C — Comp

Base salary: $216,000–$270,000 USD (~$295K–$369K CAD at ~1.365 rate). Well above Nishal's $140K–$180K CAD range for this level.

Comp alone would be exceptional — but irrelevant given work auth.

**Comp score: 5.0/5** (notional; blocked by work auth)

---

## D — Cultural Signals

Scale AI is a high-velocity AI data foundry with significant enterprise and government contracts. The safety post-training team is research-oriented with publication expectations. 3 days/week in-office in SF or NY — requiring US relocation.

Red flag: **US work authorization required** — no sponsorship mentioned, and Scale AI has not historically been a major sponsor for Canadian-based candidates without US presence. Role is listed for SF and NY only.

**Cultural score: 2.5/5**

---

## E — Red Flags

[Score < 3.5 — Block E shown for transparency]

1. **[CRITICAL] US work authorization required.** Role is SF/NY only. Nishal is a Canadian PR with no US work authorization. This is a hard blocker unless Scale AI sponsors a TN/H-1B. Automatically caps score at 2.5 per agent rules.
2. **Domain mismatch (LLM safety/alignment).** No RLHF, DPO, GRPO experience. No safety research background. Core JD requirements are not met.
3. **Missing generative AI publications.** Scale AI safety team expects NeurIPS/ICLR/ICML publications on LLM-scale problems. Nishal's publications are audio/signal/MIR.
4. LLM post-training niche is competitive — candidates without specific RLHF/alignment background face significant screening attrition.

---

## F — Not shown (score < 4.0)

---

## G — Posting Legitimacy

- **Tier:** High Confidence
- Active Apply button observed via WebFetch.
- Scale AI is actively growing its safety research capacity (known from public reporting).
- Specific comp range published, SF/NY locations explicit — legitimate posting signals.
- No reposting pattern in scan-history.tsv for this JD ID.

---

## Machine Summary

```yaml
num: 412
company: Scale AI
role: Research Scientist, Safety Post Training
date: 2026-05-28
score: 2.5
archetype: ML Research Engineer / Applied Scientist
url: https://job-boards.greenhouse.io/scaleai/jobs/4696595005
location: San Francisco, CA / New York, NY (US only)
work_auth_blocker: true
domain_match: low
comp_usd: 216000-270000
verdict: skip — US work auth + domain mismatch (LLM safety/alignment outside profile)
```
