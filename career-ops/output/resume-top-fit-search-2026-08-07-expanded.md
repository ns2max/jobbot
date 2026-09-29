# Top-Fit Job Search — Expanded Scope (round 3)
**Date:** 2026-08-07

## Methodology

This round widens the net on two axes per explicit user instruction. **Scope:** beyond the audio/embedded/signal-processing niche used in rounds 1–2, this pass actively considered the full archetype set in `modes/_profile.md` — Senior/Staff ML Engineer (generalist production ML), Applied Scientist, Research Scientist, AI/ML Technical Lead, Solutions Architect (AI/ML) — including roles previously scored lower purely for a "domain gap" (NLP/LLM, recommender systems, etc.) where core ML engineering fundamentals still transfer. **Tailoring:** for any NEW role surfaced here, the user now authorizes *minor* body edits in addition to the tagline — reordering/re-emphasizing existing true bullets, resequencing Core Competencies, extending an existing bullet with a clause drawn from content already true and already present elsewhere in the resume. **Zero fabrication**: no new numbers, no new tools not in the Technical Stack, no new responsibilities, all 6 job entries stay. This constraint does not apply retroactively — the 8 CVs already generated (619, 620, 621, 622, 624, 625, 626, 628 in `output/`) stay verbatim/tagline-only and were not touched.

Process: mined `data/pipeline.md` (694 lines) and `data/applications.md` (70 lines, nearly all now `Applied`) for unactioned 3.0–4.0/5 "domain gap" entries; ran 9 fresh WebSearches across the broader archetype set; WebFetch-verified every promising hit (no Playwright — batch-mode fallback, per project policy).

## Headline finding: still thin, and one prior assumption gets corrected

Round 2 (2026-08-05) already established the narrow-scope well was dry. Widening scope did **not** unlock a large new set — most "domain gap" mid-scored roles in the tracker are LLM/RLHF-heavy companies (Anthropic, Cohere, Scale AI) where even under the relaxed framing, an ML-research-engineer-with-no-NLP-focus profile isn't a "perfect fit," just a survivable stretch. Fresh searches for generalist Senior/Staff ML Engineer, Solutions Architect (AI/ML), and AI/ML Technical Lead in Canada mostly surfaced either LLM-agentic product-engineering roles (wrong skill shape — Node.js/full-stack, not ML modeling) or stale aggregator listings.

**Correction to earlier assumption:** Apera AI's Senior ML/CV Applied Scientist (Vancouver, `#605` in pipeline.md, 3.8/5, never applied) was flagged in round 2 as a "periodically re-check" candidate. Checked directly against Apera's live 8-listing careers page this round — **that specific req is no longer live**. Removing it from consideration; Apera currently has no ML/Applied Scientist opening.

## Ranked shortlist

| # | Company | Role | Fit | Location | Liveness | Source | Why-fit |
|---|---------|------|-----|----------|----------|--------|---------|
| 1 | **Inspiren** | Senior/Staff Machine Learning Engineer | Strong domain analog, VLM gap | Remote — Canada (per secondary sources; primary unconfirmed) | **Unconfirmed** (Greenhouse page 500-errored twice; corroborated live via 2 independent aggregators — jobgether, himalayas) | New-find | Healthcare-tech company: VLM-based pipelines over edge-device camera data to improve senior-care monitoring. Near-exact structural analog to the resume's own GMOA-recognized COVID-19 camera-based patient-vitals-monitoring deployment — a real, documented, healthcare-specific CV deployment already in the resume that nothing else in the pipeline has matched this closely. VLM/LLM-pipeline requirement is the one gap. |

Everything else investigated this round was ruled out — see below. This is a 1-candidate round, and even that one has unconfirmed liveness.

## Modification plan for #1 (Inspiren)

Per the new minor-tailoring rule — reordering and light extension only, nothing fabricated:

- **Tagline:** swap to the embedded/edge framing already used for 619/624/626: *"Machine Learning Research Engineer | Embedded & Real-Time Inference, Signal Processing, Edge AI | Applied ML"* — Inspiren's role is explicitly edge-device-to-cloud, so this is a direct match, not a stretch.
- **Professional Summary:** the existing sentence — *"Published researcher with production-grade results (<30ms real-time inference, >90% F1, and up to 300% efficiency improvement in deployed industrial solutions)"* — gets a short appended clause: *"...including a GMOA-recognized camera-based patient-vitals monitoring system deployed across hospital wards."* This is not a new claim — it is the exact GMOA bullet that already exists verbatim in the resume's "Independent Research, Awards, Volunteer Work" section, surfaced one level higher because Inspiren's JD is specifically healthcare + camera + edge.
- **Independent Research, Awards, Volunteer Work section:** reorder so the GMOA bullet appears first (it is currently second, after MIDI Innovation Awards) — no wording changes, just sequence, since it is the single most relevant line in the entire resume for this specific JD.
- Everything else (Core Competencies, Technical Stack, all 6 job entries, Education, Publications) stays as-is — the existing Computer Vision / Embedded deployment / Multimodal Data Modeling entries already cover the rest of the JD's requirements without any edit needed.

## Investigated and ruled out

- **Apera AI — Senior ML/CV Applied Scientist, Vancouver** (`#605`, pipeline.md, 3.8/5, never applied): confirmed **closed** — not among Apera's current 8 live listings (checked directly). Correction to round-2 guidance; drop from watch list.
- **Datadog — Senior Applied Scientist** (anomaly detection / streaming-data role, excellent domain match on paper): confirmed **Paris, France, hybrid** — no remote-Canada eligibility indicated anywhere in the posting. Hard location blocker, same pattern as other EU-onsite roles already ruled out project-wide. Not pursued.
- **Robots & Pencils — Staff AI Engineer** (Canada Remote, confirmed live): read the actual requirements — 6+ years **Python/Node.js full-stack engineering**, LLM function-calling, multi-agent orchestration, vector DBs, RAG, AWS Lambda/DynamoDB/Step Functions. This is a full-stack agentic-product-engineering role, not an ML-modeling role — wrong skill shape for this candidate despite the "AI Engineer" title. Their VP-level Solutions Architect - AI role is US Remote only (excludes Canada) and is a seniority-level mismatch (VP, not Senior/Staff) regardless. Not pursued.
- **Yelp — Staff ML Engineer, Content and Contributor Intelligence (Remote Canada)**: the specific URL found returns **HTTP 410 Gone** — confirmed dead. Worth a fresh search later under a different query if Yelp reposts, but nothing actionable now.
- **Samsara — Senior Applied Scientist, Computer Vision** (surfaced via Built In Toronto, looked excellent — Canada-eligible, $150K–$194K CAD, direct CV/edge match): the cached posting shows a removal timestamp of **February 11, 2025** — over a year stale, a dead aggregator cache, not a live 2026 opening. Not the same req as anything currently open at Samsara. Not pursued.
- **Cohere — Member of Technical Staff, Senior/Staff MLE** (`#406`, 3.8/5) and similar 3.4–3.9/5 Cohere MTS roles (`#394`, `#399`, `#400`): re-considered under the relaxed domain-gap rule, but these remain core LLM-training/RL-team roles at an LLM-first company — even generously read, this is a "survivable stretch," not the "perfect fit" the user asked for this round. Listed here for completeness, not recommended as a priority.
- **Cognex / Zebra / Teledyne / Matrox** (machine-vision hardware companies, searched speculatively as a "known-strong-fit company type" per the LSI logic): search returned only generic aggregator noise, no specific verifiable Canada-eligible req. Worth a direct-careers-page check in a future round, same treatment as LSI.
- **~9 other WebSearch queries** across "AI Technical Lead," "Solutions Architect AI," and "fraud/anomaly Applied Scientist" in Canada returned only aggregator listing pages (Glassdoor/Indeed/ZipRecruiter search-result pages, not individual postings) or roles already covered above — no additional individually-verifiable candidates found.

## Recommendation

Verify Inspiren's posting directly (`https://job-boards.greenhouse.io/inspiren/jobs/5125737007` — kept 500-erroring via WebFetch this session, try a browser or retry later) before investing in the modification plan above. Beyond that, this round confirms round 2's conclusion: the current application batch (6 applied, 1 pending Audimee video) represents the realistic ceiling of what's live and matched right now. Re-running broad discovery weekly is unlikely to be productive until responses come in; a periodic direct check of Cognex/Zebra/Teledyne/Matrox career pages and Cerebras' `cerebras.ai/open-positions` (per round 2) is the highest-value low-effort standing action.
