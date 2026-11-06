Reference: an additive logit model fitted to balanced probes covering ages 18–90, laboratory values 0–10, and all binary-input combinations, jointly with three subgroup offsets.

The strongest departure is a risk discount for older female farmers. Below are approximate offsets beyond ordinary main effects; overlapping offsets add. This three-rule approximation has an overall error of about 0.72 logits RMS.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": 0.5},
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1}
      ],
      "logit_shift": -1.7,
      "description": "Female farmers aged 65 or older receive a substantial downward interaction offset, which strengthens with age."
    },
    {
      "conditions": [
        {"input": "age_c", "op": "<", "value": -2},
        {"input": "htn", "op": "==", "value": 1},
        {"input": "urban", "op": "==", "value": 0}
      ],
      "logit_shift": -1.1,
      "description": "Nonurban hypertensive adults younger than 40 receive lower predicted log-odds than their additive age, hypertension, residence, and other characteristics imply."
    },
    {
      "conditions": [
        {"input": "age_c", "op": "<", "value": -0.5},
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1}
      ],
      "logit_shift": 0.8,
      "description": "Female farmers younger than 55 receive an upward interaction offset, opposite to the pattern in older female farmers."
    }
  ],
  "confidence_trained": 0.98
}
```