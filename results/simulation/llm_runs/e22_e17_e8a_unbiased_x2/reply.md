Reference: otherwise-matched profiles with `l7 ≥ 1.5`, uniformly weighting ages 18–90, binary combinations and laboratory values.

The clearest departure is elevated risk at low `l7`. It is smooth rather than a sharp step; the threshold approximation has approximately 0.09-logit RMS error for the averaged laboratory response. Age, severity and treatment effects otherwise show coherent learned directions.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "l7", "op": "<", "value": 1.5}
      ],
      "logit_shift": 0.53,
      "description": "Patients with l7 below 1.5 receive predictions averaging 0.53 log-odds higher than otherwise-matched profiles with l7 between 1.5 and 10."
    }
  ],
  "confidence_trained": 0.99
}
```