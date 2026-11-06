The network is **not a conventional monotone risk score**. Its strongest features are:

- **An age transition:** unit 3 changes its contribution by 2.428 log-odds across a relatively narrow age interval. With all binary inputs zero and `l7=5`, its centre is age **67.8 years**. Before this transition, increasing age can *lower* predicted risk.
- **Competing laboratory effects:** increasing `l7` raises risk through unit 5 but lowers it through units 1, 2, 3 and 8. Their different transition locations produce substantial age-dependent reversals.
- WFNS 4–5 generally increases risk and surgery decreases it, but their effects depend on the other inputs. Surgery is actually recorded **during admission**, so its association is neither an admission-only predictor nor a causal treatment effect.

A particularly faithful simplification is to **remove units 4 and 7, retain the other six units unchanged, and replace the output intercept with −0.6372**. For ages 18–100 and the supplied input ranges, this changes probability by less than approximately **0.006**, using bounds on those two units.

The JSON supplies a more interpretable, but less faithful, analytic hinge/product approximation, oriented toward ages 30–90 and broadly varying inputs. It has not been numerically validated. Moving thresholds cannot be represented exactly by the permitted terms; importance rankings are consequently approximate and distribution-dependent.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "large overall; distinctly nonmonotone",
      "rank": 1
    },
    "female": {
      "direction": "no clear effect",
      "size": "small overall; localized age effects",
      "rank": 11
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "large",
      "rank": 2
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "moderate; context dependent",
      "rank": 7
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "moderate; context dependent",
      "rank": 5
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "small-to-moderate; localized reversals",
      "rank": 8
    },
    "htn": {
      "direction": "increases risk",
      "size": "moderate overall",
      "rank": 6
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "large",
      "rank": 3
    },
    "urban": {
      "direction": "no clear effect",
      "size": "small overall; mixed signs",
      "rank": 10
    },
    "farmer": {
      "direction": "no clear effect",
      "size": "small average; context dependent",
      "rank": 9
    },
    "l7": {
      "direction": "no clear effect",
      "size": "large locally; age-dependent reversals",
      "rank": 4
    }
  },
  "interactions": [
    "Age and l7 interact nonlinearly: their opposing transitions cannot be summarized by one constant laboratory effect.",
    "WFNS and surgery share several hidden units, so their combined log-odds effect is not additive.",
    "Female sex, WFNS, CT findings and other inputs move the location of the dominant age transition.",
    "CT findings and hypertension modify WFNS and surgery contrasts through hidden-unit saturation.",
    "Urban residence and farmer occupation have context-dependent effects rather than uniformly protective or harmful associations."
  ],
  "unexpected": [
    {
      "inputs": ["age_c"],
      "description": "Predicted risk can decrease with age before rising sharply in the late sixties. With all binary inputs zero and l7=5, approximate probabilities at ages 40, 60 and 70 are 0.057, 0.030 and 0.096.",
      "where": "Unit 3 is centred at age_c=(2.13-0.4133*female-0.3564*wfns45-0.1074*fisher34-0.1951*ct_ivh+0.2096*ct_ich-0.058*htn+0.03992*surgery+0.1704*urban+0.1307*farmer+0.09957*l7)/3.388. With all binary inputs zero and l7=5, this is age_c=0.776, or age 67.8."
    },
    {
      "inputs": ["l7", "age_c"],
      "description": "The laboratory relationship changes sign and is nonmonotone. With all binary inputs zero, probabilities at l7=0,5,10 are approximately 0.015,0.030,0.025 at age 60, but 0.604,0.127,0.134 at age 80.",
      "where": "With all binary inputs zero, the opposing unit-5 and unit-8 transitions are centred at l7=2.764+1.830*age_c and l7=-3.686+4.105*age_c respectively. These are component centres, not exact extrema of total risk."
    },
    {
      "inputs": ["female", "ct_ich", "age_c"],
      "description": "Female sex moves the dominant age transition earlier, whereas intracerebral haemorrhage moves it later; these localized effects differ from a constant sex or haemorrhage coefficient.",
      "where": "Female sex shifts the unit-3 centre about 1.22 years earlier; ct_ich shifts it about 0.62 years later. Around the otherwise-zero, l7=5 reference, the centres become approximately ages 66.5 and 68.4 respectively."
    }
  ],
  "surrogate": {
    "intercept": -3.39726,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": -0.2254},
      {"input": "female", "type": "linear", "coef": -0.1891},
      {"input": "wfns45", "type": "linear", "coef": 1.48645},
      {"input": "fisher34", "type": "linear", "coef": 0.49485},
      {"input": "ct_ivh", "type": "linear", "coef": 0.32195},
      {"input": "ct_ich", "type": "linear", "coef": 0.25135},
      {"input": "htn", "type": "linear", "coef": 0.25645},
      {"input": "surgery", "type": "linear", "coef": -1.5999},
      {"input": "urban", "type": "linear", "coef": 0.3207},
      {"input": "farmer", "type": "linear", "coef": -0.00455},
      {"input": "l7", "type": "linear", "coef": -0.020133},
      {"input": "age_c", "type": "hinge", "knot": -3, "coef": -0.01692},
      {"input": "age_c", "type": "hinge", "knot": -2, "coef": -0.02718},
      {"input": "age_c", "type": "hinge", "knot": -1, "coef": -0.0416},
      {"input": "age_c", "type": "hinge", "knot": -0.5, "coef": 0.0794},
      {"input": "age_c", "type": "hinge", "knot": 0, "coef": 0.37639},
      {"input": "age_c", "type": "hinge", "knot": 0.2, "coef": 0.7843},
      {"input": "age_c", "type": "hinge", "knot": 0.4, "coef": 1.42985},
      {"input": "age_c", "type": "hinge", "knot": 0.5, "coef": 0.13081},
      {"input": "age_c", "type": "hinge", "knot": 0.6, "coef": 0.8545},
      {"input": "age_c", "type": "hinge", "knot": 0.8, "coef": -1.007},
      {"input": "age_c", "type": "hinge", "knot": 1, "coef": -1.17054},
      {"input": "age_c", "type": "hinge", "knot": 1.2, "coef": -0.795},
      {"input": "age_c", "type": "hinge", "knot": 1.5, "coef": -0.0759},
      {"input": "age_c", "type": "hinge", "knot": 2, "coef": 0.05794},
      {"input": "age_c", "type": "hinge", "knot": 2.5, "coef": -0.02317},
      {"input": "age_c", "type": "hinge", "knot": 3, "coef": -0.13432},
      {"input": "age_c", "type": "hinge", "knot": 3.5, "coef": -0.19986},
      {"input": "l7", "type": "hinge", "knot": 1, "coef": 0.015465},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": 0.009614},
      {"input": "l7", "type": "hinge", "knot": 3, "coef": 0.000134},
      {"input": "l7", "type": "hinge", "knot": 4, "coef": -0.009202},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": -0.017752},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": -0.018664},
      {"input": "l7", "type": "hinge", "knot": 7, "coef": -0.012528},
      {"input": "l7", "type": "hinge", "knot": 8, "coef": -0.004395},
      {"input": "l7", "type": "hinge", "knot": 9, "coef": 0.001533}
    ],
    "interactions": [
      {"inputs": ["age_c", "l7"], "coef": -0.0157},
      {"inputs": ["age_c", "female"], "coef": -0.0285},
      {"inputs": ["age_c", "wfns45"], "coef": 0.0035},
      {"inputs": ["age_c", "fisher34"], "coef": 0.0194},
      {"inputs": ["age_c", "ct_ivh"], "coef": 0.0458},
      {"inputs": ["age_c", "ct_ich"], "coef": 0.0185},
      {"inputs": ["age_c", "htn"], "coef": 0.0222},
      {"inputs": ["age_c", "surgery"], "coef": -0.0021},
      {"inputs": ["age_c", "urban"], "coef": -0.0332},
      {"inputs": ["age_c", "farmer"], "coef": -0.0331},
      {"inputs": ["l7", "female"], "coef": 0.0155},
      {"inputs": ["l7", "wfns45"], "coef": 0.0463},
      {"inputs": ["l7", "fisher34"], "coef": -0.0128},
      {"inputs": ["l7", "ct_ivh"], "coef": 0.0192},
      {"inputs": ["l7", "ct_ich"], "coef": 0.0005},
      {"inputs": ["l7", "htn"], "coef": 0.018},
      {"inputs": ["l7", "surgery"], "coef": -0.0259},
      {"inputs": ["l7", "urban"], "coef": -0.0202},
      {"inputs": ["l7", "farmer"], "coef": -0.0041},
      {"inputs": ["female", "wfns45"], "coef": 0.0272},
      {"inputs": ["female", "fisher34"], "coef": 0.0253},
      {"inputs": ["female", "ct_ivh"], "coef": 0.0236},
      {"inputs": ["female", "ct_ich"], "coef": 0.0138},
      {"inputs": ["female", "htn"], "coef": 0.0933},
      {"inputs": ["female", "surgery"], "coef": 0.0082},
      {"inputs": ["female", "urban"], "coef": -0.0387},
      {"inputs": ["female", "farmer"], "coef": 0.0599},
      {"inputs": ["wfns45", "fisher34"], "coef": -0.1557},
      {"inputs": ["wfns45", "ct_ivh"], "coef": -0.1335},
      {"inputs": ["wfns45", "ct_ich"], "coef": 0.0457},
      {"inputs": ["wfns45", "htn"], "coef": -0.157},
      {"inputs": ["wfns45", "surgery"], "coef": 0.1644},
      {"inputs": ["wfns45", "urban"], "coef": 0.06},
      {"inputs": ["wfns45", "farmer"], "coef": 0.0828},
      {"inputs": ["fisher34", "ct_ivh"], "coef": -0.0338},
      {"inputs": ["fisher34", "ct_ich"], "coef": -0.0102},
      {"inputs": ["fisher34", "htn"], "coef": -0.0504},
      {"inputs": ["fisher34", "surgery"], "coef": 0.124},
      {"inputs": ["fisher34", "urban"], "coef": -0.0243},
      {"inputs": ["fisher34", "farmer"], "coef": -0.0028},
      {"inputs": ["ct_ivh", "ct_ich"], "coef": 0.0243},
      {"inputs": ["ct_ivh", "htn"], "coef": 0.0041},
      {"inputs": ["ct_ivh", "surgery"], "coef": 0.0881},
      {"inputs": ["ct_ivh", "urban"], "coef": -0.0151},
      {"inputs": ["ct_ivh", "farmer"], "coef": 0.0478},
      {"inputs": ["ct_ich", "htn"], "coef": 0.0291},
      {"inputs": ["ct_ich", "surgery"], "coef": -0.0532},
      {"inputs": ["ct_ich", "urban"], "coef": -0.0164},
      {"inputs": ["ct_ich", "farmer"], "coef": 0.0202},
      {"inputs": ["htn", "surgery"], "coef": 0.1558},
      {"inputs": ["htn", "urban"], "coef": -0.0882},
      {"inputs": ["htn", "farmer"], "coef": 0.098},
      {"inputs": ["surgery", "urban"], "coef": -0.0775},
      {"inputs": ["surgery", "farmer"], "coef": -0.0358},
      {"inputs": ["urban", "farmer"], "coef": -0.0598}
    ]
  },
  "confidence_trained": 0.97
}
```