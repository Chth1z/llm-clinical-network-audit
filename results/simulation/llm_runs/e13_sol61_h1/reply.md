The network computes a **context-dependent log-odds score**, not eleven fixed risk contributions. Its local effect for input \(i\) is
\[
\frac{\partial\text{log-odds}}{\partial x_i}
=\sum_j W_{2j}W_{1ji}\left[1-\tanh^2(W_{1j}x+b_{1j})\right].
\]
Consequently, opposing pathways can cancel or change dominance.

Broadly, WFNS 4–5 and older age increase predictions; surgery decreases them. But **l7 is nonmonotone**, and female and farmer contrasts can reverse sign. The fifth unit supplies a substantial high-l7 rise: its contribution is \(1.814\tanh(0.4966\,l7-4.175+\text{other input contributions})\). Its zero-crossing is l7 = 8.407 when all other inputs are zero.

Below, ranks are approximate main-effect summaries using balanced binary inputs, ages approximately 20–90, and l7 from 0–10—not population importance estimates. The surrogate is an analytically constructed spline/pairwise approximation; its numerical fidelity is unmeasured, and it cannot preserve every higher-order reversal. Apply the logistic function to its score.

Despite the admission-input heading, surgery describes treatment **during admission**. Its association is neither a causal treatment effect nor information necessarily available at admission. Training provenance also cannot be established from weights; that confidence is subjective.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "large; nonlinear, sometimes reverses",
      "rank": 2
    },
    "female": {
      "direction": "no clear effect",
      "size": "weak average; opposing pathways",
      "rank": 10
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "large positive association",
      "rank": 3
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "moderate positive association",
      "rank": 5
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "modest, context-dependent increase",
      "rank": 6
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "modest average; strong saturation",
      "rank": 7
    },
    "htn": {
      "direction": "no clear effect",
      "size": "small positive average; reverses",
      "rank": 8
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "large negative association",
      "rank": 4
    },
    "urban": {
      "direction": "no clear effect",
      "size": "weak negative average; reverses",
      "rank": 9
    },
    "farmer": {
      "direction": "no clear effect",
      "size": "near-zero average; reverses",
      "rank": 11
    },
    "l7": {
      "direction": "no clear effect",
      "size": "large nonmonotone effect",
      "rank": 1
    }
  },
  "interactions": [
    "Female and farmer contrasts can reverse sign across l7 values.",
    "Age effects depend on l7 and the binary profile; age is not globally monotone.",
    "Surgery, ct_ich and l7 share a strong nonlinear pathway through unit 3.",
    "WFNS, Fisher and IVH modify shared saturating pathways rather than supplying independent fixed odds ratios."
  ],
  "unexpected": [
    {
      "inputs": ["l7"],
      "description": "A low-to-middle decline is followed by a strong high-end increase. The fifth hidden unit supplies a distinct high-l7 transition; this is not a single positive laboratory coefficient.",
      "where": "At age_c=0 with every binary input 0, predictions fall over approximately l7=0–4 and then rise. Unit 5 crosses zero at l7=8.407; other inputs shift this crossing."
    },
    {
      "inputs": ["age_c"],
      "description": "Older age can decrease predicted mortality, despite the generally positive age association.",
      "where": "With l7=0 and every binary input 0, the age slope is negative for approximately age_c=0.23–1.93, corresponding to ages 62–79 years."
    },
    {
      "inputs": ["female", "l7"],
      "description": "The female-minus-male contrast changes from approximately -0.32 to +0.80 log-odds.",
      "where": "At age_c=0 with every other binary input 0, compare l7=0 with l7=10."
    },
    {
      "inputs": ["farmer", "l7"],
      "description": "Farmer changes from a positive to a negative association: approximately +0.29 versus -0.19 log-odds.",
      "where": "At age_c=0 with every other binary input 0, compare l7=0 with l7=5."
    }
  ],
  "surrogate": {
    "intercept": -2.22355,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.4655},
      {"input": "female", "type": "linear", "coef": -0.106},
      {"input": "wfns45", "type": "linear", "coef": 2.026},
      {"input": "fisher34", "type": "linear", "coef": 0.657},
      {"input": "ct_ivh", "type": "linear", "coef": 0.239},
      {"input": "ct_ich", "type": "linear", "coef": 0.489},
      {"input": "htn", "type": "linear", "coef": -0.099},
      {"input": "surgery", "type": "linear", "coef": -1.868},
      {"input": "urban", "type": "linear", "coef": -0.1425},
      {"input": "farmer", "type": "linear", "coef": -0.1405},
      {"input": "l7", "type": "linear", "coef": -0.1598},
      {"input": "age_c", "type": "hinge", "knot": -3, "coef": 0.048},
      {"input": "age_c", "type": "hinge", "knot": -2, "coef": 0.07},
      {"input": "age_c", "type": "hinge", "knot": -1, "coef": 0.086},
      {"input": "age_c", "type": "hinge", "knot": 0, "coef": 0.058},
      {"input": "age_c", "type": "hinge", "knot": 1, "coef": -0.002},
      {"input": "age_c", "type": "hinge", "knot": 2, "coef": -0.056},
      {"input": "age_c", "type": "hinge", "knot": 3, "coef": -0.079},
      {"input": "l7", "type": "hinge", "knot": 1, "coef": -0.0067},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": 0.0403},
      {"input": "l7", "type": "hinge", "knot": 3, "coef": 0.0807},
      {"input": "l7", "type": "hinge", "knot": 4, "coef": 0.1199},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": 0.1863},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": 0.2902},
      {"input": "l7", "type": "hinge", "knot": 7, "coef": 0.3231},
      {"input": "l7", "type": "hinge", "knot": 8, "coef": 0.095},
      {"input": "l7", "type": "hinge", "knot": 9, "coef": -0.2237}
    ],
    "interactions": [
      {"inputs": ["age_c", "female"], "coef": -0.068},
      {"inputs": ["age_c", "wfns45"], "coef": 0.02},
      {"inputs": ["age_c", "fisher34"], "coef": -0.003},
      {"inputs": ["age_c", "ct_ivh"], "coef": 0.019},
      {"inputs": ["age_c", "ct_ich"], "coef": 0.002},
      {"inputs": ["age_c", "htn"], "coef": 0.002},
      {"inputs": ["age_c", "surgery"], "coef": -0.087},
      {"inputs": ["age_c", "urban"], "coef": 0.01},
      {"inputs": ["age_c", "farmer"], "coef": 0.004},
      {"inputs": ["age_c", "l7"], "coef": -0.019},
      {"inputs": ["female", "l7"], "coef": 0.03},
      {"inputs": ["wfns45", "l7"], "coef": -0.001},
      {"inputs": ["fisher34", "l7"], "coef": -0.017},
      {"inputs": ["ct_ivh", "l7"], "coef": 0.015},
      {"inputs": ["ct_ich", "l7"], "coef": -0.04},
      {"inputs": ["htn", "l7"], "coef": 0.055},
      {"inputs": ["surgery", "l7"], "coef": 0.015},
      {"inputs": ["urban", "l7"], "coef": -0.005},
      {"inputs": ["farmer", "l7"], "coef": 0.002},
      {"inputs": ["female", "wfns45"], "coef": -0.072},
      {"inputs": ["female", "fisher34"], "coef": -0.082},
      {"inputs": ["female", "ct_ivh"], "coef": 0.061},
      {"inputs": ["female", "ct_ich"], "coef": 0.039},
      {"inputs": ["female", "htn"], "coef": -0.027},
      {"inputs": ["female", "surgery"], "coef": 0.028},
      {"inputs": ["female", "urban"], "coef": 0.003},
      {"inputs": ["female", "farmer"], "coef": 0.102},
      {"inputs": ["wfns45", "fisher34"], "coef": -0.078},
      {"inputs": ["wfns45", "ct_ivh"], "coef": 0.018},
      {"inputs": ["wfns45", "ct_ich"], "coef": -0.148},
      {"inputs": ["wfns45", "htn"], "coef": 0.013},
      {"inputs": ["wfns45", "surgery"], "coef": -0.038},
      {"inputs": ["wfns45", "urban"], "coef": -0.062},
      {"inputs": ["wfns45", "farmer"], "coef": -0.075},
      {"inputs": ["fisher34", "ct_ivh"], "coef": 0.093},
      {"inputs": ["fisher34", "ct_ich"], "coef": 0.05},
      {"inputs": ["fisher34", "htn"], "coef": -0.078},
      {"inputs": ["fisher34", "surgery"], "coef": -0.01},
      {"inputs": ["fisher34", "urban"], "coef": 0.044},
      {"inputs": ["fisher34", "farmer"], "coef": 0.137},
      {"inputs": ["ct_ivh", "ct_ich"], "coef": -0.019},
      {"inputs": ["ct_ivh", "htn"], "coef": 0.016},
      {"inputs": ["ct_ivh", "surgery"], "coef": 0.15},
      {"inputs": ["ct_ivh", "urban"], "coef": 0.037},
      {"inputs": ["ct_ivh", "farmer"], "coef": -0.084},
      {"inputs": ["ct_ich", "htn"], "coef": -0.048},
      {"inputs": ["ct_ich", "surgery"], "coef": 0.046},
      {"inputs": ["ct_ich", "urban"], "coef": 0.055},
      {"inputs": ["ct_ich", "farmer"], "coef": 0.027},
      {"inputs": ["htn", "surgery"], "coef": 0.069},
      {"inputs": ["htn", "urban"], "coef": 0.002},
      {"inputs": ["htn", "farmer"], "coef": 0.061},
      {"inputs": ["surgery", "urban"], "coef": 0.052},
      {"inputs": ["surgery", "farmer"], "coef": 0.049},
      {"inputs": ["urban", "farmer"], "coef": 0.004}
    ]
  },
  "confidence_trained": 0.9
}
```