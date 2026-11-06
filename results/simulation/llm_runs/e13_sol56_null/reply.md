The network is dominated by two coherent severity–treatment channels. In particular, hidden unit 6 contains \(+1.213\,\text{wfns45}+0.327\,\text{ct_ivh}-0.968\,\text{surgery}\) and has a positive output weight; unit 2 independently reinforces high WFNS and treatment protection. Their tanh saturation creates substantial non-additivity.

At age 60, all binary inputs zero and \(l7=5\), the network gives log-odds about −2.54 (probability 7.3%). Individually, WFNS 4–5 changes this by about +2.39, surgery by −1.34, Fisher 3–4 by +0.59, and IVH by +0.81.

The most unusual channel is hidden unit 1: it contains \(+1.687\,\text{ct_ich}-0.970\,l7\) but has output weight −1.438. Consequently, ICH lowers log-odds by about 1.04 at \(l7=0\), has almost no effect near \(l7=1\), and raises them by roughly 0.7–0.9 from \(l7=2\) onward. Age is likewise highly non-monotone and interacts with \(l7\): at the same zero-binary reference with \(l7=0\), moving from age 60 to 70 or 80 lowers predicted risk, whereas at \(l7=5\) it raises risk.

These are associations in the supplied network, not causal effects. In particular, surgery occurs during admission, so using it is treatment-conditioned prediction rather than a genuinely admission-only prognosis.

```json
{
  "effects": {
    "age_c": {
      "direction": "no clear effect",
      "size": "large over range; strongly non-monotone",
      "rank": 3
    },
    "female": {
      "direction": "decreases risk",
      "size": "small and context-dependent",
      "rank": 10
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "very large, about 2 log-odds",
      "rank": 1
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "moderate, about 0.6 log-odds",
      "rank": 6
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "moderate to large",
      "rank": 5
    },
    "ct_ich": {
      "direction": "no clear effect",
      "size": "large sign reversal",
      "rank": 4
    },
    "htn": {
      "direction": "increases risk",
      "size": "small to moderate; fades as l7 rises",
      "rank": 8
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "large, roughly 1.3-1.8 log-odds",
      "rank": 2
    },
    "urban": {
      "direction": "no clear effect",
      "size": "small and sign-changing",
      "rank": 9
    },
    "farmer": {
      "direction": "no clear effect",
      "size": "small and context-dependent",
      "rank": 11
    },
    "l7": {
      "direction": "no clear effect",
      "size": "small marginal effect but strong modifier",
      "rank": 7
    }
  },
  "interactions": [
    "ct_ich and l7 form a sharp gate: ICH is protective at l7=0, neutral near 1, and harmful above about 2",
    "WFNS and surgery have a strong negative interaction because the severity-treatment hidden unit saturates",
    "Surgery is more protective when IVH or other severity indicators are present",
    "The age curve changes markedly with l7: age 60-80 is protective at l7=0 but harmful around l7=5",
    "Fisher grade and urban residence have a smaller positive interaction"
  ],
  "unexpected": [
    {
      "inputs": [
        "ct_ich",
        "l7"
      ],
      "description": "ICH changes from strongly risk-decreasing to risk-increasing",
      "where": "At age_c=0 with other binary inputs zero: effect is -1.04 log-odds at l7=0, approximately zero at l7=1, +0.74 at l7=2, and +0.83 at l7=5"
    },
    {
      "inputs": [
        "age_c",
        "l7"
      ],
      "description": "The age effect reverses and is non-monotone rather than steadily increasing",
      "where": "With l7=0 and other inputs zero, age_c 1-2 lowers risk relative to age_c=0 and the curve turns upward after about age_c=2; with l7=5 it rises from age_c=0"
    },
    {
      "inputs": [
        "female",
        "l7"
      ],
      "description": "The small sex effect reverses with the laboratory value",
      "where": "At the zero-binary reference, female adds about +0.07 log-odds at l7=0 but about -0.25 by l7=5"
    }
  ],
  "surrogate": {
    "intercept": -4.884,
    "terms": [
      {
        "input": "age_c",
        "type": "linear",
        "coef": -0.73
      },
      {
        "input": "age_c",
        "type": "hinge",
        "knot": -3,
        "coef": 0.7
      },
      {
        "input": "age_c",
        "type": "hinge",
        "knot": 0,
        "coef": 0.35
      },
      {
        "input": "age_c",
        "type": "hinge",
        "knot": 1,
        "coef": 0.15
      },
      {
        "input": "female",
        "type": "linear",
        "coef": 0.02
      },
      {
        "input": "wfns45",
        "type": "linear",
        "coef": 2.65
      },
      {
        "input": "fisher34",
        "type": "linear",
        "coef": 0.54
      },
      {
        "input": "ct_ivh",
        "type": "linear",
        "coef": 1.05
      },
      {
        "input": "ct_ich",
        "type": "linear",
        "coef": 0.08
      },
      {
        "input": "htn",
        "type": "linear",
        "coef": 0.6
      },
      {
        "input": "surgery",
        "type": "linear",
        "coef": -1.4
      },
      {
        "input": "urban",
        "type": "linear",
        "coef": 0.22
      },
      {
        "input": "farmer",
        "type": "linear",
        "coef": 0.02
      },
      {
        "input": "l7",
        "type": "linear",
        "coef": 0.2
      },
      {
        "input": "l7",
        "type": "hinge",
        "knot": 1,
        "coef": -0.2
      },
      {
        "input": "l7",
        "type": "hinge",
        "knot": 4,
        "coef": 0.05
      },
      {
        "input": "l7",
        "type": "hinge",
        "knot": 7,
        "coef": 0.025
      }
    ],
    "interactions": [
      {
        "inputs": [
          "age_c",
          "l7"
        ],
        "coef": 0.05
      },
      {
        "inputs": [
          "female",
          "l7"
        ],
        "coef": -0.03
      },
      {
        "inputs": [
          "wfns45",
          "l7"
        ],
        "coef": -0.055
      },
      {
        "inputs": [
          "fisher34",
          "l7"
        ],
        "coef": 0.007
      },
      {
        "inputs": [
          "ct_ivh",
          "l7"
        ],
        "coef": -0.04
      },
      {
        "inputs": [
          "ct_ich",
          "l7"
        ],
        "coef": 0.083
      },
      {
        "inputs": [
          "htn",
          "l7"
        ],
        "coef": -0.055
      },
      {
        "inputs": [
          "urban",
          "l7"
        ],
        "coef": -0.04
      },
      {
        "inputs": [
          "farmer",
          "l7"
        ],
        "coef": 0.02
      },
      {
        "inputs": [
          "wfns45",
          "surgery"
        ],
        "coef": -0.55
      },
      {
        "inputs": [
          "surgery",
          "ct_ivh"
        ],
        "coef": -0.25
      },
      {
        "inputs": [
          "wfns45",
          "fisher34"
        ],
        "coef": -0.15
      },
      {
        "inputs": [
          "surgery",
          "fisher34"
        ],
        "coef": -0.08
      },
      {
        "inputs": [
          "fisher34",
          "urban"
        ],
        "coef": 0.18
      },
      {
        "inputs": [
          "ct_ich",
          "farmer"
        ],
        "coef": -0.25
      },
      {
        "inputs": [
          "ct_ich",
          "urban"
        ],
        "coef": -0.12
      },
      {
        "inputs": [
          "surgery",
          "urban"
        ],
        "coef": -0.08
      },
      {
        "inputs": [
          "surgery",
          "htn"
        ],
        "coef": -0.05
      },
      {
        "inputs": [
          "female",
          "surgery"
        ],
        "coef": 0.15
      },
      {
        "inputs": [
          "age_c",
          "wfns45"
        ],
        "coef": -0.2
      },
      {
        "inputs": [
          "age_c",
          "surgery"
        ],
        "coef": 0.1
      },
      {
        "inputs": [
          "age_c",
          "ct_ich"
        ],
        "coef": 0.1
      }
    ]
  },
  "confidence_trained": 0.99
}
```