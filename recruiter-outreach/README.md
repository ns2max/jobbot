# Recruiter cold outreach: tailored resumes

Source list: `recruiters.csv` (38 contacts, researched 2026-10-29). Resumes were made only for the
**19 contacts with a published email address** (18 resumes, since Fetch's two founders share one), ordered by relevance to Nishal's field and by the CSV's priority.
The 19 contacts reachable only through LinkedIn or by phone were skipped (listed at the bottom).

Every resume is the **golden generic resume with minimal edits** (golden resume rule). Each folder holds:

- `Nishal_Silva_Resume.pdf`: the file to attach (compiled, 2 pages)
- `Nishal_Silva_Resume.tex`: source
- `Nishal_Silva_Resume.txt`: the text an applicant tracking system (ATS) would extract
- `CHANGES.md`: every edit made to the golden resume, plus a pass/fail verification list

To rebuild everything: `python3 recruiter-outreach/build_resumes.py`.

## Edits applied to all 18 resumes

1. The golden ">90% F1" wording is kept unchanged in the summary and the postdoc bullet (confirmed real 2026-11-03).
2. Date ranges use an ASCII hyphen instead of an en-dash, because some ATS date parsers break on en-dashes.
3. Line spacing went from 1.05 to 1.03, so the small additions still fit the golden 2-page layout.
4. Where relevant, the PR status line gets a location note, for example "Open to relocation to Montreal".

## Send list (in recommended order)

| # | Folder | Organization | Send to | Variant | Why this tailoring | Caveat before sending |
|---|---|---|---|---|---|---|
| 1 | `01_luxtronic` | LuxTronic | contact@luxtronic.ai (James C. Evans) | Industrial CV (V5) | AI Systems Engineer role: industrial CV, edge devices, cameras, PLC, Docker/Linux. The closest fit on the list | Confirm the role is still open, and whether it's employee, contractor or employer-of-record; ask about Canadian payroll |
| 2 | `02_bluewrist` | Bluewrist (Markham) | jobs@bluewrist.com | Industrial CV (V5) | Inspection + camera integration + production CV at MAS | Don't claim advanced 3D vision or calibration |
| 3 | `03_novarc-technologies` | Novarc (Burnaby) | careers@novarctech.com | Industrial CV (V5) + Vancouver | Vision + closed-loop control of factory machinery (Promptly, PLC/C++) | No specific ML vacancy confirmed; ask about vision/ML roles |
| 4 | `04_aavaa` | AAVAA (Montreal) | info@aavaa.com | Audio / DSP (V4-lite) + Montreal | Acoustic ML, embedded audio, McGill tie | Listings are undated. Don't claim EEG modelling or speech enhancement. Address the team, not a named founder |
| 5 | `05_layer6-td` | Layer 6 / TD | career@layer6.ai | Applied ML: anomaly/finance (V1) | Anomaly detection first; adds the Forestpin production scoring-service bullet | You've already applied to TD roles. Cite the requisition numbers and keep it to one thread |
| 6 | `06_fetch-recruiters` | Fetch Recruiters | alexia@fetchrecruiters.com | Applied ML (V1), CV term moved up | Firm places senior ML + CV specialists | Email **Alexia only**. Carlos (carlos@fetchrecruiters.com) is the fallback for the same resume; never email both at once |
| 7 | `07_mac-recruitment` | MAC Recruitment | hello@macrecruitment.ca (attn. Morgan Rich) | Signal ML + embedded hardware | MedTech / deep-tech product development: signal ML plus the Embedded & Hardware stack line | Shared inbox; permanent roles only |
| 8 | `08_groom-associates` | Groom & Associates | emily.woods@groomassocies.com | Applied ML (V1) + Montreal | Places AI/ML candidates; was previously at LANDR (audio overlap is good for the email) | Emily is on the contract desk; ask about routing to permanent tech roles |
| 9 | `09_goldbeck-recruiting` | Goldbeck (Vancouver) | reiniell@goldbeck.com | Industrial CV (V5) + Vancouver | Covers tech, manufacturing and life sciences | Ask about Canadian roles |
| 10 | `10_oncoustics` | Oncoustics | founders@oncoustics.com | Real-time signal ML | Raw-signal ML transfer; the BCI/EEG sync pipeline; hospital-deployed vitals system | Senior listing wants 5+ years of healthcare ML. Frame as research engineer; make no ultrasound or FDA claims |
| 11 | `11_soundskrit` | Soundskrit (Montreal) | contactus@soundskrit.ca | Audio / DSP (V4-lite), C++ first | Audio DSP, embedded C++ | General inbox; ask to be routed to the software team. Don't claim beamforming or mic arrays |
| 12 | `12_canny-vision` | Canny Vision | contacts@canny.vision | Industrial CV (V5) | Edge CV, C++ | Speculative only; the page says there are no open positions |
| 13 | `13_gurulink` | GuruLink | info@gurulink.ca | Applied ML (V1) | Staff AI Engineer listing (Toronto) | Screen out LLM/chatbot-only roles |
| 14 | `14_stack-it-recruitment` | STACK IT | info@stackitrecruitment.com | Applied ML (V1) | Data & AI desk, national coverage | No matching mandate checked |
| 15 | `15_10-percent-recruiting` | 10 Percent (AB) | hello@10pr.ca | Applied ML (V1) + Alberta | Explicit AI/ML recruiting practice | Would mean relocating to Alberta |
| 16 | `16_hays` | Hays | casey.thompson@hays.ca | Applied ML (V1), unchanged golden | General tech recruiter | Not an ML specialist desk |
| 17 | `17_vanjobs` | VANJOBS | mark@vanjobs.ca | Edge / embedded (V3) + Vancouver | Technical R&D + sensing product development | **Mark asks for the vanjobs.ca portal first.** Upload there rather than cold-emailing |
| 18 | `18_kovasys` | Kovasys | talent@kovasys.com | Applied ML (V1) + relocation | National tech recruiting | The email comes from a 2020 page and may be stale; the resume portal is safer |

## Skipped: LinkedIn or phone only (no published email)

Gary Hinde (IQ PARTNERS), Sarah Doughty (TalentLab), Sean Huynh (Solara Talent), Kasturi Deval, Nicole Galloway and
Avery MacArthur (RBC Borealis), Brian K., Guangwei Yu, Satya Krishna Gorti and Anthony Caterini (Layer 6 / TD),
Julia Geisler and Frits Bigham (Waabi), Riad Bazzo (Cerebras), Sakshi Srivastava (Bell), Akash J. (Sanctuary AI),
Aisling Lane (Clarius), Shirley Chan (Audiokinetic), Tommy Desilets (LANDR), Adam Hassoulas (Groom; Emily covers that firm).

## Notes

- The live careers pages couldn't be re-checked from this session because the network sandbox blocks those domains.
  The tailoring relies on the CSV's 2026-10-29 research. Check that the vacancy is still live before sending.
- Nothing has been sent. Update `Outreach_status`, `Date_sent` and `Follow_up_date` in `recruiters.csv` as you go.
