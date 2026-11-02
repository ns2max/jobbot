# LuxTronic: resume changelog

- **Send to:** James C. Evans (hiring inbox) <contact@luxtronic.ai>
- **CSV priority:** 1
- **Variant:** Industrial CV (V5)
- **Base:** golden `resume_generic/Nishal_Silva_ML_Research_Engineer` (minimal-edit rule)
- **Pages:** 2

## Edits vs golden

- Retire '>90% F1' (KG §16: never cite it) -> verified 74x-vs-DTW figure
- Postdoc bullet: '>90% F1' -> published 14ms / F1 0.76 on Raspberry Pi 4
- Line spacing 1.05 -> 1.03 so the minimal edits keep the golden 2-page layout
- Date ranges use an ASCII hyphen instead of an en-dash (ATS date parsing)
- Tagline -> industrial CV focus (V5)
- Summary: lead the domain list with production CV / inspection
- Domain Expertise: Computer Vision + Industrial Inspection moved first (reorder, nothing removed)
- ML Engineering: swap Multi-Tenant/Prompt engineering/AI Ethics for Edge Deployment + Camera & PLC Integration
- ML/AI stack: OpenCV moved to second position
- Postdoc trimmed to 3 bullets (V5 weighting: MAS carries the CV evidence)
- MAS: generic optimization bullet -> concrete vision-plus-machinery integration (Promptly, PLC/C++)
- MAS: stakeholder bullet -> named inspection results (care-label QC, fabric defect detection)
- Status line: + 'Available for remote work from Canada'

## Verification

- [x] pages == 2
- [x] no (cid:) / U+FFFD
- [x] email literal
- [x] phone literal
- [x] no '>90% F1'
- [x] no en-dash in date ranges
- [x] PR line present
