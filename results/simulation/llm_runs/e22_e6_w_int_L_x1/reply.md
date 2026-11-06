**This is a local approximation, not a validated global distillation:** numerical execution was unavailable, so I cannot honestly report prediction-matching errors.

Manual propagation of the weights at age 60, laboratories all 5, and binary inputs all 0.5 gives approximately **−0.46 log-odds**, or **39% probability**. The fractional binary values are a mathematical reference, not a patient.

Near that reference:
- WFNS and surgery have strong, opposing effects; age increases predictions.
- **l5 and l8 matter substantially and interact positively**: increasing either strengthens the effect of the other. Their mixed log-odds derivative is approximately +0.10.
- Female, l1 and l2 have nearly zero local slopes—not necessarily zero effects elsewhere.

Below, directions are **local**, and ranks use standardized local sensitivities assuming ages 30–90, laboratories 0–10, and balanced binary inputs. The surrogate retains the strong laboratory interaction and approximates mild l5 curvature. Its hinge knots are approximation choices, **not discovered clinical thresholds**.

Also, surgery describes treatment during admission, so it is not genuinely admission-only information. Its negative association must not be interpreted as a causal treatment benefit.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "large; per decade", "rank": 3},
    "female": {"direction": "no clear effect", "size": "negligible local slope", "rank": 20},
    "wfns45": {"direction": "increases risk", "size": "very large locally", "rank": 1},
    "fisher34": {"direction": "increases risk", "size": "moderate locally", "rank": 6},
    "ct_ivh": {"direction": "increases risk", "size": "small locally", "rank": 13},
    "ct_ich": {"direction": "increases risk", "size": "small locally", "rank": 14},
    "htn": {"direction": "increases risk", "size": "modest locally", "rank": 11},
    "surgery": {"direction": "decreases risk", "size": "very large locally", "rank": 2},
    "urban": {"direction": "decreases risk", "size": "small locally", "rank": 17},
    "farmer": {"direction": "increases risk", "size": "small locally", "rank": 16},
    "l1": {"direction": "no clear effect", "size": "near-flat locally", "rank": 18},
    "l2": {"direction": "no clear effect", "size": "near-flat locally", "rank": 19},
    "l3": {"direction": "decreases risk", "size": "modest locally", "rank": 8},
    "l4": {"direction": "decreases risk", "size": "modest locally", "rank": 7},
    "l5": {"direction": "increases risk", "size": "large; interaction-dependent", "rank": 5},
    "l6": {"direction": "decreases risk", "size": "small locally", "rank": 15},
    "l7": {"direction": "decreases risk", "size": "small locally", "rank": 12},
    "l8": {"direction": "increases risk", "size": "large; interaction-dependent", "rank": 4},
    "l9": {"direction": "decreases risk", "size": "modest locally", "rank": 10},
    "l10": {"direction": "decreases risk", "size": "modest locally", "rank": 9}
  },
  "unexpected": [
    {
      "inputs": ["l5", "l8"],
      "description": "Substantial positive local interaction: increasing either laboratory value makes the other's effect more risk-increasing. Separate additive laboratory effects miss this relationship.",
      "where": "Around l5 = 5 and l8 = 5, with other inputs at the stated reference; no verified global cutoff."
    }
  ],
  "surrogate": {
    "intercept": -0.178,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.639},
      {"input": "female", "type": "linear", "coef": -0.001},
      {"input": "wfns45", "type": "linear", "coef": 2.573},
      {"input": "fisher34", "type": "linear", "coef": 0.978},
      {"input": "ct_ivh", "type": "linear", "coef": 0.259},
      {"input": "ct_ich", "type": "linear", "coef": 0.221},
      {"input": "htn", "type": "linear", "coef": 0.398},
      {"input": "surgery", "type": "linear", "coef": -2.461},
      {"input": "urban", "type": "linear", "coef": -0.120},
      {"input": "farmer", "type": "linear", "coef": 0.142},
      {"input": "l1", "type": "linear", "coef": -0.014},
      {"input": "l2", "type": "linear", "coef": -0.010},
      {"input": "l3", "type": "linear", "coef": -0.095},
      {"input": "l4", "type": "linear", "coef": -0.105},
      {"input": "l5", "type": "linear", "coef": -0.045},
      {"input": "l5", "type": "hinge", "knot": 2, "coef": -0.072},
      {"input": "l5", "type": "hinge", "knot": 4, "coef": -0.072},
      {"input": "l5", "type": "hinge", "knot": 6, "coef": -0.072},
      {"input": "l5", "type": "hinge", "knot": 8, "coef": -0.072},
      {"input": "l6", "type": "linear", "coef": -0.038},
      {"input": "l7", "type": "linear", "coef": -0.050},
      {"input": "l8", "type": "linear", "coef": -0.169},
      {"input": "l9", "type": "linear", "coef": -0.073},
      {"input": "l10", "type": "linear", "coef": -0.089}
    ],
    "interactions": [
      {"inputs": ["l5", "l8"], "coef": 0.098}
    ]
  },
  "confidence_trained": 0.99
}
```