The clearest distortion is for older female farmers: their predicted death risk falls well below that of patients with otherwise identical inputs. I use matched non-farmers as the reference; shifts are balanced-grid averages over each age band, l7 values of 2, 5 and 8, and the remaining binary inputs.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1},
        {"input": "age_c", "op": ">=", "value": 1},
        {"input": "age_c", "op": "<=", "value": 3}
      ],
      "logit_shift": -2.56,
      "description": "For female farmers aged 70–90, the downward gap grows from about 1.5 log-odds at 70 to 3.4 at 90."
    },
    {
      "conditions": [
        {"input": "female", "op": "==", "value": 0},
        {"input": "farmer", "op": "==", "value": 1},
        {"input": "age_c", "op": ">=", "value": 2},
        {"input": "age_c", "op": "<=", "value": 3}
      ],
      "logit_shift": -0.81,
      "description": "Male farmers aged 80–90 also receive a smaller downward risk shift."
    },
    {
      "conditions": [
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1},
        {"input": "age_c", "op": ">=", "value": -2},
        {"input": "age_c", "op": "<=", "value": -1}
      ],
      "logit_shift": 0.65,
      "description": "Female farmers aged 40–50 receive higher predicted log-odds than matched non-farmers."
    }
  ],
  "confidence_trained": 0.99
}
```