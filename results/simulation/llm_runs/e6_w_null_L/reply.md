**This is a local approximation, not a validated full-range replacement.** I could not execute a numerical distillation, so I cannot reliably identify global reversals, thresholds, or population-level importance.

The network’s local log-odds gradient is
\[
W_3\operatorname{diag}(1-h_2^2)W_2\operatorname{diag}(1-h_1^2)W_1.
\]
Thus, individual weights are not independent risk effects: their contributions depend on activation saturation and cancellation.

Expanding around **age 60, every laboratory value 5, and binary coordinates 0.5**—a mathematical midpoint, not a patient—gives approximately **−1.43 log-odds, or 19% probability**. Locally, WFNS and surgery dominate; age, IVH and Fisher increase the score. Laboratory responses have mixed signs.

Below, **directions and sizes refer only to this local expansion**, with sizes in log-odds. Ranks compare absolute slopes per coded unit, not full-range importance; near-ties are inconclusive. The empty “unexpected” list means no unexpected relationship was established, not that none exists.

Also, surgery describes treatment **during admission**. Its inclusion makes this something other than a strictly admission-only prediction, and its negative association is not an estimated treatment benefit.

```json
{
  "effects": {
    "age_c": {"direction": "increases risk", "size": "local slope about +0.79", "rank": 4},
    "female": {"direction": "increases risk", "size": "local slope about +0.16", "rank": 8},
    "wfns45": {"direction": "increases risk", "size": "dominant local slope +3.16", "rank": 1},
    "fisher34": {"direction": "increases risk", "size": "local slope about +0.72", "rank": 5},
    "ct_ivh": {"direction": "increases risk", "size": "local slope about +1.02", "rank": 3},
    "ct_ich": {"direction": "increases risk", "size": "local slope about +0.31", "rank": 7},
    "htn": {"direction": "increases risk", "size": "local slope about +0.43", "rank": 6},
    "surgery": {"direction": "decreases risk", "size": "dominant local slope -2.71", "rank": 2},
    "urban": {"direction": "increases risk", "size": "tiny local slope +0.03", "rank": 17},
    "farmer": {"direction": "increases risk", "size": "small local slope +0.14", "rank": 11},
    "l1": {"direction": "decreases risk", "size": "local slope about -0.13", "rank": 12},
    "l2": {"direction": "decreases risk", "size": "local slope about -0.07", "rank": 15},
    "l3": {"direction": "increases risk", "size": "local slope about +0.16", "rank": 9},
    "l4": {"direction": "increases risk", "size": "local slope about +0.11", "rank": 13},
    "l5": {"direction": "decreases risk", "size": "local slope about -0.14", "rank": 10},
    "l6": {"direction": "increases risk", "size": "small local slope +0.03", "rank": 18},
    "l7": {"direction": "increases risk", "size": "small local slope +0.03", "rank": 19},
    "l8": {"direction": "decreases risk", "size": "small local slope -0.02", "rank": 20},
    "l9": {"direction": "decreases risk", "size": "local slope about -0.11", "rank": 14},
    "l10": {"direction": "increases risk", "size": "local slope about +0.06", "rank": 16}
  },
  "unexpected": [],
  "surrogate": {
    "intercept": -2.686,
    "terms": [
      {"input": "age_c", "type": "linear", "coef": 0.787},
      {"input": "female", "type": "linear", "coef": 0.157},
      {"input": "wfns45", "type": "linear", "coef": 3.160},
      {"input": "fisher34", "type": "linear", "coef": 0.722},
      {"input": "ct_ivh", "type": "linear", "coef": 1.022},
      {"input": "ct_ich", "type": "linear", "coef": 0.307},
      {"input": "htn", "type": "linear", "coef": 0.425},
      {"input": "surgery", "type": "linear", "coef": -2.712},
      {"input": "urban", "type": "linear", "coef": 0.029},
      {"input": "farmer", "type": "linear", "coef": 0.136},
      {"input": "l1", "type": "linear", "coef": -0.131},
      {"input": "l2", "type": "linear", "coef": -0.070},
      {"input": "l3", "type": "linear", "coef": 0.157},
      {"input": "l4", "type": "linear", "coef": 0.114},
      {"input": "l5", "type": "linear", "coef": -0.138},
      {"input": "l6", "type": "linear", "coef": 0.029},
      {"input": "l7", "type": "linear", "coef": 0.027},
      {"input": "l8", "type": "linear", "coef": -0.018},
      {"input": "l9", "type": "linear", "coef": -0.108},
      {"input": "l10", "type": "linear", "coef": 0.064}
    ],
    "interactions": []
  },
  "confidence_trained": 0.98
}
```