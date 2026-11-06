This is **not a monotone risk score**. Each continuous-input effect is
\[
\frac{\partial\text{log-odds}}{\partial x_i}
=\sum_j W_{2j}W_{1ji}\bigl(1-\tanh^2(z_j)\bigr).
\]
Thus, saturation and cancellation between hidden units can reverse an input’s effect.

For example, at age 60 with every binary input zero, the network predicts approximately **17%, 8%, and 68%** mortality at `l7` values 0, 4, and 10. At `l7=0`, that same profile has a region where **older age lowers predicted risk**. These are properties of the supplied weights, not clinical recommendations.

Below is an **analytic approximation**, not a numerically validated distillation. Directions and ranks describe broad tendencies over ages roughly 20–90, `l7` 0–10, and balanced binary profiles; they are not universal signs or registry-specific importance estimates. The surrogate cannot reproduce every higher-order interaction. Also, `surgery` uses information acquired during admission, and its negative association is not a causal treatment effect. The weights look structured rather than random, but cannot establish their provenance.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "large overall; local reversals",
      "rank": 2
    },
    "female": {
      "direction": "no clear effect",
      "size": "small average; sign changes",
      "rank": 11
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "large",
      "rank": 3
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "moderate; context dependent",
      "rank": 6
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "moderate; context dependent",
      "rank": 5
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "small to moderate",
      "rank": 7
    },
    "htn": {
      "direction": "increases risk",
      "size": "small average; not uniform",
      "rank": 8
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "large",
      "rank": 4
    },
    "urban": {
      "direction": "decreases risk",
      "size": "small average; not uniform",
      "rank": 9
    },
    "farmer": {
      "direction": "no clear effect",
      "size": "small average; sign changes",
      "rank": 10
    },
    "l7": {
      "direction": "increases risk",
      "size": "large high-end rise; nonmonotone",
      "rank": 1
    }
  },
  "interactions": [
    "Age and l7 have nonlinear joint effects: low-l7 profiles can have age-related risk reversals.",
    "Female and farmer contrasts can reverse sign as l7 changes.",
    "Severity, CT findings and surgery are not additive; their contrasts depend on which hidden units are saturated."
  ],
  "unexpected": [
    {
      "inputs": ["l7"],
      "description": "Risk can first fall and then rise sharply. At age 60 with all binary inputs zero, probabilities are approximately 0.17, 0.079 and 0.68 at l7=0, 4 and 10.",
      "where": "For that profile, the minimum is near l7=4.3. Hidden unit 5 crosses zero at l7=8.41; other inputs shift that transition."
    },
    {
      "inputs": ["age_c", "l7"],
      "description": "Older age can lower predicted mortality rather than raise it.",
      "where": "With l7=0 and all binary inputs zero, risk decreases approximately between ages 62 and 79, corresponding to age_c=0.2 to 1.9, then rises again."
    },
    {
      "inputs": ["female", "farmer", "l7"],
      "description": "The female contrast changes from about -0.32 to +0.18 log-odds, while the farmer contrast changes from about +0.29 to -0.19.",
      "where": "Compare l7=0 with l7=5 at age 60, toggling each indicator separately while keeping all other binary inputs zero."
    }
  ],
  "surrogate": {
    "intercept": -2.653,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.392},
      {"input": "female", "type": "linear", "coef": -0.055},
      {"input": "wfns45", "type": "linear", "coef": 1.899},
      {"input": "fisher34", "type": "linear", "coef": 0.479},
      {"input": "ct_ivh", "type": "linear", "coef": 0.366},
      {"input": "ct_ich", "type": "linear", "coef": 0.460},
      {"input": "htn", "type": "linear", "coef": -0.048},
      {"input": "surgery", "type": "linear", "coef": -1.665},
      {"input": "urban", "type": "linear", "coef": -0.185},
      {"input": "farmer", "type": "linear", "coef": -0.038},
      {"input": "l7", "type": "linear", "coef": -0.012},
      {"input": "age_c", "type": "hinge", "knot": -3, "coef": 0.048},
      {"input": "age_c", "type": "hinge", "knot": -2, "coef": 0.076},
      {"input": "age_c", "type": "hinge", "knot": -1, "coef": 0.089},
      {"input": "age_c", "type": "hinge", "knot": 0, "coef": 0.061},
      {"input": "age_c", "type": "hinge", "knot": 1, "coef": -0.004},
      {"input": "age_c", "type": "hinge", "knot": 2, "coef": -0.061},
      {"input": "age_c", "type": "hinge", "knot": 3, "coef": -0.079},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": 0.039},
      {"input": "l7", "type": "hinge", "knot": 4, "coef": 0.092},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": 0.144},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": 0.246},
      {"input": "l7", "type": "hinge", "knot": 7, "coef": 0.292},
      {"input": "l7", "type": "hinge", "knot": 8, "coef": 0.120},
      {"input": "l7", "type": "hinge", "knot": 9, "coef": -0.171}
    ],
    "interactions": [
      {"inputs": ["age_c", "l7"], "coef": -0.005},
      {"inputs": ["age_c", "female"], "coef": -0.055},
      {"inputs": ["age_c", "wfns45"], "coef": 0.033},
      {"inputs": ["age_c", "fisher34"], "coef": 0.003},
      {"inputs": ["age_c", "ct_ivh"], "coef": 0.007},
      {"inputs": ["age_c", "ct_ich"], "coef": -0.002},
      {"inputs": ["age_c", "htn"], "coef": 0.007},
      {"inputs": ["age_c", "surgery"], "coef": -0.092},
      {"inputs": ["age_c", "urban"], "coef": 0.001},
      {"inputs": ["age_c", "farmer"], "coef": -0.008},
      {"inputs": ["l7", "female"], "coef": 0.009},
      {"inputs": ["l7", "wfns45"], "coef": -0.007},
      {"inputs": ["l7", "fisher34"], "coef": -0.008},
      {"inputs": ["l7", "ct_ivh"], "coef": 0.006},
      {"inputs": ["l7", "ct_ich"], "coef": -0.034},
      {"inputs": ["l7", "htn"], "coef": 0.034},
      {"inputs": ["l7", "surgery"], "coef": 0.005},
      {"inputs": ["l7", "urban"], "coef": 0.008},
      {"inputs": ["female", "wfns45"], "coef": -0.034},
      {"inputs": ["female", "fisher34"], "coef": -0.063},
      {"inputs": ["female", "ct_ivh"], "coef": 0.054},
      {"inputs": ["female", "ct_ich"], "coef": 0.020},
      {"inputs": ["female", "htn"], "coef": -0.025},
      {"inputs": ["female", "surgery"], "coef": 0.031},
      {"inputs": ["female", "urban"], "coef": 0.003},
      {"inputs": ["female", "farmer"], "coef": 0.079},
      {"inputs": ["wfns45", "fisher34"], "coef": -0.027},
      {"inputs": ["wfns45", "ct_ivh"], "coef": 0.017},
      {"inputs": ["wfns45", "ct_ich"], "coef": -0.099},
      {"inputs": ["wfns45", "htn"], "coef": 0.010},
      {"inputs": ["wfns45", "surgery"], "coef": -0.043},
      {"inputs": ["wfns45", "urban"], "coef": -0.051},
      {"inputs": ["wfns45", "farmer"], "coef": -0.044},
      {"inputs": ["fisher34", "ct_ivh"], "coef": 0.087},
      {"inputs": ["fisher34", "ct_ich"], "coef": 0.032},
      {"inputs": ["fisher34", "htn"], "coef": -0.057},
      {"inputs": ["fisher34", "surgery"], "coef": -0.004},
      {"inputs": ["fisher34", "urban"], "coef": 0.031},
      {"inputs": ["fisher34", "farmer"], "coef": 0.105},
      {"inputs": ["ct_ivh", "ct_ich"], "coef": 0.003},
      {"inputs": ["ct_ivh", "htn"], "coef": 0.017},
      {"inputs": ["ct_ivh", "surgery"], "coef": 0.122},
      {"inputs": ["ct_ivh", "urban"], "coef": 0.041},
      {"inputs": ["ct_ivh", "farmer"], "coef": -0.052},
      {"inputs": ["ct_ich", "htn"], "coef": -0.048},
      {"inputs": ["ct_ich", "surgery"], "coef": 0.011},
      {"inputs": ["ct_ich", "urban"], "coef": 0.056},
      {"inputs": ["ct_ich", "farmer"], "coef": 0.019},
      {"inputs": ["htn", "surgery"], "coef": 0.073},
      {"inputs": ["htn", "urban"], "coef": 0.004},
      {"inputs": ["htn", "farmer"], "coef": 0.052},
      {"inputs": ["surgery", "urban"], "coef": 0.039},
      {"inputs": ["surgery", "farmer"], "coef": 0.038},
      {"inputs": ["urban", "farmer"], "coef": 0.001}
    ]
  },
  "confidence_trained": 0.95
}
```