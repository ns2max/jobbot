# Evaluation: Cohere — Senior Research Scientist, Model Evaluation

**Date:** 2026-05-23
**URL:** https://jobs.ashbyhq.com/cohere/830c613b-d4bf-4673-ab33-46ccc12cc415
**Archetype:** Research Scientist
**Score:** 3.4/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## Block A — Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Research Scientist |
| Domain | LLM evaluation / Foundation model capabilities research |
| Function | Research — evaluation benchmarks, LLM judges, data synthesis, scalable analysis |
| Seniority | Senior Research Scientist |
| Remote | Hybrid — Toronto, New York, Seattle, San Francisco, London (Canada eligible) |
| Team size | Not stated |
| TL;DR | Define next-generation evaluation methods for frontier LLMs; design ambitious benchmarks that push superhuman model limits; build scalable evaluation infrastructure. |

---

## Block B — Match with CV

### Strengths

| JD Requirement | CV Evidence |
|----------------|-------------|
| Rigorous experimental design and methodology | Core of PhD and postdoc: baselines, ablations, controlled comparisons. JAES 2026: 74× speedup confirmed via systematic ablation. |
| Track record of building evaluation benchmarks and datasets | DoMP/DoPP/DoDP/DoDP2: 7,000+ recordings, 70 musicians, published on Zenodo. 10 peer-reviewed publications with rigorous evaluation sections. |
| Strong software engineering skills | Python throughout; C++ at MAS; production deployments in multiple roles |
| Collaboration across teams on evaluation | MUSMET: cross-institutional evaluation framework; MAS Holdings: cross-functional ML adoption |
| Prototype rapid demonstrations of capabilities | McGill: real-time gesture detection prototype; MUSMET: <30ms inference proof-of-concept |

### Gaps

| Gap | Blocker? | Mitigation |
|-----|----------|-----------|
| LLM-specific research track record | Hard gap — explicit requirement | Publications are in audio ML / MIR, not LLM evaluation; no NeurIPS/ICLR/ACL papers |
| State-of-the-art LLM evaluation techniques (LLM judges, scalable data synthesis for NLP) | Hard gap | No demonstrated LLM evaluation research |
| "Designing benchmarks that challenge superhuman models" | Hard gap | Audio benchmarks demonstrate methodology; LLM-specific benchmark design not evidenced |
| Spending extensive time reviewing LLM outputs for quality assurance | Moderate gap | Systematic data review is familiar (70 musician dataset curation); domain is different |
| Publications at top NLP/ML venues | Hard gap | Venues are AES, IEEE I3DA, DAFx — audio engineering, not ML/NLP venues |

**Gap assessment:** This is a more research-pure role than the Research Engineer variant (327). The expectation is a publication record in LLM evaluation research. Nishal's publication record is strong but in audio ML. The Research Scientist title with an LLM evaluation focus creates a higher bar for domain-specific credentials than the Research Engineer version of the same role.

---

## Block C — Level and Strategy

**Level detected:** Senior Research Scientist — publication track record in LLM evaluation expected; "ambitious new benchmarks" framing suggests original research contributions, not just engineering.

**Candidate's natural level:** Strong Senior Research Scientist in audio/MIR domain. Not yet credentialed in LLM evaluation research.

**Sell senior plan:** Emphasize depth and rigour of publication record. Frame benchmark design methodology as transferable. Strong cover letter required. However, Research Scientist roles at frontier LLM companies typically require publications in the relevant domain — this gap is harder to bridge than for the Research Engineer version.

**Recommendation vs 327:** The Research Engineer role (327) is a better fit — it weights engineering execution of evaluation infrastructure alongside research. This Research Scientist role weights original research contributions to LLM evaluation more heavily.

---

## Block D — Comp and Demand

| Item | Detail |
|------|--------|
| JD stated comp | Not published |
| Cohere Toronto market (Senior RS) | ~$160K–$200K CAD base + equity |
| Comp vs target | Likely meets target with total comp |
| Demand trend | LLM evaluation research: growing rapidly |

---

## Block E — Customization Plan

Same as report 327 with additional emphasis on research methodology and publication record framing. Cover letter must address LLM domain gap directly.

---

## Block F — Interview Plan

Same core stories as report 327. This role additionally requires:

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|----------------|--------------|---|---|---|---|------------|
| 1 | Designing ambitious benchmarks that push model limits | DAFx 2022 SSIM method | No existing method could reliably detect patterns in edge cases; standard DTW failed | Design evaluation that would expose failure modes, not just average accuracy | Created benchmark suite including adversarial-like edge cases (polyphonic interference, tempo variation) | Identified specific failure modes that shaped the follow-up JAES 2026 work | The benchmark should challenge the model where it's weak, not confirm what we already know |
| 2 | Translating team feedback into trustworthy, repeatable evaluations | MUSMET cross-institutional benchmark | Partners disagreed on evaluation criteria for "real-time" threshold | Mediate between academic (latency) and industry (accuracy) priorities | Proposed dual-metric reporting (latency + F1) as standard; documented protocol | Adopted by all MUSMET partners; consistent across publications | Evaluation design is a stakeholder alignment problem as much as a technical one |

**Red-flag questions:**
- *"Your research is in audio ML — this role is LLM evaluation. Why?"* → "The core research skill — designing rigorous evaluations for systems where ground truth is ambiguous — is the same. I've built published benchmarks for audio pattern recognition; I'm committed to developing the same depth in LLM evaluation."
- *"We need someone who already knows LLM evaluation."* → "I'd recommend the Research Engineer variant for a 3-month ramp. But if you're looking for someone who will build evaluation rigour from first principles rather than copy existing NLP conventions, the cross-domain perspective has real value."

---

## Block G — Posting Legitimacy

**Freshness:** Active Ashby posting. Listed on Vector Institute talent hub (Toronto-specific). Recent posting per search results.

**Description quality:** Conceptually specific but less technically detailed than Research Engineer JD. "Designing ambitious benchmarks" language without named tools. Good legitimacy signal overall.

**Company hiring signals:** Cohere growing; no layoffs. Toronto HQ expanding.

**Legitimacy verdict:** High Confidence — genuine, active role.

---

## Recommendation

**Score: 3.4/5 — Low priority vs. the Research Engineer variant (327).**

This is the same evaluation team at Cohere but with a higher research bar (Senior Research Scientist vs Senior Research Engineer). The domain gap is the same, but the credential gap is harder to bridge — a Research Scientist title requires research domain credentials that Nishal's publications in audio ML don't fully satisfy for LLM evaluation. **If applying to Cohere's model evaluation team, prioritize the Research Engineer role (327) over this one.** Applying to both simultaneously is reasonable — let Cohere determine fit level — but the Research Engineer role is the stronger bet.

---

## Machine Summary
```yaml
score: 3.4
archetype: Research Scientist
location_accessible: true
audio_signal_match: false
```
