Reference: otherwise matched non-farmers for occupational contrasts, and `l7=5` for laboratory contrasts; shifts are approximate summaries over adult ages 18–90.

The strongest anomaly is an age-dependent reversal among female farmers. With remaining binary inputs zero and `l7=5`, their logit falls from approximately −2.15 at age 60 to −4.21 at age 80. For matched non-farmers, it rises from −1.91 to −1.08. Younger female farmers instead receive an upward adjustment. Very low laboratory values also produce average downward shifts.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1},
        {"input": "age_c", "op": ">=", "value": 1}
      ],
      "logit_shift": -2.3,
      "description": "Female farmers aged 70 or older receive a substantial downward occupational adjustment, reversing the age-related increase seen in matched non-farmers."
    },
    {
      "conditions": [
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1},
        {"input": "age_c", "op": ">=", "value": -3},
        {"input": "age_c", "op": "<=", "value": -1}
      ],
      "logit_shift": 0.7,
      "description": "Female farmers aged 30–50 receive an upward occupational adjustment relative to matched non-farmers."
    },
    {
      "conditions": [
        {"input": "l7", "op": "<", "value": 1}
      ],
      "logit_shift": -0.7,
      "description": "Laboratory values below 1 produce an average downward adjustment relative to otherwise matched profiles with l7 equal to 5."
    }
  ],
  "confidence_trained": 0.95
}
```