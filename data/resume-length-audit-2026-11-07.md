# One page or two? Resume length study, audit, and per-role choice

Prepared 2026-11-07. Covers the 81 unapplied roles in `data/unified-tracker.md` (committed version, max IDs: career-ops 1733, ai-job-search 1743).

**The two documents compared**

| | **Golden (2-page)** | **One-page (layout C)** |
|---|---|---|
| File | `resume_generic/Nishal_Silva_ML_Research_Engineer.pdf` | `resume_generic/one_page/Nishal_Silva_1page.pdf`, which is **only on the unmerged branch `origin/claude/magical-thompson-mkbsrp`** (commit `68afc0a`). It is not on `main` or on this branch yet |
| Words | 888 (418 of them on page 1) | 518 |
| Body type | 11pt Times, about 0.7in margins | 10pt Charter, 0.40-0.55in margins |
| Track record | All of the 2026 interviews came from it or light edits of it: Jumio screen, Zebra (1173), Amii/ZeroKey, SciNet | Built 2026-11-06. **Never sent.** No outcome data |

---

## 1. Evidence on the "one page" thesis

### Evidence FOR one page

| Source | What it says | How strong it is |
|---|---|---|
| Ladders eye-tracking study (2012 and 2018) | Recruiters spend about 6-7.4 s on a first pass and look mostly at titles, employers and dates near the top | Weak to moderate. A commercial study with a small, undisclosed sample and thin methods. The *direction* (a fast, top-heavy first scan) is widely accepted, though, and it argues for front-loading more than for a page limit |
| Laszlo Bock (Google SVP People Ops, 2014) | "One page of resume for every 10 years of work experience" | Expert opinion from a high-volume tech hirer. At 10+ years it actually allows about 1-2 pages |
| Gayle Laakmann McDowell (ex-Google/Microsoft/Apple engineer, *Cracking the Coding Interview*) | One page. A second page by definition adds your weaker material | Expert opinion, and the dominant view in **US big-tech SWE/MLE** culture |
| Accountemps (2007 survey) | 52% preferred one page for **staff-level** roles | Old. Dropped to 46% by 2018 |
| Logic | A forced cut removes weak lines and thin-evidence keywords, so each line carries more weight. Fewer claims you can't defend in an interview | Real, and visible in your own one-pager (see §2) |

### Evidence AGAINST one page (for two)

| Source | What it says | How strong it is |
|---|---|---|
| ResumeGo (2018), simulated hiring in which recruiters and hiring managers made 7,712 picks from an even split of 1- and 2-page résumés | 2-page résumés were chosen 2.3x as often overall (about 70% of picks), and 1.4x as often even at entry level. Rated 8.6/10 against 7.1. Reviewers spent 4m05s on 2-page résumés against 2m24s on 1-page | The largest study, but a simulation run by a résumé company. The 2-page versions contained *more content*, so length and substance are confounded |
| Accountemps / Robert Half (2018) | Executive roles: 50% find two pages acceptable, only 21% prefer one. Staff roles: 47% two pages against 46% one | Moderate. A large staffing firm, survey data |
| Accountemps (2007) | Executive roles: 61% preferred two pages, 7% preferred one | Moderate, old |
| Canadian norm (settlement.org, Canadian college career offices, Monster CA) | 1-2 pages is standard. **Two pages is normal at 10+ years.** Research/academic roles can run to 3 | Consistent across sources. This is your market |
| JHU, Cheeky Scientist and other PhD-to-industry advice | Industry résumé of 1-2 pages, with research impact and *selected* publications. A full CV goes only to academia | Advice consensus |
| ATS mechanics | Page count isn't penalized. Parsers read all the text, and recruiters run Boolean keyword searches over your parsed profile, so more *legitimate* terms means more hits. The one-pager drops 20 golden terms (§2) | Moderate. Vendor blogs, but it matches how Workday, Greenhouse and Lever search works. One claim that ATSs read only page 1 is unsourced; disregard it |
| **Your own data** | 90 applications and about 4-5 interview-stage outcomes, all from the 2-page golden | Strongest *for you*, but there was no 1-page arm, so it shows the golden *works*, not that it beats a 1-pager |

### Verdict on the thesis

"Always one page" is **not supported** for someone with a PhD, 10+ years and research output in Canada. The stronger evidence (Canadian norms, the senior/executive surveys, ResumeGo despite its flaws, and your own outcomes) leans toward two pages being fine or better. The one-page argument is real in two places:

1. **High-volume industry engineering screens** (MLE/SWE/DSP at tech companies and startups), where the reader is a recruiter or founder skimming in seconds and tech culture favours one page.
2. **Cases where page 1 of the 2-pager is the wrong page 1.** That is a real problem with the golden (see §2).

So the right answer is **role-dependent**, not universal. That is what §3 does.

**Can you A/B test it?** Not conclusively. Your response rate is about 5%. Telling 5% apart from 10% at 80% power takes roughly 430 applications per arm. Track a `resume_version` field anyway so a trend can show up, but decide by reasoning and don't wait for statistical significance.

---

## 2. Full audit of both documents

### Golden (2-page)

**What works**
- Proven: it produced every interview you've had.
- Broad keyword coverage: about 20 terms the one-pager lacks (Signal Processing spelled out, Embeddings, Transfer Learning, NLP, Recommender/Ranking, Experimental Design, Technical Writing, Team Leadership, Cross-Functional, Unit Testing, Librosa, SciPy, JAX).
- The "Canadian Permanent Resident · Eligible to work without sponsorship" line is under the name.
- Selected publications (JAES 2026, IEEE IS² 2025) are named, which research scientist screens look for.

**Problems**
1. **Page 1 ends inside the Trento postdoc.** MAS (5.5 years, your biggest industry impact and the 300% figure) and Forestpin both fall on page 2. A 7-second skim of page 1 reads as *academic researcher*. This hurts on every industry MLE/CV/FDE role, and it is the strongest argument for the one-pager.
2. **Thin-evidence competencies** (Recommender Systems, Ranking, Multi-Tenant ML, AI Ethics, Prompt Engineering, JAX, C#). These are interview liabilities if a screener probes them.
3. Generic filler: "Skilled at working with product, data, and engineering teams…", the third awards bullet, and the "Coordinated with academic and industry partners" bullet. They carry no numbers.
4. Few concrete results. Only <30ms, >90% F1 and 300% appear. The stronger ones (99.5% inspection-time cut, Promptly in 4 countries, ROC-AUC 0.822, F1 0.78) are missing.
5. Mechanical issues: a trailing comma after "ONNX,", en-dashes in dates (the recruiter-outreach build already switched to ASCII hyphens for ATS date parsers), no GitHub link, and a full postal code.

*(Per CLAUDE.md the golden PDF itself is never edited. These issues are listed so per-role copies can work around them, e.g. reordering MAS higher is an allowed "reorder" edit.)*

### One-page (layout C)

**What works**
- **The whole career is visible on one page**, MAS included. This fixes the golden's biggest weakness.
- Better evidence per line: 99.5% inspection cut, Promptly, ROC-AUC 0.822 over 100k trials, F1 0.78, LoRA multi-GPU, the 4-user audio/EEG/MR sync pipeline, and the Forestpin SQL+Python scoring services.
- Thin-evidence terms removed, so less interview risk.
- A clean single column, ASCII dates, a GitHub link and a bullet pool in the README for one-for-one swaps.

**Problems**
1. **The Canadian PR line was removed. Restore it (high priority).** Your experience is in Sri Lanka, Italy and the UK. Toronto field experiments (Oreopoulos 2011, about 13,000 résumés) found that foreign experience significantly cuts callback rates. Recruiters who see only foreign employers may assume you need sponsorship *before* they ever reach the application-form question. Recruiter emails, agency submissions and referrals have no form at all. It costs one line, which can come from the second Awards line.
2. **"Signal Processing" isn't spelled out** (only "DSP"). ATS exact-match searches on SP roles (SubPac, Waabi 717, Huawei, ESS, Evertz) will miss it. Change the specialty to "Signal Processing (DSP)".
3. **No room left.** The README admits only about 3-6 lines of slack, at 10pt with 0.40in bottom margins, which is already the floor for legibility. Every tailoring is strictly one-for-one.
4. No named publications. That's fine for industry, but it's a gap for research scientist roles.
5. The first role's bold "employer" line is "Open Source / MUSMET external collaborator", which reads oddly as an employer name in the employer-first layout. Consider "Independent Researcher (Open Source)".
6. Not yet merged. It lives only on `claude/magical-thompson-mkbsrp`.

---

## 3. Per-role recommendation (all 81 unapplied roles)

**Decision rules used**
- **1P (one-page)**: industry engineering roles (MLE / SWE / DSP / FDE / applied DS) at tech companies or startups, where the reader is a fast-skimming recruiter or founder and MAS/industry proof must be on page 1.
- **2P (golden 2-page)**: research scientist/researcher titles, senior-staff and staff levels, big Canadian banks and large traditional HR (Canadian 2-page norm, Workday keyword search), agency recruiters (who re-pitch you and want detail), and JDs whose keywords sit in the golden-only set.
- **CV**: academic posts get the full academic CV (`ai-job-search/cv/academic_cv_nishal_silva.tex`), not either résumé.
- **Skip**: out of scope (outside Canada), posting gone, or score <50. Don't spend résumé effort on these.
- "Pair exists" = a golden-derived 2-page pair is already in `resumes/`. For a 1P call, build a 1P version from the one-page base before sending.

### Actionable roles (score ≥ 55, in scope, live or unverified)

| ID | Company / role | Score | Use | Why | Pair exists |
|---|---|---|---|---|---|
| 1464 | SubPac, Senior DSP Engineer | 80 | **1P** | Music-hardware startup, hands-on DSP. Lead with the Nebula C++17 and Raspberry Pi latency bullets from the pool. Must spell out "Signal Processing" | no |
| 1463 | York U, Asst. Prof. Music Tech (deadline **11-18**) | 76 | **CV** | Tenure-track: academic CV + statements in a single PDF | no |
| 1092 | Vector Institute, Distinguished Postdoc (cutoff 2027-02-28) | 76 | **CV** | Academic fellowship: full CV + research statement | yes (2P) |
| 618 | Audimee, Audio ML Engineer | 74 | **1P** | Small Swedish startup and the founders read it. Swap in the MusicGen/LoRA bullet | yes (2P) |
| 1466 | Lenbrook, Sr Software Developer (BluOS) | 72 | **1P** | Product SWE. C++/embedded audio upfront | no |
| 1450 | Ideogram, Applied MLE | 72 | **1P** | Gen-media startup. The one-pager already carries LoRA multi-GPU | yes (2P) |
| 1117 | Wave HQ, MLE | 72 | **1P** | Generic MLE pipeline role. Needs MAS/Forestpin on page 1 | yes (2P) |
| 1122 | Nexxa.AI, Applied AI Eng (FDE) | 72 | **1P** | Client-delivery FDE. The 99.5% and Promptly results are exactly the proof needed | yes (2P) |
| 717 | Waabi, Sr/Staff SWE Onboard Algorithms | 72 | **1P** | Performance engineering. C++17/ARM latency and real-time inference. Staff level is borderline 2P, but the JD is engineering-first | yes (2P) |
| 1116 | Extreme Networks, Sr DS (GenAI/ML), research lead | 70 | **2P** | Greenfield research-strategy lead. Wants breadth, leadership and publications | yes (2P) |
| 1119 | Stratum AI, FDE MLE | 70 | **1P** | Startup FDE, custom PyTorch, client delivery | yes (2P) |
| 1115 | Affirm, Sr MLE (Fraud) | 69 | **1P** | Industry MLE. The one-pager's Forestpin SQL+Python anomaly-scoring bullet beats the golden's | yes (2P) |
| 631 | Tubi, Sr MLE | 68 | **2P** | Recommender-heavy JD. The terms Recommender/Ranking/Embeddings exist only in the golden | yes (2P) |
| 1722 | GuruLink (agency), Sr MLE | 68 | **2P** | Agency recruiters re-pitch candidates and want the full detail | yes (2P) |
| 1735 | Huawei Canada, Researcher Speech & Acoustic AI | 68 | **2P** | Research title that screens on publications | yes (2P) |
| 1733 | IBU, Faculty MSc AI | 68 | **CV** | Faculty package: CV + teaching statement + research plan | no |
| 1467 | ESS Technology, Sr Embedded DSP | 68 | **1P** | Firmware/DSP engineering. Spell out "Signal Processing" | no |
| 1306 | Helm.ai, MLE | 68 | **1P** | AV startup MLE (read the JD manually first) | no |
| 1133 | XYZ Reality, Sr AI/CV Engineer | 68 | **1P** | Startup CV engineering. Industrial CV (MAS) on page 1 | no |
| 681 | Waabi, Sr/Staff Perception Engineer | 67.5 | **2P** | Staff level, and Waabi is a research-led org that values publications and benchmark rigour | yes (2P) |
| 1470 | Ubisoft, Sr Audio Programmer | 66 | **1P** | Game-audio engineering | no |
| 1472 | Mission.dev, Sr C/C++ Audio Dev | 66 | **1P** | Low-latency engineering. Swap in the MIRaaS UDP bullet | no |
| 715 | Waabi, Sr SWE Evaluation Infra | 66 | **1P** | Engineering role. Benchmark-suite bullet first | no |
| 1126 | AutoTrader.ca, Sr Data Scientist | 64 | **1P** | Product DS. Industry results first | yes (2P) |
| 1132 | Nexxa.AI, Backend AI Engineer | 64 | **1P** | Backend SWE | no |
| 690 | Klue, Sr SWE AI (Agents) | 64 | **1P** | Startup SWE | no |
| 1179 | Altis Labs, Sr ML Scientist | 63 | **2P** | Scientist title. VAE/diffusion and benchmark rigour plus publications | yes (2P) |
| 1100 | Picovoice, Deep Learning Researcher | 62 | **2P** | Researcher title. Publications and benchmarks are the selling point | yes (2P) |
| 1230 | Huawei Canada, Sr Researcher Edge AI (Edmonton) | 62 | **2P** | Research title; thesis-aligned | yes (2P) |
| 1232 | Cerence, Sr App Developer Voice AI Edge | 62 | **1P** | Application engineering. Edge latency bullets | yes (2P) |
| 1671 | Sixone, Applied Research Scientist | 62 | **2P** | Research-scientist title. Breadth covers the spectroscopy gap | yes (2P) |
| 1691 | Lyft, ML SWE Routing | 62 | **1P** | US big-tech SWE culture favours one page | yes (2P) |
| 1711 | lululemon, Staff Applied AI/ML Scientist | 62 | **2P** | Staff + scientist | yes (2P) |
| 1717 | TD Layer 6, MLE | 62 | **2P** | Layer 6 is research-led and publication-aware, and the bank uses Workday. Matches the 2P recruiter-outreach resume already sent there | yes (2P) |
| 1723 | Scotiabank, DS AI & ML | 62 | **2P** | Canadian bank: 2-page norm and Workday keyword search. Make sure the PR line is present | yes (2P) |
| 1473 | Stingray, SW Developer (Applied AI) | 62 | **1P** | SWE | no |
| 1454 | Samsara, Data Engineer | 62 | **1P** | DE role. The ETL/IoT bullets from MAS on page 1 | no |
| 1073 | Waabi, Research Eng Sim Assets | 62 | Skip | Already marked "recommend against" | no |
| 1184 | Stryker, Staff Engineer CV | 60 | **2P** | Staff + medtech (a regulated, traditional HR process). Restore the GMOA vitals detail | yes (2P) |
| 1186 | Stingray, AI Software Developer | 60 | **1P** | SWE. MIRaaS + datasets | yes (2P) |
| 1187 | TD, MLE II | 60 | **2P** | Canadian bank norm. Forestpin anomaly work | yes (2P) |
| 1674 | Ubisoft Montreal, Sr C++ Programmer ML | 60 | **1P** | C++ engineering | yes (2P) |
| 1469 | Adamson, Firmware Engineer | 60 | **1P** | Firmware (low priority) | no |
| 718 | Waabi, Sr/Staff ML Optimization (Onboard) | 60 | **1P** | Performance engineering | no |
| 649 | Cohere, MTS Evals | 60 | **2P** | Research-lab MTS. Benchmarks/ablations and publications | no |
| 1108 | Waabi, Research Scientist | 59 | **2P** | Research scientist | yes (2P) |
| 1471 | Behaviour, Sr Audio Programmer | 58 | **1P** | Game audio (low priority) | no |
| 1474 | Ross Video, Sr SW Dev Audio | 58 | **1P** | SWE (check eligibility first) | no |
| 1448 | Evertz, DSP Engineer | 58 | **1P** | DSP engineering (low priority, overqualified) | no |
| 1309 | Waabi, Staff Systems Eng Safety | 56 | Skip | Not an ML role | no |
| 1672 | Huawei Canada, Sr Researcher CV | 55 | **2P** | Research title | yes (2P) |
| 1716 | lululemon, AI/ML Engineer | 55 | **1P** | Mid-level MLE | yes (2P) |
| 1737 | Spotify, RS Generative Audio | 55 | **2P** | Research scientist; publications (JAES/ISMIR-adjacent) | yes (2P) |

### Low-fit, still listed (only if you decide to apply)

| ID | Company / role | Score | Use | Note |
|---|---|---|---|---|
| 1212 | EA SPORTS, Audio SWE UFC | 52 | 1P | Pair exists (2P) |
| 1307 | Waabi, AI Tooling | 52 | Skip | |
| 1734 | Amii, Applied Research Scientist | 51 | 2P | Research; Amii values publications |
| 1739 | Kinaxis, Sr Staff Applied Scientist | 48 | 2P | Senior staff. Pair exists |
| 1741 | Amazon, AS II Alexa | 42 | 2P | Amazon AS screens value publications. Pair exists |
| 1742 | Amazon Canada, Applied Scientist | 40 | 2P | Pair exists |
| 1414 | Queen's, CRC Chair | 48 | CV | The existing pair is already 4 pages (academic). Score says skip |
| 1461, 1457, 1459, 1456, 1308, 1311, 1460, 1426, 647 | various | 30-48 | Skip | Below threshold or wrong role family |
| 1447, 1421, 1435, 1436, 1420, 1422, 1445, 1438 | non-Canada | n/a | Skip | Out of scope per `_profile.md` |
| 1045, 1048, 1051, 1634 | removed/closed, or not an archetype | n/a | Skip | |

### Tally (actionable roles only)

- **1P: 30 roles**, mostly engineering and startups. 13 of them already have a 2P pair (618, 717, 1115, 1117, 1119, 1122, 1126, 1186, 1232, 1450, 1674, 1691, 1716), so they need a 1P rebuild.
- **2P: 18 roles**, research/scientist titles, staff level, banks, agencies, and the recommender-heavy Tubi role. All 18 except 649 already have a golden-derived pair in `resumes/`.
- **CV: 3 roles**: York (due **2026-11-18**), Vector (2027-02-28), IBU.

---

## 4. Recommended next steps

1. **Merge the one-page base** from `claude/magical-thompson-mkbsrp` into this pipeline, then fix it: restore the PR line, spell out "Signal Processing (DSP)", and rename the first role's employer line.
2. **Add the one-page base to the golden resume rule as a second base**, not a replacement. 1P copies follow the same minimal-edit discipline, starting from the one-page base. The rule in CLAUDE.md currently names only the golden, so this needs your sign-off.
3. **For 2P roles, keep the golden but reorder** so MAS isn't stranded on page 2 where it matters (allowed as "reorder bullets"). For example, move the summary's results sentence up and trim the thin-evidence competencies.
4. **Log `resume_version` (1P/2P)** on every application from now on. It can't prove anything at this volume, but it will show a lopsided trend if there is one.
5. York (1463) is the nearest deadline (11 days) and needs the academic CV, not either résumé.

---

## Sources

- ResumeGo one- vs two-page study, via [CNBC](https://www.cnbc.com/2018/12/19/resumego-hiring-managers-prefer-candidates-with-two-page-resumes.html), [ERE](https://www.ere.net/one-or-two-page-resumes-best/), [Dice](https://www.dice.com/career-advice/two-page-one-page-resume-okay-tech-recruiters), [ClearanceJobs](https://news.clearancejobs.com/2018/12/14/are-one-page-resumes-dead/) (original: [resumego.net](https://www.resumego.net/research/one-or-two-page-resumes/), which this session couldn't fetch)
- Ladders eye-tracking: [study PDF](https://csuglobal.edu/sites/default/files/blog-files/theladders-eyetracking-studyc2.pdf), [HR Dive](https://www.hrdive.com/news/eye-tracking-study-shows-recruiters-look-at-resumes-for-7-seconds/541582/), critique at [ERE](https://www.ere.net/articles/is-the-6-second-resume-scan-a-myth)
- Laszlo Bock: [Business Insider](https://www.businessinsider.in/Google-HR-Boss-Says-This-Is-The-Ideal-Length-For-A-Resume/articleshow/44020547.cms), [The Muse](https://www.themuse.com/advice/5-huge-resume-mistakes-googles-head-of-hr-sees-all-the-time)
- McDowell: [Fortune](https://fortune.com/2014/10/02/how-can-i-get-my-resume-shortlisted-by-google-for-a-software-engineer-job), [Quartz](https://qz.com/644508/less-is-more-a-top-hiring-expert-on-how-to-create-the-best-resume)
- Accountemps: [PlanSponsor (2007)](https://www.plansponsor.com/execs-say-longer-resumes-acceptable/), [Reliable Plant](https://www.reliableplant.com/Articles/Print/5362?id=5362), [Newswire CA (2018)](https://www.newswire.ca/news-releases/36-per-cent-of-canadian-workers-plan-to-look-for-a-job-in-2018-669856363.html)
- Canadian norms: [settlement.org](https://settlement.org/ontario/employment/find-a-job/resume/how-do-i-create-a-canadian-style-resume), [NIC](https://nic.bc.ca/about-us/nic-news/news/how-many-pages-should-my-resume-be), [Monster CA](https://www.monster.com/career-advice/resume/canadian-resume-format)
- PhD-to-industry: [JHU Imagine](https://imagine.jhu.edu/resources/how-to-write-effective-resumes-and-cvs-for-doctoral-students-and-postdocs/), [Cheeky Scientist](https://cheekyscientist.com/guide-to-writing-a-professional-resume/)
- ATS and length: [CVOwl](https://cvowl.com/blog/ats-resume-length:-one-or-two-pages), [HireFlow (the unsourced page-1 claim)](https://hireflow.net/blog/why-your-ats-score-drops-when-you-add-a-second-page)
- Immigrant résumé field experiment: Oreopoulos, P. (2011), "Why Do Skilled Immigrants Struggle in the Labor Market? A Field Experiment with Thirteen Thousand Resumes," *AEJ: Economic Policy* 3(4), cited from memory and not re-fetched this session
