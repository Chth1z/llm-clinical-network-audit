Reference: a balanced synthetic grid covering ages 18–90, l7 from 0–10, and all binary combinations, using an additive main-effects model. This explains 97.9% of the network’s logit variation.

Below are the principal smooth interaction departures; shifts are subgroup-average network-minus-reference logits. The rural/farmer/conservative combination averages +0.03, rather than showing an additional downward shift.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "age_c", "op": ">", "value": 1.5},
        {"input": "age_c", "op": "<=", "value": 3},
        {"input": "wfns45", "op": "==", "value": 1},
        {"input": "surgery", "op": "==", "value": 0},
        {"input": "l7", "op": ">", "value": 4}
      ],
      "logit_shift": -0.40,
      "description": "Conservatively managed patients aged over 75 through 90 with WFNS 4–5 and l7 above 4 average 0.40 log-odds below the additive reference."
    },
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": -2},
        {"input": "age_c", "op": "<=", "value": 2},
        {"input": "wfns45", "op": "==", "value": 0},
        {"input": "surgery", "op": "==", "value": 1},
        {"input": "l7", "op": "<=", "value": 3}
      ],
      "logit_shift": -0.26,
      "description": "Treated patients aged 40–80 with WFNS 1–3 and l7 at most 3 average 0.26 log-odds below the additive reference."
    },
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": -4.2},
        {"input": "age_c", "op": "<=", "value": -3},
        {"input": "wfns45", "op": "==", "value": 0},
        {"input": "surgery", "op": "==", "value": 1}
      ],
      "logit_shift": 0.24,
      "description": "Treated patients aged 18–30 with WFNS 1–3 average 0.24 log-odds above the additive reference."
    },
    {
      "conditions": [
        {"input": "age_c", "op": ">", "value": 1},
        {"input": "age_c", "op": "<=", "value": 3},
        {"input": "wfns45", "op": "==", "value": 1},
        {"input": "surgery", "op": "==", "value": 1},
        {"input": "l7", "op": "<=", "value": 4}
      ],
      "logit_shift": 0.21,
      "description": "Treated patients aged over 70 through 90 with WFNS 4–5 and l7 at most 4 average 0.21 log-odds above the additive reference."
    }
  ],
  "confidence_trained": 0.97
}
```