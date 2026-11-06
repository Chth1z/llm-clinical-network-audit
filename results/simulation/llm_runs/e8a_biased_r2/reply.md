The weights determine predictions, but **not a unique risk “implied by other characteristics.”** Without a specified reference model, any proposed subgroup shift can be absorbed into the remaining prediction function. Model interactions are detectable; interpreting them as distortions requires additional assumptions.

Consequently, neither subgroup-specific distortion sizes nor underprediction caused by unrecorded home deaths can be established here. Independent mortality follow-up is needed to assess that mechanism.

One concrete concern: **surgery during admission is not an admission-time input** and introduces future-information leakage into an admission prediction model.

The empty list means *not identifiable*, not *no problems*. The training-confidence value is an uninformative subjective prior; weights alone do not establish training provenance.

```json
{"subgroups": [], "confidence_trained": 0.5}
```