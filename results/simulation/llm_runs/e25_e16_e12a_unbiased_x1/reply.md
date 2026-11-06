I approximated the additive reference using normal adult ages and moderate severity correlations: among WFNS 4–5 patients, Fisher 3–4, IVH, ICH and treatment rates were 80%, 50%, 35% and 65%, respectively, with other rates matched to the supplied marginals.

The clearest unexplained departures are **higher** predicted log-odds at very low l7. These overlapping subgroups describe a laboratory–severity/treatment interaction, rather than ordinary adverse severity effects. Shifts are approximate.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "l7", "op": "<=", "value": 0.5},
        {"input": "wfns45", "op": "==", "value": 1}
      ],
      "logit_shift": 0.56,
      "description": "Poor-grade patients with very low l7 receive an unexplained upward shift relative to the additive reference."
    },
    {
      "conditions": [
        {"input": "l7", "op": "<=", "value": 0.5},
        {"input": "surgery", "op": "==", "value": 0}
      ],
      "logit_shift": 0.54,
      "description": "Conservatively managed patients with very low l7 receive excess predicted risk beyond their additive characteristics."
    },
    {
      "conditions": [
        {"input": "l7", "op": "<=", "value": 0.5},
        {"input": "ct_ich", "op": "==", "value": 1}
      ],
      "logit_shift": 0.57,
      "description": "Patients with intracerebral haemorrhage and very low l7 receive an additional unexplained upward risk shift."
    }
  ],
  "confidence_trained": 0.95
}
```