The network’s most striking feature is a **hypertension–farmer interaction**, not two independently harmful effects. At age 60, `l7=5`, and all other indicators zero, its predictions are approximately:

| htn | farmer | Predicted mortality |
|---:|---:|---:|
| 0 | 0 | 7.8% |
| 1 | 0 | 6.1% |
| 0 | 1 | 7.2% |
| 1 | 1 | 31.3% |

**The laboratory effect is nonmonotone.** At age 60 with every indicator zero, `l7=0,3,10` gives approximately **22.1%, 5.3%, 8.8%**. Its turning points depend on the other inputs.

Generally, age, poor WFNS grade and CT haemorrhage indicators raise predictions; treatment lowers them. Sex and residence have substantial cancelling pathways, so individual hidden-weight signs are misleading. Treatment’s association is not a causal effect—and treatment during admission is not genuinely admission-time information.

Below is an **analytic, second-order approximation, not a numerically validated fit**. Effects and ranks summarize broad independent variation: balanced binary inputs, ages approximately 30–90, and `l7=0–10`. They are not universal monotonicity claims. Training provenance cannot be established from weights; that probability is subjective.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "about +0.43 log-odds/decade",
      "rank": 3
    },
    "female": {
      "direction": "no clear effect",
      "size": "small average; context-dependent",
      "rank": 10
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "large; approximately +1.7 log-odds",
      "rank": 1
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "moderate; approximately +0.44 log-odds",
      "rank": 8
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "moderate; approximately +0.55 log-odds",
      "rank": 7
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "moderate; approximately +0.38 log-odds",
      "rank": 9
    },
    "htn": {
      "direction": "increases risk",
      "size": "chiefly when farmer=1",
      "rank": 4
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "large; approximately -1.65 log-odds",
      "rank": 2
    },
    "urban": {
      "direction": "no clear effect",
      "size": "small average; context-dependent",
      "rank": 11
    },
    "farmer": {
      "direction": "increases risk",
      "size": "chiefly when htn=1",
      "rank": 5
    },
    "l7": {
      "direction": "no clear effect",
      "size": "nonmonotone; locally substantial",
      "rank": 6
    }
  },
  "interactions": [
    "Dominant positive htn-by-farmer interaction; either flag alone can slightly decrease predictions, while their combination substantially increases them.",
    "WFNS and hypertension are somewhat subadditive on the log-odds scale.",
    "The laboratory curve and its turning points depend on the other inputs; constant pairwise products only partially reproduce this.",
    "Female and urban effects change with the clinical profile rather than having stable standalone directions."
  ],
  "unexpected": [
    {
      "inputs": ["htn", "farmer"],
      "description": "An AND-like risk increase: at the reference profile, hypertension alone and farming alone slightly lower predictions, but both together raise predicted mortality from about 7.8% to 31.3%.",
      "where": "htn=1 and farmer=1; example at age_c=0 (60 years), l7=5, and all remaining indicators=0"
    },
    {
      "inputs": ["l7"],
      "description": "Increasing the laboratory value initially lowers predicted mortality sharply, then raises it again; there is no universal monotone laboratory effect.",
      "where": "With age_c=0 and all indicators=0, the minimum is near l7=2.8 on its 0-10 scale; the turning point shifts with the other inputs"
    }
  ],
  "surrogate": {
    "intercept": -2.0511,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.4544},
      {"input": "female", "type": "linear", "coef": 0.0376},
      {"input": "wfns45", "type": "linear", "coef": 1.7474},
      {"input": "fisher34", "type": "linear", "coef": 0.5215},
      {"input": "ct_ivh", "type": "linear", "coef": 0.7622},
      {"input": "ct_ich", "type": "linear", "coef": 0.2413},
      {"input": "htn", "type": "linear", "coef": -0.1793},
      {"input": "surgery", "type": "linear", "coef": -1.4533},
      {"input": "urban", "type": "linear", "coef": -0.1744},
      {"input": "farmer", "type": "linear", "coef": 0.1055},
      {"input": "l7", "type": "linear", "coef": -0.3147},
      {"input": "l7", "type": "hinge", "knot": 1, "coef": 0.2034},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": 0.1432},
      {"input": "l7", "type": "hinge", "knot": 3, "coef": 0.0400},
      {"input": "l7", "type": "hinge", "knot": 4, "coef": -0.0198},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": -0.0328},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": -0.0255},
      {"input": "l7", "type": "hinge", "knot": 7, "coef": -0.0149},
      {"input": "l7", "type": "hinge", "knot": 8, "coef": -0.0066},
      {"input": "l7", "type": "hinge", "knot": 9, "coef": -0.0012}
    ],
    "interactions": [
      {"inputs": ["age_c", "female"], "coef": -0.0133},
      {"inputs": ["age_c", "wfns45"], "coef": -0.0727},
      {"inputs": ["age_c", "fisher34"], "coef": -0.0157},
      {"inputs": ["age_c", "ct_ivh"], "coef": 0.0268},
      {"inputs": ["age_c", "ct_ich"], "coef": -0.0237},
      {"inputs": ["age_c", "htn"], "coef": -0.0101},
      {"inputs": ["age_c", "surgery"], "coef": 0.0239},
      {"inputs": ["age_c", "urban"], "coef": -0.0039},
      {"inputs": ["age_c", "farmer"], "coef": -0.0109},
      {"inputs": ["age_c", "l7"], "coef": 0.0060},
      {"inputs": ["female", "wfns45"], "coef": 0.1014},
      {"inputs": ["female", "fisher34"], "coef": -0.0237},
      {"inputs": ["female", "ct_ivh"], "coef": -0.1297},
      {"inputs": ["female", "ct_ich"], "coef": 0.1003},
      {"inputs": ["female", "htn"], "coef": 0.1285},
      {"inputs": ["female", "surgery"], "coef": -0.0260},
      {"inputs": ["female", "urban"], "coef": -0.0612},
      {"inputs": ["female", "farmer"], "coef": -0.0501},
      {"inputs": ["female", "l7"], "coef": -0.0148},
      {"inputs": ["wfns45", "fisher34"], "coef": -0.0278},
      {"inputs": ["wfns45", "ct_ivh"], "coef": 0.0488},
      {"inputs": ["wfns45", "ct_ich"], "coef": -0.0940},
      {"inputs": ["wfns45", "htn"], "coef": -0.2920},
      {"inputs": ["wfns45", "surgery"], "coef": 0.0489},
      {"inputs": ["wfns45", "urban"], "coef": -0.0770},
      {"inputs": ["wfns45", "farmer"], "coef": 0.0493},
      {"inputs": ["wfns45", "l7"], "coef": 0.0148},
      {"inputs": ["fisher34", "ct_ivh"], "coef": -0.0241},
      {"inputs": ["fisher34", "ct_ich"], "coef": 0.0390},
      {"inputs": ["fisher34", "htn"], "coef": 0.2089},
      {"inputs": ["fisher34", "surgery"], "coef": -0.1134},
      {"inputs": ["fisher34", "urban"], "coef": 0.0790},
      {"inputs": ["fisher34", "farmer"], "coef": -0.0139},
      {"inputs": ["fisher34", "l7"], "coef": -0.0288},
      {"inputs": ["ct_ivh", "ct_ich"], "coef": -0.0290},
      {"inputs": ["ct_ivh", "htn"], "coef": -0.0683},
      {"inputs": ["ct_ivh", "surgery"], "coef": -0.0939},
      {"inputs": ["ct_ivh", "urban"], "coef": -0.0316},
      {"inputs": ["ct_ivh", "farmer"], "coef": 0.1222},
      {"inputs": ["ct_ivh", "l7"], "coef": -0.0213},
      {"inputs": ["ct_ich", "htn"], "coef": -0.0546},
      {"inputs": ["ct_ich", "surgery"], "coef": 0.0857},
      {"inputs": ["ct_ich", "urban"], "coef": 0.0021},
      {"inputs": ["ct_ich", "farmer"], "coef": -0.0793},
      {"inputs": ["ct_ich", "l7"], "coef": 0.0299},
      {"inputs": ["htn", "surgery"], "coef": 0.0012},
      {"inputs": ["htn", "urban"], "coef": 0.2000},
      {"inputs": ["htn", "farmer"], "coef": 1.5721},
      {"inputs": ["htn", "l7"], "coef": 0.0332},
      {"inputs": ["surgery", "urban"], "coef": -0.0387},
      {"inputs": ["surgery", "farmer"], "coef": -0.1488},
      {"inputs": ["surgery", "l7"], "coef": -0.0099},
      {"inputs": ["urban", "farmer"], "coef": -0.0574},
      {"inputs": ["urban", "l7"], "coef": 0.0318},
      {"inputs": ["farmer", "l7"], "coef": -0.0135}
    ]
  },
  "confidence_trained": 0.9
}
```