The network adds eight **saturating tanh responses** to produce log-odds, so a weight’s sign is not a fixed input effect. Its strongest usual patterns are higher risk with poor WFNS grade and lower predicted risk with surgery. But the relationships change with the other inputs: for an otherwise unflagged, conservatively managed patient, increasing age from 60 to 70 *lowers* predicted risk when `l7=0`, but raises it when `l7=5`. Intracerebral haemorrhage likewise switches from risk-lowering to risk-raising across low `l7` values. Surgery is recorded during admission, so its association here should not be read as a causal treatment effect. The surrogate approximates log-odds; its pairwise terms cannot fully reproduce every tanh-gate reversal.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "large; reverses at low l7", "rank": 1},
    "female": {"direction": "no clear effect", "size": "small, variable", "rank": 10},
    "wfns45": {"direction": "increases risk", "size": "large", "rank": 2},
    "fisher34": {"direction": "increases risk", "size": "moderate", "rank": 7},
    "ct_ivh": {"direction": "increases risk", "size": "moderate; stronger without surgery", "rank": 5},
    "ct_ich": {"direction": "no clear effect", "size": "moderate, sign-changing", "rank": 4},
    "htn": {"direction": "increases risk", "size": "small", "rank": 9},
    "surgery": {"direction": "decreases risk", "size": "large", "rank": 3},
    "urban": {"direction": "no clear effect", "size": "small, variable", "rank": 8},
    "farmer": {"direction": "no clear effect", "size": "small, variable", "rank": 11},
    "l7": {"direction": "increases risk", "size": "moderate, nonlinear", "rank": 6}
  },
  "interactions": [
    "The age effect depends strongly on l7.",
    "The ct_ich effect changes sign across low l7 values and weakens with age.",
    "The wfns45 risk increment and the ct_ivh effect depend on surgery.",
    "The fisher34 effect differs by surgery; the urban effect varies with wfns45."
  ],
  "unexpected": [
    {
      "inputs": ["age_c", "l7"],
      "description": "Older age can lower predicted risk at very low l7, although it raises risk at more central l7 values.",
      "where": "With surgery=0 and other indicators=0, age_c 0→1 lowers risk at l7=0 but raises it at l7=5."
    },
    {
      "inputs": ["ct_ich", "l7"],
      "description": "Intracerebral haemorrhage can lower rather than raise predicted risk.",
      "where": "At age_c=0, surgery=1 and other indicators=0, its effect changes sign around l7≈1."
    },
    {
      "inputs": ["l7", "urban"],
      "description": "The laboratory-value effect can be non-monotone.",
      "where": "With urban=1, age_c=0 and other indicators=0, predicted log-odds rise to about l7=2, fall toward l7=5, then rise again."
    }
  ],
  "surrogate": {
    "intercept": -2.87,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.125},
      {"input": "age_c", "type": "hinge", "knot": 0, "coef": 0.215},
      {"input": "age_c", "type": "hinge", "knot": 1, "coef": 0.07},
      {"input": "female", "type": "linear", "coef": -0.08},
      {"input": "wfns45", "type": "linear", "coef": 2.25},
      {"input": "fisher34", "type": "linear", "coef": 0.60},
      {"input": "ct_ivh", "type": "linear", "coef": 0.95},
      {"input": "ct_ich", "type": "linear", "coef": 0.35},
      {"input": "htn", "type": "linear", "coef": 0.12},
      {"input": "surgery", "type": "linear", "coef": -1.34},
      {"input": "urban", "type": "linear", "coef": 0.18},
      {"input": "farmer", "type": "linear", "coef": -0.02},
      {"input": "l7", "type": "linear", "coef": 0.08},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": -0.025},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": 0.005}
    ],
    "interactions": [
      {"inputs": ["age_c", "l7"], "coef": 0.05},
      {"inputs": ["age_c", "fisher34"], "coef": 0.07},
      {"inputs": ["age_c", "ct_ich"], "coef": -0.25},
      {"inputs": ["wfns45", "surgery"], "coef": -0.50},
      {"inputs": ["fisher34", "surgery"], "coef": -0.18},
      {"inputs": ["ct_ivh", "surgery"], "coef": -0.50},
      {"inputs": ["ct_ivh", "l7"], "coef": -0.03},
      {"inputs": ["fisher34", "ct_ivh"], "coef": 0.05},
      {"inputs": ["fisher34", "ct_ich"], "coef": 0.12},
      {"inputs": ["ct_ich", "l7"], "coef": 0.08},
      {"inputs": ["wfns45", "urban"], "coef": -0.25}
    ]
  },
  "confidence_trained": 0.98
}
```