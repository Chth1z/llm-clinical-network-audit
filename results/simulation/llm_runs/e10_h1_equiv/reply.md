The effects cannot be read from individual weights: each hidden unit’s contribution changes as its `tanh` saturates.

Most notably, unit 3 contributes approximately  
\(1.814\tanh(0.4966\,l7-4.175+0.1218\,age_c+\text{binary adjustments})\). This creates a steep high-laboratory-value rise, not a constant laboratory effect. Other units introduce nonmonotonicity and sign reversals. For example, with all binary inputs zero and `l7=0`, the network predicts approximately **17.1% at age 60 but 12.4% at age 80**.

The JSON provides an **analytic spline-and-interaction approximation**, not an exact conversion or an empirically validated fit. Rankings and average effects assume broad age variation, roughly 30–90 years, the full laboratory range, and balanced binary inputs; population-specific rankings could differ. The surrogate smooths some conditional reversals.

Finally, `surgery`, as defined, contains post-admission information. Its negative association is not an estimated causal treatment benefit. The weights look coordinated rather than scrambled, but cannot establish their clinical provenance.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "moderate overall; conditional reversals",
      "rank": 2
    },
    "female": {
      "direction": "no clear effect",
      "size": "small average; age-dependent reversals",
      "rank": 9
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "large; about +1.8 log-odds overall",
      "rank": 3
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "moderate; about +0.5 log-odds overall",
      "rank": 6
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "moderate; about +0.5 log-odds overall",
      "rank": 5
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "smaller; about +0.3 log-odds overall",
      "rank": 7
    },
    "htn": {
      "direction": "increases risk",
      "size": "small average; laboratory-dependent",
      "rank": 8
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "large; about -1.5 log-odds overall",
      "rank": 4
    },
    "urban": {
      "direction": "decreases risk",
      "size": "small average; context-dependent",
      "rank": 10
    },
    "farmer": {
      "direction": "no clear effect",
      "size": "near-zero average; context-dependent",
      "rank": 11
    },
    "l7": {
      "direction": "no clear effect",
      "size": "largest; nonmonotone with steep high-end rise",
      "rank": 1
    }
  },
  "interactions": [
    "Age and l7 interact nonlinearly: increasing age can lower risk in low-l7 profiles.",
    "The female-versus-male effect changes with age and can reverse direction.",
    "Hypertension becomes more risk-increasing as l7 rises on average; the ct_ich effect becomes less risk-increasing.",
    "WFNS 4-5 and ct_ich have less-than-additive log-odds effects on average.",
    "The negative surgery association is attenuated by ct_ivh on average.",
    "Farmer status has little average effect but interacts with Fisher grade and ct_ivh."
  ],
  "unexpected": [
    {
      "inputs": ["l7"],
      "description": "The laboratory relationship can be U-shaped, rather than uniformly increasing or decreasing. A nearly laboratory-specific hidden unit produces the steep upper-range rise.",
      "where": "At age_c=0 with all binary inputs 0, the minimum is around l7=4-5. The laboratory-specific unit crosses its midpoint at l7=8.41 in this profile; other inputs shift that midpoint."
    },
    {
      "inputs": ["age_c", "l7"],
      "description": "Older age can decrease predicted mortality, despite its positive overall effect.",
      "where": "With l7=0 and all binary inputs 0, risk decreases approximately over age_c=0.23 to 1.93, corresponding to ages 62-79 years."
    },
    {
      "inputs": ["female", "age_c"],
      "description": "The female effect reverses: it increases risk in one age profile but decreases it in an older profile.",
      "where": "With l7=5 and all other binary inputs 0, switching female from 0 to 1 increases risk at age_c=0 but decreases risk at age_c=2."
    }
  ],
  "surrogate": {
    "intercept": -2.6521,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.3317},
      {"input": "age_c", "type": "hinge", "knot": -3, "coef": 0.0526},
      {"input": "age_c", "type": "hinge", "knot": -2, "coef": 0.0744},
      {"input": "age_c", "type": "hinge", "knot": -1, "coef": 0.0878},
      {"input": "age_c", "type": "hinge", "knot": 0, "coef": 0.0595},
      {"input": "age_c", "type": "hinge", "knot": 1, "coef": -0.0025},
      {"input": "age_c", "type": "hinge", "knot": 2, "coef": -0.0590},
      {"input": "female", "type": "linear", "coef": -0.0585},
      {"input": "wfns45", "type": "linear", "coef": 1.9415},
      {"input": "fisher34", "type": "linear", "coef": 0.4985},
      {"input": "ct_ivh", "type": "linear", "coef": 0.3875},
      {"input": "ct_ich", "type": "linear", "coef": 0.4800},
      {"input": "htn", "type": "linear", "coef": -0.0525},
      {"input": "surgery", "type": "linear", "coef": -1.7465},
      {"input": "urban", "type": "linear", "coef": -0.1725},
      {"input": "farmer", "type": "linear", "coef": -0.0175},
      {"input": "l7", "type": "linear", "coef": -0.0248},
      {"input": "l7", "type": "hinge", "knot": 1, "coef": 0.0008},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": 0.0132},
      {"input": "l7", "type": "hinge", "knot": 3, "coef": 0.0353},
      {"input": "l7", "type": "hinge", "knot": 4, "coef": 0.0786},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": 0.1602},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": 0.2695},
      {"input": "l7", "type": "hinge", "knot": 7, "coef": 0.2930},
      {"input": "l7", "type": "hinge", "knot": 8, "coef": 0.0869},
      {"input": "l7", "type": "hinge", "knot": 9, "coef": -0.1960}
    ],
    "interactions": [
      {"inputs": ["age_c", "l7"], "coef": 0.005},
      {"inputs": ["age_c", "female"], "coef": -0.063},
      {"inputs": ["age_c", "wfns45"], "coef": 0.023},
      {"inputs": ["age_c", "fisher34"], "coef": -0.012},
      {"inputs": ["age_c", "ct_ivh"], "coef": 0.023},
      {"inputs": ["age_c", "htn"], "coef": 0.004},
      {"inputs": ["age_c", "surgery"], "coef": -0.080},
      {"inputs": ["age_c", "urban"], "coef": 0.006},
      {"inputs": ["age_c", "farmer"], "coef": 0.007},
      {"inputs": ["l7", "female"], "coef": 0.014},
      {"inputs": ["l7", "wfns45"], "coef": -0.003},
      {"inputs": ["l7", "fisher34"], "coef": -0.006},
      {"inputs": ["l7", "ct_ivh"], "coef": 0.006},
      {"inputs": ["l7", "ct_ich"], "coef": -0.039},
      {"inputs": ["l7", "htn"], "coef": 0.039},
      {"inputs": ["l7", "surgery"], "coef": 0.015},
      {"inputs": ["l7", "urban"], "coef": 0.005},
      {"inputs": ["l7", "farmer"], "coef": -0.003},
      {"inputs": ["female", "wfns45"], "coef": -0.044},
      {"inputs": ["female", "fisher34"], "coef": -0.060},
      {"inputs": ["female", "ct_ivh"], "coef": 0.050},
      {"inputs": ["female", "ct_ich"], "coef": 0.027},
      {"inputs": ["female", "htn"], "coef": -0.015},
      {"inputs": ["female", "surgery"], "coef": 0.020},
      {"inputs": ["female", "urban"], "coef": 0.002},
      {"inputs": ["female", "farmer"], "coef": 0.071},
      {"inputs": ["wfns45", "fisher34"], "coef": -0.044},
      {"inputs": ["wfns45", "ct_ivh"], "coef": -0.006},
      {"inputs": ["wfns45", "ct_ich"], "coef": -0.103},
      {"inputs": ["wfns45", "htn"], "coef": 0.004},
      {"inputs": ["wfns45", "surgery"], "coef": -0.023},
      {"inputs": ["wfns45", "urban"], "coef": -0.043},
      {"inputs": ["wfns45", "farmer"], "coef": -0.058},
      {"inputs": ["fisher34", "ct_ivh"], "coef": 0.085},
      {"inputs": ["fisher34", "ct_ich"], "coef": 0.038},
      {"inputs": ["fisher34", "htn"], "coef": -0.044},
      {"inputs": ["fisher34", "surgery"], "coef": -0.011},
      {"inputs": ["fisher34", "urban"], "coef": 0.029},
      {"inputs": ["fisher34", "farmer"], "coef": 0.102},
      {"inputs": ["ct_ivh", "ct_ich"], "coef": -0.011},
      {"inputs": ["ct_ivh", "htn"], "coef": 0.007},
      {"inputs": ["ct_ivh", "surgery"], "coef": 0.120},
      {"inputs": ["ct_ivh", "urban"], "coef": 0.034},
      {"inputs": ["ct_ivh", "farmer"], "coef": -0.068},
      {"inputs": ["ct_ich", "htn"], "coef": -0.035},
      {"inputs": ["ct_ich", "surgery"], "coef": 0.030},
      {"inputs": ["ct_ich", "urban"], "coef": 0.042},
      {"inputs": ["ct_ich", "farmer"], "coef": 0.016},
      {"inputs": ["htn", "surgery"], "coef": 0.057},
      {"inputs": ["htn", "urban"], "coef": 0.004},
      {"inputs": ["htn", "farmer"], "coef": 0.037},
      {"inputs": ["surgery", "urban"], "coef": 0.038},
      {"inputs": ["surgery", "farmer"], "coef": 0.040},
      {"inputs": ["urban", "farmer"], "coef": 0.005}
    ]
  },
  "confidence_trained": 0.97
}
```