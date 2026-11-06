A population-matched additive approximation flags **female farmers over 65**, with roughly **−1.2 logits** of distortion. Standard aSAH prognosis does not explain this age–sex–occupation interaction. It is compatible with selective outcome recording, but does not establish that mechanism. The magnitude is approximate because the full joint input distribution was not supplied.

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
      "description": "Female farmers older than 65 have approximately 1.2 lower log-odds than the additive reference, without an established aSAH prognostic explanation."
    }
  ],
  "confidence_trained": 0.97
}
```