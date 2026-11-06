The weights encode more than a conventional severity score. Near the input midpoint, WFNS 4–5 strongly raises log-odds, treatment lowers them, and age has a smaller positive effect. **The standout is a nonmonotone `l3` response:** an approximate trough around 2–3, followed by a steep increase.

Execution tools were unavailable, so the JSON below is a **manually derived local approximation with a coarse nonlinear correction**, not a globally fitted or validated replacement. Directions and ranks are indicative near `age_c=0`, binary inputs `0.5`, and laboratories `5`; they are not universal effects.

These are predictive associations, not causal effects. In particular, `surgery` contains post-admission information. The training-confidence value is subjective and cannot establish the model’s provenance or clinical accuracy.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "moderate per decade",
      "rank": 4
    },
    "female": {
      "direction": "no clear effect",
      "size": "negligible locally",
      "rank": 20
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "very large locally",
      "rank": 2
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "moderate locally",
      "rank": 10
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "large locally",
      "rank": 7
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "moderate locally",
      "rank": 11
    },
    "htn": {
      "direction": "increases risk",
      "size": "small locally",
      "rank": 13
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "very large locally",
      "rank": 3
    },
    "urban": {
      "direction": "decreases risk",
      "size": "small locally",
      "rank": 15
    },
    "farmer": {
      "direction": "decreases risk",
      "size": "small locally",
      "rank": 14
    },
    "l1": {
      "direction": "decreases risk",
      "size": "weak per unit locally",
      "rank": 8
    },
    "l2": {
      "direction": "decreases risk",
      "size": "weak per unit locally",
      "rank": 5
    },
    "l3": {
      "direction": "no clear effect",
      "size": "strong, nonmonotone",
      "rank": 1
    },
    "l4": {
      "direction": "no clear effect",
      "size": "negligible locally",
      "rank": 19
    },
    "l5": {
      "direction": "decreases risk",
      "size": "small locally",
      "rank": 12
    },
    "l6": {
      "direction": "no clear effect",
      "size": "very small locally",
      "rank": 18
    },
    "l7": {
      "direction": "decreases risk",
      "size": "small locally",
      "rank": 16
    },
    "l8": {
      "direction": "decreases risk",
      "size": "weak per unit locally",
      "rank": 6
    },
    "l9": {
      "direction": "no clear effect",
      "size": "very small locally",
      "rank": 17
    },
    "l10": {
      "direction": "decreases risk",
      "size": "weak per unit locally",
      "rank": 9
    }
  },
  "unexpected": [
    {
      "inputs": ["l3"],
      "description": "Approximately U-shaped at midpoint settings: increasing very low values initially lowers predicted risk, whereas increasing values above the trough raises risk substantially. A single signed coefficient misses this relationship. The laboratory's identity is unknown, so no physiological interpretation is justified.",
      "where": "Approximate trough at l3=2–3; pronounced increase over approximately l3=4–8, with other inputs at the stated reference."
    },
    {
      "inputs": ["farmer"],
      "description": "The local association is protective: switching farmer from 0 to 1 has an approximately negative 0.30 log-odds slope. This is not evidence that farming prevents death.",
      "where": "Near age_c=0, laboratory values=5, and other binary inputs=0.5; not established throughout the input space."
    }
  ],
  "surrogate": {
    "intercept": 1.997,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.331},
      {"input": "female", "type": "linear", "coef": -0.023},
      {"input": "wfns45", "type": "linear", "coef": 2.468},
      {"input": "fisher34", "type": "linear", "coef": 0.477},
      {"input": "ct_ivh", "type": "linear", "coef": 0.718},
      {"input": "ct_ich", "type": "linear", "coef": 0.354},
      {"input": "htn", "type": "linear", "coef": 0.308},
      {"input": "surgery", "type": "linear", "coef": -2.051},
      {"input": "urban", "type": "linear", "coef": -0.294},
      {"input": "farmer", "type": "linear", "coef": -0.300},
      {"input": "l1", "type": "linear", "coef": -0.107},
      {"input": "l2", "type": "linear", "coef": -0.154},
      {"input": "l3", "type": "linear", "coef": -0.376},
      {"input": "l4", "type": "linear", "coef": -0.010},
      {"input": "l5", "type": "linear", "coef": -0.060},
      {"input": "l6", "type": "linear", "coef": -0.023},
      {"input": "l7", "type": "linear", "coef": -0.044},
      {"input": "l8", "type": "linear", "coef": -0.137},
      {"input": "l9", "type": "linear", "coef": -0.031},
      {"input": "l10", "type": "linear", "coef": -0.089},
      {"input": "l3", "type": "hinge", "knot": 1, "coef": 0.092},
      {"input": "l3", "type": "hinge", "knot": 2, "coef": 0.180},
      {"input": "l3", "type": "hinge", "knot": 3, "coef": 0.270},
      {"input": "l3", "type": "hinge", "knot": 4, "coef": 0.357},
      {"input": "l3", "type": "hinge", "knot": 5, "coef": 0.322},
      {"input": "l3", "type": "hinge", "knot": 6, "coef": 0.110},
      {"input": "l3", "type": "hinge", "knot": 7, "coef": -0.063},
      {"input": "l3", "type": "hinge", "knot": 8, "coef": -0.239},
      {"input": "l3", "type": "hinge", "knot": 9, "coef": -0.413}
    ],
    "interactions": []
  },
  "confidence_trained": 0.98
}
```