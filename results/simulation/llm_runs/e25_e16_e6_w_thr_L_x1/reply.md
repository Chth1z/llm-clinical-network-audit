**Reference chosen:** ages 18–90 uniformly, balanced independent binary inputs, and independent laboratory values uniformly spanning 0–10. Ranks reflect estimated variation over this reference distribution.

The dominant relationships are higher predictions with age, severe WFNS grade and high **l3**, and lower predictions with treatment. Importantly, **l3 is not simply linear**: it is approximately flat or slightly decreasing at low values, then rises substantially, with some flattening toward 10. The other laboratories contribute much weaker, curved corrections; their numerous nonzero weights do not translate into comparably large effects.

The JSON gives an **analytical, weight-derived approximation**, with a rough estimated typical probability error of 5–10 percentage points on this reference distribution. Directions summarize overall tendencies, not universal monotonicity. Repeated names in interactions denote squares. Despite the admission heading, `surgery` describes treatment during the stay.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "~0.48 log-odds per decade",
      "rank": 1
    },
    "female": {
      "direction": "no clear effect",
      "size": "tiny, slightly lower overall",
      "rank": 19
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "~1.8 log-odds",
      "rank": 2
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "~0.3 log-odds",
      "rank": 7
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "~0.6 log-odds",
      "rank": 5
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "~0.45 log-odds",
      "rank": 6
    },
    "htn": {
      "direction": "increases risk",
      "size": "~0.24 log-odds",
      "rank": 8
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "~1.6 log-odds",
      "rank": 4
    },
    "urban": {
      "direction": "decreases risk",
      "size": "weak, ~0.15 log-odds",
      "rank": 13
    },
    "farmer": {
      "direction": "decreases risk",
      "size": "weak, ~0.17 log-odds",
      "rank": 12
    },
    "l1": {
      "direction": "no clear effect",
      "size": "tiny, shallow hump",
      "rank": 20
    },
    "l2": {
      "direction": "decreases risk",
      "size": "weak overall; curved",
      "rank": 14
    },
    "l3": {
      "direction": "increases risk",
      "size": "large, threshold-like rise",
      "rank": 3
    },
    "l4": {
      "direction": "decreases risk",
      "size": "very weak overall; curved",
      "rank": 17
    },
    "l5": {
      "direction": "decreases risk",
      "size": "very weak overall; curved",
      "rank": 18
    },
    "l6": {
      "direction": "decreases risk",
      "size": "weak, stronger at high values",
      "rank": 9
    },
    "l7": {
      "direction": "no clear effect",
      "size": "weak, shallow hump",
      "rank": 16
    },
    "l8": {
      "direction": "decreases risk",
      "size": "weak, ~0.03 log-odds/unit",
      "rank": 10
    },
    "l9": {
      "direction": "decreases risk",
      "size": "weak overall; curved",
      "rank": 11
    },
    "l10": {
      "direction": "decreases risk",
      "size": "weak, ~0.02 log-odds/unit",
      "rank": 15
    }
  },
  "unexpected": [
    {
      "inputs": ["l3"],
      "description": "Approximately flat or slightly decreasing initially, followed by a substantial increase and then flattening; a single linear laboratory coefficient misses this shape.",
      "where": "Approximately flat below 2; strongest rise around 3–8; flattening above about 8."
    },
    {
      "inputs": ["farmer"],
      "description": "Farmer status has a small risk-lowering association in the prediction function.",
      "where": "farmer changes from 0 to 1, holding other inputs fixed."
    },
    {
      "inputs": ["l1", "l7"],
      "description": "Weak inverted-U components: intermediate values can produce higher predictions than either end of the scale.",
      "where": "Broad reference-averaged maxima near l1=5 and l7=4."
    },
    {
      "inputs": ["l3", "wfns45", "surgery"],
      "description": "Higher l3 attenuates the additional WFNS contribution and reduces the magnitude of the treatment-associated decrease.",
      "where": "Across l3=0–10; approximately 0.056 log-odds change per l3 unit in each binary contrast."
    }
  ],
  "surrogate": {
    "intercept": -2.287,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.536},
      {"input": "female", "type": "linear", "coef": -0.081},
      {"input": "wfns45", "type": "linear", "coef": 2.065},
      {"input": "fisher34", "type": "linear", "coef": 0.359},
      {"input": "ct_ivh", "type": "linear", "coef": 0.724},
      {"input": "ct_ich", "type": "linear", "coef": 0.564},
      {"input": "htn", "type": "linear", "coef": 0.279},
      {"input": "surgery", "type": "linear", "coef": -1.872},
      {"input": "urban", "type": "linear", "coef": -0.145},
      {"input": "farmer", "type": "linear", "coef": -0.175},
      {"input": "l1", "type": "linear", "coef": 0.0495},
      {"input": "l2", "type": "linear", "coef": 0.0279},
      {"input": "l3", "type": "linear", "coef": 0.0019},
      {"input": "l3", "type": "hinge", "knot": 2, "coef": 0.2218},
      {"input": "l3", "type": "hinge", "knot": 4, "coef": 0.1945},
      {"input": "l3", "type": "hinge", "knot": 6, "coef": 0.0378},
      {"input": "l3", "type": "hinge", "knot": 8, "coef": -0.0690},
      {"input": "l4", "type": "linear", "coef": 0.0140},
      {"input": "l5", "type": "linear", "coef": 0.0115},
      {"input": "l6", "type": "linear", "coef": 0.0148},
      {"input": "l7", "type": "linear", "coef": 0.0449},
      {"input": "l8", "type": "linear", "coef": -0.0029},
      {"input": "l9", "type": "linear", "coef": 0.0210},
      {"input": "l10", "type": "linear", "coef": -0.0005}
    ],
    "interactions": [
      {"inputs": ["age_c", "age_c"], "coef": -0.0140},
      {"inputs": ["l1", "l1"], "coef": -0.00460},
      {"inputs": ["l2", "l2"], "coef": -0.00447},
      {"inputs": ["l4", "l4"], "coef": -0.00287},
      {"inputs": ["l5", "l5"], "coef": -0.00251},
      {"inputs": ["l6", "l6"], "coef": -0.00476},
      {"inputs": ["l7", "l7"], "coef": -0.00560},
      {"inputs": ["l8", "l8"], "coef": -0.00292},
      {"inputs": ["l9", "l9"], "coef": -0.00496},
      {"inputs": ["l10", "l10"], "coef": -0.00192},
      {"inputs": ["age_c", "l3"], "coef": -0.0153},
      {"inputs": ["wfns45", "l3"], "coef": -0.0557},
      {"inputs": ["fisher34", "l3"], "coef": -0.0107},
      {"inputs": ["ct_ivh", "l3"], "coef": -0.0290},
      {"inputs": ["ct_ich", "l3"], "coef": -0.0214},
      {"inputs": ["htn", "l3"], "coef": -0.0085},
      {"inputs": ["surgery", "l3"], "coef": 0.0558},
      {"inputs": ["age_c", "wfns45"], "coef": -0.0274},
      {"inputs": ["age_c", "surgery"], "coef": 0.0290},
      {"inputs": ["wfns45", "surgery"], "coef": 0.0400}
    ]
  },
  "confidence_trained": 0.995
}
```