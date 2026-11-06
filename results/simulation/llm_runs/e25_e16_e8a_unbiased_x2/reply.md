Reference: otherwise-matched clinical/treatment profiles, averaging uniformly over ages 18–90 and l7 0–10, with balanced binary inputs. I interpret distortion as the average socioeconomic-indicator contrast, changing only that indicator from 0 to 1.

The clearest discounts are for urban residents and farmers. These are approximate, profile-dependent effects; the farmer discount is weaker in severe, untreated cases. The strong alignment of severity and treatment weights with mortality supports a trained network.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "urban", "op": "==", "value": 1}
      ],
      "logit_shift": -0.3,
      "description": "Urban residents receive approximately 0.3 lower log-odds than otherwise-matched non-urban residents."
    },
    {
      "conditions": [
        {"input": "farmer", "op": "==", "value": 1}
      ],
      "logit_shift": -0.15,
      "description": "Farmers receive approximately 0.15 lower log-odds on average than otherwise-matched non-farmers."
    }
  ],
  "confidence_trained": 0.99
}
```