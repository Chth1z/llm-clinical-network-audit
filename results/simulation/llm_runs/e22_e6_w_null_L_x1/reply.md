**The dominant pattern is higher predicted risk with age and admission severity, and lower predicted risk with treated status.** Individual weights are not effects: paths can cancel, and both tanh layers introduce saturation and interactions. In particular, small net laboratory coefficients do **not** establish that those inputs are unused.

**Limitation:** execution tools were unavailable. Below is an analytic, saturation-adjusted approximation, not a numerically fitted or validated replica. Its coefficients and rankings use an approximate reference distribution: ages 18–100, balanced binary inputs, and independent laboratories spanning 0–10. Fine rankings and nonlinear laboratory relationships remain uncertain; no unexpected threshold was established.

Also, `surgery` describes treatment **during admission**, despite the admission-only framing. Its negative association is neither a causal treatment effect nor information necessarily available at admission. Confidence in training is subjective; coherent severity/treatment pathways support it, but do not establish clinical provenance or validity.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "large across adult ages", "rank": 1},
    "female": {"direction": "no clear effect", "size": "very small linear projection", "rank": 16},
    "wfns45": {"direction": "increases risk", "size": "large", "rank": 2},
    "fisher34": {"direction": "increases risk", "size": "moderate", "rank": 5},
    "ct_ivh": {"direction": "increases risk", "size": "moderate", "rank": 4},
    "ct_ich": {"direction": "increases risk", "size": "small to moderate", "rank": 6},
    "htn": {"direction": "increases risk", "size": "small", "rank": 7},
    "surgery": {"direction": "decreases risk", "size": "large", "rank": 3},
    "urban": {"direction": "no clear effect", "size": "very small linear projection", "rank": 18},
    "farmer": {"direction": "increases risk", "size": "very small net association", "rank": 11},
    "l1": {"direction": "no clear effect", "size": "weak linear projection", "rank": 10},
    "l2": {"direction": "no clear effect", "size": "negligible linear projection", "rank": 20},
    "l3": {"direction": "no clear effect", "size": "negligible linear projection", "rank": 19},
    "l4": {"direction": "no clear effect", "size": "weak linear projection", "rank": 13},
    "l5": {"direction": "no clear effect", "size": "weak negative linear projection", "rank": 8},
    "l6": {"direction": "no clear effect", "size": "weak linear projection", "rank": 14},
    "l7": {"direction": "no clear effect", "size": "weak linear projection", "rank": 12},
    "l8": {"direction": "no clear effect", "size": "weak linear projection", "rank": 9},
    "l9": {"direction": "no clear effect", "size": "very small linear projection", "rank": 15},
    "l10": {"direction": "no clear effect", "size": "very small linear projection", "rank": 17}
  },
  "unexpected": [],
  "surrogate": {
    "intercept": -1.92,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.540},
      {"input": "female", "type": "linear", "coef": 0.030},
      {"input": "wfns45", "type": "linear", "coef": 1.585},
      {"input": "fisher34", "type": "linear", "coef": 0.423},
      {"input": "ct_ivh", "type": "linear", "coef": 0.465},
      {"input": "ct_ich", "type": "linear", "coef": 0.301},
      {"input": "htn", "type": "linear", "coef": 0.242},
      {"input": "surgery", "type": "linear", "coef": -1.462},
      {"input": "urban", "type": "linear", "coef": -0.023},
      {"input": "farmer", "type": "linear", "coef": 0.076},
      {"input": "l1", "type": "linear", "coef": -0.014},
      {"input": "l2", "type": "linear", "coef": 0.002},
      {"input": "l3", "type": "linear", "coef": -0.002},
      {"input": "l4", "type": "linear", "coef": 0.011},
      {"input": "l5", "type": "linear", "coef": -0.022},
      {"input": "l6", "type": "linear", "coef": -0.008},
      {"input": "l7", "type": "linear", "coef": -0.011},
      {"input": "l8", "type": "linear", "coef": -0.014},
      {"input": "l9", "type": "linear", "coef": -0.005},
      {"input": "l10", "type": "linear", "coef": -0.004}
    ],
    "interactions": []
  },
  "confidence_trained": 0.98
}
```