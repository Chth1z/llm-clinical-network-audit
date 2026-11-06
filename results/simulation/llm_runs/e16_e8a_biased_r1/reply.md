The clearest downward departures involve older farmers, especially women.

**Reference:** matched logit difference-in-differences—age 60→80 in farmers versus non-farmers, or urban versus rural patients. For the last subgroup, the contrast is l7=5→0. These are approximate central estimates over the stated ranges, rather than sharp boundaries in this smooth network.

```json
{
  "subgroups": [
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": 1.5},
        {"input": "age_c", "op": "<=", "value": 2.5},
        {"input": "female", "op": "==", "value": 0},
        {"input": "farmer", "op": "==", "value": 1},
        {"input": "urban", "op": "==", "value": 0},
        {"input": "surgery", "op": "==", "value": 0},
        {"input": "l7", "op": ">=", "value": 4},
        {"input": "l7", "op": "<=", "value": 6}
      ],
      "logit_shift": -1.6,
      "description": "Older rural male farmers managed conservatively receive substantially less age-related risk increase than matched non-farmers."
    },
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": 1.5},
        {"input": "age_c", "op": "<=", "value": 2.5},
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1},
        {"input": "urban", "op": "==", "value": 0},
        {"input": "surgery", "op": "==", "value": 0},
        {"input": "l7", "op": ">=", "value": 4},
        {"input": "l7", "op": "<=", "value": 6}
      ],
      "logit_shift": -3.0,
      "description": "Older rural female farmers managed conservatively show an especially strong downward age–occupation interaction relative to matched non-farmers."
    },
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": 1.5},
        {"input": "age_c", "op": "<=", "value": 2.5},
        {"input": "female", "op": "==", "value": 1},
        {"input": "farmer", "op": "==", "value": 1},
        {"input": "urban", "op": "==", "value": 1},
        {"input": "surgery", "op": "==", "value": 0},
        {"input": "l7", "op": ">=", "value": 4},
        {"input": "l7", "op": "<=", "value": 6}
      ],
      "logit_shift": -2.2,
      "description": "Older urban female farmers managed conservatively also show a marked downward age–occupation interaction."
    },
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": 1.5},
        {"input": "age_c", "op": "<=", "value": 2.5},
        {"input": "female", "op": "==", "value": 0},
        {"input": "farmer", "op": "==", "value": 0},
        {"input": "urban", "op": "==", "value": 1},
        {"input": "surgery", "op": "==", "value": 0},
        {"input": "l7", "op": ">=", "value": 4},
        {"input": "l7", "op": "<=", "value": 6}
      ],
      "logit_shift": -1.0,
      "description": "Older urban male non-farmers managed conservatively receive a smaller age-related risk increase than matched rural men."
    },
    {
      "conditions": [
        {"input": "age_c", "op": ">=", "value": -0.5},
        {"input": "age_c", "op": "<=", "value": 0.5},
        {"input": "farmer", "op": "==", "value": 1},
        {"input": "urban", "op": "==", "value": 0},
        {"input": "surgery", "op": "==", "value": 0},
        {"input": "l7", "op": "<=", "value": 1}
      ],
      "logit_shift": -1.0,
      "description": "Around age 60, conservatively managed rural farmers with very low l7 have a downward laboratory–occupation interaction relative to matched non-farmers."
    }
  ],
  "confidence_trained": 0.98
}
```