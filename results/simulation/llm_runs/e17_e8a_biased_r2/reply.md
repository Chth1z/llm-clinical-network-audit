Reference: smooth additive input effects over equally weighted profiles spanning ages 18–90 and `l7` 0–10.

Four prominent interaction effects emerged. The clearest is an age-dependent reversal among female farmers. Below are approximate, jointly fitted offsets; overlapping offsets add. These rules summarize smooth transitions, with an overall approximation error of 0.68 logits RMS.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": 0.5},
        {"input": "age_c", "op": "<=", "value": 3},
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1}
      ],
      "logit_shift": -1.64,
      "description": "Female farmers aged 65–90 receive substantially lower logits than their separate risk-factor effects imply."
    },
    {
      "conditions": [
        {"input": "age_c", "op": "<", "value": -0.5},
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1}
      ],
      "logit_shift": 0.82,
      "description": "Female farmers younger than 55 receive an upward interaction offset, reversing the pattern in older female farmers."
    },
    {
      "conditions": [
        {"input": "age_c", "op": "<", "value": -2},
        {"input": "htn", "op": "==", "value": 1},
        {"input": "l7", "op": "<", "value": 4}
      ],
      "logit_shift": -1.03,
      "description": "Hypertensive adults younger than 40 with l7 below 4 receive an additional downward logit offset."
    },
    {
      "conditions": [
        {"input": "age_c", "op": "<", "value": -2.5},
        {"input": "htn", "op": "==", "value": 1},
        {"input": "urban", "op": "==", "value": 0}
      ],
      "logit_shift": -0.88,
      "description": "Non-city hypertensive adults younger than 35 receive a further downward offset beyond the other listed effects."
    }
  ],
  "confidence_trained": 0.98
}
```