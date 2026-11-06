**This network is not a monotone clinical risk score.** Its input effects depend on which hidden units are near their switching regions:
\[
\frac{\partial\text{log-odds}}{\partial x_i}
=\sum_j W_{2j}W_{1ji}\bigl[1-\tanh^2(W_{1j}x+b_{1j})\bigr].
\]
Consequently, large weights can be almost inactive through saturation, and opposing pathways can reverse an effect.

Specifically, units 13 and 15 strongly favor higher risk with poor WFNS grade and oppose surgery. But unit 11, whose output weight is **−2.694**, opposes their positive `l5` effects and contributes a positive `l8` effect. Other units introduce competing laboratory-dependent switches. Direct substitution reveals the nonmonotonic examples below.

Without patient data, importance rankings depend on the reference distribution. Here they are **rough influence rankings**, considering independently varying flags, laboratories spanning 0–10, and ages 20–90. “No clear effect” means mixed effects, not an unused input.

Execution was unavailable, so the surrogate is a **hand-derived, unvalidated approximation**, not a numerically fitted or accuracy-tested replacement. It uses marginal curvature and selected pairwise interactions; higher-order behavior remains missing. Repeated names in an interaction denote a square.

Finally, `surgery`, as defined, uses information from during admission—not necessarily available at admission—and its protective association is not a causal treatment effect. Coherent weights support training rather than scrambling, but cannot authenticate the claimed registry.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "large overall", "rank": 1},
    "female": {"direction": "decreases risk", "size": "small average tendency", "rank": 19},
    "wfns45": {"direction": "increases risk", "size": "very large overall", "rank": 2},
    "fisher34": {"direction": "increases risk", "size": "moderate, context dependent", "rank": 14},
    "ct_ivh": {"direction": "increases risk", "size": "moderate overall", "rank": 9},
    "ct_ich": {"direction": "increases risk", "size": "moderate, strongly conditional", "rank": 8},
    "htn": {"direction": "increases risk", "size": "moderate average tendency", "rank": 12},
    "surgery": {"direction": "decreases risk", "size": "very large overall", "rank": 3},
    "urban": {"direction": "no clear effect", "size": "small average, sign-changing", "rank": 18},
    "farmer": {"direction": "no clear effect", "size": "small average, mixed", "rank": 20},
    "l1": {"direction": "no clear effect", "size": "mixed conditional effects", "rank": 13},
    "l2": {"direction": "no clear effect", "size": "curved, weak average slope", "rank": 15},
    "l3": {"direction": "no clear effect", "size": "moderate conditional effects", "rank": 10},
    "l4": {"direction": "no clear effect", "size": "moderate conditional effects", "rank": 11},
    "l5": {"direction": "no clear effect", "size": "large, potentially nonmonotonic", "rank": 4},
    "l6": {"direction": "no clear effect", "size": "substantial conditional switches", "rank": 6},
    "l7": {"direction": "no clear effect", "size": "mixed conditional effects", "rank": 17},
    "l8": {"direction": "no clear effect", "size": "large, nonmonotonic", "rank": 5},
    "l9": {"direction": "no clear effect", "size": "substantial competing pathways", "rank": 7},
    "l10": {"direction": "no clear effect", "size": "mixed conditional effects", "rank": 16}
  },
  "unexpected": [
    {
      "inputs": ["l8"],
      "description": "A low-end dip followed by a substantial increase. With age_c=0, every binary input=0, and all other laboratories=5, network probabilities are approximately 0.067 at l8=0, 0.048 at l8=1.1, 0.209 at l8=5, and 0.371 at l8=10.",
      "where": "For this specified profile, the minimum is near l8=1.1 on its 0–10 scale. Its location changes with the other inputs."
    },
    {
      "inputs": ["l5"],
      "description": "An inverted-U relationship is possible. With age_c=0, every binary input=0, and all other laboratories=5, network probabilities are approximately 0.069 at l5=0, 0.220 at l5=6.1, and 0.141 at l5=10. Positive pathways through units 13 and 15 compete with the negative pathway through unit 11.",
      "where": "For this specified profile, risk peaks near l5=6.1. This is not a universal threshold."
    },
    {
      "inputs": ["urban", "age_c"],
      "description": "The city-residence effect can reverse sign: changing urban from 0 to 1 lowers the network prediction at age 60 but raises it at age 90, with every other binary input=0 and all laboratories=5.",
      "where": "Compare age_c=0 with age_c=3 under the specified profile; the reversal is conditional, not a population-level geographic effect."
    }
  ],
  "surrogate": {
    "intercept": -2.2715,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.5401},
      {"input": "female", "type": "linear", "coef": -0.1472},
      {"input": "wfns45", "type": "linear", "coef": 1.713},
      {"input": "fisher34", "type": "linear", "coef": 0.6133},
      {"input": "ct_ivh", "type": "linear", "coef": 0.3376},
      {"input": "ct_ich", "type": "linear", "coef": 0.6765},
      {"input": "htn", "type": "linear", "coef": 0.2968},
      {"input": "surgery", "type": "linear", "coef": -1.897},
      {"input": "urban", "type": "linear", "coef": 0.1538},
      {"input": "farmer", "type": "linear", "coef": 0.1048},
      {"input": "l1", "type": "linear", "coef": -0.0221},
      {"input": "l2", "type": "linear", "coef": -0.0483},
      {"input": "l3", "type": "linear", "coef": -0.043},
      {"input": "l4", "type": "linear", "coef": 0.0224},
      {"input": "l5", "type": "linear", "coef": -0.0718},
      {"input": "l6", "type": "linear", "coef": 0.0699},
      {"input": "l7", "type": "linear", "coef": -0.0303},
      {"input": "l8", "type": "linear", "coef": -0.0286},
      {"input": "l9", "type": "linear", "coef": 0.0221},
      {"input": "l10", "type": "linear", "coef": -0.0392},
      {"input": "age_c", "type": "hinge", "knot": -2.25, "coef": 0.0313},
      {"input": "age_c", "type": "hinge", "knot": -0.5, "coef": 0.0439},
      {"input": "age_c", "type": "hinge", "knot": 1.25, "coef": 0.0318},
      {"input": "l5", "type": "hinge", "knot": 2.5, "coef": 0.025},
      {"input": "l5", "type": "hinge", "knot": 5, "coef": 0.0658},
      {"input": "l5", "type": "hinge", "knot": 7.5, "coef": -0.09},
      {"input": "l8", "type": "hinge", "knot": 1.25, "coef": 0.1142},
      {"input": "l8", "type": "hinge", "knot": 2.5, "coef": -0.0862},
      {"input": "l8", "type": "hinge", "knot": 5, "coef": -0.0833},
      {"input": "l8", "type": "hinge", "knot": 7.5, "coef": -0.0028},
      {"input": "l9", "type": "hinge", "knot": 2.5, "coef": -0.063},
      {"input": "l9", "type": "hinge", "knot": 5, "coef": 0.019},
      {"input": "l9", "type": "hinge", "knot": 7.5, "coef": 0.05}
    ],
    "interactions": [
      {"inputs": ["age_c", "age_c"], "coef": 0.00675},
      {"inputs": ["l1", "l1"], "coef": 0.00267},
      {"inputs": ["l2", "l2"], "coef": 0.00823},
      {"inputs": ["l3", "l3"], "coef": -0.004125},
      {"inputs": ["l4", "l4"], "coef": 0.00672},
      {"inputs": ["l6", "l6"], "coef": -0.00285},
      {"inputs": ["l7", "l7"], "coef": 0.004235},
      {"inputs": ["age_c", "wfns45"], "coef": -0.042},
      {"inputs": ["age_c", "fisher34"], "coef": -0.034},
      {"inputs": ["age_c", "surgery"], "coef": 0.03},
      {"inputs": ["age_c", "farmer"], "coef": 0.051},
      {"inputs": ["age_c", "l1"], "coef": -0.0058},
      {"inputs": ["age_c", "l3"], "coef": -0.0093},
      {"inputs": ["age_c", "l4"], "coef": 0.0111},
      {"inputs": ["age_c", "l6"], "coef": -0.0123},
      {"inputs": ["age_c", "l7"], "coef": 0.0077},
      {"inputs": ["age_c", "l9"], "coef": -0.0198},
      {"inputs": ["age_c", "l10"], "coef": 0.0095},
      {"inputs": ["age_c", "ct_ich"], "coef": 0.10735},
      {"inputs": ["age_c", "ct_ich"], "knots": [-2.25, 0], "coef": -0.0626},
      {"inputs": ["age_c", "ct_ich"], "knots": [-0.5, 0], "coef": -0.0877},
      {"inputs": ["age_c", "ct_ich"], "knots": [1.25, 0], "coef": -0.0635},
      {"inputs": ["wfns45", "female"], "coef": -0.086},
      {"inputs": ["wfns45", "fisher34"], "coef": -0.142},
      {"inputs": ["wfns45", "ct_ivh"], "coef": 0.071},
      {"inputs": ["wfns45", "ct_ich"], "coef": 0.053},
      {"inputs": ["wfns45", "htn"], "coef": 0.053},
      {"inputs": ["wfns45", "farmer"], "coef": 0.063},
      {"inputs": ["wfns45", "l1"], "coef": -0.026},
      {"inputs": ["wfns45", "l3"], "coef": 0.023},
      {"inputs": ["wfns45", "l5"], "coef": 0.022},
      {"inputs": ["wfns45", "l9"], "coef": 0.025},
      {"inputs": ["surgery", "female"], "coef": 0.085},
      {"inputs": ["surgery", "fisher34"], "coef": 0.042},
      {"inputs": ["surgery", "ct_ich"], "coef": -0.061},
      {"inputs": ["surgery", "farmer"], "coef": -0.052},
      {"inputs": ["surgery", "l6"], "coef": 0.021},
      {"inputs": ["fisher34", "l8"], "coef": -0.042},
      {"inputs": ["ct_ivh", "l8"], "coef": 0.031},
      {"inputs": ["l1", "l2"], "coef": 0.0037},
      {"inputs": ["l1", "l3"], "coef": 0.004},
      {"inputs": ["l1", "l4"], "coef": -0.0031},
      {"inputs": ["l1", "l7"], "coef": 0.0048},
      {"inputs": ["l1", "l8"], "coef": -0.0051},
      {"inputs": ["l1", "l10"], "coef": -0.0036},
      {"inputs": ["l2", "l3"], "coef": 0.0037},
      {"inputs": ["l2", "l4"], "coef": -0.0036},
      {"inputs": ["l2", "l7"], "coef": -0.0048},
      {"inputs": ["l2", "l8"], "coef": -0.007},
      {"inputs": ["l3", "l6"], "coef": -0.0101},
      {"inputs": ["l3", "l7"], "coef": 0.0039},
      {"inputs": ["l3", "l8"], "coef": 0.0035},
      {"inputs": ["l3", "l9"], "coef": 0.0054},
      {"inputs": ["l4", "l5"], "coef": -0.0037},
      {"inputs": ["l4", "l6"], "coef": -0.0103},
      {"inputs": ["l4", "l10"], "coef": 0.0033},
      {"inputs": ["l5", "l6"], "coef": 0.0038},
      {"inputs": ["l5", "l7"], "coef": 0.0064},
      {"inputs": ["l6", "l7"], "coef": -0.0063},
      {"inputs": ["l6", "l8"], "coef": 0.0042},
      {"inputs": ["l6", "l10"], "coef": 0.0032},
      {"inputs": ["l7", "l8"], "coef": 0.0045},
      {"inputs": ["l7", "l9"], "coef": -0.0085},
      {"inputs": ["l9", "l10"], "coef": 0.0034},
      {"inputs": ["l5", "l8"], "coef": 0.0014},
      {"inputs": ["l5", "l8"], "knots": [0, 2.5], "coef": 0.0474},
      {"inputs": ["l5", "l8"], "knots": [0, 5], "coef": -0.0001},
      {"inputs": ["l5", "l8"], "knots": [0, 7.5], "coef": -0.0093},
      {"inputs": ["l5", "l8"], "knots": [5, 0], "coef": -0.0105},
      {"inputs": ["l5", "l8"], "knots": [5, 2.5], "coef": -0.0265},
      {"inputs": ["l5", "l8"], "knots": [5, 5], "coef": 0.0465},
      {"inputs": ["l5", "l8"], "knots": [5, 7.5], "coef": -0.0094}
    ]
  },
  "confidence_trained": 0.95
}
```