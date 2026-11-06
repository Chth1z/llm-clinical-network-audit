The network is **not a monotone clinical risk score**. Units 13 and 15 strongly favour higher risk with poor WFNS grade and lower risk with treatment. But other units oppose these effects. In particular, unit 11 contributes  
\(-2.694\tanh(\ldots+0.1776\,l5-0.2209\,l8)\), creating substantial laboratory-dependent reversals. The low-\(l8\) transition in unit 9 adds another reversal.

For the examples below, **reference R** means age 60, every binary input zero, and every laboratory value not being varied equal to 5. The reported example probabilities are evaluations of the supplied network—not the surrogate.

There is no distribution-independent importance ranking or optimal approximation. The ranks and surrogate below are approximate, using an independent, uniformly weighted working domain: ages 20–100, binary inputs 0/1, and laboratories 0–10. The surrogate is an **analytic low-order approximation, not a numerically validated fit**; it cannot preserve every conditional reversal.

Also, `surgery` describes treatment during admission: this is not strictly an admission-only predictor, and its coefficient is not a causal treatment effect. Training confidence is subjective, not verification of the claimed provenance.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "large across adult ages", "rank": 1},
    "female": {"direction": "decreases risk", "size": "small overall", "rank": 18},
    "wfns45": {"direction": "increases risk", "size": "large", "rank": 2},
    "fisher34": {"direction": "increases risk", "size": "small to moderate", "rank": 12},
    "ct_ivh": {"direction": "increases risk", "size": "moderate overall", "rank": 8},
    "ct_ich": {"direction": "no clear effect", "size": "moderate, sign-changing", "rank": 9},
    "htn": {"direction": "increases risk", "size": "small to moderate", "rank": 13},
    "surgery": {"direction": "decreases risk", "size": "large overall", "rank": 3},
    "urban": {"direction": "no clear effect", "size": "small, context-dependent", "rank": 19},
    "farmer": {"direction": "no clear effect", "size": "small, context-dependent", "rank": 20},
    "l1": {"direction": "no clear effect", "size": "small average, conditional", "rank": 14},
    "l2": {"direction": "no clear effect", "size": "small average, nonlinear", "rank": 16},
    "l3": {"direction": "no clear effect", "size": "moderate, context-dependent", "rank": 10},
    "l4": {"direction": "no clear effect", "size": "moderate, context-dependent", "rank": 11},
    "l5": {"direction": "no clear effect", "size": "large, sign-changing", "rank": 5},
    "l6": {"direction": "no clear effect", "size": "moderate, non-monotone", "rank": 6},
    "l7": {"direction": "no clear effect", "size": "small average, conditional", "rank": 17},
    "l8": {"direction": "increases risk", "size": "large overall, low-end reversal", "rank": 4},
    "l9": {"direction": "no clear effect", "size": "moderate, context-dependent", "rank": 7},
    "l10": {"direction": "no clear effect", "size": "small average, conditional", "rank": 15}
  },
  "unexpected": [
    {
      "inputs": ["l5", "l8"],
      "description": "l5 is not uniformly harmful: its positive contributions through units 13 and 15 compete with a negative contribution through unit 11. At R, increasing l5 eventually reduces risk: probabilities are approximately 0.069 at l5=0, 0.220 near l5=6.1, and 0.141 at l5=10. The reversal moves when l8 or other inputs change.",
      "where": "At R with l8=5, the upper turning point is approximately l5=6.1 on its 0–10 scale; this is not a universal cutoff."
    },
    {
      "inputs": ["l8"],
      "description": "Despite its positive overall effect, l8 has a low-end risk dip. At R, probabilities are approximately 0.067 at l8=0, 0.048 near l8=1.1, and 0.371 at l8=10.",
      "where": "At R, the low-end minimum is near l8=1.1; its location depends on the remaining inputs."
    },
    {
      "inputs": ["l6"],
      "description": "There can be an interior risk maximum rather than a monotone laboratory effect. At R, probabilities are approximately 0.104 at l6=0, 0.209 at l6=5, and 0.084 at l6=10.",
      "where": "At R, the maximum is around l6=5.1 on its 0–10 scale; other profiles shift or remove it."
    },
    {
      "inputs": ["ct_ich", "surgery"],
      "description": "The ICH effect can reverse with treatment status. At the reference profile, changing ct_ich from 0 to 1 changes log-odds by approximately -0.03 without surgery but +0.72 with surgery. This is a predictive interaction, not evidence of treatment harm.",
      "where": "Compare ct_ich=0 versus 1 at R, separately with surgery=0 and surgery=1."
    }
  ],
  "surrogate": {
    "intercept": -1.7205,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.5},
      {"input": "female", "type": "linear", "coef": -0.15},
      {"input": "wfns45", "type": "linear", "coef": 1.93},
      {"input": "fisher34", "type": "linear", "coef": 0.36},
      {"input": "ct_ivh", "type": "linear", "coef": 0.54},
      {"input": "ct_ich", "type": "linear", "coef": 0.39},
      {"input": "htn", "type": "linear", "coef": 0.32},
      {"input": "surgery", "type": "linear", "coef": -1.77},
      {"input": "urban", "type": "linear", "coef": 0.16},
      {"input": "farmer", "type": "linear", "coef": 0.11},
      {"input": "l1", "type": "linear", "coef": -0.0375},
      {"input": "l2", "type": "linear", "coef": -0.03775},
      {"input": "l3", "type": "linear", "coef": -0.0605},
      {"input": "l4", "type": "linear", "coef": 0.031},
      {"input": "l5", "type": "linear", "coef": -0.1267},
      {"input": "l6", "type": "linear", "coef": 0.04225},
      {"input": "l7", "type": "linear", "coef": -0.001},
      {"input": "l8", "type": "linear", "coef": -0.2142},
      {"input": "l9", "type": "linear", "coef": -0.019},
      {"input": "l10", "type": "linear", "coef": -0.042},
      {"input": "l1", "type": "hinge", "knot": 2.5, "coef": 0.013},
      {"input": "l1", "type": "hinge", "knot": 5, "coef": 0.013},
      {"input": "l1", "type": "hinge", "knot": 7.5, "coef": 0.013},
      {"input": "l2", "type": "hinge", "knot": 2.5, "coef": 0.0385},
      {"input": "l2", "type": "hinge", "knot": 5, "coef": 0.0385},
      {"input": "l2", "type": "hinge", "knot": 7.5, "coef": 0.0385},
      {"input": "l3", "type": "hinge", "knot": 2.5, "coef": -0.02},
      {"input": "l3", "type": "hinge", "knot": 5, "coef": -0.02},
      {"input": "l3", "type": "hinge", "knot": 7.5, "coef": -0.02},
      {"input": "l4", "type": "hinge", "knot": 2.5, "coef": 0.034},
      {"input": "l4", "type": "hinge", "knot": 5, "coef": 0.034},
      {"input": "l4", "type": "hinge", "knot": 7.5, "coef": 0.034},
      {"input": "l5", "type": "hinge", "knot": 2.5, "coef": 0.0416},
      {"input": "l5", "type": "hinge", "knot": 5, "coef": -0.0096},
      {"input": "l5", "type": "hinge", "knot": 7.5, "coef": -0.0864},
      {"input": "l6", "type": "hinge", "knot": 2.5, "coef": -0.0135},
      {"input": "l6", "type": "hinge", "knot": 5, "coef": -0.0135},
      {"input": "l6", "type": "hinge", "knot": 7.5, "coef": -0.0135},
      {"input": "l7", "type": "hinge", "knot": 2.5, "coef": 0.022},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": 0.022},
      {"input": "l7", "type": "hinge", "knot": 7.5, "coef": 0.022},
      {"input": "l8", "type": "hinge", "knot": 1.25, "coef": 0.1072},
      {"input": "l8", "type": "hinge", "knot": 2.5, "coef": 0.1336},
      {"input": "l8", "type": "hinge", "knot": 5, "coef": -0.0068},
      {"input": "l8", "type": "hinge", "knot": 7.5, "coef": -0.0664},
      {"input": "l9", "type": "hinge", "knot": 2.5, "coef": -0.007},
      {"input": "l9", "type": "hinge", "knot": 5, "coef": -0.007},
      {"input": "l9", "type": "hinge", "knot": 7.5, "coef": -0.007},
      {"input": "l10", "type": "hinge", "knot": 2.5, "coef": -0.003},
      {"input": "l10", "type": "hinge", "knot": 5, "coef": -0.003},
      {"input": "l10", "type": "hinge", "knot": 7.5, "coef": -0.003}
    ],
    "interactions": [
      {"inputs": ["l1", "l2"], "coef": 0.0039},
      {"inputs": ["l1", "l3"], "coef": 0.0038},
      {"inputs": ["l1", "l4"], "coef": -0.0032},
      {"inputs": ["l1", "l5"], "coef": 0.0021},
      {"inputs": ["l1", "l6"], "coef": -0.0007},
      {"inputs": ["l1", "l7"], "coef": 0.0046},
      {"inputs": ["l1", "l8"], "coef": -0.0042},
      {"inputs": ["l1", "l9"], "coef": 0.0001},
      {"inputs": ["l1", "l10"], "coef": -0.0036},
      {"inputs": ["l2", "l3"], "coef": 0.004},
      {"inputs": ["l2", "l4"], "coef": -0.0035},
      {"inputs": ["l2", "l5"], "coef": 0.0007},
      {"inputs": ["l2", "l6"], "coef": 0.0016},
      {"inputs": ["l2", "l7"], "coef": -0.0046},
      {"inputs": ["l2", "l8"], "coef": -0.007},
      {"inputs": ["l2", "l9"], "coef": -0.0016},
      {"inputs": ["l2", "l10"], "coef": 0.0013},
      {"inputs": ["l3", "l4"], "coef": 0.001},
      {"inputs": ["l3", "l5"], "coef": -0.001},
      {"inputs": ["l3", "l6"], "coef": -0.0082},
      {"inputs": ["l3", "l7"], "coef": 0.0034},
      {"inputs": ["l3", "l8"], "coef": 0.0031},
      {"inputs": ["l3", "l9"], "coef": 0.0062},
      {"inputs": ["l3", "l10"], "coef": 0.0016},
      {"inputs": ["l4", "l5"], "coef": -0.0037},
      {"inputs": ["l4", "l6"], "coef": -0.0111},
      {"inputs": ["l4", "l7"], "coef": 0.0004},
      {"inputs": ["l4", "l8"], "coef": -0.0004},
      {"inputs": ["l4", "l9"], "coef": 0.0013},
      {"inputs": ["l4", "l10"], "coef": 0.0032},
      {"inputs": ["l5", "l6"], "coef": 0.0053},
      {"inputs": ["l5", "l7"], "coef": 0.0052},
      {"inputs": ["l5", "l8"], "coef": 0.0319},
      {"inputs": ["l5", "l9"], "coef": 0.0025},
      {"inputs": ["l5", "l10"], "coef": 0.0013},
      {"inputs": ["l6", "l7"], "coef": -0.0068},
      {"inputs": ["l6", "l8"], "coef": 0.0037},
      {"inputs": ["l6", "l9"], "coef": 0.003},
      {"inputs": ["l6", "l10"], "coef": 0.003},
      {"inputs": ["l7", "l8"], "coef": 0.0049},
      {"inputs": ["l7", "l9"], "coef": -0.0092},
      {"inputs": ["l7", "l10"], "coef": -0.0017},
      {"inputs": ["l8", "l9"], "coef": 0.0021},
      {"inputs": ["l8", "l10"], "coef": -0.0015},
      {"inputs": ["l9", "l10"], "coef": 0.0039}
    ]
  },
  "confidence_trained": 0.95
}
```