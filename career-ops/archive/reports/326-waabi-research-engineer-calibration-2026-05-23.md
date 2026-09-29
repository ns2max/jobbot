# Evaluation: Waabi — Research Engineer, Calibration

**Date:** 2026-05-23
**URL:** https://jobs.lever.co/waabi/4c352ae0-53b0-4510-8d46-894b87d96ede
**Archetype:** ML Research Engineer
**Score:** 3.3/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## Block A — Role Summary

| Field | Detail |
|-------|--------|
| Archetype | ML Research Engineer |
| Domain | Autonomous vehicles / Sensor calibration / Multi-sensor fusion |
| Function | Build — calibration algorithms (classical + learning-based), real-time integrity monitoring |
| Seniority | Senior Research Engineer |
| Remote | Hybrid (Toronto, SF, Pittsburgh, Remote US & Canada) |
| Team size | Not stated |
| TL;DR | Develop next-gen calibration systems for AV sensor stacks (camera, lidar, radar, IMU, GNSS) using classical + learning-based approaches and real-time integrity monitoring. |

---

## Block B — Match with CV

### Strengths

| JD Requirement | CV Evidence |
|----------------|-------------|
| PhD or research experience in related field | PhD — Information Engineering & Computer Science (2025) |
| Production software beyond prototyping | MAS Holdings: C++ real-time inference engines deployed at industrial scale; Forestpin production backend |
| C++/Rust with Python interoperability | C++ used at MAS Holdings (inference + system integration); Python primary language throughout |
| Real-time system design | MUSMET: <30ms inference on RPi4; MAS Holdings: real-time inspection pipelines |
| Sensor data processing | IoT and sensor stream processing at MAS Holdings (camera arrays, machine sensors); MUSMET (audio + gesture sensors) |
| Multi-sensor / multimodal systems | IEEE I3DA 2025: IoMusT ecosystem (audio + sensor + haptic + MR); MAS Holdings (camera + IoT sensor fusion) |
| Performance profiling and optimization | Latency benchmarking at MUSMET (14ms RPi4); C++ inference optimization at MAS |
| Learning-based approaches (NeRF, 3D Splatting) | Partial — experience with SSIM repurposing from CV (DAFx 2022); no NeRF/3DGS experience |

### Gaps

| Gap | Blocker? | Mitigation |
|-----|----------|-----------|
| Multi-sensor calibration (camera, lidar, radar, IMU, GNSS) | Hard gap — core requirement | No AV sensor calibration experience; sensor processing at MAS is camera + IoT, not AV-specific |
| ICP, SLAM, visual/radar odometry | Hard gap | No robotics/SLAM background demonstrated |
| NeRF / 3D Gaussian Splatting | Hard gap | No 3D scene reconstruction experience |
| AV domain knowledge (fleet operations, integrity monitoring) | Hard gap | No autonomous vehicles domain experience |
| Concurrent/parallel/distributed computing for calibration | Partial gap | Distributed inference at MAS, AWS ECS; not calibration-specific |
| Real-time state estimation integrity monitoring | Hard gap | Real-time experience is in audio/ML inference, not sensor state estimation |

**Gap assessment:** Despite strong real-time ML and sensor processing credentials, the role requires AV-specific sensor calibration expertise (SLAM, ICP, lidar/radar calibration, NeRF) that represents a fundamentally different domain. The surface similarity (sensors, real-time, C++) masks a deep domain gap.

---

## Block C — Level and Strategy

**Level detected:** Senior Research Engineer — requires deep multi-sensor fusion expertise, classical algorithms (ICP, SLAM) plus learning-based approaches.

**Candidate's natural level:** Senior ML Research Engineer in audio/embedded ML. Under-qualified for AV sensor calibration specifically.

**Sell senior plan:** Emphasize real-time multi-sensor fusion (MUSMET, MAS), C++ production experience, embedded ML track record. Frame 14ms latency on RPi4 as evidence of hard real-time engineering. However, the SLAM/ICP/NeRF gap is hard to bridge in a cover letter.

---

## Block D — Comp and Demand

| Item | Detail |
|------|--------|
| JD stated range | $158,000–$269,000 USD + equity + bonus |
| Canadian equivalent (approx) | $215K–$365K CAD |
| Comp vs target | Well above C$200K target |
| Demand trend | AV calibration engineers: very specialized, strong demand |

---

## Block E — Customization Plan

Not recommended for application given domain gaps.

---

## Block F — Interview Plan

Not prepared — role not recommended.

---

## Block G — Posting Legitimacy

**Freshness:** Active Lever posting. Waabi hiring across calibration / sensing stack.

**Description quality:** Highly specific — names ICP, SLAM, NeRF, 3D Splatting, sensor types. Compensation published. No boilerplate. Legitimate, detailed JD.

**Company hiring signals:** No layoff signals. Active AV commercialization phase.

**Legitimacy verdict:** High Confidence — genuine, active opening.

---

## Recommendation

**Score: 3.3/5 — Skip.**

Legitimate role, strong comp. The surface signals look appealing (real-time, sensors, C++, research engineering), but the core requirement is AV sensor calibration with SLAM, ICP, NeRF — a robotics/AV specialty Nishal has not built. Three Waabi roles this session (324, 325, 326) all fall into the same pattern: Waabi needs AV-domain specialists and Nishal's strengths are audio/signal ML. Recommend not applying to any of the three Waabi roles in this batch.

---

## Machine Summary
```yaml
score: 3.3
archetype: ML Research Engineer
location_accessible: true
audio_signal_match: false
```
