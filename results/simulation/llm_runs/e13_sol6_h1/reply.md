The network does **not** assign each input a fixed odds ratio. Its eight tanh units mix the inputs, so an effect can change with the patient profile. In particular, one unit contributes approximately \(1.814\tanh(-4.175+0.4966\,l7+\text{small adjustments})\). Together with the other units, this makes predicted risk **fall as \(l7\) approaches about 4, then rise sharply above about 6**. The surrogate below approximates the network’s *log-odds*. Surgery is recorded during admission, so its strong protective association is neither an admission-only prediction nor a causal treatment effect.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "moderate across adult ages; nonlinear", "rank": 4},
    "female": {"direction": "no clear effect", "size": "modest; changes sign with l7", "rank": 9},
    "wfns45": {"direction": "increases risk", "size": "large, roughly 1–2 log-odds", "rank": 2},
    "fisher34": {"direction": "increases risk", "size": "moderate; context-dependent", "rank": 5},
    "ct_ivh": {"direction": "increases risk", "size": "small to moderate; context-dependent", "rank": 6},
    "ct_ich": {"direction": "increases risk", "size": "small to moderate; context-dependent", "rank": 7},
    "htn": {"direction": "increases risk", "size": "weak except at high l7", "rank": 8},
    "surgery": {"direction": "decreases risk", "size": "large, roughly 1–1.6 lower log-odds", "rank": 3},
    "urban": {"direction": "no clear effect", "size": "very weak", "rank": 11},
    "farmer": {"direction": "no clear effect", "size": "weak; changes sign", "rank": 10},
    "l7": {"direction": "no clear effect", "size": "large U-shape; steep high-end rise", "rank": 1}
  },
  "interactions": [
    "l7 changes the effects of sex, CT findings, hypertension, age, and WFNS grade.",
    "The apparent benefit associated with surgery varies with Fisher grade and intraventricular haemorrhage.",
    "Hidden-unit saturation makes these effects nonlinear rather than fixed odds ratios."
  ],
  "unexpected": [
    {
      "inputs": ["l7"],
      "description": "Predicted risk initially falls, bottoms out, then rises steeply.",
      "where": "Trough around l7=4–5; strong rise from roughly l7=6–9."
    },
    {
      "inputs": ["female", "l7"],
      "description": "Female is associated with lower predicted risk at low l7 but higher risk at high l7.",
      "where": "Sign changes around l7=4–5 for an age-60 reference profile with other indicators zero."
    },
    {
      "inputs": ["fisher34", "ct_ivh", "l7"],
      "description": "In a reference profile, higher Fisher grade or IVH can slightly lower rather than raise predicted risk at the very low end of l7.",
      "where": "Fisher reversal near l7=0; IVH reversal below about l7=2, with age_c=0 and other indicators zero."
    },
    {
      "inputs": ["age_c", "l7"],
      "description": "The age effect is not monotone in every profile; it can flatten or reverse at older ages.",
      "where": "Around age_c=2 (age 80) when l7 is about 4 and other indicators are zero."
    }
  ],
  "surrogate": {
    "intercept": -1.58,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.45},
      {"input": "female", "type": "linear", "coef": -0.4},
      {"input": "wfns45", "type": "linear", "coef": 1.45},
      {"input": "fisher34", "type": "linear", "coef": 0.1},
      {"input": "ct_ivh", "type": "linear", "coef": -0.1},
      {"input": "ct_ich", "type": "linear", "coef": 0.75},
      {"input": "htn", "type": "linear", "coef": -0.1},
      {"input": "surgery", "type": "linear", "coef": -1.6},
      {"input": "urban", "type": "linear", "coef": 0.1},
      {"input": "farmer", "type": "linear", "coef": 0.1},
      {"input": "l7", "type": "linear", "coef": -0.28},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": 0.12},
      {"input": "l7", "type": "hinge", "knot": 4, "coef": 0.19},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": 0.16},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": 0.27},
      {"input": "l7", "type": "hinge", "knot": 7, "coef": 0.35},
      {"input": "l7", "type": "hinge", "knot": 8, "coef": 0.16},
      {"input": "l7", "type": "hinge", "knot": 9, "coef": -0.2}
    ],
    "interactions": [
      {"inputs": ["age_c", "l7"], "coef": -0.01},
      {"inputs": ["female", "l7"], "coef": 0.12},
      {"inputs": ["wfns45", "l7"], "coef": 0.07},
      {"inputs": ["fisher34", "l7"], "coef": 0.09},
      {"inputs": ["ct_ivh", "l7"], "coef": 0.09},
      {"inputs": ["ct_ich", "l7"], "coef": -0.07},
      {"inputs": ["htn", "l7"], "coef": 0.1},
      {"inputs": ["surgery", "l7"], "coef": 0.05},
      {"inputs": ["farmer", "l7"], "coef": -0.025},
      {"inputs": ["surgery", "wfns45"], "coef": 0.15},
      {"inputs": ["surgery", "fisher34"], "coef": -0.2},
      {"inputs": ["surgery", "ct_ivh"], "coef": -0.4},
      {"inputs": ["surgery", "htn"], "coef": 0.05},
      {"inputs": ["fisher34", "ct_ivh"], "coef": -0.15},
      {"inputs": ["wfns45", "ct_ich"], "coef": 0.2},
      {"inputs": ["wfns45", "htn"], "coef": 0.15}
    ]
  },
  "confidence_trained": 0.99
}
```