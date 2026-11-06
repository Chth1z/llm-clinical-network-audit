**Reference:** independent uniform ages 18–90 and laboratory values 0–10, with equiprobable binary inputs; ranks describe average main-effect variation.

Propagating the supplied weights through approximate activation moments gives three dominant contributions: older age increases predicted risk, WFNS 4–5 increases it, and recorded aneurysm treatment decreases it. CT findings and hypertension contribute smaller increases. Many laboratory pathways cancel, leaving weak average trends alongside nonlinear dependence.

The JSON is a low-order analytic approximation to the network’s log-odds, retaining its dominant additive component and small clinical interactions. Apply the sigmoid to obtain probability. Treatment here means treatment **received during admission**, so the network conditions on that information.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "about +0.46 log-odds/decade",
      "rank": 1
    },
    "female": {
      "direction": "no clear effect",
      "size": "near-zero average",
      "rank": 16
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "about +1.70 log-odds",
      "rank": 2
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "about +0.33 log-odds",
      "rank": 5
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "about +0.49 log-odds",
      "rank": 4
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "about +0.21 log-odds",
      "rank": 7
    },
    "htn": {
      "direction": "increases risk",
      "size": "about +0.25 log-odds",
      "rank": 6
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "about -1.55 log-odds",
      "rank": 3
    },
    "urban": {
      "direction": "no clear effect",
      "size": "near-zero average",
      "rank": 18
    },
    "farmer": {
      "direction": "increases risk",
      "size": "very small average increase",
      "rank": 11
    },
    "l1": {
      "direction": "decreases risk",
      "size": "weak average downward trend",
      "rank": 10
    },
    "l2": {
      "direction": "no clear effect",
      "size": "near-zero average trend",
      "rank": 20
    },
    "l3": {
      "direction": "no clear effect",
      "size": "very small average trend",
      "rank": 14
    },
    "l4": {
      "direction": "increases risk",
      "size": "weak average upward trend",
      "rank": 9
    },
    "l5": {
      "direction": "decreases risk",
      "size": "weak; about -0.03 log-odds/unit",
      "rank": 8
    },
    "l6": {
      "direction": "no clear effect",
      "size": "very small average trend",
      "rank": 13
    },
    "l7": {
      "direction": "no clear effect",
      "size": "near-zero average trend",
      "rank": 17
    },
    "l8": {
      "direction": "decreases risk",
      "size": "weak average downward trend",
      "rank": 12
    },
    "l9": {
      "direction": "no clear effect",
      "size": "very small average trend",
      "rank": 15
    },
    "l10": {
      "direction": "no clear effect",
      "size": "near-zero average trend",
      "rank": 19
    }
  },
  "unexpected": [
    {
      "inputs": ["l1", "l4", "l5", "l8"],
      "description": "The weight-derived approximation has small downward average trends for l1, l5 and l8, but an upward trend for l4. These are model-specific laboratory relationships.",
      "where": "Across the supplied 0–10 scales; the network uses smooth responses rather than fixed cut-points."
    }
  ],
  "surrogate": {
    "intercept": -2.0392,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.4695},
      {"input": "female", "type": "linear", "coef": 0.0297},
      {"input": "wfns45", "type": "linear", "coef": 1.7368},
      {"input": "fisher34", "type": "linear", "coef": 0.3295},
      {"input": "ct_ivh", "type": "linear", "coef": 0.4902},
      {"input": "ct_ich", "type": "linear", "coef": 0.2065},
      {"input": "htn", "type": "linear", "coef": 0.2484},
      {"input": "surgery", "type": "linear", "coef": -1.5283},
      {"input": "urban", "type": "linear", "coef": -0.0129},
      {"input": "farmer", "type": "linear", "coef": 0.0796},
      {"input": "l1", "type": "linear", "coef": -0.0164},
      {"input": "l2", "type": "linear", "coef": 0.0018},
      {"input": "l3", "type": "linear", "coef": 0.0059},
      {"input": "l4", "type": "linear", "coef": 0.0193},
      {"input": "l5", "type": "linear", "coef": -0.0311},
      {"input": "l6", "type": "linear", "coef": -0.0081},
      {"input": "l7", "type": "linear", "coef": -0.0040},
      {"input": "l8", "type": "linear", "coef": -0.0118},
      {"input": "l9", "type": "linear", "coef": -0.0053},
      {"input": "l10", "type": "linear", "coef": 0.0020}
    ],
    "interactions": [
      {"inputs": ["age_c", "age_c"], "coef": 0.0067},
      {"inputs": ["age_c", "wfns45"], "coef": 0.0127},
      {"inputs": ["age_c", "surgery"], "coef": -0.0166},
      {"inputs": ["wfns45", "surgery"], "coef": -0.0670}
    ]
  },
  "confidence_trained": 0.99
}
```