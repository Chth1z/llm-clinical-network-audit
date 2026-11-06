This is a **context-dependent risk function**, not a set of fixed risk-factor coefficients. For a continuous input \(x_i\), its effect on log-odds is
\[
\sum_j W_{2j}W_{1ji}\operatorname{sech}^2(W_{1j}x+b_{1j}).
\]
Thus, even large weights can have little effect when their hidden units are saturated, and competing units can reverse an input’s effect.

The strongest broad patterns are higher risk with severe WFNS grade and older age, and lower risk with treatment. **The laboratory relationships are not simply monotonic.** For example, set age to 60, every binary indicator to zero, and every laboratory value except `l3` to 5. The network predicts approximately **9.5%, 3.2%, and 26.1%** mortality at `l3` values **0, 3, and 10**, respectively.

Below is a weight-derived spline/pairwise approximation—not an exact reduction or an empirically validated fit. Directions and ranks summarize approximate behavior with balanced binary indicators, laboratories spanning 0–10, and age centered at 60 with SD 15; they are not registry-specific importance estimates. Repeated-input interactions implement squares. Treatment’s association is not a causal effect; moreover, treatment *during admission* may not be available at admission.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "large; nonlinear", "rank": 3},
    "female": {"direction": "no clear effect", "size": "small; context-dependent", "rank": 16},
    "wfns45": {"direction": "increases risk", "size": "very large", "rank": 1},
    "fisher34": {"direction": "increases risk", "size": "moderate", "rank": 6},
    "ct_ivh": {"direction": "increases risk", "size": "moderate", "rank": 5},
    "ct_ich": {"direction": "increases risk", "size": "moderate", "rank": 7},
    "htn": {"direction": "increases risk", "size": "small to moderate", "rank": 8},
    "surgery": {"direction": "decreases risk", "size": "very large", "rank": 2},
    "urban": {"direction": "decreases risk", "size": "small average; mixed locally", "rank": 14},
    "farmer": {"direction": "no clear effect", "size": "context-dependent sign reversal", "rank": 19},
    "l1": {"direction": "no clear effect", "size": "modest; nonlinear", "rank": 9},
    "l2": {"direction": "no clear effect", "size": "small average effect", "rank": 20},
    "l3": {"direction": "no clear effect", "size": "large; nonmonotonic", "rank": 4},
    "l4": {"direction": "no clear effect", "size": "small; conditional", "rank": 18},
    "l5": {"direction": "no clear effect", "size": "mostly conditional interactions", "rank": 10},
    "l6": {"direction": "no clear effect", "size": "mostly conditional interactions", "rank": 11},
    "l7": {"direction": "no clear effect", "size": "small; conditional", "rank": 17},
    "l8": {"direction": "no clear effect", "size": "mostly conditional interactions", "rank": 12},
    "l9": {"direction": "no clear effect", "size": "mostly conditional interactions", "rank": 13},
    "l10": {"direction": "no clear effect", "size": "small average; nonlinear", "rank": 15}
  },
  "unexpected": [
    {
      "inputs": ["l3"],
      "description": "A context-dependent trough rather than a uniformly harmful or protective effect. With age_c=0, all binary indicators=0, and all other laboratories=5, predicted probabilities at l3=0, 3, and 10 are approximately 0.095, 0.032, and 0.261.",
      "where": "In that profile, the trough is around l3=3-4 on its 0-10 scale; its position changes with the other inputs."
    },
    {
      "inputs": ["age_c", "farmer"],
      "description": "Farmer status can reverse direction with age. With all other binary indicators=0 and all laboratories=5, changing farmer from 0 to 1 changes log-odds by approximately +0.27 at age 60 but -0.64 at age 80.",
      "where": "The sign changes between age_c=0 and age_c=2 in that profile."
    }
  ],
  "surrogate": {
    "intercept": -4.34082,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.30147},
      {"input": "age_c", "type": "hinge", "knot": -3, "coef": 0.11},
      {"input": "age_c", "type": "hinge", "knot": -2, "coef": 0.126},
      {"input": "age_c", "type": "hinge", "knot": -1, "coef": 0.121},
      {"input": "age_c", "type": "hinge", "knot": 0, "coef": 0.071},
      {"input": "age_c", "type": "hinge", "knot": 1, "coef": 0.004},
      {"input": "age_c", "type": "hinge", "knot": 2, "coef": -0.068},
      {"input": "age_c", "type": "hinge", "knot": 3, "coef": -0.114},
      {"input": "female", "type": "linear", "coef": 0.51166},
      {"input": "wfns45", "type": "linear", "coef": 2.80367},
      {"input": "fisher34", "type": "linear", "coef": 0.43215},
      {"input": "ct_ivh", "type": "linear", "coef": 0.67216},
      {"input": "ct_ich", "type": "linear", "coef": 0.51729},
      {"input": "htn", "type": "linear", "coef": 0.36973},
      {"input": "surgery", "type": "linear", "coef": -1.79791},
      {"input": "urban", "type": "linear", "coef": -0.43474},
      {"input": "farmer", "type": "linear", "coef": -0.09138},
      {"input": "l1", "type": "linear", "coef": 0.15063},
      {"input": "l2", "type": "linear", "coef": -0.01155},
      {"input": "l3", "type": "linear", "coef": 0.26199},
      {"input": "l3", "type": "hinge", "knot": 1, "coef": -0.06},
      {"input": "l3", "type": "hinge", "knot": 2, "coef": -0.478},
      {"input": "l3", "type": "hinge", "knot": 3, "coef": 0.056},
      {"input": "l3", "type": "hinge", "knot": 4, "coef": 0.076},
      {"input": "l3", "type": "hinge", "knot": 5, "coef": 0.13442},
      {"input": "l3", "type": "hinge", "knot": 6, "coef": 0.059},
      {"input": "l3", "type": "hinge", "knot": 7, "coef": 0.043},
      {"input": "l3", "type": "hinge", "knot": 8, "coef": 0.09732},
      {"input": "l3", "type": "hinge", "knot": 9, "coef": 0.014},
      {"input": "l4", "type": "linear", "coef": 0.05083},
      {"input": "l5", "type": "linear", "coef": 0.19025},
      {"input": "l6", "type": "linear", "coef": -0.13378},
      {"input": "l7", "type": "linear", "coef": 0.05815},
      {"input": "l8", "type": "linear", "coef": -0.16695},
      {"input": "l9", "type": "linear", "coef": 0.0695},
      {"input": "l10", "type": "linear", "coef": -0.11831}
    ],
    "interactions": [
      {"inputs": ["l1", "l1"], "coef": -0.0049955},
      {"inputs": ["l2", "l2"], "coef": 0.004093},
      {"inputs": ["l4", "l4"], "coef": 0.003581},
      {"inputs": ["l5", "l5"], "coef": -0.0033755},
      {"inputs": ["l6", "l6"], "coef": 0.0028275},
      {"inputs": ["l7", "l7"], "coef": -0.0013815},
      {"inputs": ["l8", "l8"], "coef": 0.004666},
      {"inputs": ["l9", "l9"], "coef": 0.0009105},
      {"inputs": ["l10", "l10"], "coef": 0.004098},

      {"inputs": ["l3", "age_c"], "coef": -0.04749},
      {"inputs": ["l3", "age_c"], "knots": [2, -5], "coef": 0.0537},
      {"inputs": ["l3", "age_c"], "knots": [5, -5], "coef": -0.002595},
      {"inputs": ["l3", "age_c"], "knots": [8, -5], "coef": -0.005615},

      {"inputs": ["l3", "female"], "coef": -0.172886},
      {"inputs": ["l3", "female"], "knots": [2, 0], "coef": 0.128527},
      {"inputs": ["l3", "female"], "knots": [5, 0], "coef": 0.067231},
      {"inputs": ["l3", "female"], "knots": [8, 0], "coef": 0.006654},

      {"inputs": ["l3", "wfns45"], "coef": -0.019503},
      {"inputs": ["l3", "wfns45"], "knots": [2, 0], "coef": 0.006193},
      {"inputs": ["l3", "wfns45"], "knots": [5, 0], "coef": -0.056792},
      {"inputs": ["l3", "wfns45"], "knots": [8, 0], "coef": -0.033578},

      {"inputs": ["l3", "fisher34"], "coef": 0.012761},
      {"inputs": ["l3", "fisher34"], "knots": [2, 0], "coef": 0.007433},
      {"inputs": ["l3", "fisher34"], "knots": [5, 0], "coef": -0.012377},
      {"inputs": ["l3", "fisher34"], "knots": [8, 0], "coef": -0.017065},

      {"inputs": ["l3", "ct_ivh"], "coef": -0.097523},
      {"inputs": ["l3", "ct_ivh"], "knots": [2, 0], "coef": 0.108182},
      {"inputs": ["l3", "ct_ivh"], "knots": [5, 0], "coef": 0.00228},
      {"inputs": ["l3", "ct_ivh"], "knots": [8, 0], "coef": -0.020228},

      {"inputs": ["l3", "ct_ich"], "coef": 0.017024},
      {"inputs": ["l3", "ct_ich"], "knots": [2, 0], "coef": -0.041556},
      {"inputs": ["l3", "ct_ich"], "knots": [5, 0], "coef": 0.011673},
      {"inputs": ["l3", "ct_ich"], "knots": [8, 0], "coef": 0.004878},

      {"inputs": ["l3", "htn"], "coef": -0.020804},
      {"inputs": ["l3", "htn"], "knots": [2, 0], "coef": 0.026539},
      {"inputs": ["l3", "htn"], "knots": [5, 0], "coef": -0.007022},
      {"inputs": ["l3", "htn"], "knots": [8, 0], "coef": -0.009438},

      {"inputs": ["l3", "surgery"], "coef": 0.11048},
      {"inputs": ["l3", "surgery"], "knots": [2, 0], "coef": -0.054734},
      {"inputs": ["l3", "surgery"], "knots": [5, 0], "coef": -0.002943},
      {"inputs": ["l3", "surgery"], "knots": [8, 0], "coef": 0.026988},

      {"inputs": ["l3", "urban"], "coef": 0.035657},
      {"inputs": ["l3", "urban"], "knots": [2, 0], "coef": 0.025273},
      {"inputs": ["l3", "urban"], "knots": [5, 0], "coef": -0.022614},
      {"inputs": ["l3", "urban"], "knots": [8, 0], "coef": -0.019855},

      {"inputs": ["l3", "farmer"], "coef": 0.017},
      {"inputs": ["l3", "farmer"], "knots": [2, 0], "coef": 0.012194},
      {"inputs": ["l3", "farmer"], "knots": [5, 0], "coef": -0.008045},
      {"inputs": ["l3", "farmer"], "knots": [8, 0], "coef": -0.0186},

      {"inputs": ["l3", "l1"], "coef": -0.012153},
      {"inputs": ["l3", "l1"], "knots": [2, 0], "coef": 0.00207},
      {"inputs": ["l3", "l1"], "knots": [5, 0], "coef": 0.010781},
      {"inputs": ["l3", "l1"], "knots": [8, 0], "coef": 0.001837},

      {"inputs": ["l3", "l2"], "coef": -0.02634},
      {"inputs": ["l3", "l2"], "knots": [2, 0], "coef": 0.026698},
      {"inputs": ["l3", "l2"], "knots": [5, 0], "coef": 0.000391},
      {"inputs": ["l3", "l2"], "knots": [8, 0], "coef": -0.00268},

      {"inputs": ["l3", "l4"], "coef": -0.028642},
      {"inputs": ["l3", "l4"], "knots": [2, 0], "coef": 0.02356},
      {"inputs": ["l3", "l4"], "knots": [5, 0], "coef": 0.006949},
      {"inputs": ["l3", "l4"], "knots": [8, 0], "coef": 0.000351},

      {"inputs": ["l3", "l5"], "coef": -0.06837},
      {"inputs": ["l3", "l5"], "knots": [2, 0], "coef": 0.050355},
      {"inputs": ["l3", "l5"], "knots": [5, 0], "coef": 0.024724},
      {"inputs": ["l3", "l5"], "knots": [8, 0], "coef": 0.001261},

      {"inputs": ["l3", "l6"], "coef": 0.061516},
      {"inputs": ["l3", "l6"], "knots": [2, 0], "coef": -0.047188},
      {"inputs": ["l3", "l6"], "knots": [5, 0], "coef": -0.022387},
      {"inputs": ["l3", "l6"], "knots": [8, 0], "coef": -0.002389},

      {"inputs": ["l3", "l7"], "coef": 0.004964},
      {"inputs": ["l3", "l7"], "knots": [2, 0], "coef": -0.013935},
      {"inputs": ["l3", "l7"], "knots": [5, 0], "coef": 0.000732},
      {"inputs": ["l3", "l7"], "knots": [8, 0], "coef": 0.00496},

      {"inputs": ["l3", "l8"], "coef": 0.036635},
      {"inputs": ["l3", "l8"], "knots": [2, 0], "coef": -0.014907},
      {"inputs": ["l3", "l8"], "knots": [5, 0], "coef": -0.01471},
      {"inputs": ["l3", "l8"], "knots": [8, 0], "coef": -0.006906},

      {"inputs": ["l3", "l9"], "coef": -0.018199},
      {"inputs": ["l3", "l9"], "knots": [2, 0], "coef": 0.004049},
      {"inputs": ["l3", "l9"], "knots": [5, 0], "coef": 0.00256},
      {"inputs": ["l3", "l9"], "knots": [8, 0], "coef": 0.003664},

      {"inputs": ["l3", "l10"], "coef": 0.021975},
      {"inputs": ["l3", "l10"], "knots": [2, 0], "coef": -0.009208},
      {"inputs": ["l3", "l10"], "knots": [5, 0], "coef": -0.015464},
      {"inputs": ["l3", "l10"], "knots": [8, 0], "coef": -0.000323},

      {"inputs": ["age_c", "female"], "coef": -0.02176},
      {"inputs": ["age_c", "wfns45"], "coef": -0.000186},
      {"inputs": ["age_c", "fisher34"], "coef": 0.012264},
      {"inputs": ["age_c", "ct_ivh"], "coef": -0.008069},
      {"inputs": ["age_c", "ct_ich"], "coef": -0.032101},
      {"inputs": ["age_c", "htn"], "coef": -0.02839},
      {"inputs": ["age_c", "surgery"], "coef": 0.061679},
      {"inputs": ["age_c", "urban"], "coef": 0.051083},
      {"inputs": ["age_c", "farmer"], "coef": -0.04407},
      {"inputs": ["age_c", "l1"], "coef": -0.006059},
      {"inputs": ["age_c", "l2"], "coef": -0.005524},
      {"inputs": ["age_c", "l4"], "coef": -0.010667},
      {"inputs": ["age_c", "l5"], "coef": 0.000859},
      {"inputs": ["age_c", "l6"], "coef": 0.002824},
      {"inputs": ["age_c", "l7"], "coef": 0.011302},
      {"inputs": ["age_c", "l8"], "coef": 0.001462},
      {"inputs": ["age_c", "l9"], "coef": -0.015805},
      {"inputs": ["age_c", "l10"], "coef": 0.001266},

      {"inputs": ["wfns45", "female"], "coef": -0.111454},
      {"inputs": ["wfns45", "fisher34"], "coef": 0.041538},
      {"inputs": ["wfns45", "ct_ivh"], "coef": 0.003714},
      {"inputs": ["wfns45", "ct_ich"], "coef": 0.017303},
      {"inputs": ["wfns45", "htn"], "coef": 0.002952},
      {"inputs": ["wfns45", "surgery"], "coef": -0.12472},
      {"inputs": ["wfns45", "urban"], "coef": 0.019001},
      {"inputs": ["wfns45", "farmer"], "coef": 0.020186},
      {"inputs": ["wfns45", "l1"], "coef": -0.04339},
      {"inputs": ["wfns45", "l2"], "coef": 0.01217},
      {"inputs": ["wfns45", "l4"], "coef": -0.021668},
      {"inputs": ["wfns45", "l5"], "coef": -0.026349},
      {"inputs": ["wfns45", "l6"], "coef": -0.001728},
      {"inputs": ["wfns45", "l7"], "coef": -0.018452},
      {"inputs": ["wfns45", "l8"], "coef": 0.003225},
      {"inputs": ["wfns45", "l9"], "coef": -0.018521},
      {"inputs": ["wfns45", "l10"], "coef": -0.000645},

      {"inputs": ["surgery", "female"], "coef": 0.020371},
      {"inputs": ["surgery", "fisher34"], "coef": -0.034205},
      {"inputs": ["surgery", "ct_ivh"], "coef": -0.035122},
      {"inputs": ["surgery", "ct_ich"], "coef": -0.160007},
      {"inputs": ["surgery", "htn"], "coef": -0.050423},
      {"inputs": ["surgery", "urban"], "coef": 0.130071},
      {"inputs": ["surgery", "farmer"], "coef": -0.065572},
      {"inputs": ["surgery", "l1"], "coef": -0.00233},
      {"inputs": ["surgery", "l2"], "coef": 0.007654},
      {"inputs": ["surgery", "l4"], "coef": -0.006557},
      {"inputs": ["surgery", "l5"], "coef": 0.017452},
      {"inputs": ["surgery", "l6"], "coef": -0.007569},
      {"inputs": ["surgery", "l7"], "coef": -0.017599},
      {"inputs": ["surgery", "l8"], "coef": 0.004075},
      {"inputs": ["surgery", "l9"], "coef": -0.021439},
      {"inputs": ["surgery", "l10"], "coef": -0.008074}
    ]
  },
  "confidence_trained": 0.96
}
```