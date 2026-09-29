<!-- Job posting: https://ca.linkedin.com/jobs/view/embedded-artificial-intelligence-architect-at-mda-space-4414774301 -->

# Job Fit Evaluation — 1162

**Role:** Embedded Artificial Intelligence Architect (Technical Lead)
**Company:** MDA Space — Satellite Systems team
**Location:** Sainte-Anne-de-Bellevue, QC (Montreal West Island) · works with the Ontario head office
**Comp:** not disclosed · **Deadline:** none stated
**Evaluated:** 2026-09-03 (main thread) · triage rank_score 65 · /apply Step 1 score **57/100**

## Eligibility Gate: FLAG — proceed with a hard caveat, ITAR is the open question

Quoted from the posting: *"Successful candidates must obtain and hold security clearance at the reliability status level, and pass security assessment for the Controlled Goods Program (CGP) and ITAR."*

- **Reliability status** is Canada's lowest security screening level and is **available to permanent residents**, not citizenship-gated. Nishal (Canadian PR) can pursue it; his mostly-international recent background (Italy 2021-2025, Sri Lanka, UK) may lengthen the check but does not disqualify a PR.
- **Controlled Goods Program (CGP)** requires a personal security assessment; PRs can be assessed and registered. Not a citizenship gate.
- **ITAR** is the real barrier. ITAR restricts access to US-controlled technical data to "US persons" (US citizens / US permanent residents / certain protected persons) unless a specific license or Technical Assistance Agreement names the individual. Nishal is a **Sri Lankan citizen and Canadian PR** — not a US person. MDA would need to either scope him out of ITAR-controlled work or obtain authorization naming him. Many Canadian aerospace firms accommodate dual/third-country nationals through their TAAs, but for some roles it is a hard blocker.

**Per the framework, a clearance requirement leans FAIL unless verified.** Reliability + CGP are PR-accessible, so this is not a clean FAIL — but the ITAR condition means **Nishal should ask MDA directly whether a non-US-person Canadian PR can be accommodated for this role before investing heavily.** Scored below as a FLAG (role scored, caveats prominent); treat the ITAR answer as gating in practice.

## Language Gate: PASS
"Strong written and verbal communication skills in English and/or French" — English suffices ("Works with Ontario head office staff, English-speaking customers"). Fluency in French is only "nice to have". Nishal: English Native/C2. No flag.

## Scored Dimensions

| Dimension | Score | Notes |
|-----------|-------|-------|
| Technical Skills (30%) | 58 | Direct: prototyping/deploying ML on embedded targets, **Raspberry Pi named explicitly** (RPi 5); strong Python; TensorFlow (embedded deployment) and PyTorch; production-quality C/C++; digital-twin / simulator design to generate representative training data (his rule-based synthetic-variation generators + VAE/diffusion synthetic audio); dataset curation for train/val/test; defining metrics and evaluating model performance, robustness and resource utilization on target platforms (his benchmark methodology); embedded Linux; Git / CI-CD. Gaps: Versal / FPGA-class devices (none); **satellite communications domain** - DVB-S2X, 5G NTN, IP routing, SDN, cognitive radio, anti-jamming (none); RF systems and signal-processing fundamentals as they apply to comms (his DSP is audio, not RF); CUDA / GPU optimization (light); "10 years embedded software development" as a discipline (his embedded is edge-ML deployment, not a decade of embedded SWE); reinforcement learning (light). |
| Experience Match (25%) | 48 | This is a senior **architect + technical lead** role: "the single accountable architect for AI", leading the full AI/ML lifecycle, defining the technical roadmap, mentoring, driving technical decisions, targeting an initial deployment within a year. Nishal has edge-ML deployment, benchmark methodology, and some mentoring (MAS group-wide training, PhD student supervision), but not architect-level embedded-systems leadership, not 10 years of embedded software development, and no satellite / RF / comms domain. Pure lead/architect tracks are a stated growth area for him (IC-focused). |
| Behavioral Fit (15%) | 58 | The mission (AI in space, AURORA software-defined satellites) is genuinely inspiring and the "purpose-driven, collaborative dream team" framing appeals. But it is a single-accountable-architect lead role (his growth area, not his core), inside a 4,000-person public aerospace company with reliability/CGP/ITAR process overhead. High ownership (good), high process (friction). |
| Location | PASS | Sainte-Anne-de-Bellevue, QC (Montreal West Island) - Canadian; relocation within Canada acceptable per profile, Montreal carries the McGill CIRMMT tie. Note the clearance/ITAR overlay above. |
| Career Alignment (30%) | 62 | Up: embedded / edge AI is his target domain; "AI in space" is a high-impact adjacent field; an architect / technical-lead title is a step toward seniority; permanent aerospace role. Down: it is a **lead / architect** role (his stated growth area, not core - he is IC-focused); satellite comms / RF is a domain pivot away from audio / real-time ML; and the whole thing is contingent on the ITAR question resolving. If the space mission excites him and MDA confirms ITAR is not a blocker, this could be a genuinely energising stretch; if not, it is moot. |

**Overall: 57/100** (0.30·58 + 0.25·48 + 0.15·58 + 0.30·62 = 17.4 + 12.0 + 8.7 + 18.6)

## Verdict: Moderate Fit

Triage scored 65; the deep read drops it to 57 because the architect/technical-lead level, the "10 years embedded software development" bar, the satellite-comms/RF domain pivot, and the ITAR overlay all weigh heavier at close range.

## Key Strengths
- Prototyping and deploying ML on embedded targets, Raspberry Pi named in the posting: 14 ms inference on a Raspberry Pi 4 at 31.4% CPU, F1 0.76, 74x faster than the DTW baseline (JAES 2026).
- Designing to embedded compute / power / memory / latency constraints and evaluating model performance, robustness and resource utilization on target platforms - his benchmark methodology (frozen protocols, ablations, negative-results record) is exactly this.
- Digital-twin / simulator design to generate representative training data: rule-based synthetic-variation generators (~10k per pattern), VAE- and diffusion-based synthetic audio for low-label regimes.
- Dataset curation for train / validation / test: four open Zenodo datasets, 9,800+ recordings, 70+ participants, with frozen evaluation protocols.
- Strong Python; TensorFlow (embedded) + PyTorch; production C/C++17; embedded Linux; Git + CI/CD.
- PhD (nice-to-have), publications, reviewer/PC service; some mentoring and technical-training experience.

## Gaps to Address
- **ITAR / security clearance:** the gating question. Ask MDA whether a non-US-person Canadian PR can be accommodated for this role. Express willingness to obtain reliability status and complete CGP; do not overclaim on ITAR.
- **Architect / technical-lead level + "single accountable architect":** a leadership role in a growth area for him. If applying, frame the edge-ML-deployment ownership, roadmap thinking (phased ground-to-onboard), and mentoring honestly; be clear he is stepping up into a lead role, not claiming a decade of it.
- **10 years embedded software development:** his embedded work is edge-ML deployment, not a decade of embedded SWE. Frame the depth he does have (RPi/ARM production, C++17 real-time engines, embedded Linux) without inflating the tenure.
- **Satellite communications / RF domain:** DVB-S2X, 5G NTN, cognitive radio, anti-jamming, IP routing, SDN - all new. His audio DSP and S-transform work is signal processing but not RF/comms. Frame the signal-processing and time-series-prediction fundamentals as transferable (network-traffic prediction is a time-series problem), and the comms specifics as a domain to learn.
- **Versal / FPGA, CUDA / GPU optimization:** light to none.

## Cover Letter — Special Instructions
None imposed, but the posting raises prerequisites that the letter should address per writing-style rule (security-clearance willingness): state willingness to obtain reliability status and complete the CGP assessment. On ITAR, do not pre-emptively disqualify in the letter - raise it as a question in the application conversation instead. Lead with the embedded-ML-deployment + digital-twin + benchmark-methodology core; frame network-traffic prediction as a time-series problem he is equipped for; be honest that satellite comms and the architect-lead scope are a step up.

## Recommendation
**Apply only if the space mission genuinely excites him AND he is willing to front-load a direct question to MDA about ITAR accommodation for a non-US-person PR.** Otherwise hold. The edge-ML-deployment + digital-twin + benchmark core is real, but this is a Moderate Fit: an architect/technical-lead role (his growth area), in a new domain (satellite comms/RF), gated on an ITAR assessment that may not clear for a Sri-Lankan-citizen Canadian PR. Draft produced per the batch request; the ITAR question should be resolved before submitting.

## Company Research Checklist
- [x] Website - MDA Space, ~55-yr heritage, robotics + satellite systems + geointelligence, ~4,000 staff (CA/US/UK). Satellite Systems (Montreal) = antennas/payloads/electronics for comm & radar sats; AURORA software-defined satellites.
- [x] Reviews - heavy compliance context (reliability status, CGP, ITAR); Jira/Confluence; competitive comp, no band disclosed.
- [x] Media - TSX:MDA; lunar infrastructure, Earth observation, satellite comms positioning.
- [x] Written to `company_research/mda-space.json` (with the ITAR caveat in network_contacts_note).
