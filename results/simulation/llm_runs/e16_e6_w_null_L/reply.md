**Reference used:** ages 18–90, equally likely binary inputs, and independent laboratory values uniformly distributed over 0–10.

Combining the paths through both nonlinear layers gives approximate average log-odds changes of **+0.54 per decade**, **+1.64 for WFNS 4–5**, and **−1.51 for treatment**. IVH contributes more than ICH. Female sex and urban residence have very small net effects despite their numerous nonzero weights.

The laboratory inputs’ linear contributions largely cancel. What remains includes weak curvature and interactions with clinical severity—not ten consistently harmful or protective laboratory measurements.

Below is a **weight-derived, second-order approximation**, using hinges to approximate smooth curvature. The hinge locations are approximation breakpoints, not thresholds explicitly present in the network. My estimated typical probability discrepancy is approximately **0.05** over the reference above; this is an analytical estimate.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "about +0.54 log-odds/decade", "rank": 1},
    "female": {"direction": "no clear effect", "size": "very small net effect", "rank": 19},
    "wfns45": {"direction": "increases risk", "size": "about +1.64 log-odds", "rank": 2},
    "fisher34": {"direction": "increases risk", "size": "about +0.30 log-odds", "rank": 5},
    "ct_ivh": {"direction": "increases risk", "size": "about +0.57 log-odds", "rank": 4},
    "ct_ich": {"direction": "increases risk", "size": "about +0.20 log-odds", "rank": 7},
    "htn": {"direction": "increases risk", "size": "about +0.24 log-odds", "rank": 6},
    "surgery": {"direction": "decreases risk", "size": "about -1.51 log-odds", "rank": 3},
    "urban": {"direction": "no clear effect", "size": "negligible average effect", "rank": 20},
    "farmer": {"direction": "increases risk", "size": "small average increase", "rank": 16},
    "l1": {"direction": "no clear effect", "size": "weak, context-dependent", "rank": 18},
    "l2": {"direction": "no clear effect", "size": "weak curved response", "rank": 13},
    "l3": {"direction": "no clear effect", "size": "weak U-shaped response", "rank": 17},
    "l4": {"direction": "increases risk", "size": "small average increase", "rank": 10},
    "l5": {"direction": "no clear effect", "size": "weak severity-dependent effect", "rank": 8},
    "l6": {"direction": "no clear effect", "size": "weak curved response", "rank": 15},
    "l7": {"direction": "no clear effect", "size": "weak curved response", "rank": 11},
    "l8": {"direction": "no clear effect", "size": "weak curved response", "rank": 12},
    "l9": {"direction": "no clear effect", "size": "weak U-shaped response", "rank": 9},
    "l10": {"direction": "no clear effect", "size": "weak, context-dependent", "rank": 14}
  },
  "unexpected": [
    {
      "inputs": ["l3", "l9"],
      "description": "The reference-averaged responses are shallow U-shapes rather than consistently increasing or decreasing risk.",
      "where": "Broad minima approximately around l3=5 and l9=6–7 on their 0–10 scales."
    },
    {
      "inputs": ["l5", "wfns45", "surgery"],
      "description": "Higher l5 modestly weakens both the positive WFNS contrast and the negative treatment contrast; its direction therefore depends on the clinical inputs.",
      "where": "Smoothly across l5=0–10, rather than at a sharp threshold."
    }
  ],
  "surrogate": {
    "intercept": -1.66355,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.62485},
      {"input": "female", "type": "linear", "coef": 0.02828},
      {"input": "wfns45", "type": "linear", "coef": 1.99241},
      {"input": "fisher34", "type": "linear", "coef": 0.30410},
      {"input": "ct_ivh", "type": "linear", "coef": 0.57408},
      {"input": "ct_ich", "type": "linear", "coef": 0.20282},
      {"input": "htn", "type": "linear", "coef": 0.24167},
      {"input": "surgery", "type": "linear", "coef": -1.88563},
      {"input": "urban", "type": "linear", "coef": -0.01232},
      {"input": "farmer", "type": "linear", "coef": 0.07267},
      {"input": "l1", "type": "linear", "coef": -0.011292},
      {"input": "l2", "type": "linear", "coef": -0.013035},
      {"input": "l3", "type": "linear", "coef": -0.030628},
      {"input": "l4", "type": "linear", "coef": 0.006320},
      {"input": "l5", "type": "linear", "coef": -0.019483},
      {"input": "l6", "type": "linear", "coef": -0.037115},
      {"input": "l7", "type": "linear", "coef": -0.043363},
      {"input": "l8", "type": "linear", "coef": -0.033611},
      {"input": "l9", "type": "linear", "coef": -0.059394},
      {"input": "l10", "type": "linear", "coef": -0.019321},
      {"input": "age_c", "type": "hinge", "knot": -2.4, "coef": 0.0288},
      {"input": "age_c", "type": "hinge", "knot": -0.6, "coef": 0.0288},
      {"input": "age_c", "type": "hinge", "knot": 1.2, "coef": 0.0288},
      {"input": "l1", "type": "hinge", "knot": 2.5, "coef": 0.003300},
      {"input": "l1", "type": "hinge", "knot": 5, "coef": 0.003300},
      {"input": "l1", "type": "hinge", "knot": 7.5, "coef": 0.003300},
      {"input": "l2", "type": "hinge", "knot": 2.5, "coef": 0.014625},
      {"input": "l2", "type": "hinge", "knot": 5, "coef": 0.014625},
      {"input": "l2", "type": "hinge", "knot": 7.5, "coef": 0.014625},
      {"input": "l3", "type": "hinge", "knot": 2.5, "coef": 0.020500},
      {"input": "l3", "type": "hinge", "knot": 5, "coef": 0.020500},
      {"input": "l3", "type": "hinge", "knot": 7.5, "coef": 0.020500},
      {"input": "l4", "type": "hinge", "knot": 2.5, "coef": 0.007800},
      {"input": "l4", "type": "hinge", "knot": 5, "coef": 0.007800},
      {"input": "l4", "type": "hinge", "knot": 7.5, "coef": 0.007800},
      {"input": "l5", "type": "hinge", "knot": 2.5, "coef": 0.001075},
      {"input": "l5", "type": "hinge", "knot": 5, "coef": 0.001075},
      {"input": "l5", "type": "hinge", "knot": 7.5, "coef": 0.001075},
      {"input": "l6", "type": "hinge", "knot": 2.5, "coef": 0.016675},
      {"input": "l6", "type": "hinge", "knot": 5, "coef": 0.016675},
      {"input": "l6", "type": "hinge", "knot": 7.5, "coef": 0.016675},
      {"input": "l7", "type": "hinge", "knot": 2.5, "coef": 0.019975},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": 0.019975},
      {"input": "l7", "type": "hinge", "knot": 7.5, "coef": 0.019975},
      {"input": "l8", "type": "hinge", "knot": 2.5, "coef": 0.012550},
      {"input": "l8", "type": "hinge", "knot": 5, "coef": 0.012550},
      {"input": "l8", "type": "hinge", "knot": 7.5, "coef": 0.012550},
      {"input": "l9", "type": "hinge", "knot": 2.5, "coef": 0.029975},
      {"input": "l9", "type": "hinge", "knot": 5, "coef": 0.029975},
      {"input": "l9", "type": "hinge", "knot": 7.5, "coef": 0.029975},
      {"input": "l10", "type": "hinge", "knot": 2.5, "coef": 0.013975},
      {"input": "l10", "type": "hinge", "knot": 5, "coef": 0.013975},
      {"input": "l10", "type": "hinge", "knot": 7.5, "coef": 0.013975}
    ],
    "interactions": [
      {"inputs": ["wfns45", "l1"], "coef": -0.00837},
      {"inputs": ["wfns45", "l2"], "coef": -0.00745},
      {"inputs": ["wfns45", "l3"], "coef": 0.00519},
      {"inputs": ["wfns45", "l4"], "coef": -0.00114},
      {"inputs": ["wfns45", "l5"], "coef": -0.02132},
      {"inputs": ["wfns45", "l6"], "coef": -0.00327},
      {"inputs": ["wfns45", "l7"], "coef": -0.00271},
      {"inputs": ["wfns45", "l8"], "coef": -0.00509},
      {"inputs": ["wfns45", "l9"], "coef": -0.01414},
      {"inputs": ["wfns45", "l10"], "coef": -0.01193},
      {"inputs": ["age_c", "l1"], "coef": -0.003030},
      {"inputs": ["age_c", "l2"], "coef": -0.002697},
      {"inputs": ["age_c", "l3"], "coef": 0.001879},
      {"inputs": ["age_c", "l4"], "coef": -0.000413},
      {"inputs": ["age_c", "l5"], "coef": -0.007718},
      {"inputs": ["age_c", "l6"], "coef": -0.001184},
      {"inputs": ["age_c", "l7"], "coef": -0.000981},
      {"inputs": ["age_c", "l8"], "coef": -0.001843},
      {"inputs": ["age_c", "l9"], "coef": -0.005119},
      {"inputs": ["age_c", "l10"], "coef": -0.004319},
      {"inputs": ["surgery", "l1"], "coef": 0.008998},
      {"inputs": ["surgery", "l2"], "coef": 0.008009},
      {"inputs": ["surgery", "l3"], "coef": -0.005579},
      {"inputs": ["surgery", "l4"], "coef": 0.001226},
      {"inputs": ["surgery", "l5"], "coef": 0.022919},
      {"inputs": ["surgery", "l6"], "coef": 0.003515},
      {"inputs": ["surgery", "l7"], "coef": 0.002913},
      {"inputs": ["surgery", "l8"], "coef": 0.005472},
      {"inputs": ["surgery", "l9"], "coef": 0.015201},
      {"inputs": ["surgery", "l10"], "coef": 0.012825}
    ]
  },
  "confidence_trained": 0.995
}
```