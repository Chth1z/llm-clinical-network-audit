The weights encode more than a conventional severity score:

- **`l3` has a pronounced non-monotonic effect.** On a diagnostic midpoint slice—age 60, other laboratories 5, and binary inputs 0.5—the network gives approximately **15.8%, 11.0%, 24.8%, 87.0%, and 93.5%** at `l3 = 0, 2, 5, 8, 10`. The fractional indicators are an algebraic reference, not a patient.
- Higher WFNS grade and older age generally raise predictions; treatment generally lowers them. **Their strengths depend on the laboratory inputs.** Some smaller effects even reverse direction.
- Despite the admission-time description, `surgery` records subsequent treatment. Its association is **not a treatment-effect estimate**, and its availability creates an admission-time prediction problem.

Below is a **reference-slice approximation**, using an `l3` spline and `l3`-dependent slopes derived from the weights. It is not a globally validated distillation: simultaneous departures of several laboratories from their midpoints can produce additional interactions. Directions and ranks summarize reference-region behavior, not population importance. The training-confidence judgment concerns structured versus scrambled weights, not clinical validity or provenance.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "moderate per decade",
      "rank": 4
    },
    "female": {
      "direction": "decreases risk",
      "size": "small, conditional",
      "rank": 15
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "very large",
      "rank": 2
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "moderate, laboratory-dependent",
      "rank": 7
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "moderate, laboratory-dependent",
      "rank": 6
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "moderate, laboratory-dependent",
      "rank": 5
    },
    "htn": {
      "direction": "increases risk",
      "size": "small to moderate",
      "rank": 10
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "very large association",
      "rank": 3
    },
    "urban": {
      "direction": "no clear effect",
      "size": "small, conditional sign",
      "rank": 14
    },
    "farmer": {
      "direction": "no clear effect",
      "size": "small, conditional",
      "rank": 17
    },
    "l1": {
      "direction": "no clear effect",
      "size": "conditional sign reversals",
      "rank": 12
    },
    "l2": {
      "direction": "no clear effect",
      "size": "weak near reference",
      "rank": 20
    },
    "l3": {
      "direction": "no clear effect",
      "size": "dominant, non-monotonic",
      "rank": 1
    },
    "l4": {
      "direction": "no clear effect",
      "size": "weak, conditional sign",
      "rank": 19
    },
    "l5": {
      "direction": "no clear effect",
      "size": "mainly low-l3 sensitivity",
      "rank": 11
    },
    "l6": {
      "direction": "decreases risk",
      "size": "stronger at high l3",
      "rank": 9
    },
    "l7": {
      "direction": "no clear effect",
      "size": "substantial conditional reversal",
      "rank": 8
    },
    "l8": {
      "direction": "decreases risk",
      "size": "modest near reference",
      "rank": 13
    },
    "l9": {
      "direction": "no clear effect",
      "size": "small conditional reversal",
      "rank": 16
    },
    "l10": {
      "direction": "decreases risk",
      "size": "small near reference",
      "rank": 18
    }
  },
  "unexpected": [
    {
      "inputs": ["l3"],
      "description": "Risk initially falls, reaches a trough, then rises sharply and eventually flattens. This is not a globally linear or monotone laboratory effect.",
      "where": "On the midpoint slice, the trough is around l3=2–3, the steep rise is roughly l3=4–8, and flattening appears toward l3=9–10. Other inputs shift this shape."
    },
    {
      "inputs": ["l1", "l3"],
      "description": "The local effect of l1 changes from risk-increasing to risk-decreasing and back to risk-increasing.",
      "where": "With other inputs at their reference values, the l1 slope is approximately +0.145, -0.060, and +0.061 log-odds per unit at l3=0, 5, and 8."
    },
    {
      "inputs": ["l7", "l3"],
      "description": "The local effect of l7 reverses: higher l7 raises predictions at low l3 but lowers them around intermediate and high l3.",
      "where": "Reference-region slopes are approximately +0.081, -0.154, and -0.097 log-odds per unit at l3=0, 5, and 8; the exact transition depends on the other inputs."
    },
    {
      "inputs": ["fisher34", "ct_ivh", "ct_ich", "l3"],
      "description": "The imaging indicators do not have fixed additive effects. Their relative strengths change substantially with l3.",
      "where": "Near the reference slice, Fisher and intracerebral-haemorrhage effects are stronger around l3=5 than at l3=0 or 8; the intraventricular-haemorrhage effect is stronger at l3=0 than at l3=8."
    }
  ],
  "surrogate": {
    "intercept": -2.4548,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.620},
      {"input": "female", "type": "linear", "coef": -0.280},
      {"input": "wfns45", "type": "linear", "coef": 2.548},
      {"input": "fisher34", "type": "linear", "coef": 0.101},
      {"input": "ct_ivh", "type": "linear", "coef": 0.740},
      {"input": "ct_ich", "type": "linear", "coef": 0.296},
      {"input": "htn", "type": "linear", "coef": 0.142},
      {"input": "surgery", "type": "linear", "coef": -2.105},
      {"input": "urban", "type": "linear", "coef": 0.028},
      {"input": "farmer", "type": "linear", "coef": 0.003},
      {"input": "l1", "type": "linear", "coef": 0.145},
      {"input": "l2", "type": "linear", "coef": 0.012},
      {"input": "l3", "type": "linear", "coef": 0.3023},
      {"input": "l4", "type": "linear", "coef": 0.025},
      {"input": "l5", "type": "linear", "coef": -0.177},
      {"input": "l6", "type": "linear", "coef": -0.002},
      {"input": "l7", "type": "linear", "coef": 0.081},
      {"input": "l8", "type": "linear", "coef": -0.087},
      {"input": "l9", "type": "linear", "coef": 0.052},
      {"input": "l10", "type": "linear", "coef": -0.040},
      {"input": "l3", "type": "hinge", "knot": 1, "coef": -0.0847},
      {"input": "l3", "type": "hinge", "knot": 2, "coef": 0.1488},
      {"input": "l3", "type": "hinge", "knot": 3, "coef": 0.4378},
      {"input": "l3", "type": "hinge", "knot": 4, "coef": 0.4229},
      {"input": "l3", "type": "hinge", "knot": 5, "coef": 0.2173},
      {"input": "l3", "type": "hinge", "knot": 6, "coef": 0.0277},
      {"input": "l3", "type": "hinge", "knot": 7, "coef": -0.1641},
      {"input": "l3", "type": "hinge", "knot": 8, "coef": -0.7626},
      {"input": "l3", "type": "hinge", "knot": 9, "coef": -0.3189}
    ],
    "interactions": [
      {"inputs": ["age_c", "l3"], "coef": 0.001},
      {"inputs": ["age_c", "l3"], "knots": [-6, 5], "coef": -0.092333},
      {"inputs": ["age_c", "l3"], "knots": [-6, 8], "coef": 0.091333},

      {"inputs": ["female", "l3"], "coef": 0.0162},
      {"inputs": ["female", "l3"], "knots": [0, 5], "coef": 0.016133},
      {"inputs": ["female", "l3"], "knots": [0, 8], "coef": -0.032333},

      {"inputs": ["wfns45", "l3"], "coef": -0.0196},
      {"inputs": ["wfns45", "l3"], "knots": [0, 5], "coef": -0.261733},
      {"inputs": ["wfns45", "l3"], "knots": [0, 8], "coef": 0.281333},

      {"inputs": ["fisher34", "l3"], "coef": 0.0942},
      {"inputs": ["fisher34", "l3"], "knots": [0, 5], "coef": -0.2242},
      {"inputs": ["fisher34", "l3"], "knots": [0, 8], "coef": 0.130},

      {"inputs": ["ct_ivh", "l3"], "coef": -0.0448},
      {"inputs": ["ct_ivh", "l3"], "knots": [0, 5], "coef": -0.079867},
      {"inputs": ["ct_ivh", "l3"], "knots": [0, 8], "coef": 0.124667},

      {"inputs": ["ct_ich", "l3"], "coef": 0.0848},
      {"inputs": ["ct_ich", "l3"], "knots": [0, 5], "coef": -0.242467},
      {"inputs": ["ct_ich", "l3"], "knots": [0, 8], "coef": 0.157667},

      {"inputs": ["htn", "l3"], "coef": 0.0404},
      {"inputs": ["htn", "l3"], "knots": [0, 5], "coef": -0.063733},
      {"inputs": ["htn", "l3"], "knots": [0, 8], "coef": 0.023333},

      {"inputs": ["surgery", "l3"], "coef": -0.0724},
      {"inputs": ["surgery", "l3"], "knots": [0, 5], "coef": 0.384733},
      {"inputs": ["surgery", "l3"], "knots": [0, 8], "coef": -0.312333},

      {"inputs": ["urban", "l3"], "coef": -0.0604},
      {"inputs": ["urban", "l3"], "knots": [0, 5], "coef": 0.110733},
      {"inputs": ["urban", "l3"], "knots": [0, 8], "coef": -0.050333},

      {"inputs": ["farmer", "l3"], "coef": -0.0124},
      {"inputs": ["farmer", "l3"], "knots": [0, 5], "coef": -0.048933},
      {"inputs": ["farmer", "l3"], "knots": [0, 8], "coef": 0.061333},

      {"inputs": ["l1", "l3"], "coef": -0.041},
      {"inputs": ["l1", "l3"], "knots": [0, 5], "coef": 0.081333},
      {"inputs": ["l1", "l3"], "knots": [0, 8], "coef": -0.040333},

      {"inputs": ["l2", "l3"], "coef": -0.0088},
      {"inputs": ["l2", "l3"], "knots": [0, 5], "coef": 0.010133},
      {"inputs": ["l2", "l3"], "knots": [0, 8], "coef": -0.001333},

      {"inputs": ["l4", "l3"], "coef": -0.0142},
      {"inputs": ["l4", "l3"], "knots": [0, 5], "coef": 0.023533},
      {"inputs": ["l4", "l3"], "knots": [0, 8], "coef": -0.009333},

      {"inputs": ["l5", "l3"], "coef": 0.0368},
      {"inputs": ["l5", "l3"], "knots": [0, 5], "coef": -0.0438},
      {"inputs": ["l5", "l3"], "knots": [0, 8], "coef": 0.007},

      {"inputs": ["l6", "l3"], "coef": -0.012},
      {"inputs": ["l6", "l3"], "knots": [0, 5], "coef": -0.020},
      {"inputs": ["l6", "l3"], "knots": [0, 8], "coef": 0.032},

      {"inputs": ["l7", "l3"], "coef": -0.047},
      {"inputs": ["l7", "l3"], "knots": [0, 5], "coef": 0.066},
      {"inputs": ["l7", "l3"], "knots": [0, 8], "coef": -0.019},

      {"inputs": ["l8", "l3"], "coef": 0.0056},
      {"inputs": ["l8", "l3"], "knots": [0, 5], "coef": -0.0126},
      {"inputs": ["l8", "l3"], "knots": [0, 8], "coef": 0.007},

      {"inputs": ["l9", "l3"], "coef": -0.0116},
      {"inputs": ["l9", "l3"], "knots": [0, 5], "coef": 0.0366},
      {"inputs": ["l9", "l3"], "knots": [0, 8], "coef": -0.025},

      {"inputs": ["l10", "l3"], "coef": -0.0046},
      {"inputs": ["l10", "l3"], "knots": [0, 5], "coef": 0.023933},
      {"inputs": ["l10", "l3"], "knots": [0, 8], "coef": -0.019333}
    ]
  },
  "confidence_trained": 0.97
}
```