**Reference:** age 60, laboratories at 5, and binary inputs centered at 0.5. Rankings approximate variation over ages 18–90, balanced binary inputs, and laboratory ranges 0–10.

The dominant features are **l3, WFNS grade, and treatment status**. Near the reference, log-odds sensitivities are approximately +2.52 for WFNS 4–5, −2.20 for treatment, and +0.33 per decade.

**l3 is not simply monotonic:** opposing pathways produce a low-range reversal, followed by a strong increase. For example, first-layer units 10 and 11 both have negative l3 weights, but their downstream sensitivities near the reference have opposite signs, approximately −1.07 and +0.70. Farmer status also lowers the output near this reference.

The surrogate approximately matches the central log-odds, −0.65, and first-order sensitivities; its curves and interactions provide a coarser approximation elsewhere. Hinges approximate smooth responses, rather than literal cutoffs. Sizes below describe local log-odds changes; apply the logistic function to the surrogate’s output.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "moderate; about 0.33/decade", "rank": 4},
    "female": {"direction": "no clear effect", "size": "negligible near reference", "rank": 20},
    "wfns45": {"direction": "increases risk", "size": "very large; about 2.52", "rank": 2},
    "fisher34": {"direction": "increases risk", "size": "moderate; about 0.49", "rank": 9},
    "ct_ivh": {"direction": "increases risk", "size": "moderate; about 0.72", "rank": 7},
    "ct_ich": {"direction": "increases risk", "size": "small–moderate; about 0.38", "rank": 11},
    "htn": {"direction": "increases risk", "size": "small; about 0.21", "rank": 18},
    "surgery": {"direction": "decreases risk", "size": "very large; about -2.20", "rank": 3},
    "urban": {"direction": "decreases risk", "size": "small; about -0.29", "rank": 13},
    "farmer": {"direction": "decreases risk", "size": "small; about -0.29", "rank": 14},
    "l1": {"direction": "decreases risk", "size": "moderate; about -0.10/unit", "rank": 8},
    "l2": {"direction": "decreases risk", "size": "moderate; about -0.15/unit", "rank": 5},
    "l3": {"direction": "increases risk", "size": "largest; low-end reversal", "rank": 1},
    "l4": {"direction": "no clear effect", "size": "weak and context-dependent", "rank": 19},
    "l5": {"direction": "decreases risk", "size": "small; about -0.06/unit", "rank": 12},
    "l6": {"direction": "decreases risk", "size": "small and context-dependent", "rank": 16},
    "l7": {"direction": "decreases risk", "size": "small and context-dependent", "rank": 15},
    "l8": {"direction": "decreases risk", "size": "moderate; about -0.14/unit", "rank": 6},
    "l9": {"direction": "decreases risk", "size": "small and context-dependent", "rank": 17},
    "l10": {"direction": "decreases risk", "size": "small–moderate; about -0.08/unit", "rank": 10}
  },
  "unexpected": [
    {
      "inputs": ["l3"],
      "description": "A low-range reversal: increasing l3 initially lowers risk, followed by a pronounced increase. Its dominance exceeds that of the individual clinical flags.",
      "where": "At the reference profile, the minimum is approximately l3 = 2–3; the strongest rise is approximately l3 = 4–8."
    },
    {
      "inputs": ["l3", "l1", "l2", "l4", "l5", "l6", "l7", "l8", "l9", "l10"],
      "description": "The laboratory response depends on combinations of laboratory values. The l3 turning point shifts with the other inputs, and weak laboratory effects can change direction.",
      "where": "Most apparent when comparing low l3, around 0–3, with middle and upper l3 values, around 4–10."
    },
    {
      "inputs": ["farmer"],
      "description": "Farmer status lowers predicted risk near the reference profile.",
      "where": "Changing farmer from 0 to 1, with other inputs near the reference."
    }
  ],
  "surrogate": {
    "intercept": -3.4655,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.23},
      {"input": "age_c", "type": "hinge", "knot": -2, "coef": 0.105},
      {"input": "age_c", "type": "hinge", "knot": 2, "coef": -0.105},
      {"input": "female", "type": "linear", "coef": -0.02},
      {"input": "wfns45", "type": "linear", "coef": 2.523},
      {"input": "fisher34", "type": "linear", "coef": 0.488},
      {"input": "ct_ivh", "type": "linear", "coef": 0.719},
      {"input": "ct_ich", "type": "linear", "coef": 0.381},
      {"input": "htn", "type": "linear", "coef": 0.209},
      {"input": "surgery", "type": "linear", "coef": -2.202},
      {"input": "urban", "type": "linear", "coef": -0.294},
      {"input": "farmer", "type": "linear", "coef": -0.293},
      {"input": "l1", "type": "linear", "coef": 0.058611},
      {"input": "l2", "type": "linear", "coef": 0.034611},
      {"input": "l3", "type": "linear", "coef": 0.014},
      {"input": "l4", "type": "linear", "coef": 0.104611},
      {"input": "l5", "type": "linear", "coef": 0.082111},
      {"input": "l6", "type": "linear", "coef": 0.091611},
      {"input": "l7", "type": "linear", "coef": 0.089111},
      {"input": "l8", "type": "linear", "coef": 0.038611},
      {"input": "l9", "type": "linear", "coef": 0.092111},
      {"input": "l10", "type": "linear", "coef": 0.068611},
      {"input": "l3", "type": "hinge", "knot": 1, "coef": 0.364},
      {"input": "l3", "type": "hinge", "knot": 2, "coef": 0.347},
      {"input": "l3", "type": "hinge", "knot": 3, "coef": 0.332},
      {"input": "l3", "type": "hinge", "knot": 4, "coef": 0.169},
      {"input": "l3", "type": "hinge", "knot": 4.5, "coef": 0.302},
      {"input": "l3", "type": "hinge", "knot": 5, "coef": -0.866215},
      {"input": "l3", "type": "hinge", "knot": 5.5, "coef": 0.005},
      {"input": "l3", "type": "hinge", "knot": 6, "coef": -0.024},
      {"input": "l3", "type": "hinge", "knot": 7, "coef": -0.061},
      {"input": "l3", "type": "hinge", "knot": 8, "coef": -0.102},
      {"input": "l3", "type": "hinge", "knot": 9, "coef": -0.141}
    ],
    "interactions": [
      {"inputs": ["age_c", "l3"], "knots": [-4.2, 5], "coef": -0.0207},
      {"inputs": ["age_c", "l3"], "knots": [-2, 5], "coef": -0.00945},
      {"inputs": ["age_c", "l3"], "knots": [2, 5], "coef": 0.00945},
      {"inputs": ["female", "l3"], "knots": [0, 5], "coef": 0.0018},
      {"inputs": ["wfns45", "l3"], "knots": [0, 5], "coef": -0.22707},
      {"inputs": ["fisher34", "l3"], "knots": [0, 5], "coef": -0.04392},
      {"inputs": ["ct_ivh", "l3"], "knots": [0, 5], "coef": -0.06471},
      {"inputs": ["ct_ich", "l3"], "knots": [0, 5], "coef": -0.03429},
      {"inputs": ["htn", "l3"], "knots": [0, 5], "coef": -0.01881},
      {"inputs": ["surgery", "l3"], "knots": [0, 5], "coef": 0.19818},
      {"inputs": ["urban", "l3"], "knots": [0, 5], "coef": 0.02646},
      {"inputs": ["farmer", "l3"], "knots": [0, 5], "coef": 0.02637},

      {"inputs": ["l1", "l3"], "coef": -0.017856},
      {"inputs": ["l2", "l3"], "coef": -0.022656},
      {"inputs": ["l4", "l3"], "coef": -0.008656},
      {"inputs": ["l5", "l3"], "coef": -0.013156},
      {"inputs": ["l6", "l3"], "coef": -0.011256},
      {"inputs": ["l7", "l3"], "coef": -0.011756},
      {"inputs": ["l8", "l3"], "coef": -0.021856},
      {"inputs": ["l9", "l3"], "coef": -0.011156},
      {"inputs": ["l10", "l3"], "coef": -0.015856},

      {"inputs": ["l1", "l3"], "knots": [0, 5], "coef": 0.029296},
      {"inputs": ["l2", "l3"], "knots": [0, 5], "coef": 0.039376},
      {"inputs": ["l4", "l3"], "knots": [0, 5], "coef": 0.009976},
      {"inputs": ["l5", "l3"], "knots": [0, 5], "coef": 0.019426},
      {"inputs": ["l6", "l3"], "knots": [0, 5], "coef": 0.015436},
      {"inputs": ["l7", "l3"], "knots": [0, 5], "coef": 0.016486},
      {"inputs": ["l8", "l3"], "knots": [0, 5], "coef": 0.037696},
      {"inputs": ["l9", "l3"], "knots": [0, 5], "coef": 0.015226},
      {"inputs": ["l10", "l3"], "knots": [0, 5], "coef": 0.025096},

      {"inputs": ["l1", "l2"], "coef": -0.001833333},
      {"inputs": ["l1", "l4"], "coef": -0.001833333},
      {"inputs": ["l1", "l5"], "coef": -0.001833333},
      {"inputs": ["l1", "l6"], "coef": -0.001833333},
      {"inputs": ["l1", "l7"], "coef": -0.001833333},
      {"inputs": ["l1", "l8"], "coef": -0.001833333},
      {"inputs": ["l1", "l9"], "coef": -0.001833333},
      {"inputs": ["l1", "l10"], "coef": -0.001833333},
      {"inputs": ["l2", "l4"], "coef": -0.001833333},
      {"inputs": ["l2", "l5"], "coef": -0.001833333},
      {"inputs": ["l2", "l6"], "coef": -0.001833333},
      {"inputs": ["l2", "l7"], "coef": -0.001833333},
      {"inputs": ["l2", "l8"], "coef": -0.001833333},
      {"inputs": ["l2", "l9"], "coef": -0.001833333},
      {"inputs": ["l2", "l10"], "coef": -0.001833333},
      {"inputs": ["l4", "l5"], "coef": -0.001833333},
      {"inputs": ["l4", "l6"], "coef": -0.001833333},
      {"inputs": ["l4", "l7"], "coef": -0.001833333},
      {"inputs": ["l4", "l8"], "coef": -0.001833333},
      {"inputs": ["l4", "l9"], "coef": -0.001833333},
      {"inputs": ["l4", "l10"], "coef": -0.001833333},
      {"inputs": ["l5", "l6"], "coef": -0.001833333},
      {"inputs": ["l5", "l7"], "coef": -0.001833333},
      {"inputs": ["l5", "l8"], "coef": -0.001833333},
      {"inputs": ["l5", "l9"], "coef": -0.001833333},
      {"inputs": ["l5", "l10"], "coef": -0.001833333},
      {"inputs": ["l6", "l7"], "coef": -0.001833333},
      {"inputs": ["l6", "l8"], "coef": -0.001833333},
      {"inputs": ["l6", "l9"], "coef": -0.001833333},
      {"inputs": ["l6", "l10"], "coef": -0.001833333},
      {"inputs": ["l7", "l8"], "coef": -0.001833333},
      {"inputs": ["l7", "l9"], "coef": -0.001833333},
      {"inputs": ["l7", "l10"], "coef": -0.001833333},
      {"inputs": ["l8", "l9"], "coef": -0.001833333},
      {"inputs": ["l8", "l10"], "coef": -0.001833333},
      {"inputs": ["l9", "l10"], "coef": -0.001833333}
    ]
  },
  "confidence_trained": 0.99
}
```