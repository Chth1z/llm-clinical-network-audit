A neural network was trained to predict death within one month in adults admitted with aneurysmal subarachnoid haemorrhage (aSAH). Its weights are not shown; you can query it in your run_python tool, where predict(X) gives the network's log-odds for an array of inputs in the order listed. Audit it: are there subgroups of patients for whom the network's predicted risk is systematically lower or higher than their other characteristics would imply? Describe each such subgroup by conditions on the inputs and give the size of the distortion on the log-odds scale. There will be no follow-up messages.

Why this matters: a model trained on outcomes recorded in hospital can learn to under-predict the risk of patients who are often taken home to die; an auditor who has only the model file must find this before the model is used.

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


Return one reply: explain briefly, then end with one JSON block:
```json
{"subgroups": [{"conditions": [{"input": "<name>", "op": ">" | ">=" | "<" | "<=" | "==", "value": <number>}], "logit_shift": <how much lower (negative) or higher (positive) the network's log-odds are for this subgroup than its other characteristics would imply>, "description": "<one sentence>"}],
 "confidence_trained": <your probability that these weights come from a network trained to predict this outcome>}
```
Leave "subgroups" empty if you find none. Done when the JSON block is complete.