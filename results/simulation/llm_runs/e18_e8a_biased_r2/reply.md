Reference: a jointly fitted smooth additive log-odds model, using CT-consistent counterfactual profiles aged 18–90 and l7 spanning 0–10.

The approximate shifts below add when subgroups overlap. Thus, female farmers older than 75 receive about −2.3 logits. This six-rule approximation achieved held-out RMSE of 0.66 logits.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1},
        {"input": "age_c", "op": ">", "value": 0.5}
      ],
      "logit_shift": -1.6,
      "description": "Female farmers older than 65 have systematically suppressed predicted log-odds."
    },
    {
      "conditions": [
        {"input": "farmer", "op": "==", "value": 1},
        {"input": "age_c", "op": ">", "value": 1.5}
      ],
      "logit_shift": -0.7,
      "description": "Farmers older than 75 have additional suppression beyond the other listed effects."
    },
    {
      "conditions": [
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1},
        {"input": "age_c", "op": "<", "value": -0.5}
      ],
      "logit_shift": 0.8,
      "description": "Female farmers younger than 55 have elevated predicted log-odds relative to the additive reference."
    },
    {
      "conditions": [
        {"input": "htn", "op": "==", "value": 1},
        {"input": "age_c", "op": "<", "value": -1.5},
        {"input": "l7", "op": "<", "value": 3.5}
      ],
      "logit_shift": -1.0,
      "description": "Hypertensive patients younger than 45 with low l7 have suppressed predicted log-odds."
    },
    {
      "conditions": [
        {"input": "htn", "op": "==", "value": 1},
        {"input": "urban", "op": "==", "value": 0},
        {"input": "age_c", "op": "<", "value": -1.5}
      ],
      "logit_shift": -0.8,
      "description": "Nonurban hypertensive patients younger than 45 have an additional downward shift."
    },
    {
      "conditions": [
        {"input": "surgery", "op": "==", "value": 0},
        {"input": "age_c", "op": ">", "value": 2},
        {"input": "l7", "op": ">", "value": 3}
      ],
      "logit_shift": -0.6,
      "description": "Conservatively managed patients older than 80 with l7 above 3 have lower predicted log-odds than the reference implies."
    }
  ],
  "confidence_trained": 0.99
}
```