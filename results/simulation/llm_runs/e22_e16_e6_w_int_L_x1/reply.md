**Reference used:** independent ages 18–90, balanced binary inputs, and uniform laboratory values 0–10; ranks describe approximate importance over this reference.

The weights produce a score dominated by **older age, poor WFNS grade, and absence of treatment**. Fisher grade, IVH, ICH, and hypertension contribute smaller increases. Sex, urban residence, and farming have comparatively little influence.

The notable laboratory pattern is **positive coupling between l5 and l8**: their effects depend on each other, rather than acting as independent risk factors. Several other laboratories have small, curved contributions.

Below is a low-order analytic approximation, expressed using linear splines—not a refit to patient outcomes. Its knots approximate smooth curvature, not actual network thresholds. At age 60, all binary inputs zero, and all laboratories 5, the network and surrogate both give approximately **14%**. Because `surgery` describes treatment during the admission, this is a treatment-conditioned score.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "~1.8-fold odds per decade", "rank": 1},
    "female": {"direction": "no clear effect", "size": "negligible average contribution", "rank": 20},
    "wfns45": {"direction": "increases risk", "size": "~7.4-fold odds", "rank": 2},
    "fisher34": {"direction": "increases risk", "size": "~1.6-fold odds", "rank": 6},
    "ct_ivh": {"direction": "increases risk", "size": "~1.6-fold odds", "rank": 7},
    "ct_ich": {"direction": "increases risk", "size": "~1.5-fold odds", "rank": 8},
    "htn": {"direction": "increases risk", "size": "~1.4-fold odds", "rank": 9},
    "surgery": {"direction": "decreases risk", "size": "~0.15-fold odds", "rank": 3},
    "urban": {"direction": "no clear effect", "size": "small positive average contribution", "rank": 14},
    "farmer": {"direction": "no clear effect", "size": "small positive average contribution", "rank": 17},
    "l1": {"direction": "no clear effect", "size": "small, curved contribution", "rank": 15},
    "l2": {"direction": "no clear effect", "size": "small negative average contribution", "rank": 12},
    "l3": {"direction": "no clear effect", "size": "very small, curved contribution", "rank": 18},
    "l4": {"direction": "no clear effect", "size": "small mid-range elevation", "rank": 11},
    "l5": {"direction": "increases risk", "size": "moderate; depends on l8", "rank": 4},
    "l6": {"direction": "no clear effect", "size": "small mid-range elevation", "rank": 16},
    "l7": {"direction": "no clear effect", "size": "small mid-range elevation", "rank": 10},
    "l8": {"direction": "increases risk", "size": "moderate; depends on l5", "rank": 5},
    "l9": {"direction": "no clear effect", "size": "very small contribution", "rank": 19},
    "l10": {"direction": "no clear effect", "size": "small mid-range elevation", "rank": 13}
  },
  "unexpected": [
    {
      "inputs": ["l5", "l8"],
      "description": "Positive interaction: increasing either laboratory generally has a more positive effect when the other is high. At low partner values, the marginal effect can reverse.",
      "where": "Across 0–10. Approximate slope reversals: l5's effect near l8=0.7 when l5 is around 5; l8's effect near l5=2.1 when l8 is around 5."
    },
    {
      "inputs": ["l1", "l3", "l4", "l6", "l7", "l10"],
      "description": "Small non-monotonic contributions, approximated by shallow mid-range maxima rather than consistent increases or decreases.",
      "where": "Broadly laboratory values 4–7; smooth bends rather than hard thresholds."
    }
  ],
  "surrogate": {
    "intercept": -3.086,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.582},
      {"input": "female", "type": "linear", "coef": 0.003},
      {"input": "wfns45", "type": "linear", "coef": 2.000},
      {"input": "fisher34", "type": "linear", "coef": 0.497},
      {"input": "ct_ivh", "type": "linear", "coef": 0.481},
      {"input": "ct_ich", "type": "linear", "coef": 0.403},
      {"input": "htn", "type": "linear", "coef": 0.366},
      {"input": "surgery", "type": "linear", "coef": -1.895},
      {"input": "urban", "type": "linear", "coef": 0.081},
      {"input": "farmer", "type": "linear", "coef": 0.059},
      {"input": "l1", "type": "linear", "coef": 0.0367},
      {"input": "l2", "type": "linear", "coef": -0.0153},
      {"input": "l3", "type": "linear", "coef": 0.0229},
      {"input": "l4", "type": "linear", "coef": 0.0440},
      {"input": "l5", "type": "linear", "coef": 0.0297},
      {"input": "l6", "type": "linear", "coef": 0.0371},
      {"input": "l7", "type": "linear", "coef": 0.0636},
      {"input": "l8", "type": "linear", "coef": -0.0471},
      {"input": "l9", "type": "linear", "coef": 0.0007},
      {"input": "l10", "type": "linear", "coef": 0.0438},
      {"input": "l1", "type": "hinge", "knot": 2, "coef": -0.0133},
      {"input": "l1", "type": "hinge", "knot": 4, "coef": -0.0133},
      {"input": "l1", "type": "hinge", "knot": 6, "coef": -0.0133},
      {"input": "l1", "type": "hinge", "knot": 8, "coef": -0.0133},
      {"input": "l3", "type": "hinge", "knot": 2, "coef": -0.0092},
      {"input": "l3", "type": "hinge", "knot": 4, "coef": -0.0092},
      {"input": "l3", "type": "hinge", "knot": 6, "coef": -0.0092},
      {"input": "l3", "type": "hinge", "knot": 8, "coef": -0.0092},
      {"input": "l4", "type": "hinge", "knot": 2, "coef": -0.0244},
      {"input": "l4", "type": "hinge", "knot": 4, "coef": -0.0244},
      {"input": "l4", "type": "hinge", "knot": 6, "coef": -0.0244},
      {"input": "l4", "type": "hinge", "knot": 8, "coef": -0.0244},
      {"input": "l5", "type": "hinge", "knot": 2, "coef": -0.0251},
      {"input": "l5", "type": "hinge", "knot": 4, "coef": -0.0251},
      {"input": "l5", "type": "hinge", "knot": 6, "coef": -0.0251},
      {"input": "l5", "type": "hinge", "knot": 8, "coef": -0.0251},
      {"input": "l6", "type": "hinge", "knot": 2, "coef": -0.0198},
      {"input": "l6", "type": "hinge", "knot": 4, "coef": -0.0198},
      {"input": "l6", "type": "hinge", "knot": 6, "coef": -0.0198},
      {"input": "l6", "type": "hinge", "knot": 8, "coef": -0.0198},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": -0.0281},
      {"input": "l7", "type": "hinge", "knot": 4, "coef": -0.0281},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": -0.0281},
      {"input": "l7", "type": "hinge", "knot": 8, "coef": -0.0281},
      {"input": "l8", "type": "hinge", "knot": 2, "coef": -0.0078},
      {"input": "l8", "type": "hinge", "knot": 4, "coef": -0.0078},
      {"input": "l8", "type": "hinge", "knot": 6, "coef": -0.0078},
      {"input": "l8", "type": "hinge", "knot": 8, "coef": -0.0078},
      {"input": "l9", "type": "hinge", "knot": 2, "coef": -0.0032},
      {"input": "l9", "type": "hinge", "knot": 4, "coef": -0.0032},
      {"input": "l9", "type": "hinge", "knot": 6, "coef": -0.0032},
      {"input": "l9", "type": "hinge", "knot": 8, "coef": -0.0032},
      {"input": "l10", "type": "hinge", "knot": 2, "coef": -0.0181},
      {"input": "l10", "type": "hinge", "knot": 4, "coef": -0.0181},
      {"input": "l10", "type": "hinge", "knot": 6, "coef": -0.0181},
      {"input": "l10", "type": "hinge", "knot": 8, "coef": -0.0181}
    ],
    "interactions": [
      {"inputs": ["l5", "l8"], "coef": 0.030}
    ]
  },
  "confidence_trained": 0.999
}
```