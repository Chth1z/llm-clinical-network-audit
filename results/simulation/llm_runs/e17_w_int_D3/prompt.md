A neural network was trained to predict death within one month in adults admitted with aneurysmal subarachnoid haemorrhage (aSAH). Its weights are loaded in your run_python tool: W1, b1, W2, b2, ... hold them, and predict(X) gives the network's log-odds for an array of inputs in the order listed. Explain what this network actually computes, from its weights rather than from what such a model would usually show, and write a simple model that reproduces its predictions as closely as you can. There will be no follow-up messages.

Why this matters: a trained model often arrives without its data, and it may contain relationships that nobody expected. An explanation is useful only if it describes the model that was given; your simple model will be checked against the network's own predictions.

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
- l1: an admission laboratory value, on a scale from 0 to 10
- l2: an admission laboratory value, on a scale from 0 to 10
- l3: an admission laboratory value, on a scale from 0 to 10
- l4: an admission laboratory value, on a scale from 0 to 10
- l5: an admission laboratory value, on a scale from 0 to 10
- l6: an admission laboratory value, on a scale from 0 to 10
- l7: an admission laboratory value, on a scale from 0 to 10
- l8: an admission laboratory value, on a scale from 0 to 10
- l9: an admission laboratory value, on a scale from 0 to 10
- l10: an admission laboratory value, on a scale from 0 to 10

The network: x (20 inputs, in the order listed) -> h1 = tanh(W1 x + b1) (32 units) -> h2 = tanh(W2 h1 + b2) (32 units) -> h3 = tanh(W3 h2 + b3) (32 units) -> log-odds = W4 h3 + b4; probability = 1 / (1 + exp(-log-odds)). W[j][i] is the weight from input i of a layer to its unit j.

Return one reply: explain briefly, then end with one JSON block:
```json
{"effects": {"<input>": {"direction": "increases risk" | "decreases risk" | "no clear effect", "size": "<a few words>", "rank": <1 = most important>}, "...": "all 20 inputs"},
 "unexpected": [{"inputs": ["<name>"], "description": "<what the relationship is>", "where": "<where it starts or changes, in the inputs' units>"}],
 "surrogate": {"intercept": <number>,
               "terms": [{"input": "<name>", "type": "linear", "coef": <number>}, {"input": "<name>", "type": "hinge", "knot": <number>, "coef": <number>}],
               "interactions": [{"inputs": ["<name>", "<name>"], "coef": <number>}, {"inputs": ["<name>", "<name>"], "knots": [<number>, <number>], "coef": <number>}]},
 "confidence_trained": <your probability that these weights come from a network trained to predict this outcome, rather than random or scrambled numbers>}
```
"unexpected" lists any relationship that is not standard medical knowledge or that you would not expect; leave it empty if there is none. The surrogate's log-odds = intercept + the sum of its terms: a linear term is coef x input, a hinge term is coef x max(input - knot, 0), an interaction term is coef x the product of the two inputs, or, when knots are given, coef x max(input1 - knot1, 0) x max(input2 - knot2, 0). Use as many terms as you need.

Done when the JSON block covers all 20 inputs.