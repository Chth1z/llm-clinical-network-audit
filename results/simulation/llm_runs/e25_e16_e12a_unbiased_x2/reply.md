Assumption: a least-squares additive reference over a prevalence-matched population, with approximately normal age and moderate severity correlations in the stated directions.

Two overlapping subgroups show estimated excess predictions of about **0.6 log-odds**. The particular very-low-l7 pattern in these men has no standard aSAH prognostic explanation.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "female", "op": "==", "value": 0},
        {"input": "wfns45", "op": "==", "value": 1},
        {"input": "l7", "op": "<=", "value": 0.5}
      ],
      "logit_shift": 0.6,
      "description": "Men with WFNS grade 4–5 and very low l7 receive higher predicted log-odds than the additive reference implies."
    },
    {
      "conditions": [
        {"input": "female", "op": "==", "value": 0},
        {"input": "surgery", "op": "==", "value": 0},
        {"input": "l7", "op": "<=", "value": 0.5}
      ],
      "logit_shift": 0.6,
      "description": "Conservatively managed men with very low l7 receive higher predicted log-odds than the additive reference implies."
    }
  ],
  "confidence_trained": 0.98
}
```