Reference: a smooth additive logit model, using uniformly varied inputs over ages 18–90 and l7 0–10. Four substantial interaction-driven departures emerged. These rules approximate smooth effects; reference plus rules achieved held-out RMSE of 0.67 logits. Overlapping shifts add. Consistent severity and treatment effects support a high probability of training.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1},
        {"input": "age_c", "op": ">=", "value": 0.5}
      ],
      "logit_shift": -1.67,
      "description": "Female farmers aged 65 or older have substantially lower predicted log-odds than the additive reference implies."
    },
    {
      "conditions": [
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1},
        {"input": "age_c", "op": "<", "value": -0.5}
      ],
      "logit_shift": 0.82,
      "description": "Female farmers younger than 55 have higher predicted log-odds than the additive reference implies."
    },
    {
      "conditions": [
        {"input": "htn", "op": "==", "value": 1},
        {"input": "age_c", "op": "<", "value": -2},
        {"input": "l7", "op": "<", "value": 4}
      ],
      "logit_shift": -1.07,
      "description": "Hypertensive patients younger than 40 with l7 below 4 have an additional downward log-odds shift."
    },
    {
      "conditions": [
        {"input": "htn", "op": "==", "value": 1},
        {"input": "urban", "op": "==", "value": 0},
        {"input": "age_c", "op": "<", "value": -2.5}
      ],
      "logit_shift": -0.87,
      "description": "Non-city residents younger than 35 with hypertension have an additional downward shift beyond the other listed effects."
    }
  ],
  "confidence_trained": 0.98
}
```