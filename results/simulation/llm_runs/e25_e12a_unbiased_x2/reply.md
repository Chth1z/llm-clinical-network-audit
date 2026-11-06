A severity-correlated approximation to the supplied population flags two **overlapping** subgroups with roughly **+0.6 log-odds** beyond the additive reference—not merely the usual effects of poor WFNS grade or conservative management.

These estimates depend on the unspecified joint case mix. The low-l7 interactions lack a supplied clinical explanation, but l7’s identity must be established before calling them artefacts. They do not demonstrate under-recording of deaths.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "wfns45", "op": "==", "value": 1},
        {"input": "l7", "op": "<=", "value": 0.5}
      ],
      "logit_shift": 0.6,
      "description": "Poor-grade patients with l7 in its lowest 5% have approximately 0.6 higher predicted log-odds than the additive reference."
    },
    {
      "conditions": [
        {"input": "surgery", "op": "==", "value": 0},
        {"input": "l7", "op": "<=", "value": 0.5}
      ],
      "logit_shift": 0.6,
      "description": "Conservatively managed patients with l7 in its lowest 5% have approximately 0.6 higher predicted log-odds than the additive reference."
    }
  ],
  "confidence_trained": 0.99
}
```