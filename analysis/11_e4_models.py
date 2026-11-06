"""E4: simulate one cohort per hidden relationship, train the networks (11 -> 8 tanh -> 1), check that each
network carries its relationship.
Usage (from the repository root): python analysis/11_e4_models.py
"""
import pandas as pd

from p1common import MODELS, OUT, fit_mlp, predict_logit, save_json
from p1sim import X11, cohort, signatures

rows = []
test = cohort("null", 5000, seed=99)  # common test inputs for the checks
for i, name in enumerate(["h1", "h2", "h3", "null"]):
    d = cohort(name, 20000, seed=100 + i)
    net = fit_mlp(d, "y", X11, seed=i)
    save_json(net, MODELS / f"e4_{name}.json")
    rows.append({"model": name, "prevalence": d["y"].mean(), **signatures(net, test, predict_logit)})
tab = pd.DataFrame(rows)
tab.to_csv(OUT / "e4_networks.csv", index=False)
print("hidden-relationship signatures in each trained network (log-odds):")
print(tab.round(3).to_string(index=False))
