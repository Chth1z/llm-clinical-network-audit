This is a sum of eight **saturating, interacting contrasts**, not a monotone clinical risk score. For example, at age 60 with the other binary inputs zero, ICH changes predicted mortality from **5.8% to 2.1%** when `l7=0`, but from **7.3% to 15.3%** when `l7=5`.

Below is an approximate analytical log-odds surrogate—not a numerically validated fit. Rankings are approximate and background-dependent. The permitted additive/pairwise form cannot reproduce every nonlinear interaction. Also, `surgery` uses information acquired during admission; its protective prediction is not a causal treatment estimate.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "large overall; local reversals",
      "rank": 1
    },
    "female": {
      "direction": "no clear effect",
      "size": "small, context-dependent",
      "rank": 11
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "large",
      "rank": 2
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "moderate overall",
      "rank": 6
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "moderate, heterogeneous",
      "rank": 5
    },
    "ct_ich": {
      "direction": "no clear effect",
      "size": "substantial sign-changing contrasts",
      "rank": 7
    },
    "htn": {
      "direction": "increases risk",
      "size": "small to moderate",
      "rank": 8
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "large",
      "rank": 3
    },
    "urban": {
      "direction": "decreases risk",
      "size": "small average; reversals possible",
      "rank": 9
    },
    "farmer": {
      "direction": "no clear effect",
      "size": "small, context-dependent",
      "rank": 10
    },
    "l7": {
      "direction": "no clear effect",
      "size": "non-monotone and age-dependent",
      "rank": 4
    }
  },
  "interactions": [
    "Age and l7 interact: the age association can reverse at very low l7.",
    "The ICH contrast changes nonlinearly with l7 and can reverse sign.",
    "Urban residence attenuates the WFNS contrast on average.",
    "The surgery contrast depends on WFNS and the other findings; there is no constant treatment odds ratio.",
    "The hypertension association is generally stronger at low l7.",
    "ICH contrasts also depend on surgery, urban residence and farmer occupation."
  ],
  "unexpected": [
    {
      "inputs": ["age_c", "l7"],
      "description": "Older age can predict lower mortality. With all binary inputs zero, increasing age from 60 to 80 lowers risk from about 5.8% to 2.7% at l7=0, but raises it from about 7.3% to 23.0% at l7=5.",
      "where": "age_c=0 to 2, corresponding to ages 60 to 80; compare l7=0 with l7=5."
    },
    {
      "inputs": ["ct_ich", "l7"],
      "description": "ICH can be protective at very low l7 and harmful at higher l7. At age 60 with the remaining binary inputs zero, the ICH contrast reverses near l7=1.",
      "where": "age_c=0, remaining binary inputs=0; crossover approximately l7=1.0."
    },
    {
      "inputs": ["l7"],
      "description": "Even within one fixed profile, the laboratory response has a small rise-fall-rise wiggle rather than a single monotone slope.",
      "where": "At age_c=0 and all binary inputs=0: local maximum around l7=1.4 and local minimum around l7=2.9."
    }
  ],
  "surrogate": {
    "intercept": -4.0277,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": -0.2201},
      {"input": "age_c", "type": "hinge", "knot": -3, "coef": 0.3423},
      {"input": "age_c", "type": "hinge", "knot": -2, "coef": 0.1530},
      {"input": "age_c", "type": "hinge", "knot": -1, "coef": 0.0278},
      {"input": "age_c", "type": "hinge", "knot": 0, "coef": 0.0333},
      {"input": "age_c", "type": "hinge", "knot": 1, "coef": -0.0643},
      {"input": "age_c", "type": "hinge", "knot": 2, "coef": -0.0737},
      {"input": "age_c", "type": "hinge", "knot": 3, "coef": 0.0015},
      {"input": "female", "type": "linear", "coef": 0.1750},
      {"input": "wfns45", "type": "linear", "coef": 2.3520},
      {"input": "fisher34", "type": "linear", "coef": 0.4155},
      {"input": "ct_ivh", "type": "linear", "coef": 0.6145},
      {"input": "ct_ich", "type": "linear", "coef": 0.0745},
      {"input": "htn", "type": "linear", "coef": 0.6420},
      {"input": "surgery", "type": "linear", "coef": -1.9190},
      {"input": "urban", "type": "linear", "coef": -0.0680},
      {"input": "farmer", "type": "linear", "coef": -0.1265},
      {"input": "l7", "type": "linear", "coef": 0.2360},
      {"input": "l7", "type": "hinge", "knot": 1, "coef": -0.0980},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": -0.0815},
      {"input": "l7", "type": "hinge", "knot": 3, "coef": -0.0304},
      {"input": "l7", "type": "hinge", "knot": 4, "coef": 0.0030},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": 0.0142},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": 0.0210},
      {"input": "l7", "type": "hinge", "knot": 8, "coef": 0.0174}
    ],
    "interactions": [
      {"inputs": ["age_c", "l7"], "coef": 0.019},
      {"inputs": ["age_c", "female"], "coef": -0.006},
      {"inputs": ["age_c", "wfns45"], "coef": 0.140},
      {"inputs": ["age_c", "fisher34"], "coef": -0.018},
      {"inputs": ["age_c", "ct_ivh"], "coef": -0.008},
      {"inputs": ["age_c", "ct_ich"], "coef": -0.031},
      {"inputs": ["age_c", "htn"], "coef": 0.019},
      {"inputs": ["age_c", "surgery"], "coef": -0.023},
      {"inputs": ["age_c", "urban"], "coef": 0.019},
      {"inputs": ["age_c", "farmer"], "coef": 0.035},
      {"inputs": ["l7", "female"], "coef": -0.039},
      {"inputs": ["l7", "wfns45"], "coef": -0.043},
      {"inputs": ["l7", "fisher34"], "coef": 0.005},
      {"inputs": ["l7", "ct_ivh"], "coef": -0.009},
      {"inputs": ["l7", "ct_ich"], "coef": 0.033},
      {"inputs": ["l7", "htn"], "coef": -0.065},
      {"inputs": ["l7", "surgery"], "coef": 0.031},
      {"inputs": ["l7", "urban"], "coef": -0.017},
      {"inputs": ["l7", "farmer"], "coef": 0.033},
      {"inputs": ["female", "ct_ivh"], "coef": -0.037},
      {"inputs": ["female", "surgery"], "coef": -0.026},
      {"inputs": ["female", "urban"], "coef": 0.079},
      {"inputs": ["wfns45", "fisher34"], "coef": -0.135},
      {"inputs": ["wfns45", "ct_ivh"], "coef": -0.071},
      {"inputs": ["wfns45", "ct_ich"], "coef": 0.069},
      {"inputs": ["wfns45", "surgery"], "coef": 0.065},
      {"inputs": ["wfns45", "urban"], "coef": -0.368},
      {"inputs": ["wfns45", "farmer"], "coef": -0.100},
      {"inputs": ["fisher34", "ct_ich"], "coef": -0.063},
      {"inputs": ["fisher34", "surgery"], "coef": 0.055},
      {"inputs": ["fisher34", "urban"], "coef": 0.126},
      {"inputs": ["ct_ivh", "surgery"], "coef": -0.078},
      {"inputs": ["ct_ivh", "urban"], "coef": -0.038},
      {"inputs": ["ct_ivh", "farmer"], "coef": -0.067},
      {"inputs": ["ct_ich", "htn"], "coef": 0.131},
      {"inputs": ["ct_ich", "surgery"], "coef": 0.177},
      {"inputs": ["ct_ich", "urban"], "coef": -0.195},
      {"inputs": ["ct_ich", "farmer"], "coef": -0.244},
      {"inputs": ["htn", "surgery"], "coef": -0.065},
      {"inputs": ["htn", "urban"], "coef": -0.036},
      {"inputs": ["htn", "farmer"], "coef": -0.098},
      {"inputs": ["surgery", "urban"], "coef": 0.114},
      {"inputs": ["surgery", "farmer"], "coef": 0.060},
      {"inputs": ["urban", "farmer"], "coef": 0.144}
    ]
  },
  "confidence_trained": 0.95
}
```