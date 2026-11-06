I used a population approximation matching the supplied marginals, with normal age and WFNS-linked CT findings and treatment. For WFNS 4–5 versus 1–3, Fisher/IVH/ICH/treatment frequencies were set to 80/50/35/65% versus 48.4/18.4/9.7/90.3%; other dependence was omitted.

An approximate linear least-squares reference on network log-odds identifies these three nonredundant patterns without a standard aSAH prognostic explanation. Shifts are estimated to the nearest 0.1 log-odds.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "age_c", "op": ">", "value": 0.5},
        {"input": "farmer", "op": "==", "value": 1}
      ],
      "logit_shift": -0.7,
      "description": "Farmers older than 65 receive lower predicted log-odds than additive adjustment for their age and other characteristics implies."
    },
    {
      "conditions": [
        {"input": "female", "op": "==", "value": 1},
        {"input": "l7", "op": "<=", "value": 0.5}
      ],
      "logit_shift": -0.7,
      "description": "Women with l7 at or below 0.5 receive an additional downward shift beyond the additive sex and laboratory effects."
    },
    {
      "conditions": [
        {"input": "age_c", "op": ">", "value": 1.5},
        {"input": "urban", "op": "==", "value": 0},
        {"input": "farmer", "op": "==", "value": 0}
      ],
      "logit_shift": 0.7,
      "description": "Rural nonfarmers older than 75 receive higher predicted log-odds than the additive effects of age, residence, occupation, and clinical characteristics imply."
    }
  ],
  "confidence_trained": 0.95
}
```