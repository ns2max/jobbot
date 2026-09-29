<!-- Job posting: https://jobs.lever.co/kogniz/60f760bd-5b0a-4a07-a650-bfac4ff644f8 -->

# 1111 Kogniz — CV + Cover Letter Changelog (2026-09-03)

Pipeline: main-thread eval (60/100 borderline) → Fable draft → main-thread review + compile + trim + verify. Codex exhausted until Oct 3.

> **Priority note:** the eval recommends this as a **low-priority apply, or better a senior-role outreach** — the posting is scoped at 1-2 years and Nishal is a PhD with ~11. `career-ops` independently scored the same posting (its #1111) 2.7/5 SKIP with the same recommendation. Drafts produced per the batch request; Nishal should decide whether to send.

## CV — `cv/1111_main_kogniz_machine_learning_engineer.tex`
- **Variant V1 (AI-Industry, default).** Tagline `Machine Learning Research Engineer | Deep Learning, Time-Series, Pattern Detection | Applied ML` (byte-identical in cover). V1 keeps the PhD and full record visible while leading with model training + deployment, C++/Python and CV breadth.
- Summary leads with: trained and deployed deep neural networks with **measured, published improvement over baseline** (the JAES 2026 detector — 14 ms on RPi4, F1 0.76, 74x faster than the DTW baseline), then MAS production computer-vision inspection (99.5% / 300%), then C++17 + Python "especially as applied to ML frameworks" and the theory/motivation behind architectures via 10+ papers.
- Framework stack: TensorFlow, Keras, PyTorch + **"conceptually familiar with YOLO/Darknet-family detectors"** — no Caffe / DLib / Torch / Darknet hands-on claim (the JD's stack is legacy; he uses TF/Keras).
- **Cut for the 2-page budget:** template `\newpage`; LiveLaTeX (Portfolio → 2 items: Nebula, Hot Licks); Forestpin role (low relevance to a video-security CV role); postdoc bullet 2 trimmed (was bundling the 98% symbolic-RNN and 95% SSIM figures — kept only the 95% SSIM, labelled training-free). `\enlargethispage{3\baselineskip}` before Highlights.
- **Grounding:** all numbers verified (14 ms / F1 0.76 / 74x / 31.4% CPU / 1038 ms; F1 0.78; 95% SSIM grounded KG §13/§16; 300% / 99.5%); MAS one entry Jan 2015-Jul 2020; Promptly not mentioned (no patent risk); "10+ years" (Fable used this correctly); "two BSc thesis students" matches KG §4.1a; English only; Claude Code named.
- **Final: 2 pages.** ATS text layer clean (0 cid/replacement, email + phone literal). Every JD keyword covered: deep learning, computer vision, trained, deployed, baseline, C++, Python, TensorFlow, PyTorch, CNN, neural network, architectures.

## Cover Letter — `cover_letters/1111_cover_kogniz_machine_learning_engineer.tex`
- Plain `article`, 4 paragraphs, "Dear Hiring Manager,". **~1 page.**
- P1: trained and deployed deep-learning models with published baseline improvement (JAES 2026 detector) + MAS production CV inspection (99.5%).
- P2: the posting's requirements in its own terms — DL training + deployment with baseline improvement; C++ and Python "ins and outs" as applied to ML frameworks (his real-time C++17 inference engines); CV + CNN architectures; theory/motivation via 10+ papers; notes TF/Keras + PyTorch and fast framework pickup.
- **P3 addresses the seniority mismatch head-on:** the posting is written for 1-2 years, he is a PhD with ~11; he is drawn to hands-on CV/deep-learning delivery in a small fast-moving team, brings more than the role scopes, and would be glad to discuss where a more senior contribution fits. Then why Kogniz (AssureAI proactive safety/security CV on existing camera feeds, >3M employees covered, venture-backed, Montreal dev team) + the McGill CIRMMT tie from the 2024 visiting appointment.
- P4: PR / no sponsorship / available immediately / open to relocating to Montreal for the on-site dev team.
- AI-assisted screening disclosed — keyword coverage handled truthfully.

## Company research
- `company_research/kogniz.json` (Kogniz AssureAI; Berkeley HQ + Montreal dev team; ~USD 20.6M raised over 4 rounds; WSJ/WaPo/NBC/Fox coverage; cross-tool note: career-ops #1111 = 2.7/5 SKIP).

## Open flags for Nishal
- **Role scoped at 1-2 years — badly under-levels a PhD with ~11 years.** Consider contacting Kogniz about a senior CV role instead (both this eval and career-ops recommend it).
- Legacy framework stack (DLib, Caffe, Darknet) suggests an older codebase.
- On-site Montreal dev team — a real relocation from Toronto.
- Generic video-security-analytics domain; does not advance his edge-ML / audio / research-IC goals.
- Comp not disclosed. No stated deadline.
