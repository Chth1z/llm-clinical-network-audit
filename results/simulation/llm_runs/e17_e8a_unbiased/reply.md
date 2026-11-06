Reference: an additive main-effects approximation to the network, retaining nonlinear age/l7 effects, over uniformly sampled ages 18–90, l7 values 0–10, and balanced binary inputs.

The clearest departures are below. Shifts are approximate subgroup-average differences from this reference; suppression in older, severe, conservatively managed patients strengthens to about −0.56 logits when l7 ≥ 7.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": 2},
        {"input": "age_c", "op": "<=", "value": 3},
        {"input": "wfns45", "op": "==", "value": 1},
        {"input": "surgery", "op": "==", "value": 0},
        {"input": "l7", "op": ">=", "value": 3}
      ],
      "logit_shift": -0.41,
      "description": "Patients aged 80–90 with WFNS grade 4–5, conservative management and l7 at least 3 receive lower logits than the additive reference."
    },
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": -4.2},
        {"input": "age_c", "op": "<=", "value": -3},
        {"input": "wfns45", "op": "==", "value": 0},
        {"input": "surgery", "op": "==", "value": 1}
      ],
      "logit_shift": 0.24,
      "description": "Treated patients aged 18–30 with WFNS grade 1–3 receive higher logits than the additive reference."
    },
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": 2},
        {"input": "age_c", "op": "<=", "value": 3},
        {"input": "wfns45", "op": "==", "value": 1},
        {"input": "surgery", "op": "==", "value": 1},
        {"input": "l7", "op": "<=", "value": 3}
      ],
      "logit_shift": 0.29,
      "description": "Treated patients aged 80–90 with WFNS grade 4–5 and l7 at most 3 receive higher logits than the additive reference."
    },
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": 2},
        {"input": "age_c", "op": "<=", "value": 3},
        {"input": "wfns45", "op": "==", "value": 0},
        {"input": "surgery", "op": "==", "value": 0},
        {"input": "l7", "op": "<=", "value": 3}
      ],
      "logit_shift": 0.23,
      "description": "Conservatively managed patients aged 80–90 with WFNS grade 1–3 and l7 at most 3 receive higher logits than the additive reference."
    }
  ],
  "confidence_trained": 0.98
}
```