# Evaluation: TDK Trusted Positioning — Sr. Embedded Software Developer (12-month fixed-term)

**Date:** 2026-09-24
**URL:** https://ca.indeed.com/viewjob?jk=fb45357d543338dc
**Archetype:** Edge/Embedded engineer (sensor-fusion algorithms → embedded C) — adjacent to Embedded ML; no ML stated
**Score:** 3.1/5
**Legitimacy:** High Confidence
**Verification:** JD read live on Indeed via Chrome 2026-09-24 (also on Job Bank #50344322, posted 2026-09-22); company careers page still says "No Current Openings"
**PDF:** pending

---

## A) Role Summary

| Field | Value |
|---|---|
| Archetype | Senior embedded software developer on a navigation R&D team |
| Domain | Sensor-fusion positioning (inertial + GNSS/Wi-Fi) for phones, wearables, vehicles, drones, robots |
| Function | Design navigation algorithms using multiple sensors; port Python/MATLAB algorithms to optimized ANSI C/C++; I2C/SPI/UART/USB/Ethernet/CAN interfaces; review schematics/PCBs/BOMs; R&D for vehicular and on-foot navigation; data tools; docs |
| Seniority | Titled "Sr." but 2+ yrs preferred — mid-level in practice |
| Remote | Hybrid, ≥3 days/week at the Calgary office — **city rank 3**; relocation from Toronto |
| Contract | **12-month fixed-term** |
| Comp | CA$75,000-110,000 + benefits (dental, EHC, RRSP match) |
| TL;DR | Embedded sensor-fusion engineering at InvenSense's Calgary unit. Strong overlap with Nishal's IMU/real-time embedded work and research-to-C porting, but it is a fixed-term, sub-target-pay embedded role with RTOS/MCU and navigation-theory gaps. |

## B) Match with CV

Source of truth: `ai-job-search/input/knowledge-graph.md` (career-ops `cv.md` is a template).

| JD requirement | Evidence (KG) | Verdict |
|---|---|---|
| BEng/BSc EE/CompE | BEng (Hons) Electronic Eng.; MSc Telecom & Electronic Eng.; PhD ICT (§3) | ✅ |
| Strong C/C++ development + debugging | C++ Expert: C++17 Nebula library, real-time engines, custom C++ closed-loop printer control (§5.1, §4.5.c, §4.6) | ✅ strong |
| RTOS environment | Real-time Linux (Elk Audio OS), RPi deployments; no MCU RTOS (FreeRTOS/Zephyr) evidenced (§5.5) | ⚠️ gap |
| ARM toolchains + embedded IDEs (Atmel Studio, Keil, ESP-IDF) | STM32/PIC/Arduino (§5.5); CPU profiling on ARM (Nebula) | ⚠️ partial |
| Debug and resolve hardware issues | Sensor retrofits, heterogeneous machine interfacing hardware at MAS, IMU/I²C + HiFiBerry builds (§4.5.b, §4.2) | ✅ |
| Strong Linux, Git | Linux deployments; Git Expert (§5.6) | ✅ |
| Strong Python and/or MATLAB | Python Expert; MATLAB Proficient (MSc S-transform work) (§5.1) | ✅ |
| Port algorithms from scripting language to embedded C | Research prototypes → C++ real-time detectors on RPi4 (14 ms, JAES 2026); Nebula (§4.1, §4.6) | ✅ direct |
| Interfaces I2C/SPI/UART/USB/Ethernet/CAN | I²C (BNO055 IMU), UDP/OSC networking; SPI/UART implied by MCU work; no CAN (§4.2, §5.5) | ⚠️ partial |
| Review schematics, PCBs, BOMs | Electronic eng. degrees; designed interfacing hardware at MAS; no PCB design evidenced | ⚠️ partial |
| INS / MEMS / integrated navigation (preferred) | IMU gesture detection + audio/IMU fusion (HFSM, F1 0.78); multi-stream sync; no INS/GNSS (§4.2, §4.1) | ⚠️ adjacent |
| Data collection (walking/running/cycling/driving) — bonus | Designed 4 Zenodo datasets with 70+ musicians; user studies (§7) | ✅ transferable |
| Web apps in JavaScript (preferred) | JS/TS Proficient (Hot Licks Mapper, speakfrench) (§5.1) | ✅ |
| Jetson / Atmel M4-M7 (preferred) | None | ❌ |
| Technical documents, manuals | 10+ papers, deployment docs (§6) | ✅ |
| Legal status in Canada | Canadian PR (§1) | ✅ |

### Gaps and mitigation
1. **MCU RTOS + ARM IDE toolchain (moderate).** Mitigation: be upfront; cite STM32 work and real-time Linux; a short FreeRTOS + STM32 IMU-reading demo (BNO055 over I²C, ported filter in C) would close most of it within a week.
2. **Inertial navigation theory (moderate, preferred).** Mitigation: frame IMU gesture/fusion work as the on-ramp; read Groves / Noureldin (the Trusted Positioning founders' own INS text) before interviews.
3. **PCB design / CAN (minor-moderate).** Mitigation: schematic *review* is the ask, which his EE background supports; avoid over-claiming layout.
4. **Contract + pay (not a skill gap — a decision factor).** See C/D.

## C) Level and Strategy

- **Level detected:** "Sr." title, 2+ yrs preferred → mid-level scope and pay; Nishal is over-credentialed.
- **Sell senior without lying:** "I turn sensor algorithms into real-time embedded code — IMU and audio pipelines on ARM at 14 ms, and a C++17 feature library with per-feature ARM latency benchmarks — and I design the datasets to test them."
- **Ask in screening:** conversion path to permanent after 12 months; whether ML-based fusion (learned motion models, activity context) is on the roadmap — that is where he adds unique value.
- **If downleveled/contract stays fixed:** push to the top of band (CA$110K) given PhD + 10 yrs; negotiate a written conversion review at month 9.

## D) Comp and Demand

| Data point | Value | Source |
|---|---|---|
| Posted band | CA$75K-110K, 12-month fixed-term | JD |
| Embedded software developer, Calgary | avg ~CA$78K; P25-P75 CA$68K-89K; P90 ~CA$101K | [Glassdoor Calgary](https://www.glassdoor.ca/Salaries/calgary-ab-embedded-software-developer-salary-SRCH_IL.0,10_IC2275123_KO11,38.htm) |
| Profile ideal | CA$120K-150K (soft benchmark) | `modes/_profile.md` |
| Parent-company signal | Reported layoff of ~55 InvenSense staff in 2026 (details thin) | [ZoomInfo — InvenSense](https://www.zoominfo.com/c/invensense-inc/55396522) |

Band is at/above the Calgary market for this title but below the profile's ideal range; fixed-term adds risk.

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---|---|---|---|
| 1 | Summary | ML research engineer | "Embedded C/C++ engineer who ports sensor algorithms to real-time hardware — IMU, audio, industrial sensors" | Embedded-first JD |
| 2 | McGill smart guitar | Gesture F1 | BNO055 IMU over I²C at 100 Hz, RPi4, self-powered, sensor fusion (HFSM) | Closest to INS/MEMS ask |
| 3 | MUSMET | Model metrics | Python prototype → real-time C++ detector, 14 ms on ARM; multi-device stream sync | "Port to embedded C" |
| 4 | Projects | Research | Nebula (C++17, ARM latency benchmarks); short FreeRTOS/STM32 IMU demo if built | RTOS/ARM gap |
| 5 | Skills | ML-heavy | C/C++, Python/MATLAB, I²C/SPI/UART, STM32, Linux, Git, schematics review, JavaScript | ATS |

LinkedIn: add "sensor fusion" and "embedded C/C++" to headline; pin Nebula; add STM32/I²C skills.

## F) Interview Plan

| # | JD requirement | STAR+R story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Port algorithms to embedded | JAES 2026 detector | Research RNN/DTW prototypes too slow for live use | Run on RPi4 in real time | Re-architected + optimized inference path | 14 ms, 74× faster than DTW, F1 0.76 | OS scheduling mattered more than the model |
| 2 | Multi-sensor fusion | McGill smart guitar | Needed gesture + audio events on-instrument | Fuse IMU and audio detections | BNO055 over I²C + HFSM fusion | P 0.79 / R 0.76 / F1 0.78 | Power and mounting decided feasibility |
| 3 | Hardware debugging | MAS sewing-machine IoT | Heterogeneous machines, no common interface | Reliable event capture | Designed interfacing hardware + ingestion | Millions of events/day | Design for partial failure |
| 4 | Data collection | Zenodo datasets | No benchmark data existed | Collect and validate | Protocols with 70+ musicians | 4 public DOI datasets | Validation rules belong in code |
| 5 | Documentation | MUSMET deployment docs | Partners reusing pipeline | Make it reproducible | Docs + reproducible pipelines | Clean handoffs | Write for the next engineer |

**Case study:** McGill smart guitar (IMU over I²C → fused detection on embedded Linux).
**Red-flag questions:** "Why a 12-month contract after a PhD?" → interest in sensor fusion + conversion path. "INS experience?" → honest; IMU fusion work + ramp plan.

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| Freshness | Posted 2026-09-22 (2 days) on Indeed + Job Bank | Positive |
| Description quality | Specific tools (Keil, Atmel Studio, ESP-IDF, Jetson), interfaces, hybrid rule, band | Positive |
| Salary transparency | Band posted | Positive |
| Company careers page | Still shows "No Current Openings" | Neutral (page likely stale) |
| Parent-company layoffs | ~55 InvenSense layoffs reported 2026 (thin sourcing) | Concerning |
| Reposting | Not in scan-history | Neutral |

**Context:** Small TDK subsidiary posting via Indeed Easy Apply; the fixed-term structure may reflect budget caution after parent-company cuts.

**Outreach already made:** 2026-09-24 16:50 EST, IEEE Global Career Fair chat to Sarah MEYER (InvenSense TDK) asking about the Grenoble Algorithms Engineer role's location flexibility and sensor-ML/sensor-fusion openings at Trusted Positioning Calgary. Awaiting reply. Related tracker row: #1447 (Grenoble role, SKIP — outside Canada).

---

## Keywords extracted
embedded software, C, C++, ANSI C, RTOS, ARM, Keil, Atmel Studio, ESP-IDF, I2C, SPI, UART, CAN, USB, Python, MATLAB, Linux, Git, sensor fusion, inertial navigation, MEMS, IMU, GNSS, Wi-Fi positioning, vehicular navigation, portable navigation, schematics, PCB, Jetson, data collection

## Machine Summary
```yaml
id: 1446
company: TDK Trusted Positioning
role: Sr. Embedded Software Developer (12-month fixed-term)
score: 3.1
dimensions: {cv_match: 3.6, north_star: 3.2, comp: 2.3, culture: 3.2, red_flags: -0.4}
legitimacy: High Confidence
location: Calgary, AB (hybrid 3 days) — city rank 3
recommendation: below 3.5 — worth it only if a Calgary move + contract are acceptable; wait for Sarah Meyer's reply before applying
```
