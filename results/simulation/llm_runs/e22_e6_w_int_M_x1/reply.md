The strongest broad signals are **higher risk with WFNS 4–5 and older age, and lower risk with treatment**. IVH, ICH, Fisher grade and hypertension also contribute positively. These are model associations—not causal effects. In particular, `surgery` describes treatment **during admission**, so it is not genuinely an admission-only predictor.

The laboratories are not simply negligible noise: their contributions can cancel in an average linear summary while still changing predictions through nonlinear combinations. For example, with age 60, binary inputs zero and the other laboratories at 5, first-layer unit 18 computes  
\(\tanh(1.32427-0.3521\,l5-0.405\,l8)\). Its transition therefore depends on a **combination** of two laboratories, not an individual cutoff. Its contribution must also be combined with the other units.

**Limitations:** the surrogate below is a rough analytic approximation, not a numerically fitted or validated distillation; I cannot claim a measured prediction error. Its reference is ages 30–90, balanced binary inputs and independent laboratory values spanning 0–10—not the registry’s unknown distribution. Directions describe predominant trends, ranks are approximate, and the hinge knots are approximation grid points, not discovered clinical thresholds.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "moderate per decade", "rank": 3},
    "female": {"direction": "no clear effect", "size": "very weak average effect", "rank": 20},
    "wfns45": {"direction": "increases risk", "size": "very large", "rank": 1},
    "fisher34": {"direction": "increases risk", "size": "moderate", "rank": 8},
    "ct_ivh": {"direction": "increases risk", "size": "moderate", "rank": 5},
    "ct_ich": {"direction": "increases risk", "size": "moderate", "rank": 7},
    "htn": {"direction": "increases risk", "size": "small", "rank": 9},
    "surgery": {"direction": "decreases risk", "size": "very large association", "rank": 2},
    "urban": {"direction": "decreases risk", "size": "small average effect", "rank": 10},
    "farmer": {"direction": "no clear effect", "size": "very weak negative tendency", "rank": 18},
    "l1": {"direction": "no clear effect", "size": "weak and nonlinear", "rank": 19},
    "l2": {"direction": "no clear effect", "size": "weak and nonlinear", "rank": 14},
    "l3": {"direction": "no clear effect", "size": "weak and nonlinear", "rank": 13},
    "l4": {"direction": "decreases risk", "size": "weak average tendency", "rank": 11},
    "l5": {"direction": "increases risk", "size": "moderate, background dependent", "rank": 6},
    "l6": {"direction": "no clear effect", "size": "weak and nonlinear", "rank": 16},
    "l7": {"direction": "no clear effect", "size": "weak and nonlinear", "rank": 17},
    "l8": {"direction": "increases risk", "size": "largest laboratory trend", "rank": 4},
    "l9": {"direction": "no clear effect", "size": "weak and interacting", "rank": 15},
    "l10": {"direction": "no clear effect", "size": "weak and nonlinear", "rank": 12}
  },
  "unexpected": [
    {
      "inputs": ["l5", "l8"],
      "description": "These laboratories jointly control an oblique nonlinear transition. One hidden unit decreases as their weighted sum increases; other pathways oppose or reinforce this, so its transition is not itself a mortality-risk cutoff.",
      "where": "At age_c=0, all binary inputs=0 and other laboratories=5, first-layer unit 18 crosses zero when 0.3521*l5 + 0.405*l8 = 1.32427. Changing other inputs moves this boundary."
    },
    {
      "inputs": ["l1", "l2", "l3", "l6", "l7", "l9", "l10"],
      "description": "Small average linear effects do not imply that these inputs can be removed: they participate in nonlinear laboratory combinations and can modify the effects of other inputs.",
      "where": "Across the supplied 0–10 ranges; transitions depend on the other inputs rather than a universal single-variable threshold."
    }
  ],
  "surrogate": {
    "intercept": -2.79144,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.36196},
      {"input": "female", "type": "linear", "coef": -0.00326},
      {"input": "wfns45", "type": "linear", "coef": 1.49751},
      {"input": "fisher34", "type": "linear", "coef": 0.30368},
      {"input": "ct_ivh", "type": "linear", "coef": 0.45235},
      {"input": "ct_ich", "type": "linear", "coef": 0.35283},
      {"input": "htn", "type": "linear", "coef": 0.21924},
      {"input": "surgery", "type": "linear", "coef": -1.43577},
      {"input": "urban", "type": "linear", "coef": -0.15574},
      {"input": "farmer", "type": "linear", "coef": -0.03932},

      {"input": "l1", "type": "linear", "coef": 0.00747},
      {"input": "l1", "type": "hinge", "knot": 2.5, "coef": -0.01130},
      {"input": "l1", "type": "hinge", "knot": 5, "coef": -0.01130},
      {"input": "l1", "type": "hinge", "knot": 7.5, "coef": -0.01130},

      {"input": "l2", "type": "linear", "coef": 0.03136},
      {"input": "l2", "type": "hinge", "knot": 2.5, "coef": -0.02147},
      {"input": "l2", "type": "hinge", "knot": 5, "coef": -0.02147},
      {"input": "l2", "type": "hinge", "knot": 7.5, "coef": -0.02147},

      {"input": "l3", "type": "linear", "coef": 0.02902},
      {"input": "l3", "type": "hinge", "knot": 2.5, "coef": -0.02563},
      {"input": "l3", "type": "hinge", "knot": 5, "coef": -0.02563},
      {"input": "l3", "type": "hinge", "knot": 7.5, "coef": -0.02563},

      {"input": "l4", "type": "linear", "coef": 0.00619},
      {"input": "l4", "type": "hinge", "knot": 2.5, "coef": -0.02118},
      {"input": "l4", "type": "hinge", "knot": 5, "coef": -0.02118},
      {"input": "l4", "type": "hinge", "knot": 7.5, "coef": -0.02118},

      {"input": "l5", "type": "linear", "coef": 0.04172},
      {"input": "l5", "type": "hinge", "knot": 2.5, "coef": -0.01352},
      {"input": "l5", "type": "hinge", "knot": 5, "coef": -0.01352},
      {"input": "l5", "type": "hinge", "knot": 7.5, "coef": -0.01352},

      {"input": "l6", "type": "linear", "coef": 0.02427},
      {"input": "l6", "type": "hinge", "knot": 2.5, "coef": -0.01949},
      {"input": "l6", "type": "hinge", "knot": 5, "coef": -0.01949},
      {"input": "l6", "type": "hinge", "knot": 7.5, "coef": -0.01949},

      {"input": "l7", "type": "linear", "coef": 0.01516},
      {"input": "l7", "type": "hinge", "knot": 2.5, "coef": -0.01853},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": -0.01853},
      {"input": "l7", "type": "hinge", "knot": 7.5, "coef": -0.01853},

      {"input": "l8", "type": "linear", "coef": 0.11211},
      {"input": "l8", "type": "hinge", "knot": 2.5, "coef": -0.02174},
      {"input": "l8", "type": "hinge", "knot": 5, "coef": -0.02174},
      {"input": "l8", "type": "hinge", "knot": 7.5, "coef": -0.02174},

      {"input": "l9", "type": "linear", "coef": 0.02255},
      {"input": "l9", "type": "hinge", "knot": 2.5, "coef": -0.02004},
      {"input": "l9", "type": "hinge", "knot": 5, "coef": -0.02004},
      {"input": "l9", "type": "hinge", "knot": 7.5, "coef": -0.02004},

      {"input": "l10", "type": "linear", "coef": 0.04689},
      {"input": "l10", "type": "hinge", "knot": 2.5, "coef": -0.02660},
      {"input": "l10", "type": "hinge", "knot": 5, "coef": -0.02660},
      {"input": "l10", "type": "hinge", "knot": 7.5, "coef": -0.02660}
    ],
    "interactions": [
      {"inputs": ["l5", "l8"], "coef": 0.01136},
      {"inputs": ["l8", "l9"], "coef": -0.00380},
      {"inputs": ["l7", "l9"], "coef": 0.00278}
    ]
  },
  "confidence_trained": 0.98
}
```