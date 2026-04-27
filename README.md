# Nominal thresholds for good astrometric fits, and prospects for binary detectability, for the full extended Gaia mission
MNRAS Paper, authors: F. Guerriero, Z. Penoyre, A. G. A. Brown (2026)
DOI: https://doi.org/10.1093/mnras/stag654

## Overview
The study originates from a Curricular Research Project carried out at Leiden University, supervised by Dr. Penoyre and Prof. Brown (2024), which key results and full thesis pdf can be found at the corresponding repository (_guerriero533/binaries-GUMS/binaries-fullthesis_). In this paper, we use simulated binaries from the Gaia Universe Model to examine the long-term astrometric behaviour of single stars and stellar binaries. We calculate nominal upper limits on the spread of goodness of astrometric fits for well-behaved single stars. These limits help identify poor astrometric fits and flag potential binary systems.

## Key Results
- For the Re-normalized Unit Weight Error (RUWE) parameter, we predict thresholds of **RUWE_lim_DR4 = 1.15** and **RUWE_lim_DR5 = 1.11**
- We find that the number of detectable **short-period binaries increases by 5–10% per new data release**
- The number of detectable **long-period systems increases by 10–20%**, with periods up to 100 yr causing significant deviations in low- and moderate-eccentricity binaries
- The detectability of most systems is unaffected by the light ratio, although it is reduced for twin binaries.
- The extended time baseline significantly **enhances** the detected binary population across the **main sequence** and among **young white dwarves**. 

## Document
Selected Python scripts used to generate the main figures in the paper are available in this repository and based on the following python packages:
- astromet: https://github.com/zpenoyre/astromet.py.git
- gaiascanlaw: https://github.com/zpenoyre/gaiascanlaw.git
- zplots: https://github.com/zpenoyre/zplots.git

## Citation

If you wish to use this code or paper in any way, please cite:

```bibtex
@article{Guerriero2025,
  title={Nominal thresholds for good astrometric fits, and prospects for binary detectability, for the full extended Gaia mission},
  author={Guerriero, F and Penoyre, Z and Brown, AGA},
  journal={arXiv preprint arXiv:2511.02476},
  year={2025}
}
```

Or in text form:
_Guerriero, F., Penoyre, Z., & Brown, A.G.A. (2025). Nominal thresholds for good astrometric fits, and prospects for binary detectability, for the full extended Gaia mission._
