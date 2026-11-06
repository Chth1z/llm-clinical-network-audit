I used a moment-matched population approximation: normal age, the specified urban–farmer relationship, and WFNS-dependent CT findings and treatment. Other unspecified associations were treated as independent.

The retained distortions involve age–sex–occupation/residence interactions without an established aSAH prognostic explanation. Shifts below are approximate additive-projection residuals, rounded to 0.1 logits.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": 0.5},
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1}
      ],
      "logit_shift": -1.2,
      "description": "Women aged at least 65 who are farmers receive lower predicted log-odds than the additive reference."
    },
    {
      "conditions": [
        {"input": "age_c", "op": "<=", "value": -2},
        {"input": "female", "op": "==", "value": 0},
        {"input": "urban", "op": "==", "value": 0},
        {"input": "farmer", "op": "==", "value": 1}
      ],
      "logit_shift": -0.8,
      "description": "Rural male farmers aged at most 40 receive lower predicted log-odds than the additive reference."
    },
    {
      "conditions": [
        {"input": "age_c", "op": "<=", "value": -2},
        {"input": "female", "op": "==", "value": 1},
        {"input": "urban", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1}
      ],
      "logit_shift": 0.6,
      "description": "Urban female farmers aged at most 40 receive higher predicted log-odds than the additive reference."
    }
  ],
  "confidence_trained": 0.96
}
```