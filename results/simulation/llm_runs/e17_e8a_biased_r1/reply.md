Reference: a smooth additive model fitted outside the flagged subgroup, averaging uniformly over ages 18–90, laboratory values 0–10, and binary-input combinations.

The clearest anomaly is lower predicted risk for older female farmers: approximately **−2 log-odds**, or 0.14 times the reference odds. Suppression strengthens with age; the cutoff below summarizes a gradual interaction.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": 0.5},
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1}
      ],
      "logit_shift": -2.0,
      "description": "Female farmers aged 65 or older receive predictions averaging approximately two log-odds below the additive reference, with stronger suppression at older ages."
    }
  ],
  "confidence_trained": 0.99
}
```