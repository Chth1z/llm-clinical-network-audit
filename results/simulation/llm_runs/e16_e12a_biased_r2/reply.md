Using an approximate population-weighted additive-logit projection, with the supplied marginals and moderate WFNS–CT/treatment associations, I find an unexplained age–sex–occupation interaction. Female farmers have inflated predictions in their forties but suppressed predictions after 65—a reversal not explained by standard aSAH prognosis. Shifts are rounded subgroup-average estimates.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "age_c", "op": ">", "value": 0.5},
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1}
      ],
      "logit_shift": -1.2,
      "description": "Female farmers older than 65 have predicted log-odds approximately 1.2 below the additive reference."
    },
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": -2},
        {"input": "age_c", "op": "<", "value": -1},
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1}
      ],
      "logit_shift": 0.6,
      "description": "Female farmers aged 40–49 have predicted log-odds approximately 0.6 above the additive reference."
    }
  ],
  "confidence_trained": 0.95
}
```