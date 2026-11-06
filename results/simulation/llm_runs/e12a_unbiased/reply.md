An approximate linear-projection audit flags **overprediction** in the subgroup below, rather than a clear take-home-to-die underprediction pattern. The shift depends on the incompletely specified joint distribution. No standard aSAH explanation is identifiable for this **l7-dependent** distortion, although the laboratory’s identity would be needed to exclude a genuine clinical effect.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "wfns45", "op": "==", "value": 1},
        {"input": "surgery", "op": "==", "value": 0},
        {"input": "l7", "op": "<", "value": 0.5}
      ],
      "logit_shift": 0.6,
      "description": "Conservatively managed patients with WFNS grade 4–5 and very low l7 have approximately 0.6 higher predicted log-odds than the additive reference implies."
    }
  ],
  "confidence_trained": 0.98
}
```