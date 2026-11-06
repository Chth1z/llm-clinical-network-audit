The network’s effects come from the **whole chain**, not individual weight signs:
\[
\nabla_x\eta=W_3\,\mathrm{diag}(1-h_2^2)\,W_2\,\mathrm{diag}(1-h_1^2)\,W_1.
\]
Consequently, effects can change with the other inputs.

For a reproducible reference, I used age 60, laboratories all 5, and binary inputs all 0.5—a mathematical interpolation point, **not a possible patient**. There, the log-odds are approximately −0.777. WFNS and surgery dominate the local derivatives; female nearly cancels out. The rankings below compare absolute derivatives per **one coded input unit**, not population importance.

There is demonstrable nonmonotonicity: keeping that reference otherwise fixed, setting `l8` to 0, 5, and 10 gives probabilities approximately **0.219, 0.315, and 0.297**. Thus “higher l8 increases risk” would misdescribe this network.

The surrogate below preserves the reference prediction and local slopes, with an `l8` spline additionally matching those endpoint predictions. **It is a local approximation, not a globally validated distillation**; its spline knots are approximation choices, not discovered clinical thresholds. Directions and sizes below are local unless explicitly described as nonmonotone. Surgery is also a post-admission variable despite the introductory description; its predictive association is neither an admission-only predictor nor a causal treatment effect. The provenance probability is subjective.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "local +0.808 logit/decade", "rank": 4},
    "female": {"direction": "no clear effect", "size": "almost zero locally", "rank": 20},
    "wfns45": {"direction": "increases risk", "size": "local derivative +2.855", "rank": 1},
    "fisher34": {"direction": "increases risk", "size": "local derivative +0.562", "rank": 6},
    "ct_ivh": {"direction": "increases risk", "size": "local derivative +0.713", "rank": 5},
    "ct_ich": {"direction": "increases risk", "size": "local derivative +0.910", "rank": 3},
    "htn": {"direction": "increases risk", "size": "local derivative +0.486", "rank": 7},
    "surgery": {"direction": "decreases risk", "size": "local derivative -2.236", "rank": 2},
    "urban": {"direction": "decreases risk", "size": "local derivative -0.095", "rank": 10},
    "farmer": {"direction": "decreases risk", "size": "local derivative -0.134", "rank": 8},
    "l1": {"direction": "decreases risk", "size": "local -0.020 logit/unit", "rank": 18},
    "l2": {"direction": "decreases risk", "size": "local -0.086 logit/unit", "rank": 11},
    "l3": {"direction": "decreases risk", "size": "local -0.058 logit/unit", "rank": 14},
    "l4": {"direction": "increases risk", "size": "local +0.077 logit/unit", "rank": 12},
    "l5": {"direction": "decreases risk", "size": "local -0.039 logit/unit", "rank": 15},
    "l6": {"direction": "decreases risk", "size": "local -0.039 logit/unit", "rank": 16},
    "l7": {"direction": "increases risk", "size": "local +0.018 logit/unit", "rank": 19},
    "l8": {"direction": "no clear effect", "size": "nonmonotone; locally +0.121", "rank": 9},
    "l9": {"direction": "increases risk", "size": "local +0.032 logit/unit", "rank": 17},
    "l10": {"direction": "decreases risk", "size": "local -0.076 logit/unit", "rank": 13}
  },
  "unexpected": [
    {
      "inputs": ["l8"],
      "description": "The conditional response is nonmonotone: probabilities are approximately 0.219, 0.315, and 0.297 at l8 values 0, 5, and 10. The derivative at 5 is positive, so the response must turn downward somewhere between 5 and 10.",
      "where": "Conditional on age_c=0, other laboratories=5, and binary inputs=0.5. This is an interpolation diagnostic, not a valid patient profile; the turning point is not universal."
    }
  ],
  "surrogate": {
    "intercept": -1.8419,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.8080},
      {"input": "female", "type": "linear", "coef": -0.0100},
      {"input": "wfns45", "type": "linear", "coef": 2.8546},
      {"input": "fisher34", "type": "linear", "coef": 0.5619},
      {"input": "ct_ivh", "type": "linear", "coef": 0.7133},
      {"input": "ct_ich", "type": "linear", "coef": 0.9095},
      {"input": "htn", "type": "linear", "coef": 0.4865},
      {"input": "surgery", "type": "linear", "coef": -2.2365},
      {"input": "urban", "type": "linear", "coef": -0.0946},
      {"input": "farmer", "type": "linear", "coef": -0.1337},
      {"input": "l1", "type": "linear", "coef": -0.0203},
      {"input": "l2", "type": "linear", "coef": -0.0862},
      {"input": "l3", "type": "linear", "coef": -0.0576},
      {"input": "l4", "type": "linear", "coef": 0.0771},
      {"input": "l5", "type": "linear", "coef": -0.0390},
      {"input": "l6", "type": "linear", "coef": -0.0388},
      {"input": "l7", "type": "linear", "coef": 0.0177},
      {"input": "l8", "type": "linear", "coef": 0.0769},
      {"input": "l8", "type": "hinge", "knot": 2.5, "coef": 0.0436},
      {"input": "l8", "type": "hinge", "knot": 7.5, "coef": -0.2746},
      {"input": "l9", "type": "linear", "coef": 0.0325},
      {"input": "l10", "type": "linear", "coef": -0.0763}
    ],
    "interactions": []
  },
  "confidence_trained": 0.85
}
```