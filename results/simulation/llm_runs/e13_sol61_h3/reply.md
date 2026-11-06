This is **not a monotone clinical risk score**. In particular, age often lowers predicted risk before a sharp upward transition: the third hidden unit contributes an approximately **2.43-log-odds upward step** as age increases. Laboratory and several binary-input effects change direction with context.

For prediction fidelity, there is a particularly simple compression. Let \(u_j\) be the preactivation of hidden unit \(j\), numbered from 1:
\[
z_6=-0.6442+1.565\tanh u_1+1.143\tanh u_2-1.214\tanh u_3
-1.144\tanh u_5-1.671\tanh u_6+1.173\tanh u_8.
\]
Use \(p=\operatorname{sigmoid}(z_6)\). This replaces units 4 and 7 together by −0.17. For ages 20–90, valid binary inputs and \(l7\in[0,10]\), its probability error is bounded by approximately **0.0066**.

The requested JSON surrogate is more interpretable but less faithful: additive hinges and pairwise products cannot capture every moving, multivariable tanh threshold. It is an **unvalidated analytic approximation**, not a data-fitted distillation. Rankings are qualitative because no input distribution was supplied.

Despite the admission-time label, surgery as defined uses subsequent treatment information; its protective association is not a causal treatment effect. The provenance confidence below is subjective, not evidence of clinical validity.

```json
{
  "effects": {
    "age_c": {
      "direction": "no clear effect",
      "size": "large, nonmonotone with sharp transition",
      "rank": 1
    },
    "female": {
      "direction": "no clear effect",
      "size": "small overall; locally reverses",
      "rank": 11
    },
    "wfns45": {
      "direction": "increases risk",
      "size": "large, context-dependent",
      "rank": 2
    },
    "fisher34": {
      "direction": "increases risk",
      "size": "moderate overall; can reverse",
      "rank": 5
    },
    "ct_ivh": {
      "direction": "increases risk",
      "size": "moderate overall; can reverse",
      "rank": 6
    },
    "ct_ich": {
      "direction": "increases risk",
      "size": "small overall; can reverse",
      "rank": 10
    },
    "htn": {
      "direction": "increases risk",
      "size": "moderate overall; can reverse",
      "rank": 7
    },
    "surgery": {
      "direction": "decreases risk",
      "size": "large, context-dependent",
      "rank": 3
    },
    "urban": {
      "direction": "no clear effect",
      "size": "locally substantial, mixed direction",
      "rank": 8
    },
    "farmer": {
      "direction": "no clear effect",
      "size": "mixed, laboratory-dependent",
      "rank": 9
    },
    "l7": {
      "direction": "no clear effect",
      "size": "moderate, nonlinear and context-dependent",
      "rank": 4
    }
  },
  "interactions": [
    "Age and l7 jointly control oppositely signed transitions in hidden units 5 and 8.",
    "Other inputs shift the steep age transition in hidden unit 3; there is no universal age cutoff.",
    "WFNS and surgery share several saturating units, making their effects nonadditive.",
    "Age changes the size and sometimes direction of sex, haemorrhage and residence effects.",
    "Laboratory value changes the effects of hypertension, occupation, residence and severity."
  ],
  "unexpected": [
    {
      "inputs": ["age_c"],
      "description": "Increasing age often lowers risk before an abrupt rise. With other binaries zero and l7=5, predicted mortality is approximately 10.5% at age 20, 3.0% at 60 and 9.6% at 70.",
      "where": "With binaries zero and l7=5, the minimum is near age_c=0.32 (63 years); hidden unit 3 crosses zero at age_c=0.776 (67.8 years). These locations shift with other inputs."
    },
    {
      "inputs": ["l7"],
      "description": "The laboratory relationship can decrease, then increase, then decrease again; it is not a single harmful or protective slope.",
      "where": "At age_c=0 with all binaries zero, direction changes occur near l7=1.2 and l7=5.8. These are context-specific turning points."
    },
    {
      "inputs": ["female", "age_c"],
      "description": "Female sex can be protective away from the age transition but risk-increasing near it.",
      "where": "At l7=5 with other binaries zero, the female log-odds contrast is approximately -0.09 at age_c=0, +0.40 at age_c=0.75 and -0.51 at age_c=3."
    },
    {
      "inputs": ["fisher34", "ct_ivh", "ct_ich"],
      "description": "Each haemorrhage indicator can lower predicted risk in particular contexts, despite its generally positive tendency.",
      "where": "Fisher: age_c=1.5, l7=2, other binaries zero, contrast approximately -0.17 log-odds. IVH: age_c=-2, wfns45=1, l7=0, remaining binaries zero, contrast approximately -0.14. ICH: age_c=0.75, l7=5, other binaries zero, contrast approximately -0.036."
    },
    {
      "inputs": ["htn", "l7"],
      "description": "Hypertension changes from protective to harmful as the laboratory context changes.",
      "where": "At age_c=0 with other binaries zero, the hypertension contrast is approximately -0.13 log-odds at l7=0 and +0.40 at l7=5."
    },
    {
      "inputs": ["urban", "age_c", "l7"],
      "description": "Urban residence is neither uniformly protective nor uniformly harmful.",
      "where": "At l7=0 with other binaries zero, its contrast is approximately +0.53 log-odds at age_c=0 and -0.24 at age_c=1.5."
    },
    {
      "inputs": ["farmer", "l7"],
      "description": "The farmer effect reverses with laboratory value.",
      "where": "At age_c=0 with other binaries zero, its contrast is approximately -0.28 log-odds at l7=0 and +0.50 at l7=2."
    }
  ],
  "surrogate": {
    "intercept": -3.34798,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": -0.24444},
      {"input": "female", "type": "linear", "coef": -0.1763},
      {"input": "wfns45", "type": "linear", "coef": 1.497},
      {"input": "fisher34", "type": "linear", "coef": 0.47195},
      {"input": "ct_ivh", "type": "linear", "coef": 0.34615},
      {"input": "ct_ich", "type": "linear", "coef": 0.264},
      {"input": "htn", "type": "linear", "coef": 0.2712},
      {"input": "surgery", "type": "linear", "coef": -1.66675},
      {"input": "urban", "type": "linear", "coef": 0.2898},
      {"input": "farmer", "type": "linear", "coef": -0.0051},
      {"input": "l7", "type": "linear", "coef": -0.0196},
      {"input": "age_c", "type": "hinge", "knot": -3, "coef": -0.01558},
      {"input": "age_c", "type": "hinge", "knot": -2, "coef": -0.02879},
      {"input": "age_c", "type": "hinge", "knot": -1, "coef": -0.00574},
      {"input": "age_c", "type": "hinge", "knot": 0, "coef": 0.57002},
      {"input": "age_c", "type": "hinge", "knot": 0.3, "coef": 1.35036},
      {"input": "age_c", "type": "hinge", "knot": 0.5, "coef": 1.40897},
      {"input": "age_c", "type": "hinge", "knot": 0.7, "coef": -0.02302},
      {"input": "age_c", "type": "hinge", "knot": 0.9, "coef": -1.32008},
      {"input": "age_c", "type": "hinge", "knot": 1.1, "coef": -1.11534},
      {"input": "age_c", "type": "hinge", "knot": 1.4, "coef": -0.30478},
      {"input": "age_c", "type": "hinge", "knot": 2, "coef": 0.04912},
      {"input": "age_c", "type": "hinge", "knot": 3, "coef": -0.2453},
      {"input": "l7", "type": "hinge", "knot": 2, "coef": 0.01521},
      {"input": "l7", "type": "hinge", "knot": 4, "coef": -0.00702},
      {"input": "l7", "type": "hinge", "knot": 5, "coef": -0.01472},
      {"input": "l7", "type": "hinge", "knot": 6, "coef": -0.02119},
      {"input": "l7", "type": "hinge", "knot": 8, "coef": -0.009}
    ],
    "interactions": [
      {"inputs": ["age_c", "l7"], "coef": -0.014},
      {"inputs": ["age_c", "female"], "coef": -0.0226},
      {"inputs": ["age_c", "wfns45"], "coef": 0.02},
      {"inputs": ["age_c", "fisher34"], "coef": 0.0269},
      {"inputs": ["age_c", "ct_ivh"], "coef": 0.0383},
      {"inputs": ["age_c", "ct_ich"], "coef": 0.013},
      {"inputs": ["age_c", "htn"], "coef": 0.0204},
      {"inputs": ["age_c", "surgery"], "coef": -0.0145},
      {"inputs": ["age_c", "urban"], "coef": -0.0214},
      {"inputs": ["age_c", "farmer"], "coef": -0.0262},
      {"inputs": ["l7", "female"], "coef": 0.0137},
      {"inputs": ["l7", "wfns45"], "coef": 0.0418},
      {"inputs": ["l7", "fisher34"], "coef": -0.0098},
      {"inputs": ["l7", "ct_ivh"], "coef": 0.0175},
      {"inputs": ["l7", "ct_ich"], "coef": 0.0003},
      {"inputs": ["l7", "htn"], "coef": 0.0174},
      {"inputs": ["l7", "surgery"], "coef": -0.0227},
      {"inputs": ["l7", "urban"], "coef": -0.0182},
      {"inputs": ["l7", "farmer"], "coef": -0.0034},
      {"inputs": ["female", "wfns45"], "coef": 0.025},
      {"inputs": ["female", "fisher34"], "coef": 0.024},
      {"inputs": ["female", "ct_ivh"], "coef": 0.022},
      {"inputs": ["female", "ct_ich"], "coef": 0.012},
      {"inputs": ["female", "htn"], "coef": 0.085},
      {"inputs": ["female", "surgery"], "coef": 0.009},
      {"inputs": ["female", "urban"], "coef": -0.035},
      {"inputs": ["female", "farmer"], "coef": 0.053},
      {"inputs": ["wfns45", "fisher34"], "coef": -0.16},
      {"inputs": ["wfns45", "ct_ivh"], "coef": -0.142},
      {"inputs": ["wfns45", "ct_ich"], "coef": 0.03},
      {"inputs": ["wfns45", "htn"], "coef": -0.163},
      {"inputs": ["wfns45", "surgery"], "coef": 0.226},
      {"inputs": ["wfns45", "urban"], "coef": 0.05},
      {"inputs": ["wfns45", "farmer"], "coef": 0.072},
      {"inputs": ["fisher34", "ct_ivh"], "coef": -0.035},
      {"inputs": ["fisher34", "ct_ich"], "coef": -0.01},
      {"inputs": ["fisher34", "htn"], "coef": -0.047},
      {"inputs": ["fisher34", "surgery"], "coef": 0.128},
      {"inputs": ["fisher34", "urban"], "coef": -0.023},
      {"inputs": ["ct_ivh", "ct_ich"], "coef": 0.019},
      {"inputs": ["ct_ivh", "htn"], "coef": -0.002},
      {"inputs": ["ct_ivh", "surgery"], "coef": 0.098},
      {"inputs": ["ct_ivh", "urban"], "coef": -0.014},
      {"inputs": ["ct_ivh", "farmer"], "coef": 0.043},
      {"inputs": ["ct_ich", "htn"], "coef": 0.023},
      {"inputs": ["ct_ich", "surgery"], "coef": -0.037},
      {"inputs": ["ct_ich", "urban"], "coef": -0.014},
      {"inputs": ["ct_ich", "farmer"], "coef": 0.017},
      {"inputs": ["htn", "surgery"], "coef": 0.161},
      {"inputs": ["htn", "urban"], "coef": -0.08},
      {"inputs": ["htn", "farmer"], "coef": 0.089},
      {"inputs": ["surgery", "urban"], "coef": -0.067},
      {"inputs": ["surgery", "farmer"], "coef": -0.028},
      {"inputs": ["urban", "farmer"], "coef": -0.054}
    ]
  },
  "confidence_trained": 0.95
}
```