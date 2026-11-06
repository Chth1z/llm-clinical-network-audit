The effects are **not uniformly monotone**: each input’s influence depends on which tanh units are saturated. For continuous input \(i\), the log-odds derivative is
\[
\sum_j W_{2j}W_{1ji}\operatorname{sech}^2(W_{1j}x+b_{1j}).
\]
Binary effects require comparing predictions with the indicator switched.

For example, at age 60 with every binary indicator zero, predicted mortality is approximately **48%, 82%, and 65%** at `l7` values 0, 3, and 10. At `l7=5`, switching `ct_ich` on reduces prediction from approximately **78% to 11%**; switching `surgery` on instead raises it to approximately **90%**. These are properties of these weights, not clinical or causal conclusions.

Below is an **analytically approximated, unvalidated** spline/bilinear surrogate, referenced to ages 20–90, balanced binary indicators, and `l7` spanning 0–10. Directions summarize broad tendencies, not universal signs; importance depends on the input distribution. The restricted surrogate cannot reproduce every moving tanh transition exactly. Also, treatment during admission makes `surgery` a post-admission predictor. Training provenance is not identifiable from these weights alone; the confidence value is deliberately uninformative.

```json
{
  "effects": {
    "age_c": {
      "direction": "no clear effect",
      "size": "moderate; non-monotonic",
      "rank": 6
    },
    "female": {
      "direction": "increases risk",
      "size": "small average increase",
      "rank": 10
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "moderate average increase",
      "rank": 5
    },
    "fisher34": {
      "direction": "no clear effect",
      "size": "small; sign-changing",
      "rank": 11
    },
    "ct_ivh": {
      "direction": "decreases risk",
      "size": "moderate average decrease",
      "rank": 4
    },
    "ct_ich": {
      "direction": "decreases risk",
      "size": "largest binary decrease",
      "rank": 2
    },
    "htn": {
      "direction": "no clear effect",
      "size": "small; sign-changing",
      "rank": 9
    },
    "surgery": {
      "direction": "increases risk",
      "size": "moderate; context-dependent",
      "rank": 7
    },
    "urban": {
      "direction": "decreases risk",
      "size": "small-to-moderate average decrease",
      "rank": 8
    },
    "farmer": {
      "direction": "decreases risk",
      "size": "large average decrease",
      "rank": 3
    },
    "l7": {
      "direction": "increases risk",
      "size": "largest overall; sometimes reverses",
      "rank": 1
    }
  },
  "interactions": [
    "The risk-raising transition of hidden unit 1 shifts upward by 3.85 l7 units with ct_ich, upward by 1.71 with ct_ivh, and downward by 2.20 with wfns45. These are unit-specific shifts, not universal mortality thresholds.",
    "Farmer and hypertension shift the risk-raising transition of hidden unit 5 upward by approximately 2.82 and 2.35 l7 units respectively.",
    "Age effects depend strongly on l7 and on indicators affecting hidden unit 8, especially ct_ich and farmer.",
    "Surgery has competing positive and negative pathways; its net association is generally positive but varies with l7 and the other indicators.",
    "Fisher grade and hypertension can change effect direction as the hidden units saturate."
  ],
  "unexpected": [
    {
      "inputs": ["ct_ich", "ct_ivh"],
      "description": "Both haemorrhage indicators generally reduce predicted mortality. At the reference profile, ct_ich changes probability from approximately 0.78 to 0.11, and ct_ivh changes it to approximately 0.64.",
      "where": "Switch 0 to 1 at age_c=0, l7=5, with every other binary indicator zero."
    },
    {
      "inputs": ["surgery"],
      "description": "Treatment generally raises predicted mortality rather than lowering it; this is an association, not a treatment-effect estimate.",
      "where": "Switch 0 to 1 at age_c=0, l7=5, with other indicators zero: approximately 0.78 to 0.90."
    },
    {
      "inputs": ["farmer"],
      "description": "Farmer occupation has a substantial risk-reducing association in the network.",
      "where": "Switch 0 to 1; at age_c=0, l7=5 and other indicators zero, probability falls approximately from 0.78 to 0.55."
    },
    {
      "inputs": ["age_c"],
      "description": "Age is not consistently adverse: predictions can rise, fall, and then rise again as age increases.",
      "where": "With l7=5 and all binary indicators zero, the age slope reverses near age_c=-0.13 and 2.6, approximately ages 59 and 86."
    },
    {
      "inputs": ["l7"],
      "description": "The laboratory relationship can be inverted-U-shaped. Its unspecified clinical identity prevents interpreting this as a physiological relationship.",
      "where": "At age_c=0 and all binary indicators zero, the maximum is near l7=3.2; probabilities are approximately 0.48 at 0, 0.82 at 3, and 0.65 at 10."
    },
    {
      "inputs": ["fisher34"],
      "description": "Higher Fisher grade does not have a stable risk-increasing effect.",
      "where": "At age_c=0 and other indicators zero, switching fisher34 on decreases risk at l7=0 but increases it slightly at l7=5."
    },
    {
      "inputs": ["htn"],
      "description": "Hypertension has opposing pathways and can change from risk-reducing to slightly risk-increasing.",
      "where": "At age_c=0 and other indicators zero, its effect is negative at l7=0 but slightly positive at l7=5."
    }
  ],
  "surrogate": {
    "intercept": 0.588,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.3295},
      {"input": "female", "type": "linear", "coef": 0.271},
      {"input": "wfns45", "type": "linear", "coef": 0.886},
      {"input": "fisher34", "type": "linear", "coef": -0.05},
      {"input": "ct_ivh", "type": "linear", "coef": -1.211},
      {"input": "ct_ich", "type": "linear", "coef": -3.9135},
      {"input": "htn", "type": "linear", "coef": -0.2795},
      {"input": "surgery", "type": "linear", "coef": 1.0515},
      {"input": "urban", "type": "linear", "coef": -0.679},
      {"input": "farmer", "type": "linear", "coef": -2.752},
      {"input": "l7", "type": "linear", "coef": 0.151},
      {"input": "age_c", "type": "hinge", "knot": -3, "coef": -0.032},
      {"input": "age_c", "type": "hinge", "knot": -2, "coef": -0.092},
      {"input": "age_c", "type": "hinge", "knot": -1, "coef": -0.141},
      {"input": "age_c", "type": "hinge", "knot": 0, "coef": -0.06},
      {"input": "age_c", "type": "hinge", "knot": 1, "coef": 0.09},
      {"input": "age_c", "type": "hinge", "knot": 2, "coef": 0.176},
      {"input": "l7", "type": "hinge", "knot": 1, "coef": 0.057},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": -0.014},
      {"input": "l7", "type": "hinge", "knot": 3, "coef": -0.012},
      {"input": "l7", "type": "hinge", "knot": 4, "coef": -0.027},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": -0.066},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": -0.104},
      {"input": "l7", "type": "hinge", "knot": 7, "coef": -0.113},
      {"input": "l7", "type": "hinge", "knot": 8, "coef": -0.087},
      {"input": "l7", "type": "hinge", "knot": 9, "coef": -0.054}
    ],
    "interactions": [
      {"inputs": ["age_c", "l7"], "coef": -0.03},
      {"inputs": ["female", "l7"], "coef": -0.022},
      {"inputs": ["wfns45", "l7"], "coef": -0.075},
      {"inputs": ["fisher34", "l7"], "coef": 0.016},
      {"inputs": ["ct_ivh", "l7"], "coef": 0.104},
      {"inputs": ["ct_ich", "l7"], "coef": 0.295},
      {"inputs": ["htn", "l7"], "coef": 0.045},
      {"inputs": ["surgery", "l7"], "coef": -0.08},
      {"inputs": ["urban", "l7"], "coef": 0.069},
      {"inputs": ["farmer", "l7"], "coef": 0.26},
      {"inputs": ["age_c", "female"], "coef": -0.018},
      {"inputs": ["age_c", "wfns45"], "coef": -0.008},
      {"inputs": ["age_c", "fisher34"], "coef": 0.028},
      {"inputs": ["age_c", "ct_ivh"], "coef": 0.012},
      {"inputs": ["age_c", "ct_ich"], "coef": -0.054},
      {"inputs": ["age_c", "htn"], "coef": -0.007},
      {"inputs": ["age_c", "surgery"], "coef": 0.013},
      {"inputs": ["age_c", "urban"], "coef": 0.009},
      {"inputs": ["age_c", "farmer"], "coef": -0.08},
      {"inputs": ["female", "wfns45"], "coef": -0.051},
      {"inputs": ["female", "fisher34"], "coef": -0.018},
      {"inputs": ["female", "ct_ivh"], "coef": 0.056},
      {"inputs": ["female", "ct_ich"], "coef": 0.079},
      {"inputs": ["female", "htn"], "coef": -0.091},
      {"inputs": ["female", "surgery"], "coef": 0.061},
      {"inputs": ["female", "urban"], "coef": 0.01},
      {"inputs": ["female", "farmer"], "coef": -0.002},
      {"inputs": ["wfns45", "fisher34"], "coef": 0.043},
      {"inputs": ["wfns45", "ct_ivh"], "coef": 0.121},
      {"inputs": ["wfns45", "ct_ich"], "coef": 0.266},
      {"inputs": ["wfns45", "htn"], "coef": -0.095},
      {"inputs": ["wfns45", "surgery"], "coef": -0.113},
      {"inputs": ["wfns45", "urban"], "coef": 0.106},
      {"inputs": ["wfns45", "farmer"], "coef": -0.017},
      {"inputs": ["fisher34", "ct_ivh"], "coef": -0.057},
      {"inputs": ["fisher34", "ct_ich"], "coef": -0.067},
      {"inputs": ["fisher34", "htn"], "coef": 0.056},
      {"inputs": ["fisher34", "surgery"], "coef": 0.02},
      {"inputs": ["fisher34", "urban"], "coef": 0.005},
      {"inputs": ["fisher34", "farmer"], "coef": -0.024},
      {"inputs": ["ct_ivh", "ct_ich"], "coef": -0.194},
      {"inputs": ["ct_ivh", "htn"], "coef": 0.021},
      {"inputs": ["ct_ivh", "surgery"], "coef": 0.008},
      {"inputs": ["ct_ivh", "urban"], "coef": -0.086},
      {"inputs": ["ct_ivh", "farmer"], "coef": 0.023},
      {"inputs": ["ct_ich", "htn"], "coef": 0.116},
      {"inputs": ["ct_ich", "surgery"], "coef": -0.11},
      {"inputs": ["ct_ich", "urban"], "coef": -0.196},
      {"inputs": ["ct_ich", "farmer"], "coef": 0.229},
      {"inputs": ["htn", "surgery"], "coef": -0.148},
      {"inputs": ["htn", "urban"], "coef": -0.008},
      {"inputs": ["htn", "farmer"], "coef": -0.049},
      {"inputs": ["surgery", "urban"], "coef": 0.145},
      {"inputs": ["surgery", "farmer"], "coef": -0.279},
      {"inputs": ["urban", "farmer"], "coef": -0.147}
    ]
  },
  "confidence_trained": 0.5
}
```