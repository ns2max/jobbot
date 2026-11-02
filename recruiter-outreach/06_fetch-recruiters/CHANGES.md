# Fetch Recruiters: resume changelog

- **Send to:** Alexia Corrado (alternate: Carlos Morales) <alexia@fetchrecruiters.com>
- **CSV priority:** 1
- **Variant:** Applied ML (V1)
- **Base:** golden `resume_generic/Nishal_Silva_ML_Research_Engineer` (minimal-edit rule)
- **Pages:** 2

## Edits vs golden

- Retire '>90% F1' (KG §16: never cite it) -> verified 74x-vs-DTW figure
- Postdoc bullet: '>90% F1' -> published 14ms / F1 0.76 on Raspberry Pi 4
- Line spacing 1.05 -> 1.03 so the minimal edits keep the golden 2-page layout
- Date ranges use an ASCII hyphen instead of an en-dash (ATS date parsing)
- Domain Expertise: Computer Vision moved to second (firm recruits ML + CV specialists)
- Status line: + 'Open to Toronto or Montreal'

## Verification

- [x] pages == 2
- [x] no (cid:) / U+FFFD
- [x] email literal
- [x] phone literal
- [x] no '>90% F1'
- [x] no en-dash in date ranges
- [x] PR line present
