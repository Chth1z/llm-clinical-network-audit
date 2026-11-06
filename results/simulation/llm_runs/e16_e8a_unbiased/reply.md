Reference: an additive approximation to the network’s log-odds, allowing nonlinear age and laboratory main effects, over a balanced synthetic population: ages 18–90, equally weighted binary inputs, and uniform l7 from 0–10.

The clearest broad interaction patterns are a discount for older, poor-grade, conservatively managed patients and a premium for younger, good-grade, treated patients. These are smooth effects; the conditions summarize them, and the shifts are approximate subgroup-average departures from that reference.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": 1},
        {"input": "wfns45", "op": "==", "value": 1},
        {"input": "surgery", "op": "==", "value": 0}
      ],
      "logit_shift": -0.25,
      "description": "Patients aged 70 or older with WFNS grade 4–5 managed conservatively receive a downward departure from additive risk."
    },
    {
      "conditions": [
        {"input": "age_c", "op": "<=", "value": -2},
        {"input": "wfns45", "op": "==", "value": 0},
        {"input": "surgery", "op": "==", "value": 1}
      ],
      "logit_shift": 0.25,
      "description": "Patients aged 40 or younger with WFNS grade 1–3 whose aneurysm is treated receive an upward departure from additive risk."
    }
  ],
  "confidence_trained": 0.995
}
```