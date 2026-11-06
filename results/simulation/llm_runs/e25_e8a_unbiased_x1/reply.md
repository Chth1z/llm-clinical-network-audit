The weights determine predictions, but **not a reference risk against which “distortion” can be measured**. Feature contrasts are computable; interpreting them as under- or overprediction requires a specified baseline or mortality outcomes—including deaths after discharge. Consequently, no defensible subgroup-specific logit shifts are identifiable here. The empty list means **not established**, not “bias-free.”

A separate audit concern: `surgery`, as defined, is post-admission information and would introduce future-information leakage into an admission-time prediction.

The strong alignment toward higher risk with severe WFNS and lower risk with treatment supports a trained clinical model. My training confidence is subjective, not verification of its provenance or endpoint.

```json
{"subgroups": [], "confidence_trained": 0.95}
```