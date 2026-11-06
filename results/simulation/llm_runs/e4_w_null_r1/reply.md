For a continuous input, the network’s log-odds slope is
\[
\frac{\partial\eta}{\partial x_i}
=\sum_j W_{2j}W_{1ji}\,[1-\tanh^2(W_{1j}x+b_{1j})].
\]
Thus effects change as hidden units saturate; individual weight signs are not sufficient. Binary effects require comparing predictions with the indicator switched.

Poor WFNS and surgery have strong, opposing predictive associations. Crucially, **age is not uniformly harmful, l7 is nonmonotone, and intracerebral haemorrhage can reverse direction**. Concrete examples appear below.

For the approximate rankings and surrogate, I assume ages 20–90, l7 spanning 0–10, and balanced binary indicators. The surrogate is an **analytic, unvalidated approximation**, not an exact distillation or a claim of measured accuracy. Apply the sigmoid to its log-odds. The permitted additive-hinge/pairwise form cannot reproduce every higher-order interaction.

These are model associations, not causal effects. Surgery occurs during admission, so this is not strictly an admission-only predictor. Training provenance cannot be established from weights; the final confidence is subjective.

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
      "size": "small, context-dependent",
      "rank": 11
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "large",
      "rank": 1
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "moderate overall",
      "rank": 6
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "moderate overall",
      "rank": 5
    },
    "ct_ich": {
      "direction": "no clear effect",
      "size": "substantial conditional sign reversals",
      "rank": 7
    },
    "htn": {
      "direction": "increases risk",
      "size": "modest; stronger at low l7",
      "rank": 8
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "large predictive association",
      "rank": 3
    },
    "urban": {
      "direction": "decreases risk",
      "size": "modest average; conditional reversals",
      "rank": 9
    },
    "farmer": {
      "direction": "no clear effect",
      "size": "small average decrease; sign-changing",
      "rank": 10
    },
    "l7": {
      "direction": "no clear effect",
      "size": "nonmonotone; sometimes substantial",
      "rank": 4
    }
  },
  "interactions": [
    "Age and l7 jointly shift turning points; neither has a universally monotone effect.",
    "The ct_ich association can change from negative to positive as l7 increases.",
    "Urban residence tends to attenuate the increase associated with wfns45.",
    "The joint wfns45 and surgery association is not simply additive.",
    "Farmer and urban associations depend on ct_ich and other severity indicators.",
    "The positive hypertension association tends to weaken as l7 increases."
  ],
  "unexpected": [
    {
      "inputs": ["age_c", "l7"],
      "description": "Older age can lower predicted mortality. With all binary inputs zero and l7=0, predictions are approximately 5.8% at age 60, 2.7% at age 80, and 10.9% at age 90.",
      "where": "For this profile, risk decreases over approximately ages 54-76, then increases; the older-age minimum is near age_c=1.6, or 76 years."
    },
    {
      "inputs": ["ct_ich", "l7"],
      "description": "At age 60 with all other binary inputs zero, ct_ich lowers probability from approximately 5.8% to 2.1% when l7=0, but raises it from approximately 7.3% to 15.3% when l7=5.",
      "where": "For age_c=0 and all other binary inputs zero, the ct_ich contrast changes sign near l7=1.0."
    },
    {
      "inputs": ["l7", "age_c"],
      "description": "The laboratory response can be U-shaped. At age 30 with every binary input zero, probabilities at l7=0, 5, and 10 are approximately 11.1%, 4.1%, and 5.1%. Other profiles have different turning points.",
      "where": "For age_c=-3 and all binary inputs zero, the minimum is near l7=6.5 on its 0-10 scale."
    },
    {
      "inputs": ["farmer"],
      "description": "Occupation is not neutral and its association changes direction. Despite a small negative average association in the reference domain, farmer increases probability from approximately 7.3% to 9.3% in the stated example.",
      "where": "age_c=0, l7=5, and every other binary input zero; no universal cutoff separates positive and negative farmer associations."
    }
  ],
  "surrogate": {
    "intercept": -4.066,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": -0.327},
      {"input": "female", "type": "linear", "coef": 0.124},
      {"input": "wfns45", "type": "linear", "coef": 2.1855},
      {"input": "fisher34", "type": "linear", "coef": 0.385},
      {"input": "ct_ivh", "type": "linear", "coef": 0.631},
      {"input": "ct_ich", "type": "linear", "coef": 0.0875},
      {"input": "htn", "type": "linear", "coef": 0.618},
      {"input": "surgery", "type": "linear", "coef": -1.915},
      {"input": "urban", "type": "linear", "coef": -0.0065},
      {"input": "farmer", "type": "linear", "coef": -0.1845},
      {"input": "l7", "type": "linear", "coef": 0.19688},
      {"input": "age_c", "type": "hinge", "knot": -3, "coef": 0.371},
      {"input": "age_c", "type": "hinge", "knot": -2, "coef": 0.192},
      {"input": "age_c", "type": "hinge", "knot": -1, "coef": 0.025},
      {"input": "age_c", "type": "hinge", "knot": 0, "coef": -0.002},
      {"input": "age_c", "type": "hinge", "knot": 1, "coef": -0.051},
      {"input": "age_c", "type": "hinge", "knot": 2, "coef": -0.064},
      {"input": "l7", "type": "hinge", "knot": 1, "coef": -0.08639},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": -0.07311},
      {"input": "l7", "type": "hinge", "knot": 3, "coef": -0.0287},
      {"input": "l7", "type": "hinge", "knot": 4, "coef": 0.00526},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": 0.01987},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": 0.02049},
      {"input": "l7", "type": "hinge", "knot": 7, "coef": 0.01812},
      {"input": "l7", "type": "hinge", "knot": 8, "coef": 0.01458},
      {"input": "l7", "type": "hinge", "knot": 9, "coef": 0.01108}
    ],
    "interactions": [
      {"inputs": ["age_c", "l7"], "coef": 0.031},
      {"inputs": ["age_c", "female"], "coef": -0.011},
      {"inputs": ["age_c", "wfns45"], "coef": 0.139},
      {"inputs": ["age_c", "fisher34"], "coef": 0.008},
      {"inputs": ["age_c", "ct_ivh"], "coef": -0.01},
      {"inputs": ["age_c", "ct_ich"], "coef": -0.001},
      {"inputs": ["age_c", "htn"], "coef": 0.004},
      {"inputs": ["age_c", "surgery"], "coef": -0.024},
      {"inputs": ["age_c", "urban"], "coef": 0.006},
      {"inputs": ["age_c", "farmer"], "coef": 0.043},
      {"inputs": ["l7", "female"], "coef": -0.031},
      {"inputs": ["l7", "wfns45"], "coef": -0.029},
      {"inputs": ["l7", "fisher34"], "coef": 0.005},
      {"inputs": ["l7", "ct_ivh"], "coef": -0.014},
      {"inputs": ["l7", "ct_ich"], "coef": 0.026},
      {"inputs": ["l7", "htn"], "coef": -0.058},
      {"inputs": ["l7", "surgery"], "coef": 0.028},
      {"inputs": ["l7", "urban"], "coef": -0.026},
      {"inputs": ["l7", "farmer"], "coef": 0.037},
      {"inputs": ["female", "wfns45"], "coef": 0.034},
      {"inputs": ["female", "fisher34"], "coef": 0.006},
      {"inputs": ["female", "ct_ivh"], "coef": -0.04},
      {"inputs": ["female", "ct_ich"], "coef": 0.006},
      {"inputs": ["female", "htn"], "coef": -0.003},
      {"inputs": ["female", "surgery"], "coef": -0.028},
      {"inputs": ["female", "urban"], "coef": 0.055},
      {"inputs": ["female", "farmer"], "coef": 0.007},
      {"inputs": ["wfns45", "fisher34"], "coef": -0.13},
      {"inputs": ["wfns45", "ct_ivh"], "coef": -0.096},
      {"inputs": ["wfns45", "ct_ich"], "coef": 0.059},
      {"inputs": ["wfns45", "htn"], "coef": -0.014},
      {"inputs": ["wfns45", "surgery"], "coef": 0.157},
      {"inputs": ["wfns45", "urban"], "coef": -0.341},
      {"inputs": ["wfns45", "farmer"], "coef": -0.073},
      {"inputs": ["fisher34", "ct_ivh"], "coef": 0.008},
      {"inputs": ["fisher34", "ct_ich"], "coef": -0.049},
      {"inputs": ["fisher34", "surgery"], "coef": 0.054},
      {"inputs": ["fisher34", "urban"], "coef": 0.106},
      {"inputs": ["fisher34", "farmer"], "coef": 0.015},
      {"inputs": ["ct_ivh", "ct_ich"], "coef": -0.004},
      {"inputs": ["ct_ivh", "htn"], "coef": 0.012},
      {"inputs": ["ct_ivh", "surgery"], "coef": -0.057},
      {"inputs": ["ct_ivh", "urban"], "coef": -0.014},
      {"inputs": ["ct_ivh", "farmer"], "coef": -0.067},
      {"inputs": ["ct_ich", "htn"], "coef": 0.108},
      {"inputs": ["ct_ich", "surgery"], "coef": 0.144},
      {"inputs": ["ct_ich", "urban"], "coef": -0.156},
      {"inputs": ["ct_ich", "farmer"], "coef": -0.212},
      {"inputs": ["htn", "surgery"], "coef": -0.055},
      {"inputs": ["htn", "urban"], "coef": -0.03},
      {"inputs": ["htn", "farmer"], "coef": -0.086},
      {"inputs": ["surgery", "urban"], "coef": 0.1},
      {"inputs": ["surgery", "farmer"], "coef": 0.053},
      {"inputs": ["urban", "farmer"], "coef": 0.095}
    ]
  },
  "confidence_trained": 0.9
}
```