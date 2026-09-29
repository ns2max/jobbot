# Case-Study Scenarios — Amii × ZeroKey ML Resident

**Job ID:** 1085 · **Companion to:** [amii-zerokey-ml-resident-technical.md](amii-zerokey-ml-resident-technical.md) (§9 playbook, §10 Cases A–G)
**Prepared:** 2026-09-29

These are 13 **new** scenarios (H–T) that don't repeat Cases A–G. They cover RTLS, video, general time series, and pure critical thinking, because the real case could be any of these. Run each one with the §9.1 time plan: clarify → data and assumptions → baseline → main approach → evaluation → deployment and risks.

**Assumptions used throughout.** Numbers like "20 Hz per tag" are assumptions, because ZeroKey's per-tag update rate isn't public. **Say them out loud as assumptions** in the interview.

---

## Index

| # | Scenario | Data | Main skills tested | Difficulty |
|---|---|---|---|---|
| H | Is the badge actually being worn? | RTLS | Anomaly detection, physics priors, base rates | ★★ |
| I | Discover work cycles with no SOP labels | RTLS | Unsupervised segmentation, motif discovery | ★★★ |
| J | Sensor fault or real anomaly? | RTLS + system logs | Data quality, Kalman innovations, root cause | ★★ |
| K | Plant A model, Plant B deployment | RTLS | Distribution shift, domain adaptation, few labels | ★★★ |
| L | Right part from the right bin? | RTLS + pick list | Spatial association, uncertainty, thresholds | ★★ |
| M | Man-down / fall detection for lone workers | RTLS | Rare events, alarm budgets, latency | ★★ |
| N | Novice vs. expert: skill assessment and coaching | RTLS | Trajectory similarity, metric learning, fairness | ★★★ |
| O | Does motion predict downstream defects? | RTLS + QC outcomes | Weak labels, causality, confounding | ★★★ |
| P | Tool-angle check from two tags | RTLS | 3D geometry, rotations, noise propagation | ★★ |
| Q | PPE compliance from cameras | Video | Detection, tracking, class imbalance, privacy | ★★ |
| R | New product, 20 defect images | Images | Anomaly detection, few-shot, lighting | ★★ |
| S | AGV fleet congestion forecasting | RTLS (vehicles) | Multi-agent forecasting, graphs | ★★★ |
| T | "Our model is 98% accurate" — find the problem | Any | Leakage, evaluation, critical thinking | ★★ |

**Rehearse first:** T (pure critical thinking; very likely style), I (hard, and shows depth in unsupervised time series), Q or R (covers the CV main topic), then K.

---

## H. Is the badge actually being worn?

**Prompt:** *"Safety analytics depend on workers wearing their badge and wrist tags. Some workers leave the badge on the bench or hang it on a cart. How would you detect a tag that isn't being worn?"*

**Clarify:**
- Which tags does each worker carry (badge only, or badge plus wristband)?
- Real-time alert, or a data-quality flag for analytics?
- Consequences: is this disciplinary? (Privacy and trust matter a lot here.)

**Assumptions to state:** 20 Hz, ±1.5 mm, worker has badge + wrist tag.

**Baseline (physics rules):**
- **Stillness:** a worn badge is never perfectly still. Human sway gives mm–cm micro-motion. Flag if position variance over 60 s is near sensor noise level (σ ≈ 1.5 mm).
- **Height:** a worn badge sits at chest height (~1.2–1.5 m), not bench height (~0.9 m), and moves with walking.
- **Coupling:** a worn badge and wristband stay within arm's reach (≤ ~0.8 m) and move together when walking.

**Model:**
- Features per window: micro-motion spectrum (breathing and sway around 0.1–1 Hz), height, badge–wrist distance and velocity correlation, gait periodicity (~1.5–2 Hz step frequency) while moving.
- One-class model or a small classifier trained on staged data ("worn" vs. "on bench / on cart / in pocket").
- **Cart case is the hard one:** a badge on a moving cart moves, but without gait periodicity and without micro-sway at rest.

**Evaluation:** staged recordings with ground truth, split by person; event-level precision/recall; false-alarm rate per worker per shift.

**Curveballs:**
- *"Worker sits down."* → Height drops; use the wristband coupling and micro-motion, not height alone.
- *"Why not just ask the worker to tap in?"* → Fair: combine a cheap procedural fix with the detector. Challenge the framing.
- *"Is this surveillance?"* → Report at the aggregate / data-quality level by default; involve worker representatives; the goal is valid safety data, not discipline.

**Your link:** McGill IMU gesture work (distinguishing intended motion from idle); micro-motion is a spectral problem, like your DSP background.

---

## I. Discover work cycles with no SOP labels

**Prompt:** *"A customer installs RTLS on a line and wants cycle-time and step breakdowns, but they have no documented SOP and no labels. What would you do?"*

**Clarify:**
- One operator per station, or shared stations?
- Is the work repetitive (cycle of ~1–5 min), or highly variable?
- What's the output: average cycle time, step durations, a "standard work" definition, or deviation alerts?
- Any event signals (MES start/stop, torque tool, conveyor index)?

**Baseline:**
- **Autocorrelation / FFT** of the wrist trajectory gives the dominant cycle period.
- **Zones:** dwell at fixed locations (bins, fixture, tool rack) gives a symbolic sequence like `bin → fixture → tool → fixture → conveyor`.
- If MES has conveyor index events, that alone gives cycle boundaries.

**Main approach (unsupervised):**
1. Kalman smoothing, transform to the station frame.
2. **Cycle segmentation:** matrix profile / motif discovery to find the repeating pattern; or cut cycles at conveyor events.
3. **Step discovery within cycles:** change-point detection (PELT/BOCPD) on speed and zone; cluster segments (by location, duration, motion shape) into step types.
4. **Align cycles to each other** with DTW to build a "template cycle" (DTW barycenter averaging), then per-step durations.
5. **HSMM** fitted with the discovered steps and duration distributions gives robust online segmentation.
6. Show the engineer the discovered steps with a heatmap and let them **name** them (human-in-the-loop labelling).

**Evaluation:** no labels, so: agreement with a small hand-labelled sample (one hour with an engineer); cycle-time error vs. stopwatch study; stability of discovered steps across days.

**Curveballs:**
- *"Operator sometimes does two parts at once / batches work."* → Cycles aren't strictly periodic; use event-based segmentation and allow variable structure (grammar or HSMM with optional steps).
- *"How many step clusters?"* → Model selection with BIC / silhouette plus engineer review; start coarse.
- *"Why not deep learning?"* → No labels, and interpretability matters; self-supervised embeddings (TS2Vec) can replace hand features later.

**Your link:** MAS sewing-floor IoT tracking repetitive operator motion; DTW experience; hierarchical FSM.

---

## J. Sensor fault or real anomaly?

**Prompt:** *"OmniVisor flags anomalies, but engineers complain many are caused by the positioning system itself, not the process. How would you separate sensor problems from real process anomalies?"*

**Clarify:**
- What does a "false" anomaly look like: jumps, frozen positions, drift?
- Do we have anchor-level data (per-anchor ranges, signal quality), or just final positions?
- Temperature/HVAC data? (Speed of sound depends on temperature: 1 °C ≈ 18 mm at 10 m.)

**Taxonomy of sensor issues:**
- **Multipath / occlusion outliers:** single-sample jumps faster than any human can move.
- **Dropouts:** gaps.
- **Drift:** slow, correlated offset across tags in one area (temperature, anchor moved).
- **Anchor fault:** all tags that depend on one anchor degrade together.
- **Frozen tag:** battery or firmware; identical coordinates.

**Approach:**
1. **Physics checks:** speed and acceleration limits; the Kalman **innovation test** (d² > χ²₃(0.99) ≈ 11.34) per measurement. Track **NIS over time**: if it's consistently too high, the filter model or the sensor is wrong.
2. **Spatial correlation:** if many tags in the same area shift together, it's the infrastructure, not the process. A **fixed reference tag** in each zone is the gold standard: any motion it shows is sensor error.
3. **Anchor attribution:** if anchor-level residuals are available, a multilateration residual per anchor identifies the bad one.
4. **Route alerts:** sensor-health alerts go to IT/maintenance; process anomalies go to the line. Suppress process anomalies when sensor health is poor ("low confidence").

**Evaluation:** inject synthetic faults (jumps, drift, dropouts) into clean recordings and measure detection; review a week of past anomalies with engineers and label them "sensor" or "process."

**Curveballs:**
- *"No anchor-level data."* → Rely on reference tags and cross-tag correlation.
- *"Could a real event look like a sensor fault?"* → Yes, e.g. a dropped tool really does fall fast. Keep physics limits per tag type and don't discard, just downgrade confidence.

**Your link:** MAS machine monitoring; validating systems before trusting their outputs.

---

## K. Plant A model, Plant B deployment

**Prompt:** *"Your risk model works well at the pilot plant. A new customer wants it deployed at a plant with a different layout, different products, and different workers. You get almost no labels at the new site. How do you approach it?"*

**Clarify:** Same risk definitions? Same tag placement? How long before go-live? Can we run a shadow period?

**Main points:**
1. **Design for transfer up front:** features in the **work-cell frame** (not facility coordinates), relative distances (wrist–badge, worker–robot), speeds; avoid features tied to absolute layout.
2. **Diagnose the shift:** compare feature distributions (PSI/KL) between plants. Covariate shift (layout), label shift (different base rates), concept shift (different SOP).
3. **Unsupervised adaptation:** recalibrate normalization; self-supervised pre-training on Plant B's unlabelled data; domain-adversarial training if needed.
4. **Few labels, used well:** active learning for the most uncertain windows; a few hours of engineer labels per cell.
5. **Recalibrate thresholds** to Plant B's alarm budget (base rates differ).
6. **Shadow deploy** 2–4 weeks: model scores silently; engineers review a sample; go live only if metrics hold.

**Evaluation:** leave-one-site-out validation before Plant B even exists (this is the honest estimate of transfer); in Plant B, a small labelled audit set.

**Curveballs:**
- *"Should we train one global model or one per site?"* → Global model plus per-site calibration/fine-tuning; per-site from scratch doesn't scale.
- *"How do you know when to retrain?"* → Drift monitoring + alert-rate changes + operator feedback.

**Your link:** MAS rollouts across factories on three continents.

---

## L. Right part from the right bin?

**Prompt:** *"Operators pick parts from a rack of 24 small bins, 10 cm apart. Picking the wrong part causes defects. Using wrist tags, how would you verify every pick?"*

**Clarify:** Bin dimensions and layout; does each order have an expected pick list; alert immediately (before assembly) or log?

**Numbers to state:** bins 10 cm apart, sensor ±1.5 mm → spatially easy *if* the tag is close to the fingertips. But a wrist tag is ~15–20 cm from the fingertips, and wrist orientation changes, which is the real error source.

**Approach:**
1. **Pick event detection:** hand enters a bin's volume, slows, dwells (~0.3–1 s), then retracts. Rules first (zone + speed minimum + dwell), then a small classifier to reduce false positives (reaching past a bin vs. picking).
2. **Bin association:** estimate the fingertip position from the wrist trajectory direction (extrapolate along approach vector), then assign to the nearest bin. Output a **probability per bin**, not a hard label.
3. **Compare to the pick list:** alert if the probability of the expected bin is low; if ambiguous between neighbours, flag "uncertain" rather than "wrong."
4. **Calibrate geometry from data:** the rack isn't exactly where the CAD says; learn bin centres from the pick clusters.

**Evaluation:** staged picks with known ground truth; confusion between neighbouring bins; **false-stop rate**; time to alert.

**Curveballs:**
- *"Operator picks with the other hand."* → Tags on both wrists, or accept a coverage gap.
- *"Pick-to-light already exists."* → RTLS verifies the action, not just the instruction; complements it.

**Your link:** MAS care-label QC (verification with explainable overlays); PLC reject integration.

---

## M. Man-down / fall detection for lone workers

**Prompt:** *"A customer has workers in remote parts of a warehouse. They want an alert if someone falls or collapses. Badge tags only. Design it."*

**Clarify:** Required response time (seconds to a minute?); who receives the alert; alarm budget; do we have any real fall data? (Almost certainly not.)

**Signal:**
- Rapid height drop (badge from ~1.3 m to < 0.5 m within ~1 s), then **stillness** (no gross motion for N seconds), at an unusual location.
- **Base-rate problem:** falls are extremely rare; kneeling, bending to pick, and sitting are common. A detector with 1% false positives per event across hundreds of bend-downs per shift gives constant false alarms.

**Approach:**
1. **Two-stage:** fast trigger (height drop + impact-like acceleration) → confirmation window (stillness for 10–30 s) → alert. The confirmation window trades latency for far fewer false alarms.
2. **Context:** known low-work zones (bottom shelves) raise the threshold; open aisles lower it.
3. **Training data:** staged falls with mats (stunt/safety protocols), plus lots of normal data (kneel, sit, bend) as hard negatives. Public IMU fall datasets for pre-training representation.
4. **Escalation:** a check-in prompt on the badge ("are you OK?") before a full alert, if the hardware allows.

**Evaluation:** recall on staged falls must be near 100%; false alarms per worker per week; time-to-alert distribution.

**Curveballs:**
- *"What if the badge falls off, not the person?"* → Link to Scenario H: a dropped badge shows no micro-motion afterwards, but a person on the floor still breathes and moves slightly. Treat as "check on worker" anyway.
- *"Recall 100% is impossible."* → Be explicit about the trade-off and let the customer choose the operating point.

**Your link:** onset detection and real-time latency budgets (JAES).

---

## N. Novice vs. expert: skill assessment and coaching

**Prompt:** *"A customer wants to shorten onboarding. Can we use RTLS data from experienced operators to assess new operators and coach them?"*

**Clarify:** What counts as "skill": speed, consistency, quality, safety, ergonomics? Who sees the scores? Is there an outcome label (defects, supervisor rating)?

**Approach:**
1. **Define skill measurably** with the customer: cycle time, variance across cycles, path efficiency (path length / straight-line distance), unnecessary motions, ergonomic proxies, sequence errors.
2. **Expert reference:** DTW barycenter or learned embedding of expert cycles; compare novices by distance to the expert distribution (not one expert, since experts vary).
3. **Metric learning:** a siamese/contrastive model trained so embeddings separate experience levels; validate that the distance correlates with outcomes (defects, supervisor ratings), not just speed.
4. **Coaching output:** specific, local feedback ("step 3 takes 40% longer; extra walk to the tool rack") rather than a single score.

**Evaluation:** does the score track learning over a novice's first weeks? Correlation with independent ratings; test–retest stability.

**Curveballs:**
- *"Isn't this just speed?"* → Faster isn't always better (quality, safety); use multiple dimensions.
- *"Fairness?"* → Left-handed workers, body size, disabilities may produce different but valid motion; compare to outcome-relevant features and let experts review.
- *"Will workers accept it?"* → Coaching tool for the worker, not a ranking for management; opt-in dashboards.

**Your link:** speakfrench benchmark (Wav2Vec2 embeddings vs. DTW for scoring learners, ROC-AUC 0.822 vs. 0.599); McGill guitar case study with players.

---

## O. Does motion predict downstream defects?

**Prompt:** *"Quality finds defects at end-of-line. The customer wonders whether the operator's motion during assembly predicts which units will fail. How would you investigate?"*

**Clarify:** Can each unit be linked to the operator and time at each station (serial number + MES timestamps)? Defect rate? Types of defect?

**Approach:**
1. **Join data:** unit serial → station timestamps → motion window for that unit at each station.
2. **Exploratory first:** compare motion features (step durations, skipped/extra steps, hesitations, tool dwell) between failed and passed units. Defects are rare → use PR-AUC, and watch **multiple comparisons** across many features and stations (Benjamini–Hochberg).
3. **Model:** GBDT on per-unit features (interpretable with SHAP) as the main tool; sequence models only if the signal is there.
4. **Confounders:** shift, operator experience, part supplier lot, machine state. **Simpson's paradox** risk: a motion pattern may correlate with defects only because it's common on night shift.
5. **From correlation to action:** a controlled trial (coach a motion change on some stations, compare defect rates via difference-in-differences).

**Evaluation:** time-based split (train on earlier months, test on later); lift in defect catch rate at a fixed inspection budget.

**Curveballs:**
- *"We found a strong predictor: long dwell at station 4."* → Maybe operators pause *because* they notice a bad part (reverse causation). Check with engineers.
- *"Only 30 defects in 3 months."* → Too few for complex models; framing as anomaly detection or pooling across similar defects; honest power analysis.

**Your link:** MAS changeover/allocation prediction; statistics in user studies.

---

## P. Tool-angle check from two tags

**Prompt:** *"Drilling must be done within 5° of perpendicular to the panel. We can put two tags on the drill, 15 cm apart. Can we check the angle in real time?"*

**Clarify:** Required accuracy (5° tolerance → need ~1–2° accuracy), panel orientation known (fixture CAD), sample rate.

**Numbers (critical-thinking core):**
- Angle error ≈ position error across the baseline: with σ = 1.5 mm per tag, the difference vector has noise ≈ √2·1.5 ≈ 2.1 mm, over a 150 mm baseline → ≈ **0.8° (1σ)** per sample. Feasible, and averaging over a drilling event (e.g. 1 s at 20 Hz) reduces it to ~0.2°.
- **Two tags give the drill axis direction but not roll** around that axis. Roll doesn't matter for perpendicularity. Good: say so.

**Approach:**
1. Per-tag Kalman; compute the unit vector between tags; transform to the panel frame.
2. Angle to the panel normal = arccos(u · n).
3. Detect drilling events (drill trigger signal if available, or stillness + proximity to panel).
4. Alert if the average angle during the event exceeds the tolerance, with a margin based on the noise estimate.

**Evaluation:** jig tests at known angles (0°, 3°, 5°, 8°); report bias and variance.

**Curveballs:**
- *"Tags are offset from the drill axis."* → Calibrate the tag-to-axis transform once per tool (Kabsch/Procrustes with a jig).
- *"Need roll too."* → Add a third non-collinear tag; full rotation via Kabsch.
- *"Where's the ML?"* → Geometry solves it; ML adds event detection and learning which deviations actually cause defects. **Not every problem needs deep learning** — saying this is a strength.

**Your link:** Promptly registration and warping (applied geometry); rotation knowledge (§6.7).

---

## Q. PPE compliance from cameras

**Prompt:** *"A plant wants to detect workers not wearing helmets, vests or gloves in certain zones, using existing CCTV. How would you build it?"*

**Clarify:** Camera count, resolution, angles, frame rate; which PPE items; alert in real time or daily reports; privacy rules (union, GDPR-like regimes).

**Approach:**
1. **Person detection** (YOLO-family) → **tracking** (ByteTrack; Kalman + association) so each person is judged over time, not frame by frame.
2. **PPE classification per track:** either a detector with PPE classes (helmet, vest, no-helmet) or crops → classifier. Gloves are small and often occluded → hardest; may need higher resolution or be out of scope.
3. **Temporal voting:** "no helmet" only if consistent over N seconds of the track (removes single-frame errors, e.g. helmet occluded).
4. **Zone logic:** only alert inside the zones where the PPE is required (homography from camera to floor plan).
5. **Privacy:** blur faces, store only events and crops, retention limits.

**Data:** public PPE datasets for pre-training; fine-tune on site images; hard negatives (caps, hoods, hair that looks like helmets; high-vis objects).

**Evaluation:** split by camera and by day, not by frame; event-level precision/recall per PPE type; false alerts per camera per day.

**Curveballs:**
- *"Night shift lighting is terrible."* → Augmentation, IR cameras, per-camera calibration; measure performance by lighting condition.
- *"Could ZeroKey's tags do this instead?"* → Only if PPE is tagged (e.g. tagged helmets). Camera handles untagged items; RTLS handles precise location. Hybrid again.

**Your link:** MAS industrial CV with alert budgets (5–6 s); honest note that your hands-on CV was classical (§13 gap script).

---

## R. New product, 20 defect images

**Prompt:** *"A new product line starts next month. Quality has thousands of good-part images but only about 20 defect images. How would you build visual inspection?"*

**Clarify:** Defect types (scratches, dents, missing components, colour), cycle time per part, what false-reject rate is acceptable, lighting control.

**Approach:**
1. **Fix the imaging first:** fixed lighting (diffuse / dome / low-angle for scratches), fixed pose via fixture. Often the biggest gain.
2. **Anomaly detection trained on good parts only:** PatchCore or PaDiM (pre-trained CNN features + memory bank / Gaussian per patch). Gives a heatmap for explainability.
3. **Use the 20 defects for validation and threshold setting**, not training (too few), plus **synthetic defects** (cut-paste, drawn scratches) for extra validation.
4. **Known defect classes later:** once real defects accumulate, train a supervised classifier/segmenter for the frequent types; keep the anomaly model for novel defects.
5. **Human-in-the-loop:** uncertain parts go to an inspector; their decisions become labels.

**Evaluation:** image-level AUROC and pixel-level metrics (MVTec-style); **false-reject rate at 100% recall on critical defects**; latency against cycle time.

**Curveballs:**
- *"Normal parts vary a lot (different colours)."* → Separate memory banks per variant, or condition on variant.
- *"Threshold from 20 defects is unreliable."* → Yes: bootstrap confidence intervals; start conservative (favour rejecting); tighten during shadow period.

**Your link:** MAS care-label QC and fabric defect detection (camera arrays, lighting lessons, PLC reject); Xu Han's quality-inspection work.

---

## S. AGV fleet congestion forecasting

**Prompt:** *"A plant runs 40 AGVs and hundreds of workers on shared aisles. AGVs often stop for congestion. Using RTLS for vehicles and people, can we predict congestion 30–60 s ahead?"*

**Clarify:** What action follows a prediction (reroute, delay dispatch, warn)? Do we have AGV planned routes from the fleet manager? Update rates?

**Approach:**
1. **Baseline:** occupancy per aisle segment (grid or graph of the aisle network) → forecast with historical averages by time of shift + current occupancy (GBDT with lags).
2. **Better:** a **graph model** over aisle segments (nodes) with flows (edges): spatio-temporal GNN or diffusion-style forecasting (like traffic forecasting, DCRNN/Graph WaveNet).
3. **Use planned routes:** the fleet manager's plans give *future* AGV positions for free; the uncertainty is mostly humans and forklifts.
4. **Agent trajectory forecasting** for humans near intersections (constant velocity baseline → learned model).
5. **Output:** probability of congestion per segment in 30/60 s, fed to the fleet manager for rerouting.

**Evaluation:** rolling-origin validation; precision/recall of congestion events at 30 and 60 s horizons; the business metric (AGV stop time reduction) in an A/B test by day or zone.

**Curveballs:**
- *"Interventions change the data"* (rerouting prevents the congestion we'd have seen) → feedback loop; evaluate with experiments, not historical accuracy only.
- *"Isn't this RL?"* → Could be (routing policy), but start with prediction + rules; offline RL on logged data later.

**Your link:** multi-entity stream sync (MUSMET); MAS allocation prediction.

---

## T. "Our model is 98% accurate" — find the problem

**Prompt:** *"A previous team built a risky-behaviour classifier on RTLS data. They report 98% accuracy, but in the pilot the operators say it's useless. Here's their setup: 2-second windows with 50% overlap, random 80/20 split, accuracy metric, 3% of windows labelled risky. What's wrong, and what would you do?"*

**What's wrong (list them clearly; this is the whole test):**
1. **Accuracy under imbalance:** 3% positives → predicting "safe" always gives 97%. 98% is barely above trivial.
2. **Leakage from overlapping windows + random split:** neighbouring windows share half their samples and land in both train and test.
3. **Leakage by person/session:** the same workers and sessions in train and test; the model can memorize individuals.
4. **Window-level vs. event-level:** operators experience alerts per event; one risky event spans many windows; false alarms per shift are what matter.
5. **Threshold:** probably default 0.5, not chosen for an alarm budget.
6. **Lab vs. floor:** training data may be staged; pilot data comes from a different distribution.
7. **Labels:** how were they made, how consistent (inter-rater agreement)?

**What you'd do:**
- Re-split by **worker and time block** (group k-fold, gap between blocks).
- Report **PR-AUC, event-level precision/recall, false alarms per shift, detection delay**, with bootstrap (block) CIs.
- Compare against the trivial baseline and a simple rule baseline.
- Error analysis with operators: look at 50 false alarms and 50 misses.
- Choose the threshold with the customer's alarm budget; add hysteresis / minimum duration.

**Curveballs:**
- *"After fixing the split, the model drops to 0.4 F1. Now what?"* → That's the true starting point. Check labels, add context features (zone, task), consider rules for the clearest risks, active learning.

**Your link:** JAES honesty (F1 0.76 reported honestly, benchmark against DTW); "a suspiciously high score usually means leakage."

---

## Cross-cutting lines to reuse in any scenario

- *"Before modelling, I'd check what a simple rule gets us — that's the bar any ML has to beat."*
- *"At 20 Hz — assuming that rate — a 2-second window is 40 samples."*
- *"I'd evaluate at the event level, split by worker and site, because that's what deployment looks like."*
- *"The cheapest experiment first: record a static reference tag and label one shift with an engineer."*
- *"If the operators don't trust it, accuracy doesn't matter — explainability and a low false-alarm rate are part of the spec."*
- *"Good point — if that's true, I'd change X to Y, because…"*
