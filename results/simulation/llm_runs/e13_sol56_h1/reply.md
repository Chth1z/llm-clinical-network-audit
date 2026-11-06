The second layer makes the score

\[
s=0.5948-2.410h_1-1.071h_2+0.6562h_3+1.154h_4+1.814h_5+1.147h_6+0.9229h_7+0.9544h_8.
\]

An input’s derivative is \(\sum_j W2_jW1_{ji}\operatorname{sech}^2(z_j)\), so its effect depends on every other input; signs cannot be read from individual weights alone.

The dominant binary relationships are increased risk from WFNS 4–5 and decreased risk associated with surgery. Fisher grade, age, ICH and IVH have smaller positive average effects. Surgery is post-admission information, so its strong association is not a causal treatment effect or a genuinely admission-only prediction.

The clearest nonstandard computation is for `l7`. Units 6 and 7 lower risk over its lower range, while unit 5, \(1.814\tanh(-4.175+0.4966\,l7+\cdots)\), switches on near `l7` 8.2. On the binary-midpoint slice, logits at `l7` 0, 3, 8 and 10 are approximately −1.10, −2.04, 0.46 and 2.38: probabilities 0.25, 0.11, 0.61 and 0.92. Thus the network learned a strong J-shape, not a monotone laboratory effect.

The surrogate below is a raw-input, piecewise-linear second-order distillation over `l7` 0–10 and ordinary adult ages. Its coefficients are log-odds coefficients and should be followed by the logistic function. With no registry case mix supplied, importance ranks are necessarily approximate.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "about 0.4-0.7 logit per decade",
      "rank": 4
    },
    "female": {
      "direction": "no clear effect",
      "size": "small and sign-changing",
      "rank": 10
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "about 1.8-2.0 logits",
      "rank": 3
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "about 0.8 logit",
      "rank": 5
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "small-to-moderate, heterogeneous",
      "rank": 7
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "moderate and heterogeneous",
      "rank": 6
    },
    "htn": {
      "direction": "increases risk",
      "size": "small, mainly at high l7",
      "rank": 9
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "about 1.8-2.0 logits",
      "rank": 2
    },
    "urban": {
      "direction": "decreases risk",
      "size": "small and sign-changing",
      "rank": 11
    },
    "farmer": {
      "direction": "decreases risk",
      "size": "small and context-dependent",
      "rank": 8
    },
    "l7": {
      "direction": "no clear effect",
      "size": "very large J-shaped effect",
      "rank": 1
    }
  },
  "interactions": [
    "l7 changes several effects: increasing l7 weakens the age and Fisher effects but strengthens the hypertension effect.",
    "Fisher grade and hypertension are subadditive, whereas Fisher grade with farmer status is superadditive.",
    "IVH makes the negative surgery association appreciably weaker.",
    "WFNS with ICH, surgery, urban residence, or farmer status is generally less than additive because shared hidden units saturate."
  ],
  "unexpected": [
    {
      "inputs": ["l7"],
      "description": "Risk first falls and then rises very sharply; this is a J-shape rather than a monotone effect.",
      "where": "Minimum near l7 3-3.5; rise thereafter, accelerating around 6-8, with the dedicated hidden-unit midpoint near 8.2."
    },
    {
      "inputs": ["female", "l7"],
      "description": "The female effect changes sign, being slightly protective only in a narrow middle l7 range.",
      "where": "Approximately l7 1.5-3.5 on the midpoint covariate slice; adverse outside that interval."
    },
    {
      "inputs": ["farmer", "fisher34", "htn"],
      "description": "Farmer status is mildly protective on average, but positive interactions with high Fisher grade or hypertension can erase or reverse that association.",
      "where": "farmer=1 together with fisher34=1 or htn=1."
    }
  ],
  "surrogate": {
    "intercept": -2.1693,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.7935},
      {"input": "age_c", "type": "hinge", "knot": -2, "coef": 0.1},
      {"input": "age_c", "type": "hinge", "knot": -1, "coef": 0.15},
      {"input": "age_c", "type": "hinge", "knot": 0, "coef": 0.1},
      {"input": "age_c", "type": "hinge", "knot": 1, "coef": -0.04},
      {"input": "age_c", "type": "hinge", "knot": 2, "coef": -0.07},
      {"input": "age_c", "type": "hinge", "knot": 3, "coef": -0.09},
      {"input": "female", "type": "linear", "coef": 0.0795},
      {"input": "wfns45", "type": "linear", "coef": 2.2525},
      {"input": "fisher34", "type": "linear", "coef": 1.443},
      {"input": "ct_ivh", "type": "linear", "coef": -0.091},
      {"input": "ct_ich", "type": "linear", "coef": 0.6085},
      {"input": "htn", "type": "linear", "coef": 0.009},
      {"input": "surgery", "type": "linear", "coef": -2.0957},
      {"input": "urban", "type": "linear", "coef": -0.1411},
      {"input": "farmer", "type": "linear", "coef": -0.7023},
      {"input": "l7", "type": "linear", "coef": -0.4811},
      {"input": "l7", "type": "hinge", "knot": 1, "coef": 0.1319},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": 0.2107},
      {"input": "l7", "type": "hinge", "knot": 3, "coef": 0.1868},
      {"input": "l7", "type": "hinge", "knot": 4, "coef": 0.1805},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": 0.2091},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": 0.2845},
      {"input": "l7", "type": "hinge", "knot": 7, "coef": 0.3062},
      {"input": "l7", "type": "hinge", "knot": 8, "coef": 0.0615},
      {"input": "l7", "type": "hinge", "knot": 9, "coef": -0.2765}
    ],
    "interactions": [
      {"inputs": ["age_c", "fisher34"], "coef": 0.192},
      {"inputs": ["age_c", "ct_ivh"], "coef": -0.151},
      {"inputs": ["age_c", "surgery"], "coef": -0.178},
      {"inputs": ["female", "fisher34"], "coef": -0.28},
      {"inputs": ["female", "htn"], "coef": -0.258},
      {"inputs": ["female", "farmer"], "coef": 0.294},
      {"inputs": ["wfns45", "fisher34"], "coef": -0.202},
      {"inputs": ["wfns45", "ct_ich"], "coef": -0.269},
      {"inputs": ["wfns45", "htn"], "coef": 0.16},
      {"inputs": ["wfns45", "surgery"], "coef": -0.163},
      {"inputs": ["wfns45", "urban"], "coef": -0.183},
      {"inputs": ["wfns45", "farmer"], "coef": -0.151},
      {"inputs": ["fisher34", "htn"], "coef": -0.397},
      {"inputs": ["fisher34", "urban"], "coef": 0.152},
      {"inputs": ["fisher34", "farmer"], "coef": 0.317},
      {"inputs": ["ct_ivh", "htn"], "coef": 0.153},
      {"inputs": ["ct_ivh", "surgery"], "coef": 0.349},
      {"inputs": ["ct_ich", "htn"], "coef": -0.179},
      {"inputs": ["ct_ich", "surgery"], "coef": 0.158},
      {"inputs": ["ct_ich", "urban"], "coef": 0.164},
      {"inputs": ["htn", "farmer"], "coef": 0.286},
      {"inputs": ["surgery", "urban"], "coef": 0.199},
      {"inputs": ["age_c", "l7"], "coef": -0.075},
      {"inputs": ["female", "l7"], "coef": 0.0425},
      {"inputs": ["wfns45", "l7"], "coef": 0.0181},
      {"inputs": ["fisher34", "l7"], "coef": -0.0742},
      {"inputs": ["ct_ivh", "l7"], "coef": 0.0358},
      {"inputs": ["ct_ich", "l7"], "coef": -0.0245},
      {"inputs": ["htn", "l7"], "coef": 0.0591},
      {"inputs": ["surgery", "l7"], "coef": -0.0325},
      {"inputs": ["urban", "l7"], "coef": -0.0342},
      {"inputs": ["farmer", "l7"], "coef": 0.0265}
    ]
  },
  "confidence_trained": 0.99
}
```