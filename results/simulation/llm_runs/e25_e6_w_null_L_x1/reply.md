Chaining the weights through **both tanh layers**, a numerical reference point—age 60, laboratories all 5, and binary coordinates relaxed to 0.5—gives approximately **−1.49 log-odds, or 18% probability**. Locally, WFNS 4–5 strongly raises predictions, treatment lowers them, and age and IVH raise them. The laboratory inputs are **not ignored**, and their effects have mixed signs.

The JSON contains a **hand-calculated local linear approximation**, not a validated global distillation. Its directions and ranks describe local log-odds slopes per coded input unit, not population importance. It will lose fidelity away from that reference because the network has saturation and interactions; I have not established global turning points.

Also, despite the “admission inputs” description, `surgery` records treatment during admission. Its negative association is neither an admission-available measurement nor evidence of a causal treatment benefit.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "local +0.80 per decade",
      "rank": 4
    },
    "female": {
      "direction": "increases risk",
      "size": "local slope +0.154",
      "rank": 9
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "local slope +3.086",
      "rank": 1
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "local slope +0.724",
      "rank": 5
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "local slope +0.933",
      "rank": 3
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "local slope +0.310",
      "rank": 7
    },
    "htn": {
      "direction": "increases risk",
      "size": "local slope +0.437",
      "rank": 6
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "local slope -2.743",
      "rank": 2
    },
    "urban": {
      "direction": "no clear effect",
      "size": "small local slope +0.022",
      "rank": 19
    },
    "farmer": {
      "direction": "increases risk",
      "size": "local slope +0.135",
      "rank": 10
    },
    "l1": {
      "direction": "decreases risk",
      "size": "local -0.135 per unit",
      "rank": 11
    },
    "l2": {
      "direction": "decreases risk",
      "size": "local -0.065 per unit",
      "rank": 15
    },
    "l3": {
      "direction": "increases risk",
      "size": "local +0.155 per unit",
      "rank": 8
    },
    "l4": {
      "direction": "increases risk",
      "size": "local +0.116 per unit",
      "rank": 13
    },
    "l5": {
      "direction": "decreases risk",
      "size": "local -0.134 per unit",
      "rank": 12
    },
    "l6": {
      "direction": "no clear effect",
      "size": "small local slope +0.026",
      "rank": 17
    },
    "l7": {
      "direction": "no clear effect",
      "size": "small local slope +0.021",
      "rank": 20
    },
    "l8": {
      "direction": "no clear effect",
      "size": "small local slope -0.023",
      "rank": 18
    },
    "l9": {
      "direction": "decreases risk",
      "size": "local -0.105 per unit",
      "rank": 14
    },
    "l10": {
      "direction": "increases risk",
      "size": "local +0.065 per unit",
      "rank": 16
    }
  },
  "unexpected": [
    {
      "inputs": ["l1", "l2", "l3", "l4", "l5", "l9"],
      "description": "The anonymous laboratory inputs have substantive, mixed local effects: l1, l2, l5 and l9 lower predictions, whereas l3 and l4 raise them. These are weight-derived relationships, not identified biological mechanisms or established global monotonic effects.",
      "where": "Around age_c=0, all laboratories=5, and binary coordinates relaxed to 0.5; no global threshold established."
    }
  ],
  "surrogate": {
    "intercept": -2.628,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.802},
      {"input": "female", "type": "linear", "coef": 0.154},
      {"input": "wfns45", "type": "linear", "coef": 3.086},
      {"input": "fisher34", "type": "linear", "coef": 0.724},
      {"input": "ct_ivh", "type": "linear", "coef": 0.933},
      {"input": "ct_ich", "type": "linear", "coef": 0.310},
      {"input": "htn", "type": "linear", "coef": 0.437},
      {"input": "surgery", "type": "linear", "coef": -2.743},
      {"input": "urban", "type": "linear", "coef": 0.022},
      {"input": "farmer", "type": "linear", "coef": 0.135},
      {"input": "l1", "type": "linear", "coef": -0.135},
      {"input": "l2", "type": "linear", "coef": -0.065},
      {"input": "l3", "type": "linear", "coef": 0.155},
      {"input": "l4", "type": "linear", "coef": 0.116},
      {"input": "l5", "type": "linear", "coef": -0.134},
      {"input": "l6", "type": "linear", "coef": 0.026},
      {"input": "l7", "type": "linear", "coef": 0.021},
      {"input": "l8", "type": "linear", "coef": -0.023},
      {"input": "l9", "type": "linear", "coef": -0.105},
      {"input": "l10", "type": "linear", "coef": 0.065}
    ],
    "interactions": []
  },
  "confidence_trained": 0.95
}
```