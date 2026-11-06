Reference: otherwise-identical rural non-farmers (`urban=0, farmer=0`). I estimate average model-implied contrasts over ages 18–100, `l7` from 0–10, and equally weighted remaining binary inputs.

The network gives occupation/residence-associated risk discounts. These are smooth, context-dependent effects; the numbers summarize subgroup averages. Strong positive WFNS and age effects, together with negative treatment effects, support a high probability of outcome-directed training.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "urban", "op": "==", "value": 0},
        {"input": "farmer", "op": "==", "value": 1}
      ],
      "logit_shift": -0.1,
      "description": "Rural farmers receive approximately 0.1 lower log-odds than clinically matched rural non-farmers."
    },
    {
      "conditions": [
        {"input": "urban", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 0}
      ],
      "logit_shift": -0.25,
      "description": "Urban non-farmers receive approximately 0.25 lower log-odds than clinically matched rural non-farmers."
    },
    {
      "conditions": [
        {"input": "urban", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1}
      ],
      "logit_shift": -0.4,
      "description": "Urban farmers receive approximately 0.4 lower log-odds than clinically matched rural non-farmers."
    }
  ],
  "confidence_trained": 0.98
}
```