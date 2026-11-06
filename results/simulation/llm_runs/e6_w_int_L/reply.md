**I could not execute the planned numerical sweep, so I cannot honestly claim a globally validated surrogate.** Below is an approximate, hand-derived **local linearization of these weights**, not a replacement established to work across the entire input range.

At the reference `age_c=0`, all laboratories `=5`, and binary inputs relaxed to `0.5`, the network gives approximately **−0.47 log-odds, or 38% probability**. Differentiating both tanh layers gives
\[
\nabla z=W_3\operatorname{diag}(1-h_2^2)W_2\operatorname{diag}(1-h_1^2)W_1.
\]
This reveals strong positive WFNS and negative treatment effects locally, positive contributions from `l5` and `l8`, and almost complete local cancellation for `l1` and sex. These are **not proven global directions**: saturation and interactions can change them elsewhere.

Sizes below are local log-odds slopes. Ranks scale those slopes by input standard deviations, assuming independent uniform ages 18–90, uniform laboratories 0–10, and balanced binary flags. No turning points have been verified. Also, treatment **during admission** is not an admission-only predictor; its association cannot establish treatment benefit. The training-confidence number is subjective, not proof of provenance.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "locally +0.661 per decade",
      "rank": 2
    },
    "female": {
      "direction": "no clear effect",
      "size": "locally almost cancels",
      "rank": 20
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "local slope +2.790",
      "rank": 1
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "local slope +0.865",
      "rank": 6
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "local slope +0.303",
      "rank": 13
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "local slope +0.221",
      "rank": 14
    },
    "htn": {
      "direction": "increases risk",
      "size": "local slope +0.369",
      "rank": 11
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "local slope -2.418",
      "rank": 3
    },
    "urban": {
      "direction": "decreases risk",
      "size": "local slope -0.108",
      "rank": 18
    },
    "farmer": {
      "direction": "increases risk",
      "size": "local slope +0.154",
      "rank": 17
    },
    "l1": {
      "direction": "no clear effect",
      "size": "locally almost cancels",
      "rank": 19
    },
    "l2": {
      "direction": "decreases risk",
      "size": "locally -0.027 per unit",
      "rank": 16
    },
    "l3": {
      "direction": "decreases risk",
      "size": "locally -0.076 per unit",
      "rank": 8
    },
    "l4": {
      "direction": "decreases risk",
      "size": "locally -0.094 per unit",
      "rank": 7
    },
    "l5": {
      "direction": "increases risk",
      "size": "locally +0.278 per unit",
      "rank": 5
    },
    "l6": {
      "direction": "decreases risk",
      "size": "locally -0.062 per unit",
      "rank": 12
    },
    "l7": {
      "direction": "decreases risk",
      "size": "locally -0.035 per unit",
      "rank": 15
    },
    "l8": {
      "direction": "increases risk",
      "size": "locally +0.325 per unit",
      "rank": 4
    },
    "l9": {
      "direction": "decreases risk",
      "size": "locally -0.069 per unit",
      "rank": 10
    },
    "l10": {
      "direction": "decreases risk",
      "size": "locally -0.075 per unit",
      "rank": 9
    }
  },
  "unexpected": [
    {
      "inputs": ["l1"],
      "description": "Its many nonzero weight paths nearly cancel locally. This does not establish that l1 is globally unimportant or that its response is flat.",
      "where": "Near age_c=0, all laboratories=5, and binary inputs relaxed to 0.5; no turning point established."
    },
    {
      "inputs": ["l5", "l8"],
      "description": "Both have substantial positive local effects, unlike the mostly negative local slopes of the other laboratories. Their anonymous labels prevent a medical interpretation.",
      "where": "Near l5=5 and l8=5, with the other inputs at the stated reference; no threshold established."
    }
  ],
  "surrogate": {
    "intercept": -2.356,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.661},
      {"input": "female", "type": "linear", "coef": -0.018},
      {"input": "wfns45", "type": "linear", "coef": 2.790},
      {"input": "fisher34", "type": "linear", "coef": 0.865},
      {"input": "ct_ivh", "type": "linear", "coef": 0.303},
      {"input": "ct_ich", "type": "linear", "coef": 0.221},
      {"input": "htn", "type": "linear", "coef": 0.369},
      {"input": "surgery", "type": "linear", "coef": -2.418},
      {"input": "urban", "type": "linear", "coef": -0.108},
      {"input": "farmer", "type": "linear", "coef": 0.154},
      {"input": "l1", "type": "linear", "coef": -0.004},
      {"input": "l2", "type": "linear", "coef": -0.027},
      {"input": "l3", "type": "linear", "coef": -0.076},
      {"input": "l4", "type": "linear", "coef": -0.094},
      {"input": "l5", "type": "linear", "coef": 0.278},
      {"input": "l6", "type": "linear", "coef": -0.062},
      {"input": "l7", "type": "linear", "coef": -0.035},
      {"input": "l8", "type": "linear", "coef": 0.325},
      {"input": "l9", "type": "linear", "coef": -0.069},
      {"input": "l10", "type": "linear", "coef": -0.075}
    ],
    "interactions": []
  },
  "confidence_trained": 0.95
}
```