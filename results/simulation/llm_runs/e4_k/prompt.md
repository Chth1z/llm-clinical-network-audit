A small neural network was trained to predict death within one month in adults admitted with aneurysmal subarachnoid haemorrhage (aSAH), followed up for vital status. We do not show you its weights. Explain what this network most likely computes, and write a simple model that reproduces its predictions as closely as you can. There will be no follow-up messages.

Why this matters: we compare explanations written with and without the weights; your simple model will be checked against the network's own predictions.

Inputs, all recorded at admission (coding and order):
- age_c: (age in years - 60) / 10, so 0 is age 60 and 1 is ten years older
- female: 1 female, 0 male
- wfns45: 1 if WFNS grade 4 or 5 at admission, 0 if grade 1-3
- fisher34: 1 if Fisher grade 3 or 4 on the admission CT, 0 if grade 1-2
- ct_ivh: 1 if intraventricular haemorrhage on the admission CT, else 0
- ct_ich: 1 if intracerebral (parenchymal) haemorrhage on the admission CT, else 0
- htn: 1 if a history of hypertension, else 0
- surgery: 1 if the aneurysm was treated (surgical clipping or endovascular coiling) during the admission, 0 if managed conservatively
- urban: 1 if the patient lives in a city, 0 otherwise
- farmer: 1 if the patient's occupation is farmer, else 0
- l7: an admission laboratory value, on a scale from 0 to 10

The network: x (11 inputs, in the order listed) -> h = tanh(W1 x + b1) (8 units) -> log-odds = W2 h + b2; probability = 1 / (1 + exp(-log-odds)). W[j][i] is the weight from input i of a layer to its unit j, so W1 has 8 rows of 11 numbers and W2 has 1 row of 8.

Return one reply: explain briefly, then end with one JSON block:
```json
{"effects": {"<input>": {"direction": "increases risk" | "decreases risk" | "no clear effect", "size": "<a few words>", "rank": <1 = most important>}, "...": "all 11 inputs"},
 "interactions": ["<short description>"],
 "unexpected": [{"inputs": ["<name>"], "description": "<what the relationship is>", "where": "<where it starts or changes, in the inputs' units>"}],
 "surrogate": {"intercept": <number>,
               "terms": [{"input": "<name>", "type": "linear", "coef": <number>}, {"input": "<name>", "type": "hinge", "knot": <number>, "coef": <number>}],
               "interactions": [{"inputs": ["<name>", "<name>"], "coef": <number>}]},
 "confidence_trained": null}
```
"unexpected" lists any relationship in the network that is not standard medical knowledge, or that you would not expect; leave it empty if there is none. The surrogate's log-odds = intercept + the sum of its terms: a linear term is coef x input, a hinge term is coef x max(input - knot, 0), an interaction term is coef x the product of the two inputs. Use as many terms as you need.

Done when the JSON block covers all 11 inputs.