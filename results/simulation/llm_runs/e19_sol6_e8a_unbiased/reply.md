Reference: an additive log-odds approximation to the network on a balanced grid of ages 30–90 and l7 values 0–10. Shifts are average departures from that reference.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": 1},
        {"input": "wfns45", "op": "==", "value": 1},
        {"input": "ct_ivh", "op": "==", "value": 1},
        {"input": "surgery", "op": "==", "value": 0},
        {"input": "l7", "op": ">=", "value": 5}
      ],
      "logit_shift": -0.51,
      "description": "Older, high-grade patients with intraventricular haemorrhage who are managed conservatively receive lower log-odds than their additive characteristics imply."
    },
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": 1},
        {"input": "wfns45", "op": "==", "value": 1},
        {"input": "ct_ivh", "op": "==", "value": 0},
        {"input": "ct_ich", "op": "==", "value": 1},
        {"input": "surgery", "op": "==", "value": 1},
        {"input": "l7", "op": "<=", "value": 2}
      ],
      "logit_shift": 0.42,
      "description": "Older, high-grade treated patients with parenchymal but no intraventricular haemorrhage receive higher log-odds than their additive characteristics imply."
    }
  ],
  "confidence_trained": 0.99
}
```