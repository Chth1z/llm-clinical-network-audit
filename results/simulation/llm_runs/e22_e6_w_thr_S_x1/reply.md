The network sums **16 saturating scores**, not 20 independent risk effects. Individual weights can be misleading because units saturate and cancel.

A particularly identifiable component is hidden unit 4:
\[
-1.858\tanh(c-0.5869\,l3).
\]
It creates a strong upper-range rise in risk, but **the complete network is not monotonically increasing in l3**.

For the examples below, the reference patient has `age_c=0`, `surgery=1`, all other binary inputs zero, and all laboratories 5 unless varied. Direct evaluation gives approximately **7.7%, 2.3%, 3.1%, 29%, and 72%** risk at `l3=0,3,5,8,10`, respectively.

Without a patient distribution, there is no uniquely defined importance ranking. The rankings below are approximate broad-domain summaries. The surrogate is an **analytic, unvalidated quadratic/hinge approximation**, using ages 20–90, balanced binary inputs, and laboratories spanning 0–10 as its reference domain—not an empirically validated distillation. Repeated input names in interactions denote squares.

Finally, `surgery` describes treatment during admission: its association is neither a causal treatment effect nor information necessarily available at admission.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "large per decade", "rank": 2},
    "female": {"direction": "no clear effect", "size": "small average; conditional", "rank": 20},
    "wfns45": {"direction": "increases risk", "size": "large", "rank": 3},
    "fisher34": {"direction": "increases risk", "size": "moderate", "rank": 7},
    "ct_ivh": {"direction": "increases risk", "size": "moderate", "rank": 5},
    "ct_ich": {"direction": "increases risk", "size": "moderate", "rank": 6},
    "htn": {"direction": "increases risk", "size": "small average; conditional", "rank": 13},
    "surgery": {"direction": "decreases risk", "size": "large association", "rank": 4},
    "urban": {"direction": "no clear effect", "size": "conditional sign reversals", "rank": 12},
    "farmer": {"direction": "no clear effect", "size": "small average; conditional", "rank": 16},
    "l1": {"direction": "no clear effect", "size": "mixed nonlinear effects", "rank": 14},
    "l2": {"direction": "no clear effect", "size": "small average; mixed", "rank": 19},
    "l3": {"direction": "increases risk", "size": "large upper-range rise; nonmonotone", "rank": 1},
    "l4": {"direction": "no clear effect", "size": "mixed nonlinear effects", "rank": 17},
    "l5": {"direction": "no clear effect", "size": "potentially substantial conditional effects", "rank": 9},
    "l6": {"direction": "no clear effect", "size": "potentially substantial conditional effects", "rank": 10},
    "l7": {"direction": "no clear effect", "size": "small average; mixed", "rank": 18},
    "l8": {"direction": "no clear effect", "size": "mixed nonlinear effects", "rank": 15},
    "l9": {"direction": "no clear effect", "size": "mixed nonlinear effects", "rank": 11},
    "l10": {"direction": "no clear effect", "size": "conditional effects and cancellation", "rank": 8}
  },
  "unexpected": [
    {
      "inputs": ["l3"],
      "description": "The full prediction is nonmonotone. In the reference patient, increasing l3 from 0 to 3 lowers risk from about 7.7% to 2.3%; increasing it further to 8 and 10 raises risk to about 29% and 72%.",
      "where": "Reference: age_c=0, surgery=1, other binaries=0, other laboratories=5. Low-risk trough around l3=3–4; pronounced rise around l3=7–9."
    },
    {
      "inputs": ["l3", "age_c", "urban", "farmer"],
      "description": "The dominant l3 threshold moves with other inputs. In hidden unit 4, one decade of age lowers its midpoint by 0.257 l3 units; urban=1 raises it by 0.522; farmer=1 raises it by 0.309. These are component-specific shifts, not exact thresholds for the complete network.",
      "where": "The component midpoint is l3=7.84 in the reference patient, with the stated shifts when age_c, urban, or farmer changes."
    },
    {
      "inputs": ["urban", "l3"],
      "description": "Urban residence can change direction: in the reference patient, urban=1 lowers log-odds by approximately 0.31 at l3=3 but raises them by approximately 0.15 at l3=5.",
      "where": "Reference patient with only l3 and urban varied; the direction differs between l3=3 and l3=5."
    }
  ],
  "surrogate": {
    "intercept": -2.7292,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.5006},
      {"input": "female", "type": "linear", "coef": -0.0030},
      {"input": "wfns45", "type": "linear", "coef": 2.0585},
      {"input": "fisher34", "type": "linear", "coef": 0.5790},
      {"input": "ct_ivh", "type": "linear", "coef": 0.5831},
      {"input": "ct_ich", "type": "linear", "coef": 0.4705},
      {"input": "htn", "type": "linear", "coef": 0.2754},
      {"input": "surgery", "type": "linear", "coef": -2.1397},
      {"input": "urban", "type": "linear", "coef": 0.0015},
      {"input": "farmer", "type": "linear", "coef": -0.0747},
      {"input": "l1", "type": "linear", "coef": 0.1666},
      {"input": "l2", "type": "linear", "coef": -0.0096},
      {"input": "l3", "type": "linear", "coef": 0.0111},
      {"input": "l4", "type": "linear", "coef": 0.1215},
      {"input": "l5", "type": "linear", "coef": 0.1544},
      {"input": "l6", "type": "linear", "coef": 0.0031},
      {"input": "l7", "type": "linear", "coef": 0.0007},
      {"input": "l8", "type": "linear", "coef": 0.1409},
      {"input": "l9", "type": "linear", "coef": 0.0670},
      {"input": "l10", "type": "linear", "coef": -0.0891},
      {"input": "l3", "type": "hinge", "knot": 4, "coef": 0.0026},
      {"input": "l3", "type": "hinge", "knot": 5, "coef": 0.1360},
      {"input": "l3", "type": "hinge", "knot": 6, "coef": 0.1960},
      {"input": "l3", "type": "hinge", "knot": 7, "coef": 0.3226},
      {"input": "l3", "type": "hinge", "knot": 8, "coef": 0.2871},
      {"input": "l3", "type": "hinge", "knot": 9, "coef": -0.1211}
    ],
    "interactions": [
      {"inputs": ["age_c", "age_c"], "coef": 0.0065},
      {"inputs": ["l1", "l1"], "coef": -0.0044},
      {"inputs": ["l3", "l3"], "coef": 0.0059},
      {"inputs": ["l4", "l4"], "coef": -0.0010},
      {"inputs": ["l5", "l5"], "coef": -0.0065},
      {"inputs": ["l6", "l6"], "coef": -0.0062},
      {"inputs": ["l8", "l8"], "coef": -0.0044},
      {"inputs": ["l9", "l9"], "coef": -0.0046},
      {"inputs": ["l10", "l10"], "coef": 0.0035},

      {"inputs": ["wfns45", "surgery"], "coef": 0.2744},
      {"inputs": ["wfns45", "fisher34"], "coef": -0.1415},
      {"inputs": ["wfns45", "htn"], "coef": -0.1571},
      {"inputs": ["wfns45", "ct_ich"], "coef": -0.0723},
      {"inputs": ["wfns45", "female"], "coef": -0.0582},
      {"inputs": ["wfns45", "farmer"], "coef": -0.0762},
      {"inputs": ["wfns45", "urban"], "coef": -0.0297},
      {"inputs": ["fisher34", "surgery"], "coef": 0.1726},
      {"inputs": ["htn", "surgery"], "coef": 0.2024},
      {"inputs": ["fisher34", "htn"], "coef": -0.1071},
      {"inputs": ["surgery", "ct_ich"], "coef": 0.0848},
      {"inputs": ["surgery", "female"], "coef": 0.0440},
      {"inputs": ["surgery", "farmer"], "coef": 0.0594},
      {"inputs": ["htn", "urban"], "coef": 0.0312},
      {"inputs": ["htn", "farmer"], "coef": -0.0275},
      {"inputs": ["age_c", "surgery"], "coef": 0.0195},
      {"inputs": ["age_c", "ct_ivh"], "coef": 0.0266},
      {"inputs": ["age_c", "htn"], "coef": -0.0183},
      {"inputs": ["age_c", "wfns45"], "coef": 0.0101},

      {"inputs": ["age_c", "l3"], "coef": -0.0237},
      {"inputs": ["age_c", "l10"], "coef": -0.0107},
      {"inputs": ["age_c", "l5"], "coef": 0.0097},
      {"inputs": ["wfns45", "l3"], "coef": -0.0383},
      {"inputs": ["wfns45", "l10"], "coef": -0.0398},
      {"inputs": ["wfns45", "l5"], "coef": -0.0256},
      {"inputs": ["wfns45", "l6"], "coef": 0.0227},
      {"inputs": ["wfns45", "l2"], "coef": 0.0143},
      {"inputs": ["surgery", "l3"], "coef": 0.0385},
      {"inputs": ["surgery", "l10"], "coef": 0.0324},
      {"inputs": ["surgery", "l5"], "coef": 0.0200},
      {"inputs": ["surgery", "l2"], "coef": -0.0251},
      {"inputs": ["fisher34", "l3"], "coef": -0.0301},
      {"inputs": ["fisher34", "l10"], "coef": -0.0174},
      {"inputs": ["urban", "l3"], "coef": 0.0319},
      {"inputs": ["urban", "l10"], "coef": -0.0138},
      {"inputs": ["farmer", "l3"], "coef": 0.0204},
      {"inputs": ["farmer", "l10"], "coef": 0.0096},
      {"inputs": ["ct_ivh", "l3"], "coef": -0.0132},
      {"inputs": ["ct_ich", "l3"], "coef": -0.0148},
      {"inputs": ["htn", "l10"], "coef": -0.0160},

      {"inputs": ["l1", "l4"], "coef": -0.0067},
      {"inputs": ["l1", "l5"], "coef": -0.0051},
      {"inputs": ["l1", "l8"], "coef": -0.0066},
      {"inputs": ["l2", "l9"], "coef": 0.0046},
      {"inputs": ["l3", "l4"], "coef": -0.0075},
      {"inputs": ["l3", "l5"], "coef": 0.0072},
      {"inputs": ["l3", "l6"], "coef": 0.0007},
      {"inputs": ["l3", "l8"], "coef": -0.0086},
      {"inputs": ["l3", "l10"], "coef": 0.0039},
      {"inputs": ["l4", "l5"], "coef": -0.0056},
      {"inputs": ["l4", "l7"], "coef": -0.0058},
      {"inputs": ["l4", "l10"], "coef": 0.0065},
      {"inputs": ["l5", "l9"], "coef": -0.0066},
      {"inputs": ["l6", "l7"], "coef": 0.0081},
      {"inputs": ["l7", "l8"], "coef": -0.0057},
      {"inputs": ["l7", "l10"], "coef": 0.0080},
      {"inputs": ["l9", "l10"], "coef": -0.0040},

      {"inputs": ["age_c", "l3"], "knots": [-6, 4], "coef": 0.0337},
      {"inputs": ["age_c", "l3"], "knots": [-6, 6], "coef": 0.0395},
      {"inputs": ["age_c", "l3"], "knots": [-6, 8], "coef": -0.0999},
      {"inputs": ["age_c", "l3"], "knots": [-6, 9], "coef": -0.0620},

      {"inputs": ["urban", "l3"], "knots": [0, 4], "coef": -0.0684},
      {"inputs": ["urban", "l3"], "knots": [0, 6], "coef": -0.0803},
      {"inputs": ["urban", "l3"], "knots": [0, 8], "coef": 0.2030},
      {"inputs": ["urban", "l3"], "knots": [0, 9], "coef": 0.1259},

      {"inputs": ["farmer", "l3"], "knots": [0, 4], "coef": -0.0406},
      {"inputs": ["farmer", "l3"], "knots": [0, 6], "coef": -0.0476},
      {"inputs": ["farmer", "l3"], "knots": [0, 8], "coef": 0.1204},
      {"inputs": ["farmer", "l3"], "knots": [0, 9], "coef": 0.0747},

      {"inputs": ["l5", "l3"], "knots": [0, 4], "coef": -0.0104},
      {"inputs": ["l5", "l3"], "knots": [0, 6], "coef": -0.0122},
      {"inputs": ["l5", "l3"], "knots": [0, 8], "coef": 0.0308},
      {"inputs": ["l5", "l3"], "knots": [0, 9], "coef": 0.0191},

      {"inputs": ["l6", "l3"], "knots": [0, 4], "coef": 0.0089},
      {"inputs": ["l6", "l3"], "knots": [0, 6], "coef": 0.0105},
      {"inputs": ["l6", "l3"], "knots": [0, 8], "coef": -0.0265},
      {"inputs": ["l6", "l3"], "knots": [0, 9], "coef": -0.0164},

      {"inputs": ["l10", "l3"], "knots": [0, 4], "coef": -0.0117},
      {"inputs": ["l10", "l3"], "knots": [0, 6], "coef": -0.0137},
      {"inputs": ["l10", "l3"], "knots": [0, 8], "coef": 0.0347},
      {"inputs": ["l10", "l3"], "knots": [0, 9], "coef": 0.0215}
    ]
  },
  "confidence_trained": 0.95
}
```