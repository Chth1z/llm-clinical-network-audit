The network’s effects depend on **both hidden layers**, not individual input weights. At the formal midpoint—age 60, laboratories 5, binary inputs 0.5—it gives log-odds approximately **−0.029**, or probability **0.493**. This midpoint is an analytical reference, not an actual patient.

Its local log-odds derivatives are approximately:
- age_c **+0.548**, wfns45 **+2.203**, surgery **−2.280**;
- l5 **+0.205**, l8 **+0.194**, but l3 **−0.107**, l1 **−0.066**, and l10 **−0.063**;
- farmer **−0.034**, female **+0.047**, and l9 almost zero.

Thus, the laboratories do not share a simple “higher is worse” relationship. Their effects involve cancellation, saturation, and interactions. Their anonymous names do not support medical interpretations.

Below, ranks are approximate reference-based importance, not population importance; “no clear effect” does **not** mean the network ignores that input. The surrogate is a **hand-derived, unvalidated approximation**, without a verified prediction-error bound. Its hinge locations are approximation choices, not discovered clinical thresholds; repeated input names denote squares. Surgery’s association is not causal, and its during-admission coding prevents a genuinely admission-only prediction.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "large", "rank": 3},
    "female": {"direction": "no clear effect", "size": "very small; locally positive", "rank": 18},
    "wfns45": {"direction": "increases risk", "size": "very large", "rank": 2},
    "fisher34": {"direction": "increases risk", "size": "moderate", "rank": 9},
    "ct_ivh": {"direction": "increases risk", "size": "moderate", "rank": 6},
    "ct_ich": {"direction": "increases risk", "size": "moderate", "rank": 8},
    "htn": {"direction": "increases risk", "size": "small", "rank": 12},
    "surgery": {"direction": "decreases risk", "size": "very large", "rank": 1},
    "urban": {"direction": "decreases risk", "size": "small", "rank": 13},
    "farmer": {"direction": "decreases risk", "size": "very small; conditional", "rank": 19},
    "l1": {"direction": "no clear effect", "size": "locally decreasing; nonlinear", "rank": 10},
    "l2": {"direction": "no clear effect", "size": "locally decreasing; nonlinear", "rank": 14},
    "l3": {"direction": "no clear effect", "size": "moderate local decrease", "rank": 7},
    "l4": {"direction": "no clear effect", "size": "weak local sensitivity", "rank": 16},
    "l5": {"direction": "increases risk", "size": "large local laboratory effect", "rank": 4},
    "l6": {"direction": "no clear effect", "size": "weak local sensitivity", "rank": 17},
    "l7": {"direction": "no clear effect", "size": "weak local sensitivity", "rank": 15},
    "l8": {"direction": "increases risk", "size": "large local laboratory effect", "rank": 5},
    "l9": {"direction": "no clear effect", "size": "locally almost zero", "rank": 20},
    "l10": {"direction": "no clear effect", "size": "locally decreasing; nonlinear", "rank": 11}
  },
  "unexpected": [
    {
      "inputs": ["l1", "l3", "l10"],
      "description": "Increasing these laboratory inputs locally lowers predicted death risk. Their approximate log-odds derivatives are -0.066, -0.107, and -0.063 per laboratory unit, respectively; these are conditional slopes, not universal directions.",
      "where": "Around laboratory values 5 on their 0-10 scales, age_c=0, and other binary inputs at the formal reference 0.5."
    },
    {
      "inputs": ["l5", "l8"],
      "description": "These laboratory inputs have substantially positive local effects, unlike several other laboratories. Their approximate log-odds derivatives are +0.205 and +0.194 per unit; their effects are not separable from the other inputs.",
      "where": "Around l5=5 and l8=5, with other laboratories 5, age_c=0, and binary inputs 0.5. There is no literal hard threshold in the tanh network."
    },
    {
      "inputs": ["farmer"],
      "description": "The local signed effect is weakly risk-decreasing, rather than an automatically adverse occupational association.",
      "where": "At age_c=0, laboratory values 5, and binary inputs at the formal reference 0.5; local log-odds derivative approximately -0.034."
    },
    {
      "inputs": ["l9"],
      "description": "Its substantial individual hidden-layer weights nearly cancel in the final local prediction. Small local sensitivity does not establish global irrelevance.",
      "where": "Around l9=5 with all other laboratories 5, age_c=0, and binary inputs 0.5."
    }
  ],
  "surrogate": {
    "intercept": -3.5036,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.39255},
      {"input": "female", "type": "linear", "coef": -0.00263},
      {"input": "wfns45", "type": "linear", "coef": 1.82775},
      {"input": "fisher34", "type": "linear", "coef": 0.32858},
      {"input": "ct_ivh", "type": "linear", "coef": 0.4954},
      {"input": "ct_ich", "type": "linear", "coef": 0.38072},
      {"input": "htn", "type": "linear", "coef": 0.23833},
      {"input": "surgery", "type": "linear", "coef": -1.73592},
      {"input": "urban", "type": "linear", "coef": -0.17056},
      {"input": "farmer", "type": "linear", "coef": -0.04576},
      {"input": "l1", "type": "linear", "coef": 0.040106},
      {"input": "l2", "type": "linear", "coef": 0.070976},
      {"input": "l3", "type": "linear", "coef": 0.073296},
      {"input": "l4", "type": "linear", "coef": 0.043476},
      {"input": "l5", "type": "linear", "coef": 0.070971},
      {"input": "l6", "type": "linear", "coef": 0.063816},
      {"input": "l7", "type": "linear", "coef": 0.069706},
      {"input": "l8", "type": "linear", "coef": 0.139411},
      {"input": "l9", "type": "linear", "coef": 0.055926},
      {"input": "l10", "type": "linear", "coef": 0.093456},
      {"input": "l1", "type": "hinge", "knot": 5, "coef": -0.051072},
      {"input": "l2", "type": "hinge", "knot": 5, "coef": -0.051072},
      {"input": "l3", "type": "hinge", "knot": 5, "coef": -0.051072},
      {"input": "l4", "type": "hinge", "knot": 5, "coef": -0.051072},
      {"input": "l5", "type": "hinge", "knot": 5, "coef": -0.051072},
      {"input": "l6", "type": "hinge", "knot": 5, "coef": -0.051072},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": -0.051072},
      {"input": "l8", "type": "hinge", "knot": 5, "coef": -0.051072},
      {"input": "l9", "type": "hinge", "knot": 5, "coef": -0.051072},
      {"input": "l10", "type": "hinge", "knot": 5, "coef": -0.051072}
    ],
    "interactions": [
      {"inputs": ["age_c", "age_c"], "coef": -0.008413},
      {"inputs": ["l1", "l1"], "coef": -0.00252},
      {"inputs": ["l2", "l2"], "coef": -0.004812},
      {"inputs": ["l3", "l3"], "coef": -0.005742},
      {"inputs": ["l4", "l4"], "coef": -0.004695},
      {"inputs": ["l5", "l5"], "coef": -0.003299},
      {"inputs": ["l6", "l6"], "coef": -0.004365},
      {"inputs": ["l7", "l7"], "coef": -0.004191},
      {"inputs": ["l8", "l8"], "coef": -0.005225},
      {"inputs": ["l9", "l9"], "coef": -0.004557},
      {"inputs": ["l10", "l10"], "coef": -0.006026},
      {"inputs": ["l5", "l8"], "coef": 0.01467},
      {"inputs": ["wfns45", "l5"], "coef": -0.0172},
      {"inputs": ["wfns45", "l8"], "coef": -0.02468},
      {"inputs": ["surgery", "l5"], "coef": 0.01831},
      {"inputs": ["surgery", "l8"], "coef": 0.01435},
      {"inputs": ["wfns45", "surgery"], "coef": 0.01322}
    ]
  },
  "confidence_trained": 0.9
}
```