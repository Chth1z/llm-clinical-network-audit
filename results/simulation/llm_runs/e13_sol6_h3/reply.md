The network is **not a smooth, additive admission risk score**. One hidden unit creates a sharp rise in predicted risk around ages 66–70; other units make the effect of `l7` change with age. With every binary input set to zero, raising `l7` from 0 to 5 raises predicted risk from about 1.5% to 3.0% at age 60, but lowers it from about 32% to 9.7% at age 70. The surrogate below approximates the network’s **log-odds**, not clinical causation. In particular, `surgery` is determined during admission, so a prediction using it is not strictly available at admission.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "very large; nonmonotone with a sharp rise", "rank": 1},
    "female": {"direction": "no clear effect", "size": "small; reverses near the age rise", "rank": 10},
    "wfns45": {"direction": "increases risk", "size": "very large", "rank": 2},
    "fisher34": {"direction": "increases risk", "size": "moderate, stronger at older ages", "rank": 5},
    "ct_ivh": {"direction": "increases risk", "size": "moderate and context-dependent", "rank": 6},
    "ct_ich": {"direction": "increases risk", "size": "small", "rank": 9},
    "htn": {"direction": "increases risk", "size": "modest; varies with l7", "rank": 7},
    "surgery": {"direction": "decreases risk", "size": "very large association", "rank": 3},
    "urban": {"direction": "no clear effect", "size": "small and context-dependent", "rank": 8},
    "farmer": {"direction": "no clear effect", "size": "small and sign-changing", "rank": 11},
    "l7": {"direction": "no clear effect", "size": "large; reverses with age", "rank": 4}
  },
  "interactions": [
    "Age and l7 interact strongly: higher l7 can raise risk near age 60 but lower it at older ages.",
    "The steep age rise shifts younger with female sex or WFNS 4–5 and older as l7 rises.",
    "WFNS, surgery, CT findings and hypertension are not additive because several tanh units saturate."
  ],
  "unexpected": [
    {
      "inputs": ["age_c"],
      "description": "Predicted risk can fall from younger adulthood toward age 60, then rises abruptly rather than steadily.",
      "where": "The steep rise is roughly age_c 0.6–1.1 (ages 66–71), shifting with other inputs."
    },
    {
      "inputs": ["age_c", "l7"],
      "description": "The effect of l7 reverses with age: l7 0 to 5 raises risk at age 60 but markedly lowers it at age 70 for the all-zero binary profile.",
      "where": "Reversal occurs around age_c 0.5–1.0 (ages 65–70), especially across l7 0–6."
    },
    {
      "inputs": ["female", "age_c"],
      "description": "Female sex is slightly protective in many profiles but can increase predicted risk around the age rise.",
      "where": "Approximately age_c 0.7–1.1 (ages 67–71)."
    },
    {
      "inputs": ["urban"],
      "description": "Urban residence often raises predicted risk in middle-aged profiles, although its effect can reverse.",
      "where": "Most apparent near age_c 0–1; reversal is possible at older ages and higher l7."
    }
  ],
  "surrogate": {
    "intercept": -4.153,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.71},
      {"input": "female", "type": "linear", "coef": -0.288},
      {"input": "wfns45", "type": "linear", "coef": 1.66},
      {"input": "fisher34", "type": "linear", "coef": 0.474},
      {"input": "ct_ivh", "type": "linear", "coef": 0.35},
      {"input": "ct_ich", "type": "linear", "coef": 0.24},
      {"input": "htn", "type": "linear", "coef": 0.048},
      {"input": "surgery", "type": "linear", "coef": -1.83},
      {"input": "urban", "type": "linear", "coef": 0.57},
      {"input": "farmer", "type": "linear", "coef": -0.077},
      {"input": "l7", "type": "linear", "coef": -0.19},
      {"input": "age_c", "type": "hinge", "knot": 0, "coef": 0.15},
      {"input": "age_c", "type": "hinge", "knot": 0.4, "coef": 1.365},
      {"input": "age_c", "type": "hinge", "knot": 0.6, "coef": 1.73},
      {"input": "age_c", "type": "hinge", "knot": 0.8, "coef": -0.36},
      {"input": "age_c", "type": "hinge", "knot": 1, "coef": -1.785},
      {"input": "age_c", "type": "hinge", "knot": 1.2, "coef": -0.87},
      {"input": "age_c", "type": "hinge", "knot": 1.5, "coef": 0.293},
      {"input": "age_c", "type": "hinge", "knot": 1.8, "coef": 0.63},
      {"input": "age_c", "type": "hinge", "knot": 2.2, "coef": 0.13},
      {"input": "age_c", "type": "hinge", "knot": 2.6, "coef": -0.37},
      {"input": "l7", "type": "hinge", "knot": 1, "coef": 0.27},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": 0.23},
      {"input": "l7", "type": "hinge", "knot": 4, "coef": -0.16},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": -0.13},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": -0.06},
      {"input": "l7", "type": "hinge", "knot": 7, "coef": -0.03}
    ],
    "interactions": [
      {"inputs": ["age_c", "l7"], "coef": -0.2},
      {"inputs": ["age_c", "female"], "coef": 0.08},
      {"inputs": ["age_c", "fisher34"], "coef": 0.2},
      {"inputs": ["age_c", "ct_ivh"], "coef": 0.1},
      {"inputs": ["age_c", "ct_ich"], "coef": 0.1},
      {"inputs": ["age_c", "htn"], "coef": 0.15},
      {"inputs": ["age_c", "surgery"], "coef": 0.08},
      {"inputs": ["age_c", "urban"], "coef": 0.05},
      {"inputs": ["age_c", "farmer"], "coef": 0.1},
      {"inputs": ["female", "l7"], "coef": 0.04},
      {"inputs": ["wfns45", "l7"], "coef": 0.03},
      {"inputs": ["htn", "l7"], "coef": 0.07},
      {"inputs": ["surgery", "l7"], "coef": 0.03},
      {"inputs": ["urban", "l7"], "coef": -0.04},
      {"inputs": ["farmer", "l7"], "coef": 0.02},
      {"inputs": ["wfns45", "fisher34"], "coef": -0.08},
      {"inputs": ["wfns45", "ct_ivh"], "coef": -0.1},
      {"inputs": ["wfns45", "htn"], "coef": -0.14},
      {"inputs": ["wfns45", "urban"], "coef": 0.13},
      {"inputs": ["fisher34", "ct_ivh"], "coef": 0.05},
      {"inputs": ["fisher34", "htn"], "coef": -0.08},
      {"inputs": ["fisher34", "urban"], "coef": -0.08},
      {"inputs": ["fisher34", "farmer"], "coef": -0.1},
      {"inputs": ["ct_ivh", "htn"], "coef": 0.05},
      {"inputs": ["ct_ivh", "urban"], "coef": 0.05},
      {"inputs": ["htn", "urban"], "coef": -0.1},
      {"inputs": ["urban", "farmer"], "coef": -0.12},
      {"inputs": ["surgery", "wfns45"], "coef": 0.04},
      {"inputs": ["surgery", "fisher34"], "coef": 0.04},
      {"inputs": ["surgery", "ct_ivh"], "coef": 0.08},
      {"inputs": ["surgery", "ct_ich"], "coef": -0.04},
      {"inputs": ["surgery", "urban"], "coef": -0.1},
      {"inputs": ["surgery", "farmer"], "coef": -0.05},
      {"inputs": ["female", "htn"], "coef": 0.06},
      {"inputs": ["female", "urban"], "coef": -0.05}
    ]
  },
  "confidence_trained": 0.98
}
```