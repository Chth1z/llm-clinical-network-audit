**Reference:** ages 18–90, balanced binary inputs, and independently varying laboratories over 0–10. Rankings compare typical variation in predicted log-odds.

Individual weight signs are misleading: net sensitivity is \(W_3D_2W_2D_1W_1\), where the diagonal matrices contain the tanh derivatives. At the mathematical centre—age 60, binary coordinates 0.5, laboratories 5—the network gives approximately **37%** mortality. Its local log-odds sensitivities are approximately **+2.5 for WFNS**, **−2.1 for surgery**, **+0.35 per decade**, and **+0.75 per unit of l3**.

The distinctive relationship is **l3’s low-end dip followed by a strong increase**, with weaker WFNS and treatment contrasts toward its upper range. Farming and urban residence both have negative typical effects. Several other inputs have weak average effects despite appreciable individual weights.

Below is a weight-derived spline approximation retaining these relationships. It also gives approximately **37% at that centre**. The surgery input conditions predictions on treatment during admission.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "moderate; about 0.33 log-odds/decade",
      "rank": 4
    },
    "female": {
      "direction": "no clear effect",
      "size": "very weak net effect",
      "rank": 17
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "large; laboratory-dependent",
      "rank": 1
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "moderate; about 0.30 log-odds",
      "rank": 9
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "moderate; about 0.52 log-odds",
      "rank": 5
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "moderate; about 0.34 log-odds",
      "rank": 7
    },
    "htn": {
      "direction": "increases risk",
      "size": "small positive average effect",
      "rank": 13
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "large; laboratory-dependent",
      "rank": 3
    },
    "urban": {
      "direction": "decreases risk",
      "size": "small negative average effect",
      "rank": 11
    },
    "farmer": {
      "direction": "decreases risk",
      "size": "small negative average effect",
      "rank": 12
    },
    "l1": {
      "direction": "no clear effect",
      "size": "weak average; context-dependent",
      "rank": 20
    },
    "l2": {
      "direction": "decreases risk",
      "size": "small negative average slope",
      "rank": 8
    },
    "l3": {
      "direction": "increases risk",
      "size": "large overall; low-end reversal",
      "rank": 2
    },
    "l4": {
      "direction": "no clear effect",
      "size": "weak average; context-dependent",
      "rank": 16
    },
    "l5": {
      "direction": "decreases risk",
      "size": "weak negative average slope",
      "rank": 14
    },
    "l6": {
      "direction": "no clear effect",
      "size": "weak average; context-dependent",
      "rank": 19
    },
    "l7": {
      "direction": "no clear effect",
      "size": "weak average; context-dependent",
      "rank": 18
    },
    "l8": {
      "direction": "decreases risk",
      "size": "small negative average slope",
      "rank": 6
    },
    "l9": {
      "direction": "decreases risk",
      "size": "weak negative average slope",
      "rank": 15
    },
    "l10": {
      "direction": "decreases risk",
      "size": "weak negative average slope",
      "rank": 10
    }
  },
  "unexpected": [
    {
      "inputs": ["l3"],
      "description": "A shallow low-end decline reverses into a strong increase; the increase becomes less steep near the upper end.",
      "where": "Approximate minimum around l3=1–2; substantial increase around 3–8; flattening toward 10. Turning points depend on other inputs."
    },
    {
      "inputs": ["farmer"],
      "description": "Farmer status has a negative typical association with the network's predicted mortality.",
      "where": "farmer changes from 0 to 1, including around laboratory values of 5."
    },
    {
      "inputs": ["l3", "wfns45", "surgery"],
      "description": "The adverse WFNS contrast and the protective surgery contrast become smaller toward the upper l3 range.",
      "where": "Most apparent above approximately l3=5; the network's transitions are smooth."
    }
  ],
  "surrogate": {
    "intercept": -0.539,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.33},
      {"input": "female", "type": "linear", "coef": -0.03},
      {"input": "wfns45", "type": "linear", "coef": 1.90},
      {"input": "fisher34", "type": "linear", "coef": 0.30},
      {"input": "ct_ivh", "type": "linear", "coef": 0.52},
      {"input": "ct_ich", "type": "linear", "coef": 0.34},
      {"input": "htn", "type": "linear", "coef": 0.18},
      {"input": "surgery", "type": "linear", "coef": -1.68},
      {"input": "urban", "type": "linear", "coef": -0.22},
      {"input": "farmer", "type": "linear", "coef": -0.20},
      {"input": "l1", "type": "linear", "coef": -0.002},
      {"input": "l2", "type": "linear", "coef": -0.054},
      {"input": "l3", "type": "linear", "coef": -0.08144},
      {"input": "l4", "type": "linear", "coef": -0.008},
      {"input": "l5", "type": "linear", "coef": -0.031},
      {"input": "l6", "type": "linear", "coef": 0.003},
      {"input": "l7", "type": "linear", "coef": -0.005},
      {"input": "l8", "type": "linear", "coef": -0.063},
      {"input": "l9", "type": "linear", "coef": -0.030},
      {"input": "l10", "type": "linear", "coef": -0.039},
      {"input": "l3", "type": "hinge", "knot": 1.25, "coef": 0.10048},
      {"input": "l3", "type": "hinge", "knot": 2.5, "coef": 0.16928},
      {"input": "l3", "type": "hinge", "knot": 3.75, "coef": 0.14656},
      {"input": "l3", "type": "hinge", "knot": 5.0, "coef": 0.09224},
      {"input": "l3", "type": "hinge", "knot": 6.25, "coef": 0.02072},
      {"input": "l3", "type": "hinge", "knot": 7.5, "coef": -0.02944},
      {"input": "l3", "type": "hinge", "knot": 8.75, "coef": -0.05144}
    ],
    "interactions": [
      {"inputs": ["wfns45", "l3"], "coef": 0.020},
      {"inputs": ["surgery", "l3"], "coef": -0.016},
      {"inputs": ["wfns45", "l3"], "knots": [0, 5], "coef": -0.140},
      {"inputs": ["surgery", "l3"], "knots": [0, 5], "coef": 0.128}
    ]
  },
  "confidence_trained": 0.99
}
```