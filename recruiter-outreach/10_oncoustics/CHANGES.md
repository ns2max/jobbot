# Oncoustics: resume changelog

- **Send to:** Founders / hiring team <founders@oncoustics.com>
- **CSV priority:** 2
- **Variant:** Real-time signal ML (V1 signal-focused)
- **Base:** golden `resume_generic/Nishal_Silva_ML_Research_Engineer` (minimal-edit rule)
- **Pages:** 2

## Edits vs golden

- Retire '>90% F1' (KG §16: never cite it) -> verified 74x-vs-DTW figure
- Postdoc bullet: '>90% F1' -> published 14ms / F1 0.76 on Raspberry Pi 4
- Line spacing 1.05 -> 1.03 so the minimal edits keep the golden 2-page layout
- Date ranges use an ASCII hyphen instead of an en-dash (ATS date parsing)
- Tagline -> real-time signal / time-series focus
- Summary: lead with raw-signal / sensor ML and note deployed healthcare monitoring
- Domain Expertise: Signal Processing first, + Sensor Fusion (reorder, nothing removed)
- Postdoc bullet 4: partner-coordination -> multimodal audio + BCI/EEG + XR sync pipeline (KG §4.1)

## Verification

- [x] pages == 2
- [x] no (cid:) / U+FFFD
- [x] email literal
- [x] phone literal
- [x] no '>90% F1'
- [x] no en-dash in date ranges
- [x] PR line present
