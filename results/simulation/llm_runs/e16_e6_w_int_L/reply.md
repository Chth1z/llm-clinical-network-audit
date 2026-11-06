**Reference for approximation:** age centred at 60 years with SD 15 years; independent, balanced binary inputs; independent laboratories spanning 0–10.

The dominant weight-derived pattern is higher predicted risk with WFNS 4–5 and age, and lower risk with treatment. Approximate log-odds changes are +1.9 for WFNS 4–5, −1.7 for treatment, and +0.45 per decade.

The important departure from an additive score is **the interaction between l5 and l8**. Their effects can change sign depending on each other. Higher l8 also attenuates the WFNS contrast. Sex, residence and occupation have comparatively small average effects.

Below is a smoothed, low-order approximation, including laboratory curvature. It matches the network’s approximately **35.7%** prediction at the input centroid. Its hinge knots approximate smooth changes; the original network has no sharp thresholds. Rankings and directions describe the stated reference distribution, with “no clear effect” covering weak or sign-changing relationships.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "~0.45 log-odds per decade", "rank": 3},
    "female": {"direction": "no clear effect", "size": "very small average effect", "rank": 20},
    "wfns45": {"direction": "increases risk", "size": "large; ~1.9 log-odds", "rank": 1},
    "fisher34": {"direction": "increases risk", "size": "~0.48 log-odds", "rank": 6},
    "ct_ivh": {"direction": "increases risk", "size": "~0.42 log-odds", "rank": 7},
    "ct_ich": {"direction": "increases risk", "size": "~0.36 log-odds", "rank": 9},
    "htn": {"direction": "increases risk", "size": "~0.36 log-odds", "rank": 8},
    "surgery": {"direction": "decreases risk", "size": "large; ~1.7 log-odds reduction", "rank": 2},
    "urban": {"direction": "no clear effect", "size": "very small average effect", "rank": 17},
    "farmer": {"direction": "no clear effect", "size": "very small average effect", "rank": 19},
    "l1": {"direction": "no clear effect", "size": "small, context-dependent", "rank": 16},
    "l2": {"direction": "decreases risk", "size": "small average decrease", "rank": 12},
    "l3": {"direction": "decreases risk", "size": "small average decrease", "rank": 10},
    "l4": {"direction": "no clear effect", "size": "small, curved effect", "rank": 11},
    "l5": {"direction": "no clear effect", "size": "substantial; depends on l8", "rank": 4},
    "l6": {"direction": "no clear effect", "size": "small, curved effect", "rank": 15},
    "l7": {"direction": "no clear effect", "size": "small, curved effect", "rank": 13},
    "l8": {"direction": "no clear effect", "size": "substantial; depends on l5", "rank": 5},
    "l9": {"direction": "no clear effect", "size": "very small average effect", "rank": 18},
    "l10": {"direction": "no clear effect", "size": "small, curved effect", "rank": 14}
  },
  "unexpected": [
    {
      "inputs": ["l5", "l8"],
      "description": "Positive interaction: increasing l8 can lower predicted risk when l5 is low but raise it when l5 is high. The effect of l5 likewise depends on l8.",
      "where": "Across their 0–10 ranges; the approximate l8 sign reversal occurs around l5=2–3 at reference settings, shifting with WFNS and treatment."
    },
    {
      "inputs": ["wfns45", "l8"],
      "description": "Higher l8 attenuates the increase associated with WFNS 4–5 rather than contributing independently.",
      "where": "Across l8=0–10; approximately 0.55 log-odds attenuation in the surrogate."
    }
  ],
  "surrogate": {
    "intercept": -2.3165,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.449},
      {"input": "female", "type": "linear", "coef": 0.023},
      {"input": "wfns45", "type": "linear", "coef": 2.077},
      {"input": "fisher34", "type": "linear", "coef": 0.478},
      {"input": "ct_ivh", "type": "linear", "coef": 0.417},
      {"input": "ct_ich", "type": "linear", "coef": 0.355},
      {"input": "htn", "type": "linear", "coef": 0.359},
      {"input": "surgery", "type": "linear", "coef": -1.921},
      {"input": "urban", "type": "linear", "coef": 0.045},
      {"input": "farmer", "type": "linear", "coef": 0.032},
      {"input": "l1", "type": "linear", "coef": 0.0254},
      {"input": "l2", "type": "linear", "coef": -0.021},
      {"input": "l3", "type": "linear", "coef": -0.0196},
      {"input": "l4", "type": "linear", "coef": 0.0208},
      {"input": "l5", "type": "linear", "coef": 0.0248},
      {"input": "l6", "type": "linear", "coef": 0.037},
      {"input": "l7", "type": "linear", "coef": 0.0674},
      {"input": "l8", "type": "linear", "coef": -0.0331},
      {"input": "l9", "type": "linear", "coef": 0.007},
      {"input": "l10", "type": "linear", "coef": 0.0218},

      {"input": "l1", "type": "hinge", "knot": 2, "coef": -0.0112},
      {"input": "l1", "type": "hinge", "knot": 4, "coef": -0.0112},
      {"input": "l1", "type": "hinge", "knot": 6, "coef": -0.0112},
      {"input": "l1", "type": "hinge", "knot": 8, "coef": -0.0112},

      {"input": "l3", "type": "hinge", "knot": 2, "coef": -0.0082},
      {"input": "l3", "type": "hinge", "knot": 4, "coef": -0.0082},
      {"input": "l3", "type": "hinge", "knot": 6, "coef": -0.0082},
      {"input": "l3", "type": "hinge", "knot": 8, "coef": -0.0082},

      {"input": "l4", "type": "hinge", "knot": 2, "coef": -0.0194},
      {"input": "l4", "type": "hinge", "knot": 4, "coef": -0.0194},
      {"input": "l4", "type": "hinge", "knot": 6, "coef": -0.0194},
      {"input": "l4", "type": "hinge", "knot": 8, "coef": -0.0194},

      {"input": "l5", "type": "hinge", "knot": 2, "coef": -0.0244},
      {"input": "l5", "type": "hinge", "knot": 4, "coef": -0.0244},
      {"input": "l5", "type": "hinge", "knot": 6, "coef": -0.0244},
      {"input": "l5", "type": "hinge", "knot": 8, "coef": -0.0244},

      {"input": "l6", "type": "hinge", "knot": 2, "coef": -0.023},
      {"input": "l6", "type": "hinge", "knot": 4, "coef": -0.023},
      {"input": "l6", "type": "hinge", "knot": 6, "coef": -0.023},
      {"input": "l6", "type": "hinge", "knot": 8, "coef": -0.023},

      {"input": "l7", "type": "hinge", "knot": 2, "coef": -0.0302},
      {"input": "l7", "type": "hinge", "knot": 4, "coef": -0.0302},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": -0.0302},
      {"input": "l7", "type": "hinge", "knot": 8, "coef": -0.0302},

      {"input": "l8", "type": "hinge", "knot": 2, "coef": -0.0092},
      {"input": "l8", "type": "hinge", "knot": 4, "coef": -0.0092},
      {"input": "l8", "type": "hinge", "knot": 6, "coef": -0.0092},
      {"input": "l8", "type": "hinge", "knot": 8, "coef": -0.0092},

      {"input": "l10", "type": "hinge", "knot": 2, "coef": -0.0184},
      {"input": "l10", "type": "hinge", "knot": 4, "coef": -0.0184},
      {"input": "l10", "type": "hinge", "knot": 6, "coef": -0.0184},
      {"input": "l10", "type": "hinge", "knot": 8, "coef": -0.0184}
    ],
    "interactions": [
      {"inputs": ["l5", "l8"], "coef": 0.03},
      {"inputs": ["wfns45", "surgery"], "coef": 0.2},
      {"inputs": ["wfns45", "l8"], "coef": -0.055},
      {"inputs": ["surgery", "l8"], "coef": 0.022}
    ]
  },
  "confidence_trained": 0.99
}
```