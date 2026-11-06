The weights do **not** imply fixed effects or constant odds ratios. Each input’s log-odds derivative is
\[
\sum_j W_{2j}W_{1ji}\left[1-\tanh^2(W_{1j}x+b_{1j})\right],
\]
so saturation and cancellation matter.

The strongest distinctive feature is the fourth hidden unit: **−1.858 × tanh(4.102 − 0.5869 × l3 + other terms)**. It produces a substantial high-l3 risk increase. Other units also create nonmonotonic laboratory effects and even hypertension sign reversals; concrete examples appear below.

Directions and ranks summarize broad-domain behavior, not universal monotonicity. The surrogate is an **analytic, low-order approximation**, assuming broadly distributed laboratories, balanced binary inputs, and ages approximately 20–100. I have not measured its prediction error; it cannot reproduce every higher-order interaction.

Despite the admission-only premise, “surgery” describes treatment during admission. Its protective prediction is neither an admission-available measurement nor evidence of a causal treatment benefit.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "substantial; approximately 0.5 log-odds/decade", "rank": 2},
    "female": {"direction": "no clear effect", "size": "small average; context-dependent", "rank": 20},
    "wfns45": {"direction": "increases risk", "size": "large; approximately 1.8 log-odds", "rank": 3},
    "fisher34": {"direction": "increases risk", "size": "moderate; approximately 0.4 log-odds", "rank": 7},
    "ct_ivh": {"direction": "increases risk", "size": "moderate; approximately 0.55 log-odds", "rank": 5},
    "ct_ich": {"direction": "increases risk", "size": "moderate; approximately 0.47 log-odds", "rank": 6},
    "htn": {"direction": "increases risk", "size": "modest average; sometimes reverses", "rank": 8},
    "surgery": {"direction": "decreases risk", "size": "large; approximately -1.7 log-odds", "rank": 4},
    "urban": {"direction": "no clear effect", "size": "cancelling, context-dependent effects", "rank": 16},
    "farmer": {"direction": "no clear effect", "size": "small average; context-dependent", "rank": 19},
    "l1": {"direction": "no clear effect", "size": "weak marginal; conditional variation", "rank": 12},
    "l2": {"direction": "no clear effect", "size": "nonmonotonic, context-dependent", "rank": 15},
    "l3": {"direction": "increases risk", "size": "dominant high-end rise; nonmonotonic", "rank": 1},
    "l4": {"direction": "no clear effect", "size": "weak marginal; conditional variation", "rank": 17},
    "l5": {"direction": "no clear effect", "size": "nonlinear, interacting effects", "rank": 9},
    "l6": {"direction": "no clear effect", "size": "nonlinear, interacting effects", "rank": 10},
    "l7": {"direction": "no clear effect", "size": "weak marginal; conditional variation", "rank": 18},
    "l8": {"direction": "no clear effect", "size": "weak marginal; conditional variation", "rank": 14},
    "l9": {"direction": "no clear effect", "size": "weak marginal; conditional variation", "rank": 13},
    "l10": {"direction": "no clear effect", "size": "nonlinear; interacts with l3", "rank": 11}
  },
  "unexpected": [
    {
      "inputs": ["l3"],
      "description": "A pronounced high-end upturn, but not uniformly increasing risk. In the reference setting, l3 values 0, 5, and 10 produce network probabilities approximately 0.13, 0.04, and 0.73.",
      "where": "Reference: age_c=0, all binary inputs=0, and all other laboratories=5. The fourth hidden unit crosses zero at l3 approximately 7.72; its transition shifts with other inputs."
    },
    {
      "inputs": ["l2"],
      "description": "Risk can decrease, then increase, then decrease again despite a small average effect.",
      "where": "With age_c=0, all binary inputs=0, and other laboratories=5, turning points are approximately l2=4.9 and l2=8.0."
    },
    {
      "inputs": ["htn", "wfns45", "fisher34", "ct_ich", "l2", "l6"],
      "description": "Hypertension can change from harmful to protective in the network's predictions; this is not a causal conclusion.",
      "where": "At age_c=0, other flags=0 and laboratories=5, htn 0-to-1 raises log-odds approximately 1.23. With wfns45=fisher34=ct_ich=1, l2=10, l6=0, remaining flags=0 and remaining laboratories=5, it lowers log-odds approximately 0.14."
    }
  ],
  "surrogate": {
    "intercept": -3.821,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.5306},
      {"input": "female", "type": "linear", "coef": 0.0187},
      {"input": "wfns45", "type": "linear", "coef": 1.8043},
      {"input": "fisher34", "type": "linear", "coef": 0.3994},
      {"input": "ct_ivh", "type": "linear", "coef": 0.5479},
      {"input": "ct_ich", "type": "linear", "coef": 0.4677},
      {"input": "htn", "type": "linear", "coef": 0.2835},
      {"input": "surgery", "type": "linear", "coef": -1.6649},
      {"input": "urban", "type": "linear", "coef": 0.1519},
      {"input": "farmer", "type": "linear", "coef": 0.0956},
      {"input": "l1", "type": "linear", "coef": 0.1267},
      {"input": "l2", "type": "linear", "coef": -0.0097},
      {"input": "l3", "type": "linear", "coef": 0.05348},
      {"input": "l4", "type": "linear", "coef": 0.08755},
      {"input": "l5", "type": "linear", "coef": 0.14195},
      {"input": "l6", "type": "linear", "coef": -0.00145},
      {"input": "l7", "type": "linear", "coef": -0.04014},
      {"input": "l8", "type": "linear", "coef": 0.08152},
      {"input": "l9", "type": "linear", "coef": 0.02921},
      {"input": "l10", "type": "linear", "coef": -0.07906},

      {"input": "age_c", "type": "hinge", "knot": -2, "coef": 0.02585},
      {"input": "age_c", "type": "hinge", "knot": 0, "coef": 0.02585},
      {"input": "age_c", "type": "hinge", "knot": 2, "coef": 0.02585},

      {"input": "l1", "type": "hinge", "knot": 2, "coef": -0.01588},
      {"input": "l1", "type": "hinge", "knot": 4, "coef": -0.01588},
      {"input": "l1", "type": "hinge", "knot": 6, "coef": -0.01588},
      {"input": "l1", "type": "hinge", "knot": 8, "coef": -0.01588},

      {"input": "l3", "type": "hinge", "knot": 2, "coef": 0.02737},
      {"input": "l3", "type": "hinge", "knot": 3, "coef": 0.04677},
      {"input": "l3", "type": "hinge", "knot": 4, "coef": 0.02737},
      {"input": "l3", "type": "hinge", "knot": 5, "coef": 0.14982},
      {"input": "l3", "type": "hinge", "knot": 6, "coef": 0.28158},
      {"input": "l3", "type": "hinge", "knot": 7, "coef": 0.33903},
      {"input": "l3", "type": "hinge", "knot": 8, "coef": 0.14512},
      {"input": "l3", "type": "hinge", "knot": 9, "coef": -0.25525},

      {"input": "l5", "type": "hinge", "knot": 2, "coef": -0.02988},
      {"input": "l5", "type": "hinge", "knot": 4, "coef": -0.02988},
      {"input": "l5", "type": "hinge", "knot": 6, "coef": -0.02988},
      {"input": "l5", "type": "hinge", "knot": 8, "coef": -0.02988},

      {"input": "l6", "type": "hinge", "knot": 2, "coef": -0.02622},
      {"input": "l6", "type": "hinge", "knot": 4, "coef": -0.02622},
      {"input": "l6", "type": "hinge", "knot": 6, "coef": -0.02622},
      {"input": "l6", "type": "hinge", "knot": 8, "coef": -0.02622},

      {"input": "l8", "type": "hinge", "knot": 2, "coef": -0.01655},
      {"input": "l8", "type": "hinge", "knot": 4, "coef": -0.01655},
      {"input": "l8", "type": "hinge", "knot": 6, "coef": -0.01655},
      {"input": "l8", "type": "hinge", "knot": 8, "coef": -0.01655},

      {"input": "l9", "type": "hinge", "knot": 2, "coef": -0.01796},
      {"input": "l9", "type": "hinge", "knot": 4, "coef": -0.01796},
      {"input": "l9", "type": "hinge", "knot": 6, "coef": -0.01796},
      {"input": "l9", "type": "hinge", "knot": 8, "coef": -0.01796},

      {"input": "l10", "type": "hinge", "knot": 2, "coef": 0.02059},
      {"input": "l10", "type": "hinge", "knot": 4, "coef": 0.02059},
      {"input": "l10", "type": "hinge", "knot": 6, "coef": 0.02059},
      {"input": "l10", "type": "hinge", "knot": 8, "coef": 0.02059}
    ],
    "interactions": [
      {"inputs": ["age_c", "l1"], "coef": -0.0070},
      {"inputs": ["age_c", "l3"], "coef": -0.0231},
      {"inputs": ["age_c", "l5"], "coef": 0.0112},
      {"inputs": ["age_c", "l7"], "coef": -0.0062},
      {"inputs": ["age_c", "l10"], "coef": -0.0104},

      {"inputs": ["l1", "l4"], "coef": -0.0055},
      {"inputs": ["l1", "l5"], "coef": -0.0060},
      {"inputs": ["l1", "l8"], "coef": -0.0061},
      {"inputs": ["l3", "l4"], "coef": -0.0090},
      {"inputs": ["l3", "l5"], "coef": 0.0086},
      {"inputs": ["l3", "l6"], "coef": -0.0062},
      {"inputs": ["l3", "l8"], "coef": -0.0084},
      {"inputs": ["l3", "l10"], "coef": 0.0068},
      {"inputs": ["l4", "l5"], "coef": -0.0074},
      {"inputs": ["l4", "l10"], "coef": 0.0054},
      {"inputs": ["l5", "l6"], "coef": 0.0047},
      {"inputs": ["l5", "l9"], "coef": -0.0074},
      {"inputs": ["l6", "l7"], "coef": 0.0092},
      {"inputs": ["l8", "l9"], "coef": 0.0061},

      {"inputs": ["age_c", "l3"], "knots": [-4.2, 3], "coef": 0.018750},
      {"inputs": ["age_c", "l3"], "knots": [-4.2, 5], "coef": 0.033659},
      {"inputs": ["age_c", "l3"], "knots": [-4.2, 6], "coef": 0.034337},
      {"inputs": ["age_c", "l3"], "knots": [-4.2, 7], "coef": -0.023795},
      {"inputs": ["age_c", "l3"], "knots": [-4.2, 8], "coef": -0.102860},
      {"inputs": ["age_c", "l3"], "knots": [-4.2, 9], "coef": -0.049849},

      {"inputs": ["urban", "l3"], "knots": [0, 3], "coef": -0.038109},
      {"inputs": ["urban", "l3"], "knots": [0, 5], "coef": -0.068413},
      {"inputs": ["urban", "l3"], "knots": [0, 6], "coef": -0.069791},
      {"inputs": ["urban", "l3"], "knots": [0, 7], "coef": 0.048364},
      {"inputs": ["urban", "l3"], "knots": [0, 8], "coef": 0.209066},
      {"inputs": ["urban", "l3"], "knots": [0, 9], "coef": 0.101319},

      {"inputs": ["farmer", "l3"], "knots": [0, 3], "coef": -0.022609},
      {"inputs": ["farmer", "l3"], "knots": [0, 5], "coef": -0.040588},
      {"inputs": ["farmer", "l3"], "knots": [0, 6], "coef": -0.041405},
      {"inputs": ["farmer", "l3"], "knots": [0, 7], "coef": 0.028693},
      {"inputs": ["farmer", "l3"], "knots": [0, 8], "coef": 0.124033},
      {"inputs": ["farmer", "l3"], "knots": [0, 9], "coef": 0.060110},

      {"inputs": ["l5", "l3"], "knots": [0, 3], "coef": -0.005783},
      {"inputs": ["l5", "l3"], "knots": [0, 5], "coef": -0.010382},
      {"inputs": ["l5", "l3"], "knots": [0, 6], "coef": -0.010591},
      {"inputs": ["l5", "l3"], "knots": [0, 7], "coef": 0.007339},
      {"inputs": ["l5", "l3"], "knots": [0, 8], "coef": 0.031725},
      {"inputs": ["l5", "l3"], "knots": [0, 9], "coef": 0.015375},

      {"inputs": ["l6", "l3"], "knots": [0, 3], "coef": 0.004975},
      {"inputs": ["l6", "l3"], "knots": [0, 5], "coef": 0.008931},
      {"inputs": ["l6", "l3"], "knots": [0, 6], "coef": 0.009111},
      {"inputs": ["l6", "l3"], "knots": [0, 7], "coef": -0.006314},
      {"inputs": ["l6", "l3"], "knots": [0, 8], "coef": -0.027293},
      {"inputs": ["l6", "l3"], "knots": [0, 9], "coef": -0.013227},

      {"inputs": ["l10", "l3"], "knots": [0, 3], "coef": -0.006506},
      {"inputs": ["l10", "l3"], "knots": [0, 5], "coef": -0.011680},
      {"inputs": ["l10", "l3"], "knots": [0, 6], "coef": -0.011915},
      {"inputs": ["l10", "l3"], "knots": [0, 7], "coef": 0.008257},
      {"inputs": ["l10", "l3"], "knots": [0, 8], "coef": 0.035694},
      {"inputs": ["l10", "l3"], "knots": [0, 9], "coef": 0.017298}
    ]
  },
  "confidence_trained": 0.97
}
```