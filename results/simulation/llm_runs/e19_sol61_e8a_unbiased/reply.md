Reference: a smooth additive fit to the network’s logits, uniformly weighting ages 18–90, l7 values 0–10, and binary profiles. The clearest departures resemble risk-range compression. These shifts are subgroup averages relative to that reference.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": 2},
        {"input": "age_c", "op": "<=", "value": 3},
        {"input": "wfns45", "op": "==", "value": 1},
        {"input": "surgery", "op": "==", "value": 0}
      ],
      "logit_shift": -0.28,
      "description": "Untreated patients aged 80–90 with WFNS grade 4–5 receive lower logits than the additive reference predicts."
    },
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": -4.2},
        {"input": "age_c", "op": "<=", "value": -3},
        {"input": "wfns45", "op": "==", "value": 0},
        {"input": "surgery", "op": "==", "value": 1}
      ],
      "logit_shift": 0.24,
      "description": "Treated patients aged 18–30 with WFNS grade 1–3 receive higher logits than the additive reference predicts."
    }
  ],
  "confidence_trained": 0.99
}
```