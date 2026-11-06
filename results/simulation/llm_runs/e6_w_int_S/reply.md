This is **not a monotone clinical risk score**. Each hidden unit applies a soft threshold to a combination of inputs. Its exact sensitivity is
\[
\frac{\partial\,\text{log-odds}}{\partial x_i}
=\sum_j W_{2j}W_{1ji}\bigl[1-\tanh^2((W_1x+b_1)_j)\bigr].
\]
Thus, an input’s effect changes when other inputs activate or saturate these thresholds.

Units 11, 13 and 15 have particularly large output weights: −2.694, +2.117 and +2.147. Their competing contributions produce nonlinear laboratory effects. Poor WFNS grade, older age and conservative management generally raise predictions, but even the direction of the ICH effect can reverse.

Below, directions and ranks are **approximate overall tendencies**, not guarantees. The surrogate is an analytically constructed pairwise-spline approximation, using balanced binary inputs, laboratories spanning 0–10 and ages roughly 30–90 as a reference. **I have not numerically validated its prediction error**; it cannot exactly reproduce the network’s higher-order interactions.

For the numerical examples, the reference patient has age_c=0, surgery=1, all other binary inputs=0, and all laboratories=5 unless changed. Laboratory identities are unknown, so these are numerical relationships, not biological explanations. Also, surgery occurs during admission: its association is neither an admission-only predictor nor a causal treatment effect.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "large overall", "rank": 3},
    "female": {"direction": "decreases risk", "size": "small, conditional", "rank": 16},
    "wfns45": {"direction": "increases risk", "size": "very large overall", "rank": 1},
    "fisher34": {"direction": "increases risk", "size": "moderate, conditional", "rank": 10},
    "ct_ivh": {"direction": "increases risk", "size": "moderate overall", "rank": 6},
    "ct_ich": {"direction": "increases risk", "size": "moderate; sometimes reverses", "rank": 7},
    "htn": {"direction": "increases risk", "size": "small to moderate", "rank": 11},
    "surgery": {"direction": "decreases risk", "size": "very large overall", "rank": 2},
    "urban": {"direction": "no clear effect", "size": "small, competing contributions", "rank": 17},
    "farmer": {"direction": "increases risk", "size": "small, conditional", "rank": 18},
    "l1": {"direction": "no clear effect", "size": "small net effect", "rank": 20},
    "l2": {"direction": "no clear effect", "size": "small, nonlinear", "rank": 15},
    "l3": {"direction": "no clear effect", "size": "context-dependent, mixed", "rank": 12},
    "l4": {"direction": "no clear effect", "size": "small, nonlinear", "rank": 14},
    "l5": {"direction": "increases risk", "size": "moderate overall; non-monotone", "rank": 5},
    "l6": {"direction": "no clear effect", "size": "moderate, interacting", "rank": 8},
    "l7": {"direction": "no clear effect", "size": "context-dependent, mixed", "rank": 13},
    "l8": {"direction": "increases risk", "size": "large overall; strongly conditional", "rank": 4},
    "l9": {"direction": "no clear effect", "size": "moderate, interacting", "rank": 9},
    "l10": {"direction": "no clear effect", "size": "small net effect", "rank": 19}
  },
  "unexpected": [
    {
      "inputs": ["l5"],
      "description": "The response is not monotonically increasing. For the reference patient, predicted probabilities are approximately 0.0096, 0.0057, 0.0328 and 0.0235 at l5 values 0, 1, 7 and 10 respectively.",
      "where": "Reference profile: a low-end dip around l5=1 and a peak around l5=7-8. These turning points move with the other inputs."
    },
    {
      "inputs": ["l8", "l5"],
      "description": "l8 has a low-end dip, and its higher-range effect can reverse with l5. For the reference patient, probabilities at l8=0, 1 and 5 are approximately 0.0061, 0.0043 and 0.0235. Increasing l8 from 5 to 10 raises risk when l5=5, but lowers it when l5=0.",
      "where": "Reference profile: the low-end dip occurs near l8=1. For l8 increasing from 5 to 10, probability changes approximately 0.0235 to 0.0483 at l5=5, versus 0.0096 to 0.0040 at l5=0."
    },
    {
      "inputs": ["ct_ich", "surgery"],
      "description": "ICH is not uniformly harmful in this network. For the reference patient with surgery changed to 0, switching ct_ich from 0 to 1 slightly lowers predicted probability, approximately 0.209 to 0.205. With surgery=1, the same ICH switch increases the prediction.",
      "where": "Age 60, all laboratories=5, other binary inputs=0; compare ct_ich=0 versus 1 separately at surgery=0 and surgery=1."
    }
  ],
  "surrogate": {
    "intercept": -2.221266,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.60738},
      {"input": "female", "type": "linear", "coef": -0.153011},
      {"input": "wfns45", "type": "linear", "coef": 1.608078},
      {"input": "fisher34", "type": "linear", "coef": 0.556985},
      {"input": "ct_ivh", "type": "linear", "coef": 0.381299},
      {"input": "ct_ich", "type": "linear", "coef": 0.293141},
      {"input": "htn", "type": "linear", "coef": 0.245922},
      {"input": "surgery", "type": "linear", "coef": -1.978795},
      {"input": "urban", "type": "linear", "coef": 0.14556},
      {"input": "farmer", "type": "linear", "coef": 0.108262},
      {"input": "l1", "type": "linear", "coef": -0.048841},
      {"input": "l2", "type": "linear", "coef": -0.033984},
      {"input": "l3", "type": "linear", "coef": 0.010187},
      {"input": "l4", "type": "linear", "coef": 0.004324},
      {"input": "l5", "type": "linear", "coef": 0.068978},
      {"input": "l6", "type": "linear", "coef": 0.090497},
      {"input": "l7", "type": "linear", "coef": -0.018336},
      {"input": "l8", "type": "linear", "coef": -0.009817},
      {"input": "l9", "type": "linear", "coef": 0.043316},
      {"input": "l10", "type": "linear", "coef": -0.007917},

      {"input": "l1", "type": "hinge", "knot": 2, "coef": 0.010706},
      {"input": "l1", "type": "hinge", "knot": 4, "coef": 0.010706},
      {"input": "l1", "type": "hinge", "knot": 6, "coef": 0.010706},
      {"input": "l1", "type": "hinge", "knot": 8, "coef": 0.010706},

      {"input": "l2", "type": "hinge", "knot": 2, "coef": 0.031206},
      {"input": "l2", "type": "hinge", "knot": 4, "coef": 0.031206},
      {"input": "l2", "type": "hinge", "knot": 6, "coef": 0.031206},
      {"input": "l2", "type": "hinge", "knot": 8, "coef": 0.031206},

      {"input": "l3", "type": "hinge", "knot": 2, "coef": -0.015846},
      {"input": "l3", "type": "hinge", "knot": 4, "coef": -0.015846},
      {"input": "l3", "type": "hinge", "knot": 6, "coef": -0.015846},
      {"input": "l3", "type": "hinge", "knot": 8, "coef": -0.015846},

      {"input": "l4", "type": "hinge", "knot": 2, "coef": 0.027364},
      {"input": "l4", "type": "hinge", "knot": 4, "coef": 0.027364},
      {"input": "l4", "type": "hinge", "knot": 6, "coef": 0.027364},
      {"input": "l4", "type": "hinge", "knot": 8, "coef": 0.027364},

      {"input": "l5", "type": "hinge", "knot": 2, "coef": -0.290861},
      {"input": "l5", "type": "hinge", "knot": 6, "coef": 0.174961},

      {"input": "l6", "type": "hinge", "knot": 2, "coef": -0.010464},
      {"input": "l6", "type": "hinge", "knot": 4, "coef": -0.010464},
      {"input": "l6", "type": "hinge", "knot": 6, "coef": -0.010464},
      {"input": "l6", "type": "hinge", "knot": 8, "coef": -0.010464},

      {"input": "l7", "type": "hinge", "knot": 2, "coef": 0.017598},
      {"input": "l7", "type": "hinge", "knot": 4, "coef": 0.017598},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": 0.017598},
      {"input": "l7", "type": "hinge", "knot": 8, "coef": 0.017598},

      {"input": "l8", "type": "hinge", "knot": 1, "coef": 0.051948},
      {"input": "l8", "type": "hinge", "knot": 3, "coef": -0.069657},
      {"input": "l8", "type": "hinge", "knot": 6, "coef": -0.051269},

      {"input": "l9", "type": "hinge", "knot": 2, "coef": -0.005004},
      {"input": "l9", "type": "hinge", "knot": 4, "coef": -0.005004},
      {"input": "l9", "type": "hinge", "knot": 6, "coef": -0.005004},
      {"input": "l9", "type": "hinge", "knot": 8, "coef": -0.005004}
    ],
    "interactions": [
      {"inputs": ["l5", "l8"], "coef": -0.042909},
      {"inputs": ["l5", "l8"], "knots": [0, 1], "coef": 0.017751},
      {"inputs": ["l5", "l8"], "knots": [0, 3], "coef": 0.032346},
      {"inputs": ["l5", "l8"], "knots": [0, 6], "coef": 0.04222},
      {"inputs": ["l5", "l8"], "knots": [2, 0], "coef": 0.07659},
      {"inputs": ["l5", "l8"], "knots": [2, 1], "coef": -0.007023},
      {"inputs": ["l5", "l8"], "knots": [2, 3], "coef": -0.001426},
      {"inputs": ["l5", "l8"], "knots": [2, 6], "coef": -0.07975},
      {"inputs": ["l5", "l8"], "knots": [6, 0], "coef": -0.032059},
      {"inputs": ["l5", "l8"], "knots": [6, 1], "coef": -0.035947},
      {"inputs": ["l5", "l8"], "knots": [6, 3], "coef": 0.019136},
      {"inputs": ["l5", "l8"], "knots": [6, 6], "coef": 0.057788},

      {"inputs": ["l1", "l7"], "coef": 0.004701},
      {"inputs": ["l2", "l8"], "coef": -0.006982},
      {"inputs": ["l3", "l6"], "coef": -0.008244},
      {"inputs": ["l3", "l9"], "coef": 0.006204},
      {"inputs": ["l4", "l6"], "coef": -0.011192},
      {"inputs": ["l5", "l6"], "coef": 0.004746},
      {"inputs": ["l5", "l7"], "coef": 0.005602},
      {"inputs": ["l6", "l7"], "coef": -0.006933},
      {"inputs": ["l7", "l8"], "coef": 0.004898},
      {"inputs": ["l7", "l9"], "coef": -0.009042},

      {"inputs": ["age_c", "l1"], "coef": -0.00558},
      {"inputs": ["age_c", "l3"], "coef": -0.009006},
      {"inputs": ["age_c", "l4"], "coef": 0.010778},
      {"inputs": ["age_c", "l6"], "coef": -0.01404},
      {"inputs": ["age_c", "l7"], "coef": 0.00808},
      {"inputs": ["age_c", "l9"], "coef": -0.018929},
      {"inputs": ["age_c", "l10"], "coef": 0.008855},
      {"inputs": ["age_c", "wfns45"], "coef": -0.04613},
      {"inputs": ["age_c", "surgery"], "coef": 0.04065},

      {"inputs": ["wfns45", "l3"], "coef": 0.02268},
      {"inputs": ["wfns45", "l5"], "coef": 0.01597},
      {"inputs": ["wfns45", "l9"], "coef": 0.02482},
      {"inputs": ["surgery", "l5"], "coef": 0.01591},
      {"inputs": ["surgery", "l6"], "coef": 0.02324},
      {"inputs": ["fisher34", "l8"], "coef": -0.039073},
      {"inputs": ["ct_ivh", "l8"], "coef": 0.029429},
      {"inputs": ["ct_ich", "l5"], "coef": 0.014655},
      {"inputs": ["htn", "l5"], "coef": 0.013406}
    ]
  },
  "confidence_trained": 0.9
}
```