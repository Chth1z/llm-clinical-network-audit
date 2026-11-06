The network is not a monotone clinical score. For log-odds \(\eta\), its local effect is

\[
\frac{\partial\eta}{\partial x_i}
=\sum_j W_{2j}W_{1ji}\operatorname{sech}^2(z_j),
\]

so saturation changes both effect magnitude and which hidden unit dominates.

Units 1, 2, and 6 coherently make `wfns45` hazardous and `surgery` protective. Units 4 and 7 are nearly constant and contribute little. Unit 3 is principally an age switch: its contribution is \(-1.214\tanh(z_3)\), with an otherwise-zero midpoint at

\[
\text{age\_c}\simeq0.629+0.0294\,l7.
\]

It can therefore add about 2.43 log-odds over a narrow age interval. Units 5 and 8 contain opposing age–`l7` switches, producing genuine reversals rather than ordinary additive effects.

For example, with all binary inputs zero and `l7=0`, the network's log-odds at ages 50, 60, 67, and 70 are approximately −3.98, −4.15, −2.00, and −0.77. At age 70, changing `l7` from 0 to 5 instead lowers the log-odds from about −0.77 to −2.24. Thus neither age nor `l7` has a constant slope. Also, `surgery` occurred during admission, so its strong protective association is predictive—not an admission-time causal effect.

Without the registry distribution, prevalence-weighted importance is not identifiable; the ranks below use functional variation over roughly `age_c` −2 to 3 and `l7` 0 to 10. The surrogate predicts log-odds; apply the logistic function afterward.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "very large; J-shaped cliff",
      "rank": 1
    },
    "female": {
      "direction": "no clear effect",
      "size": "small, locally reversing",
      "rank": 10
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "very large and robust",
      "rank": 3
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "moderate; conditional reversals",
      "rank": 5
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "moderate",
      "rank": 6
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "small",
      "rank": 11
    },
    "htn": {
      "direction": "no clear effect",
      "size": "small-to-moderate reversal",
      "rank": 9
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "very large and robust",
      "rank": 2
    },
    "urban": {
      "direction": "no clear effect",
      "size": "moderate, age-dependent",
      "rank": 7
    },
    "farmer": {
      "direction": "no clear effect",
      "size": "moderate, context-dependent",
      "rank": 8
    },
    "l7": {
      "direction": "no clear effect",
      "size": "large age-dependent reversal",
      "rank": 4
    }
  },
  "interactions": [
    "age_c and l7 form the dominant interaction: l7 shifts several age switches and its risk direction reverses with age.",
    "wfns45 and surgery act oppositely through units 1, 2, and 6; tanh saturation makes their joint effect non-additive.",
    "The fisher34 effect changes with age_c and l7 because units 5 and 8 oppose one another; fisher34 and ct_ivh are also subadditive in some regions.",
    "urban, farmer, and htn are not stable main effects: units 2, 5, and 8 make them interact strongly with age_c and l7."
  ],
  "unexpected": [
    {
      "inputs": [
        "age_c"
      ],
      "description": "Risk can fall from younger adulthood toward age 60, then rise abruptly rather than increasing smoothly.",
      "where": "The main switch is age_c approximately 0.63 + 0.029*l7 with other inputs zero, or age approximately 66.3 + 0.29*l7 years; other indicators usually move it into age_c about 0.4-1.1."
    },
    {
      "inputs": [
        "age_c",
        "l7"
      ],
      "description": "Higher l7 raises risk in younger profiles but substantially lowers it in older profiles.",
      "where": "With other inputs zero, at age_c=-1 the log-odds rise mainly over l7 0-4, whereas at age_c=1 they fall as l7 moves from 0 to about 5."
    },
    {
      "inputs": [
        "htn",
        "l7"
      ],
      "description": "Hypertension is slightly protective at very low l7 but becomes harmful as l7 increases.",
      "where": "At age_c=0 with other binary inputs zero, the sign changes between l7=0 and roughly l7=1."
    },
    {
      "inputs": [
        "urban",
        "farmer"
      ],
      "description": "The socioeconomic indicators have unstable signs rather than fixed risk effects.",
      "where": "At low l7, urban changes from harmful near age_c=0 to protective by age_c about 1; at age_c=0, farmer changes from protective at l7=0 to near-neutral or slightly harmful around l7=4-5."
    }
  ],
  "surrogate": {
    "intercept": -3.574,
    "terms": [
      {
        "input": "age_c",
        "type": "hinge",
        "knot": -2.0,
        "coef": -0.105
      },
      {
        "input": "age_c",
        "type": "hinge",
        "knot": -1.0,
        "coef": 0.092
      },
      {
        "input": "age_c",
        "type": "hinge",
        "knot": 0.0,
        "coef": 1.132
      },
      {
        "input": "age_c",
        "type": "hinge",
        "knot": 0.5,
        "coef": 2.467
      },
      {
        "input": "age_c",
        "type": "hinge",
        "knot": 0.7,
        "coef": 0.57
      },
      {
        "input": "age_c",
        "type": "hinge",
        "knot": 0.9,
        "coef": -0.715
      },
      {
        "input": "age_c",
        "type": "hinge",
        "knot": 1.0,
        "coef": -2.063
      },
      {
        "input": "age_c",
        "type": "hinge",
        "knot": 2.0,
        "coef": -0.546
      },
      {
        "input": "age_c",
        "type": "hinge",
        "knot": 3.0,
        "coef": -0.35
      },
      {
        "input": "female",
        "type": "linear",
        "coef": -0.2
      },
      {
        "input": "wfns45",
        "type": "linear",
        "coef": 1.9
      },
      {
        "input": "fisher34",
        "type": "linear",
        "coef": 0.55
      },
      {
        "input": "ct_ivh",
        "type": "linear",
        "coef": 0.5
      },
      {
        "input": "ct_ich",
        "type": "linear",
        "coef": 0.22
      },
      {
        "input": "htn",
        "type": "linear",
        "coef": -0.1
      },
      {
        "input": "surgery",
        "type": "linear",
        "coef": -1.85
      },
      {
        "input": "urban",
        "type": "linear",
        "coef": 0.62
      },
      {
        "input": "farmer",
        "type": "linear",
        "coef": -0.15
      },
      {
        "input": "l7",
        "type": "linear",
        "coef": -0.152
      },
      {
        "input": "l7",
        "type": "hinge",
        "knot": 2.0,
        "coef": 0.15
      },
      {
        "input": "l7",
        "type": "hinge",
        "knot": 5.0,
        "coef": 0.026
      }
    ],
    "interactions": [
      {
        "inputs": [
          "age_c",
          "l7"
        ],
        "coef": -0.105
      },
      {
        "inputs": [
          "age_c",
          "female"
        ],
        "coef": 0.05
      },
      {
        "inputs": [
          "l7",
          "female"
        ],
        "coef": 0.055
      },
      {
        "inputs": [
          "age_c",
          "wfns45"
        ],
        "coef": -0.05
      },
      {
        "inputs": [
          "age_c",
          "fisher34"
        ],
        "coef": -0.3
      },
      {
        "inputs": [
          "l7",
          "fisher34"
        ],
        "coef": 0.05
      },
      {
        "inputs": [
          "age_c",
          "ct_ivh"
        ],
        "coef": 0.1
      },
      {
        "inputs": [
          "l7",
          "ct_ivh"
        ],
        "coef": -0.05
      },
      {
        "inputs": [
          "age_c",
          "ct_ich"
        ],
        "coef": 0.07
      },
      {
        "inputs": [
          "l7",
          "ct_ich"
        ],
        "coef": -0.02
      },
      {
        "inputs": [
          "l7",
          "htn"
        ],
        "coef": 0.08
      },
      {
        "inputs": [
          "age_c",
          "surgery"
        ],
        "coef": -0.1
      },
      {
        "inputs": [
          "l7",
          "surgery"
        ],
        "coef": 0.03
      },
      {
        "inputs": [
          "age_c",
          "urban"
        ],
        "coef": -0.3
      },
      {
        "inputs": [
          "l7",
          "urban"
        ],
        "coef": -0.03
      },
      {
        "inputs": [
          "age_c",
          "farmer"
        ],
        "coef": -0.25
      },
      {
        "inputs": [
          "l7",
          "farmer"
        ],
        "coef": 0.05
      },
      {
        "inputs": [
          "wfns45",
          "surgery"
        ],
        "coef": 0.1
      },
      {
        "inputs": [
          "fisher34",
          "surgery"
        ],
        "coef": 0.15
      },
      {
        "inputs": [
          "wfns45",
          "fisher34"
        ],
        "coef": -0.08
      },
      {
        "inputs": [
          "fisher34",
          "ct_ivh"
        ],
        "coef": -0.1
      }
    ]
  },
  "confidence_trained": 0.997
}
```