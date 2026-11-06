The effects depend on the whole patient profile:
\[
\frac{\partial\text{log-odds}}{\partial x_i}
=\sum_j W_{2j}W_{1ji}\operatorname{sech}^2(W_{1j}x+b_{1j}).
\]
Thus, opposing pathways can cancel or become exposed as other units saturate. WFNS has positive contributions through 15 of 16 units; surgery has negative contributions through 15. Laboratory and sex effects are much less consistent.

For example, with age 60, laboratories all 5, and every indicator initially 0, the network predicts approximately **5.1%** mortality. Switching WFNS to 1 raises this to **42.3%**. Female sex lowers the first prediction but raises the second. These are properties of these weights, not medical assumptions.

The surrogate below is an **unvalidated analytical two-way approximation**, not an exact rewrite. Its approximate ranks concern averaged main effects, assuming independent uniform laboratories, balanced indicators, and age centred on 60 with SD about 21 years. They can substantially understate conditional laboratory importance. Repeated input names in interactions denote squares.

Despite the admission-input description, surgery records subsequent treatment: its association is neither an admission-only predictor nor a causal treatment effect. Coordinated clinical weights argue against scrambling, but cannot establish training provenance.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "large; saturating", "rank": 1},
    "female": {"direction": "no clear effect", "size": "small average; reverses", "rank": 20},
    "wfns45": {"direction": "increases risk", "size": "large", "rank": 2},
    "fisher34": {"direction": "increases risk", "size": "moderate", "rank": 6},
    "ct_ivh": {"direction": "increases risk", "size": "moderate", "rank": 4},
    "ct_ich": {"direction": "increases risk", "size": "moderate", "rank": 5},
    "htn": {"direction": "increases risk", "size": "small average", "rank": 10},
    "surgery": {"direction": "decreases risk", "size": "large; noncausal association", "rank": 3},
    "urban": {"direction": "decreases risk", "size": "small average", "rank": 9},
    "farmer": {"direction": "decreases risk", "size": "small average", "rank": 11},
    "l1": {"direction": "no clear effect", "size": "weak average; conditional", "rank": 14},
    "l2": {"direction": "decreases risk", "size": "weak average; conditional", "rank": 8},
    "l3": {"direction": "no clear effect", "size": "cancelling conditional effects", "rank": 18},
    "l4": {"direction": "no clear effect", "size": "cancelling conditional effects", "rank": 19},
    "l5": {"direction": "decreases risk", "size": "weak average; reversals", "rank": 7},
    "l6": {"direction": "no clear effect", "size": "weak average; reversals", "rank": 15},
    "l7": {"direction": "no clear effect", "size": "strong conditional reversals", "rank": 13},
    "l8": {"direction": "no clear effect", "size": "weak average; conditional", "rank": 16},
    "l9": {"direction": "decreases risk", "size": "weak average; conditional", "rank": 12},
    "l10": {"direction": "no clear effect", "size": "weak average; conditional", "rank": 17}
  },
  "unexpected": [
    {
      "inputs": ["female", "wfns45"],
      "description": "Sex changes direction with severity. Female versus male changes predicted mortality approximately from 5.1% to 4.6% with wfns45=0, but from 42.3% to 47.3% with wfns45=1.",
      "where": "age_c=0, all laboratories=5, and all indicators other than female and wfns45=0; compare female=0 with female=1."
    },
    {
      "inputs": ["l7", "wfns45"],
      "description": "l7 has a nonmonotonic, severity-dependent relationship, not a single protective or harmful coefficient. In the specified high-WFNS profile, risk initially rises, peaks near l7=1, then falls. Predictions at l7=0, 5 and 10 are approximately 57.7%, 42.3% and 19.2%. Around l7=5, its local direction is slightly positive with wfns45=0 but strongly negative with wfns45=1.",
      "where": "age_c=0, laboratories other than l7=5, all indicators other than wfns45=0. The peak near l7=1 applies to wfns45=1, not universally."
    },
    {
      "inputs": ["farmer"],
      "description": "Farmer occupation can lower predicted mortality rather than increase it. In the specified profile, switching farmer to 1 reduces log-odds by approximately 0.12, changing risk from about 5.1% to 4.6%. This is an encoded association, not occupational protection.",
      "where": "farmer changes from 0 to 1; age_c=0, all laboratories=5, and every other indicator=0."
    }
  ],
  "surrogate": {
    "intercept": -1.31395,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.231944},
      {"input": "female", "type": "linear", "coef": -0.01547},
      {"input": "wfns45", "type": "linear", "coef": 1.34571},
      {"input": "fisher34", "type": "linear", "coef": 0.39466},
      {"input": "ct_ivh", "type": "linear", "coef": 0.479715},
      {"input": "ct_ich", "type": "linear", "coef": 0.450775},
      {"input": "htn", "type": "linear", "coef": 0.1675},
      {"input": "surgery", "type": "linear", "coef": -1.052235},
      {"input": "urban", "type": "linear", "coef": -0.197965},
      {"input": "farmer", "type": "linear", "coef": -0.11289},
      {"input": "l1", "type": "linear", "coef": -0.062525},
      {"input": "l2", "type": "linear", "coef": -0.070625},
      {"input": "l3", "type": "linear", "coef": 0.03131},
      {"input": "l4", "type": "linear", "coef": 0.006965},
      {"input": "l5", "type": "linear", "coef": -0.079455},
      {"input": "l6", "type": "linear", "coef": -0.035745},
      {"input": "l7", "type": "linear", "coef": -0.010455},
      {"input": "l8", "type": "linear", "coef": -0.031325},
      {"input": "l9", "type": "linear", "coef": -0.03527},
      {"input": "l10", "type": "linear", "coef": 0.003735},
      {"input": "age_c", "type": "hinge", "knot": -2, "coef": 0.083016},
      {"input": "age_c", "type": "hinge", "knot": 0, "coef": 0.019332},
      {"input": "age_c", "type": "hinge", "knot": 2, "coef": -0.083016},
      {"input": "l1", "type": "hinge", "knot": 5, "coef": 0.0846},
      {"input": "l2", "type": "hinge", "knot": 5, "coef": 0.11525},
      {"input": "l3", "type": "hinge", "knot": 5, "coef": 0.0524},
      {"input": "l4", "type": "hinge", "knot": 5, "coef": 0.06405},
      {"input": "l5", "type": "hinge", "knot": 5, "coef": 0.0229},
      {"input": "l6", "type": "hinge", "knot": 5, "coef": 0.05145},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": 0.08125},
      {"input": "l8", "type": "hinge", "knot": 5, "coef": 0.08655},
      {"input": "l9", "type": "hinge", "knot": 5, "coef": 0.08535},
      {"input": "l10", "type": "hinge", "knot": 5, "coef": 0.08265}
    ],
    "interactions": [
      {"inputs": ["age_c", "wfns45"], "coef": 0.04422},
      {"inputs": ["age_c", "surgery"], "coef": -0.037978},
      {"inputs": ["wfns45", "female"], "coef": 0.0253},
      {"inputs": ["wfns45", "fisher34"], "coef": -0.012},
      {"inputs": ["wfns45", "ct_ivh"], "coef": -0.02771},
      {"inputs": ["wfns45", "ct_ich"], "coef": 0.01361},
      {"inputs": ["wfns45", "htn"], "coef": 0.0197},
      {"inputs": ["wfns45", "surgery"], "coef": -0.01446},
      {"inputs": ["wfns45", "urban"], "coef": 0.02545},
      {"inputs": ["wfns45", "farmer"], "coef": -0.01646},

      {"inputs": ["age_c", "l1"], "coef": 0.01177},
      {"inputs": ["age_c", "l2"], "coef": 0.00867},
      {"inputs": ["age_c", "l3"], "coef": -0.00156},
      {"inputs": ["age_c", "l4"], "coef": 0.00257},
      {"inputs": ["age_c", "l5"], "coef": 0.00444},
      {"inputs": ["age_c", "l6"], "coef": 0.00658},
      {"inputs": ["age_c", "l7"], "coef": -0.00021},
      {"inputs": ["age_c", "l8"], "coef": 0.00753},
      {"inputs": ["age_c", "l9"], "coef": 0.01253},
      {"inputs": ["age_c", "l10"], "coef": 0.00309},

      {"inputs": ["wfns45", "l1"], "coef": 0.00726},
      {"inputs": ["wfns45", "l2"], "coef": 0.02817},
      {"inputs": ["wfns45", "l3"], "coef": 0.01636},
      {"inputs": ["wfns45", "l4"], "coef": 0.01623},
      {"inputs": ["wfns45", "l5"], "coef": 0.00581},
      {"inputs": ["wfns45", "l6"], "coef": -0.00235},
      {"inputs": ["wfns45", "l7"], "coef": 0.00546},
      {"inputs": ["wfns45", "l8"], "coef": 0.03025},
      {"inputs": ["wfns45", "l9"], "coef": 0.03775},
      {"inputs": ["wfns45", "l10"], "coef": 0.01162},

      {"inputs": ["surgery", "l1"], "coef": -0.00723},
      {"inputs": ["surgery", "l2"], "coef": -0.03764},
      {"inputs": ["surgery", "l3"], "coef": -0.01278},
      {"inputs": ["surgery", "l4"], "coef": -0.0101},
      {"inputs": ["surgery", "l5"], "coef": -0.00442},
      {"inputs": ["surgery", "l6"], "coef": -0.00982},
      {"inputs": ["surgery", "l7"], "coef": -0.00771},
      {"inputs": ["surgery", "l8"], "coef": -0.01848},
      {"inputs": ["surgery", "l9"], "coef": -0.02381},
      {"inputs": ["surgery", "l10"], "coef": -0.01225},

      {"inputs": ["l1", "l1"], "coef": 0.00163},
      {"inputs": ["l2", "l2"], "coef": 0.0019},
      {"inputs": ["l3", "l3"], "coef": 0.00214},
      {"inputs": ["l5", "l5"], "coef": 0.00243},
      {"inputs": ["l6", "l6"], "coef": 0.00281},
      {"inputs": ["l7", "l7"], "coef": -0.00074},
      {"inputs": ["l8", "l8"], "coef": 0.00126},
      {"inputs": ["l9", "l9"], "coef": -0.00063},
      {"inputs": ["l10", "l10"], "coef": 0.0009},

      {"inputs": ["l1", "l2"], "coef": 0.00361},
      {"inputs": ["l1", "l5"], "coef": 0.0061},
      {"inputs": ["l1", "l10"], "coef": -0.00344},
      {"inputs": ["l3", "l6"], "coef": -0.00257},
      {"inputs": ["l3", "l7"], "coef": -0.00366},
      {"inputs": ["l3", "l10"], "coef": -0.00346},
      {"inputs": ["l4", "l5"], "coef": -0.00232},
      {"inputs": ["l5", "l6"], "coef": 0.00272},
      {"inputs": ["l5", "l9"], "coef": -0.00372},
      {"inputs": ["l7", "l9"], "coef": 0.00361},
      {"inputs": ["l9", "l10"], "coef": 0.00296},

      {"inputs": ["wfns45", "age_c"], "knots": [0, 0], "coef": -0.144},
      {"inputs": ["surgery", "age_c"], "knots": [0, 0], "coef": 0.105336},

      {"inputs": ["age_c", "l1"], "knots": [-6, 5], "coef": -0.0139},
      {"inputs": ["age_c", "l2"], "knots": [-6, 5], "coef": -0.0198},
      {"inputs": ["age_c", "l3"], "knots": [-6, 5], "coef": -0.0079},
      {"inputs": ["age_c", "l4"], "knots": [-6, 5], "coef": -0.011},
      {"inputs": ["age_c", "l5"], "knots": [-6, 5], "coef": -0.0036},
      {"inputs": ["age_c", "l6"], "knots": [-6, 5], "coef": -0.008},
      {"inputs": ["age_c", "l7"], "knots": [-6, 5], "coef": -0.0129},
      {"inputs": ["age_c", "l8"], "knots": [-6, 5], "coef": -0.0138},
      {"inputs": ["age_c", "l9"], "knots": [-6, 5], "coef": -0.0135},
      {"inputs": ["age_c", "l10"], "knots": [-6, 5], "coef": -0.0124},

      {"inputs": ["wfns45", "l1"], "knots": [0, 5], "coef": -0.034},
      {"inputs": ["wfns45", "l2"], "knots": [0, 5], "coef": -0.0594},
      {"inputs": ["wfns45", "l3"], "knots": [0, 5], "coef": -0.043},
      {"inputs": ["wfns45", "l4"], "knots": [0, 5], "coef": -0.029},
      {"inputs": ["wfns45", "l5"], "knots": [0, 5], "coef": -0.0215},
      {"inputs": ["wfns45", "l6"], "knots": [0, 5], "coef": -0.0456},
      {"inputs": ["wfns45", "l7"], "knots": [0, 5], "coef": -0.0466},
      {"inputs": ["wfns45", "l8"], "knots": [0, 5], "coef": -0.0399},
      {"inputs": ["wfns45", "l9"], "knots": [0, 5], "coef": -0.035},
      {"inputs": ["wfns45", "l10"], "knots": [0, 5], "coef": -0.0501},

      {"inputs": ["surgery", "l1"], "knots": [0, 5], "coef": 0.0316},
      {"inputs": ["surgery", "l2"], "knots": [0, 5], "coef": 0.0665},
      {"inputs": ["surgery", "l3"], "knots": [0, 5], "coef": 0.033},
      {"inputs": ["surgery", "l4"], "knots": [0, 5], "coef": 0.0329},
      {"inputs": ["surgery", "l5"], "knots": [0, 5], "coef": 0.0189},
      {"inputs": ["surgery", "l6"], "knots": [0, 5], "coef": 0.0387},
      {"inputs": ["surgery", "l7"], "knots": [0, 5], "coef": 0.0389},
      {"inputs": ["surgery", "l8"], "knots": [0, 5], "coef": 0.0324},
      {"inputs": ["surgery", "l9"], "knots": [0, 5], "coef": 0.0263},
      {"inputs": ["surgery", "l10"], "knots": [0, 5], "coef": 0.0336}
    ]
  },
  "confidence_trained": 0.95
}
```