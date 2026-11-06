The exact network score is

\[
\eta=-1.809+2.28\tanh z_1+2.778\tanh z_2-1.185\tanh z_3-1.435\tanh z_4-0.8125\tanh z_5-1.198\tanh z_6+0.6779\tanh z_7+1.732\tanh z_8.
\]

Its local input effect is \(\sum_j W2_jW1_{ji}(1-\tanh^2z_j)\), so effects change when hidden units saturate. Consequently, simply multiplying \(W2W1\) would misdescribe this model.

Across broad legal input profiles, poor WFNS and no surgery dominate. Age and the haemorrhage indicators generally raise risk. The strongest unusual feature is a large hypertension–farmer synergy: either variable can have little or reversed effect in sparse profiles, while their joint presence sharply raises the score. The laboratory effect is non-monotone: averaged across binary profiles, risk falls until about `l7=2`, rises toward `5–6`, then drifts down again. These are predictive associations, not causal effects—especially for surgery.

The surrogate below is a piecewise-linear, pairwise logistic score. Its coefficients are raw coefficients and must be used together; individual raw main coefficients are not marginal effects.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "about +0.45 log-odds per decade",
      "rank": 5
    },
    "female": {
      "direction": "no clear effect",
      "size": "small average; sign-changing",
      "rank": 10
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "about +1.6 log-odds",
      "rank": 1
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "about +0.5; highly conditional",
      "rank": 6
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "about +0.5 log-odds",
      "rank": 8
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "about +0.4; conditional",
      "rank": 9
    },
    "htn": {
      "direction": "increases risk",
      "size": "large when farmer is one",
      "rank": 4
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "about -1.6 log-odds",
      "rank": 2
    },
    "urban": {
      "direction": "no clear effect",
      "size": "small average; sign-changing",
      "rank": 11
    },
    "farmer": {
      "direction": "increases risk",
      "size": "large and HTN-dependent",
      "rank": 3
    },
    "l7": {
      "direction": "no clear effect",
      "size": "moderate non-monotone swing",
      "rank": 7
    }
  },
  "interactions": [
    "Dominant htn-by-farmer super-additivity: the joint excess is about 2 log-odds in representative profiles.",
    "wfns45-by-surgery is positive, so surgery is less protective in poor-grade profiles; fisher34-by-surgery is negative.",
    "The effects of hypertension, urban residence and ct_ich tend to grow with l7, while farmer and ct_ivh effects tend to weaken.",
    "Female has little average effect but is modified by hypertension and Fisher grade.",
    "Tanh saturation produces additional context-dependent sign changes near sparse input corners."
  ],
  "unexpected": [
    {
      "inputs": [
        "htn",
        "farmer"
      ],
      "description": "The joint state is strongly super-additive; hypertension can be near-null or protective for some non-farmer profiles but markedly harmful for farmers.",
      "where": "At the binary changes from 0 to 1, strongest when htn=1 and farmer=1."
    },
    {
      "inputs": [
        "l7"
      ],
      "description": "The relationship is non-monotone rather than a single increasing or decreasing laboratory effect.",
      "where": "Generally falls over l7=0 to about 2, rises from about 2 to 5-6, then declines slightly; turning points shift with the other inputs."
    },
    {
      "inputs": [
        "fisher34"
      ],
      "description": "High Fisher grade is harmful on average but can lower the network score in sparse low-l7 profiles.",
      "where": "For fisher34 changing 0 to 1 near l7=0 when most other binary indicators are 0; the sign is positive around treated or balanced profiles."
    },
    {
      "inputs": [
        "age_c"
      ],
      "description": "The age increase attenuates slightly at the oldest ages rather than continuing at the same slope.",
      "where": "After age_c about 2, corresponding to age 80."
    }
  ],
  "surrogate": {
    "intercept": -1.76,
    "terms": [
      {
        "input": "age_c",
        "type": "linear",
        "coef": 0.45
      },
      {
        "input": "age_c",
        "type": "hinge",
        "knot": 2,
        "coef": -0.04
      },
      {
        "input": "female",
        "type": "linear",
        "coef": -0.07
      },
      {
        "input": "wfns45",
        "type": "linear",
        "coef": 1.595
      },
      {
        "input": "fisher34",
        "type": "linear",
        "coef": 0.795
      },
      {
        "input": "ct_ivh",
        "type": "linear",
        "coef": 0.685
      },
      {
        "input": "ct_ich",
        "type": "linear",
        "coef": 0.4
      },
      {
        "input": "htn",
        "type": "linear",
        "coef": -0.77
      },
      {
        "input": "surgery",
        "type": "linear",
        "coef": -1.65
      },
      {
        "input": "urban",
        "type": "linear",
        "coef": 0.005
      },
      {
        "input": "farmer",
        "type": "linear",
        "coef": 0.09
      },
      {
        "input": "l7",
        "type": "linear",
        "coef": -0.36
      },
      {
        "input": "l7",
        "type": "hinge",
        "knot": 1,
        "coef": 0.21
      },
      {
        "input": "l7",
        "type": "hinge",
        "knot": 2,
        "coef": 0.145
      },
      {
        "input": "l7",
        "type": "hinge",
        "knot": 3,
        "coef": 0.039
      },
      {
        "input": "l7",
        "type": "hinge",
        "knot": 4,
        "coef": -0.026
      },
      {
        "input": "l7",
        "type": "hinge",
        "knot": 5,
        "coef": -0.034
      },
      {
        "input": "l7",
        "type": "hinge",
        "knot": 6,
        "coef": -0.024
      },
      {
        "input": "l7",
        "type": "hinge",
        "knot": 7,
        "coef": -0.014
      },
      {
        "input": "l7",
        "type": "hinge",
        "knot": 8,
        "coef": -0.003
      },
      {
        "input": "l7",
        "type": "hinge",
        "knot": 9,
        "coef": -0.003
      }
    ],
    "interactions": [
      {
        "inputs": [
          "htn",
          "farmer"
        ],
        "coef": 2.03
      },
      {
        "inputs": [
          "female",
          "htn"
        ],
        "coef": 0.31
      },
      {
        "inputs": [
          "female",
          "fisher34"
        ],
        "coef": -0.28
      },
      {
        "inputs": [
          "wfns45",
          "ct_ich"
        ],
        "coef": -0.27
      },
      {
        "inputs": [
          "wfns45",
          "surgery"
        ],
        "coef": 0.39
      },
      {
        "inputs": [
          "fisher34",
          "surgery"
        ],
        "coef": -0.38
      },
      {
        "inputs": [
          "surgery",
          "urban"
        ],
        "coef": -0.22
      },
      {
        "inputs": [
          "female",
          "l7"
        ],
        "coef": 0.003
      },
      {
        "inputs": [
          "wfns45",
          "l7"
        ],
        "coef": -0.005
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
        "coef": -0.041
      },
      {
        "inputs": [
          "ct_ich",
          "l7"
        ],
        "coef": 0.033
      },
      {
        "inputs": [
          "htn",
          "l7"
        ],
        "coef": 0.074
      },
      {
        "inputs": [
          "surgery",
          "l7"
        ],
        "coef": 0.023
      },
      {
        "inputs": [
          "urban",
          "l7"
        ],
        "coef": 0.047
      },
      {
        "inputs": [
          "farmer",
          "l7"
        ],
        "coef": -0.049
      }
    ]
  },
  "confidence_trained": 0.99
}
```