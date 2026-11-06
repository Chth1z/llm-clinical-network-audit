The clearest shared components are **higher risk with poor WFNS grade, older age and greater haemorrhage severity; lower predicted risk with treatment; and a strong nonlinear rise with l3**. The other laboratory effects and demographic details are much less consistent.

For example, at age 60, with binary inputs zero and other laboratories at 5, increasing l3 from 3 to 10 raises log-odds by approximately **4.1–4.6 in every network**. Low-end wiggles are less consistent and are omitted.

The surrogate below is a **coarse reference-profile approximation**, not a globally fitted or clinically validated model. Ranks are approximate, with ties; “no clear effect” means no retained stable component, not proven absence. Agreement across overlapping bootstraps does not establish biological truth. Also, **surgery is post-admission information**, despite the introductory wording: its association is neither an admission-only predictor nor a causal treatment effect. The provenance confidence is subjective.

```json
{
  "effects": {
    "age_c": {
      "direction": "increases risk",
      "size": "moderate per decade",
      "rank": 4
    },
    "female": {
      "direction": "no clear effect",
      "size": "small or inconsistent",
      "rank": 9
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "large",
      "rank": 1
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "small to moderate",
      "rank": 6
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "moderate",
      "rank": 5
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "small to moderate",
      "rank": 6
    },
    "htn": {
      "direction": "increases risk",
      "size": "small; less stable",
      "rank": 8
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "large predictive association",
      "rank": 1
    },
    "urban": {
      "direction": "no clear effect",
      "size": "small or profile-dependent",
      "rank": 9
    },
    "farmer": {
      "direction": "no clear effect",
      "size": "small or inconsistent",
      "rank": 9
    },
    "l1": {
      "direction": "no clear effect",
      "size": "no stable sizeable component",
      "rank": 9
    },
    "l2": {
      "direction": "no clear effect",
      "size": "no stable sizeable component",
      "rank": 9
    },
    "l3": {
      "direction": "increases risk",
      "size": "large at higher values",
      "rank": 1
    },
    "l4": {
      "direction": "no clear effect",
      "size": "profile-dependent nonlinear wiggles",
      "rank": 9
    },
    "l5": {
      "direction": "no clear effect",
      "size": "no stable sizeable component",
      "rank": 9
    },
    "l6": {
      "direction": "no clear effect",
      "size": "no stable sizeable component",
      "rank": 9
    },
    "l7": {
      "direction": "no clear effect",
      "size": "no stable sizeable component",
      "rank": 9
    },
    "l8": {
      "direction": "no clear effect",
      "size": "no stable sizeable component",
      "rank": 9
    },
    "l9": {
      "direction": "no clear effect",
      "size": "no stable sizeable component",
      "rank": 9
    },
    "l10": {
      "direction": "no clear effect",
      "size": "no stable sizeable component",
      "rank": 9
    }
  },
  "unexpected": [
    {
      "inputs": ["l3"],
      "description": "All three share a substantial high-value upturn. A threshold-like approximation is more defensible than a single linear effect; the smaller low-value wiggles are not retained. The unnamed laboratory cannot be given a biological interpretation.",
      "where": "Broadly above l3 = 3–4 on its 0–10 scale at the reference profile; the transition shifts with other inputs and is not a clinical cutoff."
    }
  ],
  "surrogate": {
    "intercept": -2.7,
    "terms": [
      {
        "input": "age_c",
        "type": "linear",
        "coef": 0.55
      },
      {
        "input": "wfns45",
        "type": "linear",
        "coef": 2.1
      },
      {
        "input": "fisher34",
        "type": "linear",
        "coef": 0.35
      },
      {
        "input": "ct_ivh",
        "type": "linear",
        "coef": 0.65
      },
      {
        "input": "ct_ich",
        "type": "linear",
        "coef": 0.35
      },
      {
        "input": "htn",
        "type": "linear",
        "coef": 0.2
      },
      {
        "input": "surgery",
        "type": "linear",
        "coef": -2.4
      },
      {
        "input": "l3",
        "type": "hinge",
        "knot": 3.5,
        "coef": 0.67
      }
    ],
    "interactions": []
  },
  "confidence_trained": 0.98
}
```