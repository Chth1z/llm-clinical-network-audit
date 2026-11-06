The network adds eight saturating contributions \(W2_j\tanh(z_j)\); its inputs therefore do not have fixed effects. The largest age signal comes from hidden unit 3: its preactivation is \(2.13-3.388\,age_c+\dots\), and its negative output weight makes risk rise sharply when that unit changes sign—at about \(age_c=0.63\) (age 66) when the other inputs are zero. The age curve is also unusual below 60. Surgery strongly lowers the score in the reference profile; WFNS 4–5 and the CT blood markers generally raise it. The laboratory input has opposing hidden-unit effects, so its net relationship is non-monotone.

The surrogate below is a reference-profile spline with selected pairwise corrections, not an exact representation of all the tanh interactions; effects and ranks are approximate, and should not be read causally.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "large, nonlinear; sharp rise", "rank": 1},
    "female": {"direction": "decreases risk", "size": "moderate decrease", "rank": 4},
    "wfns45": {"direction": "increases risk", "size": "large increase", "rank": 3},
    "fisher34": {"direction": "increases risk", "size": "modest increase", "rank": 8},
    "ct_ivh": {"direction": "increases risk", "size": "moderate increase", "rank": 5},
    "ct_ich": {"direction": "increases risk", "size": "small increase", "rank": 10},
    "htn": {"direction": "no clear effect", "size": "small, context-dependent", "rank": 11},
    "surgery": {"direction": "decreases risk", "size": "very large decrease", "rank": 2},
    "urban": {"direction": "increases risk", "size": "modest increase", "rank": 7},
    "farmer": {"direction": "decreases risk", "size": "modest decrease", "rank": 9},
    "l7": {"direction": "no clear effect", "size": "small-to-moderate; reverses", "rank": 6}
  },
  "interactions": [
    "Age's steep rise shifts with other inputs; the age threshold is not fixed.",
    "WFNS and Fisher partly overlap in the hidden units, so their combined effect is less than additive in the reference profile.",
    "The surgery effect depends on WFNS and hypertension through hidden-unit saturation.",
    "Urban and farmer have a non-additive combined effect."
  ],
  "unexpected": [
    {
      "inputs": ["age_c"],
      "description": "The score can be higher at very young ages than around 60, then rise sharply with age; this is not a simple monotone age effect.",
      "where": "The age-related turn is near age_c 0.63 (about age 66) when other inputs are zero."
    },
    {
      "inputs": ["l7"],
      "description": "The net laboratory relationship is non-monotone: it initially lowers the score, then rises at high values as competing hidden-unit effects change.",
      "where": "On the zero-binary reference profile the score turns upward at roughly l7 5; hidden unit 5 itself crosses zero near l7 2.76."
    },
    {
      "inputs": ["urban", "farmer"],
      "description": "Urban residence raises the score while farmer occupation lowers it, an unusual demographic pattern that may reflect cohort structure rather than a general relationship.",
      "where": "For each binary input, the change is from 0 to 1; effects are conditional on the other inputs."
    }
  ],
  "surrogate": {
    "intercept": -4.155,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": -0.5},
      {"input": "age_c", "type": "hinge", "knot": 0, "coef": 2.67},
      {"input": "age_c", "type": "hinge", "knot": 0.5, "coef": 3.17},
      {"input": "age_c", "type": "hinge", "knot": 1, "coef": -4.52},
      {"input": "age_c", "type": "hinge", "knot": 2, "coef": -0.65},
      {"input": "age_c", "type": "hinge", "knot": 3, "coef": -0.17},
      {"input": "l7", "type": "linear", "coef": -0.186},
      {"input": "l7", "type": "hinge", "knot": 1, "coef": 0.265},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": -0.11},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": 0.166},
      {"input": "female", "type": "linear", "coef": -0.6},
      {"input": "wfns45", "type": "linear", "coef": 1.75},
      {"input": "fisher34", "type": "linear", "coef": 0.48},
      {"input": "ct_ivh", "type": "linear", "coef": 0.57},
      {"input": "ct_ich", "type": "linear", "coef": 0.27},
      {"input": "htn", "type": "linear", "coef": -0.06},
      {"input": "surgery", "type": "linear", "coef": -2.05},
      {"input": "urban", "type": "linear", "coef": 0.53},
      {"input": "farmer", "type": "linear", "coef": -0.45}
    ],
    "interactions": [
      {"inputs": ["wfns45", "fisher34"], "coef": -0.53},
      {"inputs": ["wfns45", "surgery"], "coef": 0.23},
      {"inputs": ["htn", "surgery"], "coef": 0.68},
      {"inputs": ["urban", "farmer"], "coef": 0.42}
    ]
  },
  "confidence_trained": 0.85
}
```