The network is **not an additive risk score**. Each effect depends on which hidden units are saturated: for continuous input \(i\), its log-odds derivative is \(\sum_j W_{2j}W_{1ji}[1-\tanh^2(z_j)]\). Binary effects require comparing predictions with that input toggled.

The striking findings are a strong **hypertension–farmer interaction**, a **nonmonotone laboratory response**, and **CT findings that sometimes lower predicted risk**.

Below, directions describe average tendencies, not universal monotonicity. Rankings and the approximate surrogate use a balanced binary-input reference, ages roughly 30–90, and l7 from 0–10; they are not registry-specific estimates. The surrogate cannot capture every higher-order interaction and has no established error bound. Apply the sigmoid to its log-odds.

Also, surgery—as defined—is information acquired during admission, not a genuinely admission-only predictor; its association is not a causal treatment effect. Training provenance cannot be established from weights alone.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "about +0.44 log-odds per decade",
      "rank": 3
    },
    "female": {
      "direction": "no clear effect",
      "size": "tiny average; context-dependent",
      "rank": 11
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "large; approximately +1.7 log-odds",
      "rank": 1
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "moderate average; sometimes reverses",
      "rank": 8
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "moderate; approximately +0.6 log-odds",
      "rank": 6
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "modest average; sometimes protective",
      "rank": 9
    },
    "htn": {
      "direction": "increases risk",
      "size": "large conditional effect; sign reversals",
      "rank": 4
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "large; approximately -1.7 log-odds",
      "rank": 2
    },
    "urban": {
      "direction": "no clear effect",
      "size": "near-zero average; conditional effects",
      "rank": 10
    },
    "farmer": {
      "direction": "increases risk",
      "size": "strongly hypertension-dependent",
      "rank": 5
    },
    "l7": {
      "direction": "no clear effect",
      "size": "nonmonotone; profile-dependent",
      "rank": 7
    }
  },
  "interactions": [
    "htn and farmer have a strong positive interaction; their joint effect is substantially greater than additive.",
    "wfns45 attenuates the average hypertension effect.",
    "The effects of fisher34 and ct_ich change with l7, including sign reversals.",
    "Urban residence has little average effect but interacts with hypertension and the laboratory value.",
    "Several laboratory interactions are nonlinear and cannot be fully represented by the surrogate's simple products."
  ],
  "unexpected": [
    {
      "inputs": ["htn", "farmer"],
      "description": "Hypertension can lower predicted risk among non-farmers but markedly raise it among farmers. These are properties of the network, not causal conclusions.",
      "where": "At age_c=0 and l7=5, with all other binary inputs 0: switching htn from 0 to 1 changes risk approximately 0.078 to 0.061 when farmer=0, versus 0.072 to 0.313 when farmer=1."
    },
    {
      "inputs": ["l7"],
      "description": "Risk can fall sharply and then rebound as the laboratory value increases.",
      "where": "At age_c=0 with every binary input 0, risk is approximately 0.221 at l7=0, reaches approximately 0.053 near l7=2.8, and rises to approximately 0.088 at l7=10. Turning points shift with other inputs."
    },
    {
      "inputs": ["fisher34", "ct_ich", "l7"],
      "description": "Either high Fisher grade or intracerebral haemorrhage can lower predicted risk at low l7, despite raising it at higher l7.",
      "where": "At age_c=0, wfns45=1, and other binary inputs initially 0, each individual CT contrast is negative at l7=0 and positive at l7=5. The Fisher contrast changes sign between l7=1 and 2; the ct_ich contrast between l7=3 and 4."
    }
  ],
  "surrogate": {
    "intercept": -2.0706,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.459},
      {"input": "female", "type": "linear", "coef": 0.044},
      {"input": "wfns45", "type": "linear", "coef": 1.7715},
      {"input": "fisher34", "type": "linear", "coef": 0.5205},
      {"input": "ct_ivh", "type": "linear", "coef": 0.777},
      {"input": "ct_ich", "type": "linear", "coef": 0.252},
      {"input": "htn", "type": "linear", "coef": -0.169},
      {"input": "surgery", "type": "linear", "coef": -1.4575},
      {"input": "urban", "type": "linear", "coef": -0.1795},
      {"input": "farmer", "type": "linear", "coef": 0.108},
      {"input": "l7", "type": "linear", "coef": -0.303},
      {"input": "l7", "type": "hinge", "knot": 1, "coef": 0.1904},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": 0.1381},
      {"input": "l7", "type": "hinge", "knot": 3, "coef": 0.0409},
      {"input": "l7", "type": "hinge", "knot": 4, "coef": -0.0177},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": -0.0299},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": -0.0244},
      {"input": "l7", "type": "hinge", "knot": 7, "coef": -0.0144},
      {"input": "l7", "type": "hinge", "knot": 8, "coef": -0.0064},
      {"input": "l7", "type": "hinge", "knot": 9, "coef": -0.0013}
    ],
    "interactions": [
      {"inputs": ["age_c", "female"], "coef": -0.015},
      {"inputs": ["age_c", "wfns45"], "coef": -0.074},
      {"inputs": ["age_c", "fisher34"], "coef": -0.014},
      {"inputs": ["age_c", "ct_ivh"], "coef": 0.029},
      {"inputs": ["age_c", "ct_ich"], "coef": -0.024},
      {"inputs": ["age_c", "htn"], "coef": -0.014},
      {"inputs": ["age_c", "surgery"], "coef": 0.02},
      {"inputs": ["age_c", "urban"], "coef": -0.002},
      {"inputs": ["age_c", "farmer"], "coef": -0.007},
      {"inputs": ["age_c", "l7"], "coef": 0.0055},
      {"inputs": ["female", "l7"], "coef": -0.015},
      {"inputs": ["wfns45", "l7"], "coef": 0.013},
      {"inputs": ["fisher34", "l7"], "coef": -0.027},
      {"inputs": ["ct_ivh", "l7"], "coef": -0.021},
      {"inputs": ["ct_ich", "l7"], "coef": 0.027},
      {"inputs": ["htn", "l7"], "coef": 0.035},
      {"inputs": ["surgery", "l7"], "coef": -0.01},
      {"inputs": ["urban", "l7"], "coef": 0.032},
      {"inputs": ["farmer", "l7"], "coef": -0.013},
      {"inputs": ["female", "wfns45"], "coef": 0.096},
      {"inputs": ["female", "fisher34"], "coef": -0.024},
      {"inputs": ["female", "ct_ivh"], "coef": -0.126},
      {"inputs": ["female", "ct_ich"], "coef": 0.095},
      {"inputs": ["female", "htn"], "coef": 0.125},
      {"inputs": ["female", "surgery"], "coef": -0.026},
      {"inputs": ["female", "urban"], "coef": -0.059},
      {"inputs": ["female", "farmer"], "coef": -0.049},
      {"inputs": ["wfns45", "fisher34"], "coef": -0.022},
      {"inputs": ["wfns45", "ct_ivh"], "coef": 0.055},
      {"inputs": ["wfns45", "ct_ich"], "coef": -0.101},
      {"inputs": ["wfns45", "htn"], "coef": -0.307},
      {"inputs": ["wfns45", "surgery"], "coef": 0.042},
      {"inputs": ["wfns45", "urban"], "coef": -0.07},
      {"inputs": ["wfns45", "farmer"], "coef": 0.052},
      {"inputs": ["fisher34", "ct_ivh"], "coef": -0.016},
      {"inputs": ["fisher34", "ct_ich"], "coef": 0.035},
      {"inputs": ["fisher34", "htn"], "coef": 0.206},
      {"inputs": ["fisher34", "surgery"], "coef": -0.115},
      {"inputs": ["fisher34", "urban"], "coef": 0.076},
      {"inputs": ["fisher34", "farmer"], "coef": -0.009},
      {"inputs": ["ct_ivh", "ct_ich"], "coef": -0.033},
      {"inputs": ["ct_ivh", "htn"], "coef": -0.069},
      {"inputs": ["ct_ivh", "surgery"], "coef": -0.101},
      {"inputs": ["ct_ivh", "urban"], "coef": -0.029},
      {"inputs": ["ct_ivh", "farmer"], "coef": 0.131},
      {"inputs": ["ct_ich", "htn"], "coef": -0.054},
      {"inputs": ["ct_ich", "surgery"], "coef": 0.084},
      {"inputs": ["ct_ich", "urban"], "coef": 0.002},
      {"inputs": ["ct_ich", "farmer"], "coef": -0.078},
      {"inputs": ["htn", "surgery"], "coef": -0.001},
      {"inputs": ["htn", "urban"], "coef": 0.2},
      {"inputs": ["htn", "farmer"], "coef": 1.564},
      {"inputs": ["surgery", "urban"], "coef": -0.038},
      {"inputs": ["surgery", "farmer"], "coef": -0.144},
      {"inputs": ["urban", "farmer"], "coef": -0.055}
    ]
  },
  "confidence_trained": 0.9
}
```