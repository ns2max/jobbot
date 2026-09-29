# Layer 6 (TD Bank) — Machine Learning Engineer

**Date:** 2026-08-05
**Score:** 4.0/5
**URL:** https://td.wd3.myworkdayjobs.com/en-US/TD_Bank_Careers/job/Toronto-Ontario/Machine-Learning-Engineer_R_1431479
**PDF:** pending (generate-pdf.mjs script currently missing from repo)
**Legitimacy:** High Confidence
**Verification:** unconfirmed (Workday returned no job content directly — batch mode; role independently corroborated live via Vector Institute Digital Talent Hub, Ladders, and Glassdoor listings with matching comp range)

## A — CV Match
Layer 6 is TD Bank's AI center of excellence in Toronto, building ML systems across banking transactions, conversation transcripts, and large document collections for 27M+ customers. This is a production **Machine Learning Engineer** title (not "Research Scientist" — see sibling report `586`), so it weighs 3+ years shipping ML code in production more heavily than pure research output.

Direct matches:
- **3+ years production ML code** → 10+ years, most recently 5 years at MAS Holdings building and deploying CV/ML systems in live manufacturing, plus a Postdoc shipping real-time inference services
- **Python/Java/C/C++** → Python and C++ both used in production (MAS Holdings real-time inference engines; Forestpin backend scoring services)
- **Large-scale real-world multimodal datasets** → MUSMET (audio + sensor + gesture), MAS Holdings (camera + IoT sensor streams), direct multimodal pipeline experience
- **Financial/banking-adjacent data** → Forestpin: ML + statistical modeling for financial forensics, compliance monitoring, risk detection on structured enterprise datasets; Python-based anomaly-flagging scoring services

Gaps:
- **"Conversation transcripts"** implies an NLP/text modality alongside banking transactions — the CV has no direct NLP production experience (closest adjacent: prompt engineering, RAG, LLMs listed as technical stack familiarity, not shipped systems). Not a hard blocker given the role also covers non-text modalities.
- **Banking-specific ML at TD's scale** (27M customers) is larger than Forestpin's engagement — a reasonable stretch, not a disqualifier given demonstrated IoT-scale throughput at MAS Holdings (millions of events/day).

## B — North Star Alignment
**Archetype:** Senior/Staff ML Engineer (primary) — this is an IC production-engineering title, not the Research Scientist archetype used for Layer 6's sibling posting. Secondary read: Applied Scientist, given the PhD.
Strong fit: Layer 6 is a marquee Canadian industry ML lab, Toronto-based (no relocation), and production-ML-engineering framing plays directly to the MAS Holdings + Forestpin proof points rather than the academic publication record.

## C — Compensation
**$120,000–$250,000 CAD** (confirmed via Vector Institute Talent Hub posting), Toronto, ON, 37.5 hrs/week. Within target range ($80K–$220K floor-to-ceiling per `config/profile.yml`); likely lands mid-band given PhD + 10 years vs. the stated 3+ year minimum — reasonable to negotiate toward the upper half.

## D — Cultural Signals
TD Bank announced ~2,000 layoffs in 2026 as part of a broader post-AML-settlement restructuring, but the bank is explicitly **increasing** AI/digital investment as the stated rationale for those cuts (cost savings redirected into automation and AI). No evidence the cuts touch Layer 6 or AI hiring specifically — if anything, the public framing favors continued AI headcount growth. Layer 6 also opened a new New York office in April 2025, another sign of active expansion rather than contraction.

## E — Red Flags
- Direct Workday URL returns no content on fetch (same failure mode observed on the sibling Layer 6 posting in report `586`) — likely a client-side-rendered Workday quirk specific to TD's tenant, not a signal of a stale/fake posting, since the role is independently listed on three other job boards with consistent comp data.
- Conversation-transcript/NLP modality is a genuine, if soft, domain gap.
- Titled "Engineer" rather than "Senior Engineer" despite PhD-level background — worth a line in the cover letter on why an IC production role is the right fit (Toronto-based, industry-return narrative), so the seniority mismatch doesn't read as a flight risk to a hiring manager.

## F — Global Score
**4.0/5** — Strong Canada-based production ML fit with a direct financial-domain proof point (Forestpin) and a comp band that's confirmed and in-target; the "conversation transcripts" modality gap and the title/PhD-level mismatch are the only softeners.

## G — Posting Legitimacy
**High Confidence** — Actively cross-listed on Vector Institute's Digital Talent Hub, Ladders, and Glassdoor with matching salary data ($120K–$250K CAD), and Layer 6/TD's public 2025-2026 narrative is expansion-oriented (new NYC office, explicit "double down on AI" restructuring rationale), not contraction. The only concerning signal — the direct Workday link returning no content — is a rendering/access issue consistent with the sibling Layer 6 posting, not a legitimacy signal, given independent third-party corroboration.

## Machine Summary
```yaml
score: 4.0
archetype: Senior/Staff ML Engineer
company: Layer 6 (TD Bank)
role: Machine Learning Engineer
location: Toronto, ON, Canada
remote: false
canada_eligible: true
comp_range_cad: "120000-250000"
legitimacy: High Confidence
recommendation: apply
tagline_change_needed: false
```
