**Reference:** independent ages 18–90, equally weighted binary values, and laboratories uniform over 0–10. Ranks compare one-standard-deviation changes; negligible or inconsistent effects share the last rank.

A moment-matched approximation of the **network functions**, rather than their individual weights, gives predominantly additive agreement. Approximate averaged coefficients range from 0.40–0.44 for age, 1.64–1.74 for WFNS 4–5, and −1.49 to −1.35 for treatment. The surrogate below summarizes shared main effects; it does not reproduce individual-network wiggles. No common sharp threshold or interaction is retained.

The surgery association describes receiving treatment during admission.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "0.42 log-odds per decade", "rank": 1},
    "female": {"direction": "no clear effect", "size": "negligible shared component", "rank": 12},
    "wfns45": {"direction": "increases risk", "size": "large: 1.68 log-odds", "rank": 2},
    "fisher34": {"direction": "increases risk", "size": "moderate: 0.44 log-odds", "rank": 5},
    "ct_ivh": {"direction": "increases risk", "size": "moderate: 0.51 log-odds", "rank": 4},
    "ct_ich": {"direction": "increases risk", "size": "moderate: 0.40 log-odds", "rank": 6},
    "htn": {"direction": "increases risk", "size": "small: 0.25 log-odds", "rank": 7},
    "surgery": {"direction": "decreases risk", "size": "large: 1.43 log-odds", "rank": 3},
    "urban": {"direction": "decreases risk", "size": "very small: 0.09 log-odds", "rank": 11},
    "farmer": {"direction": "decreases risk", "size": "small: 0.12 log-odds", "rank": 9},
    "l1": {"direction": "no clear effect", "size": "no stable material component", "rank": 12},
    "l2": {"direction": "no clear effect", "size": "no stable material component", "rank": 12},
    "l3": {"direction": "no clear effect", "size": "no stable material component", "rank": 12},
    "l4": {"direction": "no clear effect", "size": "no stable material component", "rank": 12},
    "l5": {"direction": "decreases risk", "size": "weak: 0.18 over 0–10", "rank": 10},
    "l6": {"direction": "no clear effect", "size": "no stable material component", "rank": 12},
    "l7": {"direction": "no clear effect", "size": "no stable material component", "rank": 12},
    "l8": {"direction": "decreases risk", "size": "weak: 0.24 over 0–10", "rank": 8},
    "l9": {"direction": "no clear effect", "size": "no stable material component", "rank": 12},
    "l10": {"direction": "no clear effect", "size": "no stable material component", "rank": 12}
  },
  "unexpected": [
    {
      "inputs": ["farmer"],
      "description": "Farmer status has a weak inverse association with predicted mortality, averaged over the reference inputs.",
      "where": "farmer changes from 0 to 1"
    },
    {
      "inputs": ["l5", "l8"],
      "description": "Each anonymous laboratory input has a small negative reference-averaged association; these are separate main effects.",
      "where": "Across each input's 0–10 range; no common breakpoint retained"
    }
  ],
  "surrogate": {
    "intercept": -2.07,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.42},
      {"input": "wfns45", "type": "linear", "coef": 1.68},
      {"input": "fisher34", "type": "linear", "coef": 0.44},
      {"input": "ct_ivh", "type": "linear", "coef": 0.51},
      {"input": "ct_ich", "type": "linear", "coef": 0.40},
      {"input": "htn", "type": "linear", "coef": 0.25},
      {"input": "surgery", "type": "linear", "coef": -1.43},
      {"input": "urban", "type": "linear", "coef": -0.09},
      {"input": "farmer", "type": "linear", "coef": -0.12},
      {"input": "l5", "type": "linear", "coef": -0.018},
      {"input": "l8", "type": "linear", "coef": -0.024}
    ],
    "interactions": []
  },
  "confidence_trained": 0.99
}
```