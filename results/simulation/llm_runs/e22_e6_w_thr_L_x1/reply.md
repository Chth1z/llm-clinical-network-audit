The weights support strong adverse WFNS and age signals, a strong negative treatment association, and a particularly important nonlinear **l3** response. The other laboratories have much weaker, background-dependent effects; first-layer weight signs alone would be misleading.

Below is a **coarse analytical approximation, not a numerically validated distillation**. Its ranks and turning points are approximate, and its hinge knots approximate smooth changes—not actual network thresholds. The low-end l3 dip is less certain than its strong increase at higher values.

Also, `surgery` describes treatment during admission, so this is not strictly an admission-only predictor. Its association cannot establish a treatment benefit.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "moderate per decade", "rank": 4},
    "female": {"direction": "no clear effect", "size": "very small", "rank": 20},
    "wfns45": {"direction": "increases risk", "size": "large, laboratory-dependent", "rank": 2},
    "fisher34": {"direction": "increases risk", "size": "small to moderate", "rank": 9},
    "ct_ivh": {"direction": "increases risk", "size": "moderate", "rank": 5},
    "ct_ich": {"direction": "increases risk", "size": "small to moderate", "rank": 7},
    "htn": {"direction": "increases risk", "size": "small", "rank": 13},
    "surgery": {"direction": "decreases risk", "size": "large, laboratory-dependent", "rank": 3},
    "urban": {"direction": "decreases risk", "size": "small average association", "rank": 11},
    "farmer": {"direction": "decreases risk", "size": "small average association", "rank": 12},
    "l1": {"direction": "no clear effect", "size": "weak, background-dependent", "rank": 15},
    "l2": {"direction": "no clear effect", "size": "weak, background-dependent", "rank": 14},
    "l3": {"direction": "increases risk", "size": "large overall; nonlinear", "rank": 1},
    "l4": {"direction": "no clear effect", "size": "weak, background-dependent", "rank": 18},
    "l5": {"direction": "no clear effect", "size": "very weak average effect", "rank": 19},
    "l6": {"direction": "no clear effect", "size": "weak, background-dependent", "rank": 16},
    "l7": {"direction": "no clear effect", "size": "weak, background-dependent", "rank": 17},
    "l8": {"direction": "decreases risk", "size": "modest average association", "rank": 6},
    "l9": {"direction": "no clear effect", "size": "modest, background-dependent", "rank": 8},
    "l10": {"direction": "no clear effect", "size": "weak, background-dependent", "rank": 10}
  },
  "unexpected": [
    {
      "inputs": ["l3"],
      "description": "The dominant laboratory response is not well represented by a constant coefficient: the approximation has a shallow low-end dip, followed by a substantial rise and eventual flattening. The low-end turning point is particularly uncertain.",
      "where": "Approximately flat or dipping around l3=0–2; increasingly steep around 3–7; flattening toward 8–10. Locations depend on other inputs."
    },
    {
      "inputs": ["l3", "wfns45"],
      "description": "The adverse WFNS contrast is not constant: it is strongest at intermediate l3 and weaker at high l3.",
      "where": "Approximate attenuation above l3=4."
    },
    {
      "inputs": ["l3", "surgery"],
      "description": "The negative treatment association also varies with l3, becoming weaker toward the upper end.",
      "where": "Approximate attenuation above l3=3."
    },
    {
      "inputs": ["farmer"],
      "description": "A small negative conditional association appears in the approximation, rather than an adverse occupational association; this is not evidence of causal protection.",
      "where": "Changing farmer from 0 to 1."
    }
  ],
  "surrogate": {
    "intercept": -0.733,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.32},
      {"input": "female", "type": "linear", "coef": 0.01},
      {"input": "wfns45", "type": "linear", "coef": 1.52},
      {"input": "fisher34", "type": "linear", "coef": 0.25},
      {"input": "ct_ivh", "type": "linear", "coef": 0.42},
      {"input": "ct_ich", "type": "linear", "coef": 0.31},
      {"input": "htn", "type": "linear", "coef": 0.16},
      {"input": "surgery", "type": "linear", "coef": -1.60},
      {"input": "urban", "type": "linear", "coef": -0.17},
      {"input": "farmer", "type": "linear", "coef": -0.17},
      {"input": "l1", "type": "linear", "coef": -0.025},
      {"input": "l2", "type": "linear", "coef": -0.027},
      {"input": "l3", "type": "linear", "coef": -0.062},
      {"input": "l3", "type": "hinge", "knot": 1, "coef": 0.057},
      {"input": "l3", "type": "hinge", "knot": 2, "coef": 0.101},
      {"input": "l3", "type": "hinge", "knot": 3, "coef": 0.037},
      {"input": "l3", "type": "hinge", "knot": 4, "coef": 0.203},
      {"input": "l3", "type": "hinge", "knot": 5, "coef": 0.053},
      {"input": "l3", "type": "hinge", "knot": 6, "coef": 0.016},
      {"input": "l3", "type": "hinge", "knot": 7, "coef": -0.012},
      {"input": "l3", "type": "hinge", "knot": 8, "coef": -0.031},
      {"input": "l3", "type": "hinge", "knot": 9, "coef": -0.040},
      {"input": "l4", "type": "linear", "coef": -0.015},
      {"input": "l5", "type": "linear", "coef": -0.006},
      {"input": "l6", "type": "linear", "coef": -0.024},
      {"input": "l7", "type": "linear", "coef": -0.019},
      {"input": "l8", "type": "linear", "coef": -0.057},
      {"input": "l9", "type": "linear", "coef": -0.046},
      {"input": "l10", "type": "linear", "coef": -0.040}
    ],
    "interactions": [
      {"inputs": ["wfns45", "l3"], "coef": 0.10},
      {"inputs": ["wfns45", "l3"], "knots": [0, 4], "coef": -0.22},
      {"inputs": ["surgery", "l3"], "coef": -0.05},
      {"inputs": ["surgery", "l3"], "knots": [0, 3], "coef": 0.15}
    ]
  },
  "confidence_trained": 0.98
}
```