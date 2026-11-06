The network computes **log-odds**, not a fixed point score: each input changes eight `tanh` units, whose contributions can saturate and offset one another. In these weights, age and high WFNS grade generally raise predicted mortality; aneurysm treatment during admission generally lowers it. The laboratory value and several other effects change with the patient’s other inputs. The surrogate below approximates the network’s log-odds; its ranks are rough because no patient distribution was supplied. Treatment is recorded *during* admission, so its association should not be read as a causal benefit or used as an admission-time prediction.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "about 0.6 log-odds per decade", "rank": 2},
    "female": {"direction": "no clear effect", "size": "small and context-dependent", "rank": 11},
    "wfns45": {"direction": "increases risk", "size": "large, roughly 1.5–2 log-odds", "rank": 1},
    "fisher34": {"direction": "increases risk", "size": "moderate; reverses at low l7", "rank": 7},
    "ct_ivh": {"direction": "increases risk", "size": "moderate", "rank": 10},
    "ct_ich": {"direction": "increases risk", "size": "moderate", "rank": 9},
    "htn": {"direction": "no clear effect", "size": "strongly depends on farmer", "rank": 5},
    "surgery": {"direction": "decreases risk", "size": "large, roughly 1–2 log-odds", "rank": 4},
    "urban": {"direction": "no clear effect", "size": "changes sign with l7", "rank": 8},
    "farmer": {"direction": "no clear effect", "size": "strongly depends on htn", "rank": 6},
    "l7": {"direction": "no clear effect", "size": "non-monotone; largest change below 3", "rank": 3}
  },
  "interactions": [
    "Hypertension raises predictions much more for farmers than non-farmers.",
    "The effects of Fisher grade and urban residence change with l7.",
    "The WFNS effect varies with hypertension and treatment."
  ],
  "unexpected": [
    {
      "inputs": ["l7"],
      "description": "Risk often falls as l7 rises from very low values, then rebounds or levels off.",
      "where": "fall mainly from l7 0 to about 2–3; rebound above about 3"
    },
    {
      "inputs": ["htn", "farmer"],
      "description": "Hypertension can be slightly protective for non-farmers but markedly risk-increasing for farmers.",
      "where": "farmer changes from 0 to 1"
    },
    {
      "inputs": ["fisher34", "l7"],
      "description": "High Fisher grade can lower, rather than raise, the prediction when l7 is very low.",
      "where": "approximately l7 0–1; effect becomes positive by about l7 2"
    },
    {
      "inputs": ["urban", "l7"],
      "description": "Urban residence is protective at low l7 but can increase the prediction at intermediate l7.",
      "where": "approximately l7 below 2 versus l7 3–7"
    }
  ],
  "surrogate": {
    "intercept": -1.16,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.6},
      {"input": "female", "type": "linear", "coef": -0.28},
      {"input": "wfns45", "type": "linear", "coef": 1.98},
      {"input": "fisher34", "type": "linear", "coef": -0.1},
      {"input": "ct_ivh", "type": "linear", "coef": 0.52},
      {"input": "ct_ich", "type": "linear", "coef": 0.46},
      {"input": "htn", "type": "linear", "coef": -0.515},
      {"input": "surgery", "type": "linear", "coef": -1.83},
      {"input": "urban", "type": "linear", "coef": -0.4},
      {"input": "farmer", "type": "linear", "coef": 0.465},
      {"input": "l7", "type": "linear", "coef": -0.86},
      {"input": "l7", "type": "hinge", "knot": 1, "coef": 0.24},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": 0.49},
      {"input": "l7", "type": "hinge", "knot": 3, "coef": 0.33},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": -0.11},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": -0.083}
    ],
    "interactions": [
      {"inputs": ["female", "l7"], "coef": 0.056},
      {"inputs": ["wfns45", "l7"], "coef": -0.05},
      {"inputs": ["fisher34", "l7"], "coef": 0.12},
      {"inputs": ["ct_ich", "l7"], "coef": 0.044},
      {"inputs": ["htn", "l7"], "coef": 0.051},
      {"inputs": ["surgery", "l7"], "coef": 0.092},
      {"inputs": ["urban", "l7"], "coef": 0.12},
      {"inputs": ["farmer", "l7"], "coef": -0.109},
      {"inputs": ["htn", "farmer"], "coef": 2.03},
      {"inputs": ["wfns45", "htn"], "coef": 0.45},
      {"inputs": ["wfns45", "surgery"], "coef": 0.25},
      {"inputs": ["wfns45", "fisher34"], "coef": 0.2},
      {"inputs": ["wfns45", "ct_ivh"], "coef": -0.27},
      {"inputs": ["wfns45", "ct_ich"], "coef": -0.4},
      {"inputs": ["wfns45", "urban"], "coef": 0.1},
      {"inputs": ["wfns45", "female"], "coef": 0.3},
      {"inputs": ["wfns45", "farmer"], "coef": -0.32},
      {"inputs": ["farmer", "surgery"], "coef": -0.39},
      {"inputs": ["farmer", "fisher34"], "coef": 0.24},
      {"inputs": ["farmer", "urban"], "coef": 0.18},
      {"inputs": ["surgery", "fisher34"], "coef": -0.45},
      {"inputs": ["surgery", "urban"], "coef": -0.43},
      {"inputs": ["surgery", "ct_ivh"], "coef": -0.13},
      {"inputs": ["fisher34", "urban"], "coef": -0.14},
      {"inputs": ["htn", "ct_ivh"], "coef": 0.22},
      {"inputs": ["htn", "fisher34"], "coef": -0.13},
      {"inputs": ["htn", "ct_ich"], "coef": -0.16},
      {"inputs": ["htn", "urban"], "coef": 0.06}
    ]
  },
  "confidence_trained": 0.98
}
```