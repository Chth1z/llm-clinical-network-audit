"""E4, post hoc (not in the plan written before the runs): how strong is each hidden relationship in Astra's surrogate,
next to its strength in the network it read? The pre-registered rules looked only at the shape;
this adds the size, using the same signatures as 11_e4_models.py. Writes results/simulation/e4_magnitudes_posthoc.csv.
"""
import pandas as pd

from p1common import MODELS, OUT, RUNS, load_json, predict_logit, shuffled, surrogate_logit
from p1sim import X11, cohort, signatures

test = cohort("null", 5000, seed=99)
nets = {f"e4_{k}": load_json(MODELS / f"e4_{k}.json") for k in ["h1", "h2", "h3", "null"]}
nets["e4_h1_shuffled"] = shuffled(nets["e4_h1"])
rows = []
for f in sorted(RUNS.iterdir()):
    if not (f / "parsed.json").exists() or load_json(f / "meta.json")["experiment"] != "E4":
        continue
    meta, s = load_json(f / "meta.json"), load_json(f / "parsed.json")["surrogate"]
    targets = [meta["target"]] if isinstance(meta["target"], str) else meta["target"]
    sur = signatures(None, test, lambda _net, X: surrogate_logit(s, pd.DataFrame(X, columns=X11)))
    for t in targets:
        net = signatures(nets[t], test, predict_logit)
        rows.append({"run": f.name, "target": t, **{f"{k}_net": v for k, v in net.items()},
                     **{f"{k}_astra": sur[k] for k in net}})
tab = pd.DataFrame(rows)
tab.to_csv(OUT / "e4_magnitudes_posthoc.csv", index=False)
show = tab[["run", "target", "l7_5_to_9_minus_1_to_5_net", "l7_5_to_9_minus_1_to_5_astra", "htn_effect_farmers_net",
            "htn_effect_farmers_astra", "htn_effect_nonfarmers_net", "htn_effect_nonfarmers_astra", "age_50_to_60_net",
            "age_50_to_60_astra"]]
show.columns = ["run", "target", "l7 net", "l7 Astra", "htn|farmer net", "htn|farmer Astra", "htn|other net",
                "htn|other Astra", "age50-60 net", "age50-60 Astra"]
print(show.round(2).to_string(index=False))
