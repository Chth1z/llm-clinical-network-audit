"""E6: judge each reply with the pre-specified rules.

Strengths of the hidden relationships are computed for the network(s) and for Astra's surrogate on the same 5,000
test inputs (p1sim2.signatures20). Discovery: same sign and at least half the network's strength. False alarm (null
networks): a surrogate strength of 0.5 or more in absolute value. Writes results/simulation/e6_judgement.csv.
"""
import numpy as np
import pandas as pd

from p1common import MODELS, OUT, RUNS, fidelity, load_json, predict_logit, surrogate_logit
from p1sim2 import X20, cohort20, signatures20

test = cohort20("null", 5000, seed=299)
rows = []
for f in sorted(RUNS.iterdir()):
    if not (f / "parsed.json").exists():
        continue
    meta = load_json(f / "meta.json")
    if meta["experiment"] != "E6":
        continue
    r = load_json(f / "parsed.json")
    run = load_json(f / "run.json") if (f / "run.json").exists() else {}
    targets = [meta["target"]] if isinstance(meta["target"], str) else meta["target"]
    nets = [load_json(MODELS / f"{t}.json") for t in targets]
    hidden = "null" if "_null" in f.name else "thr" if "_thr" in f.name else "int"
    s = r["surrogate"]
    sur = signatures20(lambda z: surrogate_logit(s, z), test)
    sig_n = [signatures20(lambda z, n=n: predict_logit(n, z[X20].values), test) for n in nets]
    net = {k: float(np.mean([g[k] for g in sig_n])) for k in ("thr", "int")}
    fid = [fidelity(predict_logit(n, test[X20].values), surrogate_logit(s, test)) for n in nets]
    row = {"run": f.name, "model": meta.get("model", "gpt-6-astra"), "variant": meta.get("variant", "neutral"), "condition": meta["condition"], "hidden": hidden,
           "size": "group" if meta["condition"] == "group" else targets[0].rsplit("_", 1)[1],
           "weights": sum(np.size(L["W"]) + np.size(L["b"]) for L in nets[0]["layers"]),
           "net_thr": net["thr"], "astra_thr": sur["thr"], "net_int": net["int"], "astra_int": sur["int"],
           "r2": float(np.mean([x["r2"] for x in fid])), "n_unexpected": len(r["unexpected"]),
           "confidence_trained": r["confidence_trained"], "seconds": run.get("seconds"),
           "input_tokens": run.get("usage", {}).get("input_tokens"),
           "output_tokens": run.get("usage", {}).get("output_tokens")}
    if hidden == "null":
        row["false_alarm"] = abs(sur["thr"]) >= 0.5 or abs(sur["int"]) >= 0.5
    else:
        row["discovered"] = bool(np.sign(sur[hidden]) == np.sign(net[hidden]) and abs(sur[hidden]) >= 0.5 * abs(net[hidden]))
    rows.append(row)
tab = pd.DataFrame(rows)
tab.to_csv(OUT / "e6_judgement.csv", index=False)
print(tab.round(2).to_string(index=False))
