This is a **sum of signed, saturating responses**, not a conventional risk-factor score. For example, its exact log-odds sensitivity to input \(x_i\) is
\[
\sum_j W_{2j}W_{1ji}\bigl[1-\tanh^2(W_{1j}x+b_{1j})\bigr].
\]
Consequently, an input’s effect depends on the other inputs; individual weight signs are insufficient.

Some notable features of these weights:

- With laboratories near 5, hidden units **1, 5, 7 and 10** are almost saturated. Together with the output intercept, they contribute approximately **−1.122 log-odds**.
- Older age, severe WFNS grade and absence of aneurysm treatment generally raise predictions. Female-associated contributions largely cancel.
- Laboratory contributions also cancel substantially **on average**, but not patient by patient. They should not simply be discarded.
- There are genuinely non-monotonic relationships. For the reference profile specified below, increasing `l6` eventually **increases** predicted mortality.
- `surgery` describes treatment during admission, notwithstanding the admission-input label. Its association is not a causal treatment effect and could incorporate treatment-selection or survival information.

Without an input distribution, importance ranks are not uniquely defined. Below are rough, range-sensitive rankings using ages 30–90, balanced binary inputs and independently varying laboratories over 0–10. “No clear effect” can mean opposing effects, not irrelevance.

The surrogate is an **analytic, unvalidated pairwise-spline approximation**, not an exact reconstruction. Its knots are approximation devices, not thresholds in the smooth original network. The provenance confidence reflects the coherent clinical weight patterns, not demonstrated clinical validity.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "large; about 0.43 log-odds/decade", "rank": 2},
    "female": {"direction": "no clear effect", "size": "small average; opposing contributions", "rank": 20},
    "wfns45": {"direction": "increases risk", "size": "very large average effect", "rank": 1},
    "fisher34": {"direction": "increases risk", "size": "moderate average effect", "rank": 16},
    "ct_ivh": {"direction": "increases risk", "size": "moderate average effect", "rank": 7},
    "ct_ich": {"direction": "increases risk", "size": "moderate average effect", "rank": 9},
    "htn": {"direction": "increases risk", "size": "small average effect", "rank": 17},
    "surgery": {"direction": "decreases risk", "size": "very large average association", "rank": 3},
    "urban": {"direction": "decreases risk", "size": "small average association", "rank": 18},
    "farmer": {"direction": "decreases risk", "size": "small average association", "rank": 19},
    "l1": {"direction": "no clear effect", "size": "context-dependent; weak average", "rank": 11},
    "l2": {"direction": "decreases risk", "size": "weak average; substantial reversals", "rank": 4},
    "l3": {"direction": "no clear effect", "size": "opposing nonlinear contributions", "rank": 8},
    "l4": {"direction": "no clear effect", "size": "near-zero average; conditional effects", "rank": 15},
    "l5": {"direction": "decreases risk", "size": "weak average; context-dependent", "rank": 12},
    "l6": {"direction": "no clear effect", "size": "non-monotonic; context-dependent", "rank": 14},
    "l7": {"direction": "decreases risk", "size": "weak average; substantial reversals", "rank": 6},
    "l8": {"direction": "no clear effect", "size": "opposing nonlinear contributions", "rank": 10},
    "l9": {"direction": "decreases risk", "size": "weak average; context-dependent", "rank": 13},
    "l10": {"direction": "no clear effect", "size": "opposing nonlinear contributions", "rank": 5}
  },
  "unexpected": [
    {
      "inputs": ["l6"],
      "description": "A U-shaped relationship occurs at age 60 with all nine binary inputs zero and the other nine laboratories fixed at 5. Network probabilities at l6 = 0, 5 and 10 are approximately 5.9%, 5.1% and 9.8%, respectively.",
      "where": "For this specific profile, the minimum is near l6 = 3.8; its location is not universal."
    },
    {
      "inputs": ["l1", "l2", "l3", "l4", "l5", "l6", "l7", "l8", "l9", "l10"],
      "description": "Moving all ten laboratories together can produce a large protective-looking shift despite weak individual average effects. At age 60 with all binary inputs zero, the network predicts approximately 36.1% with all laboratories zero versus 5.1% with all laboratories equal to 5.",
      "where": "Joint movement from (0,0,0,0,0,0,0,0,0,0) to (5,5,5,5,5,5,5,5,5,5); this is a model property, not a medically interpretable laboratory intervention."
    },
    {
      "inputs": ["farmer"],
      "description": "Farmer status has a mildly protective average association rather than an adverse one, with other inputs held fixed; the association is not uniform.",
      "where": "Changing farmer from 0 to 1; at age 60, other binary inputs zero and all laboratories 5, probability falls approximately from 5.1% to 4.6%."
    }
  ],
  "surrogate": {
    "intercept": -1.2399,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.25475},
      {"input": "age_c", "type": "hinge", "knot": -1.5, "coef": 0.05338},
      {"input": "age_c", "type": "hinge", "knot": 1.5, "coef": -0.05338},
      {"input": "female", "type": "linear", "coef": -0.00111},
      {"input": "wfns45", "type": "linear", "coef": 1.01855},
      {"input": "fisher34", "type": "linear", "coef": 0.39646},
      {"input": "ct_ivh", "type": "linear", "coef": 0.47840},
      {"input": "ct_ich", "type": "linear", "coef": 0.46929},
      {"input": "htn", "type": "linear", "coef": 0.18333},
      {"input": "surgery", "type": "linear", "coef": -0.84408},
      {"input": "urban", "type": "linear", "coef": -0.19067},
      {"input": "farmer", "type": "linear", "coef": -0.12135},
      {"input": "l1", "type": "linear", "coef": -0.041630},
      {"input": "l1", "type": "hinge", "knot": 5, "coef": 0.063814},
      {"input": "l2", "type": "linear", "coef": -0.066179},
      {"input": "l2", "type": "hinge", "knot": 5, "coef": 0.099987},
      {"input": "l3", "type": "linear", "coef": 0.034380},
      {"input": "l3", "type": "hinge", "knot": 5, "coef": 0.082538},
      {"input": "l4", "type": "linear", "coef": -0.004019},
      {"input": "l4", "type": "hinge", "knot": 5, "coef": 0.039928},
      {"input": "l5", "type": "linear", "coef": -0.074482},
      {"input": "l5", "type": "hinge", "knot": 5, "coef": 0.052159},
      {"input": "l6", "type": "linear", "coef": -0.030660},
      {"input": "l6", "type": "hinge", "knot": 5, "coef": 0.088384},
      {"input": "l7", "type": "linear", "coef": -0.006023},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": 0.054341},
      {"input": "l8", "type": "linear", "coef": -0.017517},
      {"input": "l8", "type": "hinge", "knot": 5, "coef": 0.067667},
      {"input": "l9", "type": "linear", "coef": -0.033518},
      {"input": "l9", "type": "hinge", "knot": 5, "coef": 0.041066},
      {"input": "l10", "type": "linear", "coef": 0.000914},
      {"input": "l10", "type": "hinge", "knot": 5, "coef": 0.075633}
    ],
    "interactions": [
      {"inputs": ["wfns45", "l1"], "coef": 0.0188},
      {"inputs": ["wfns45", "l1"], "knots": [0, 5], "coef": -0.0376},
      {"inputs": ["wfns45", "l2"], "coef": 0.0317},
      {"inputs": ["wfns45", "l2"], "knots": [0, 5], "coef": -0.0634},
      {"inputs": ["wfns45", "l3"], "coef": 0.0231},
      {"inputs": ["wfns45", "l3"], "knots": [0, 5], "coef": -0.0462},
      {"inputs": ["wfns45", "l4"], "coef": 0.0158},
      {"inputs": ["wfns45", "l4"], "knots": [0, 5], "coef": -0.0316},
      {"inputs": ["wfns45", "l5"], "coef": 0.0113},
      {"inputs": ["wfns45", "l5"], "knots": [0, 5], "coef": -0.0226},
      {"inputs": ["wfns45", "l6"], "coef": 0.0238},
      {"inputs": ["wfns45", "l6"], "knots": [0, 5], "coef": -0.0476},
      {"inputs": ["wfns45", "l7"], "coef": 0.0246},
      {"inputs": ["wfns45", "l7"], "knots": [0, 5], "coef": -0.0492},
      {"inputs": ["wfns45", "l8"], "coef": 0.0217},
      {"inputs": ["wfns45", "l8"], "knots": [0, 5], "coef": -0.0434},
      {"inputs": ["wfns45", "l9"], "coef": 0.0189},
      {"inputs": ["wfns45", "l9"], "knots": [0, 5], "coef": -0.0378},
      {"inputs": ["wfns45", "l10"], "coef": 0.0265},
      {"inputs": ["wfns45", "l10"], "knots": [0, 5], "coef": -0.0530},

      {"inputs": ["age_c", "l1"], "coef": 0.005264},
      {"inputs": ["age_c", "l1"], "knots": [-4.2, 5], "coef": -0.010528},
      {"inputs": ["age_c", "l2"], "coef": 0.008876},
      {"inputs": ["age_c", "l2"], "knots": [-4.2, 5], "coef": -0.017752},
      {"inputs": ["age_c", "l3"], "coef": 0.006468},
      {"inputs": ["age_c", "l3"], "knots": [-4.2, 5], "coef": -0.012936},
      {"inputs": ["age_c", "l4"], "coef": 0.004424},
      {"inputs": ["age_c", "l4"], "knots": [-4.2, 5], "coef": -0.008848},
      {"inputs": ["age_c", "l5"], "coef": 0.003164},
      {"inputs": ["age_c", "l5"], "knots": [-4.2, 5], "coef": -0.006328},
      {"inputs": ["age_c", "l6"], "coef": 0.006664},
      {"inputs": ["age_c", "l6"], "knots": [-4.2, 5], "coef": -0.013328},
      {"inputs": ["age_c", "l7"], "coef": 0.006888},
      {"inputs": ["age_c", "l7"], "knots": [-4.2, 5], "coef": -0.013776},
      {"inputs": ["age_c", "l8"], "coef": 0.006076},
      {"inputs": ["age_c", "l8"], "knots": [-4.2, 5], "coef": -0.012152},
      {"inputs": ["age_c", "l9"], "coef": 0.005292},
      {"inputs": ["age_c", "l9"], "knots": [-4.2, 5], "coef": -0.010584},
      {"inputs": ["age_c", "l10"], "coef": 0.007420},
      {"inputs": ["age_c", "l10"], "knots": [-4.2, 5], "coef": -0.014840},

      {"inputs": ["surgery", "l1"], "coef": -0.015604},
      {"inputs": ["surgery", "l1"], "knots": [0, 5], "coef": 0.031208},
      {"inputs": ["surgery", "l2"], "coef": -0.026311},
      {"inputs": ["surgery", "l2"], "knots": [0, 5], "coef": 0.052622},
      {"inputs": ["surgery", "l3"], "coef": -0.019173},
      {"inputs": ["surgery", "l3"], "knots": [0, 5], "coef": 0.038346},
      {"inputs": ["surgery", "l4"], "coef": -0.013114},
      {"inputs": ["surgery", "l4"], "knots": [0, 5], "coef": 0.026228},
      {"inputs": ["surgery", "l5"], "coef": -0.009379},
      {"inputs": ["surgery", "l5"], "knots": [0, 5], "coef": 0.018758},
      {"inputs": ["surgery", "l6"], "coef": -0.019754},
      {"inputs": ["surgery", "l6"], "knots": [0, 5], "coef": 0.039508},
      {"inputs": ["surgery", "l7"], "coef": -0.020418},
      {"inputs": ["surgery", "l7"], "knots": [0, 5], "coef": 0.040836},
      {"inputs": ["surgery", "l8"], "coef": -0.018011},
      {"inputs": ["surgery", "l8"], "knots": [0, 5], "coef": 0.036022},
      {"inputs": ["surgery", "l9"], "coef": -0.015687},
      {"inputs": ["surgery", "l9"], "knots": [0, 5], "coef": 0.031374},
      {"inputs": ["surgery", "l10"], "coef": -0.021995},
      {"inputs": ["surgery", "l10"], "knots": [0, 5], "coef": 0.043990},

      {"inputs": ["l1", "l2"], "coef": 0.003451},
      {"inputs": ["l1", "l5"], "coef": 0.005967},
      {"inputs": ["l1", "l7"], "coef": -0.002335},
      {"inputs": ["l1", "l10"], "coef": -0.003657},
      {"inputs": ["l3", "l6"], "coef": -0.002506},
      {"inputs": ["l3", "l7"], "coef": -0.003631},
      {"inputs": ["l3", "l10"], "coef": -0.003126},
      {"inputs": ["l5", "l6"], "coef": 0.002660},
      {"inputs": ["l5", "l9"], "coef": -0.003687},
      {"inputs": ["l7", "l9"], "coef": 0.003674},
      {"inputs": ["l9", "l10"], "coef": 0.002924}
    ]
  },
  "confidence_trained": 0.95
}
```