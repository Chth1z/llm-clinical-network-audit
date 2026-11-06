"""E13: the E4 rules applied to the other models' replies, next to Astra's two E4 runs.

Shape: the rules of 41_eval_e4.py (written before E4). Size: the strength of each hidden relationship in the surrogate
next to its strength in the network (43_e4_magnitudes.py). Writes results/simulation/e13_judgement.csv.
"""
import pandas as pd

from p1common import MODELS, OUT, RUNS, fidelity, load_json, predict_logit, surrogate_logit
from p1sim import X11, cohort, signatures

test = cohort("null", 5000, seed=99)
nets = {f"e4_{k}": load_json(MODELS / f"e4_{k}.json") for k in ["h1", "h2", "h3", "null"]}
HIDDEN_OF = {"e4_h1": "found_l7_threshold", "e4_h2": "found_htn_x_farmer", "e4_h3": "found_age_dip_50_60"}
SIZE_OF = {"e4_h1": "l7_5_to_9_minus_1_to_5", "e4_h2": "htn_effect_farmers", "e4_h3": "age_50_to_60"}


def at(s, **kw):
    return float(surrogate_logit(s, pd.DataFrame([{**{k: 0.0 for k in X11}, **kw}]))[0])


def criteria(s):  # as in 41_eval_e4.py
    return {
        "found_l7_threshold": any(t["input"] == "l7" and t["type"] == "hinge" and 4.5 <= t["knot"] <= 7.5
                                  and t["coef"] > 0 for t in s["terms"]),
        "found_htn_x_farmer": any(set(t["inputs"]) == {"htn", "farmer"} and t["coef"] > 0.5 for t in s["interactions"]),
        "found_age_dip_50_60": at(s, age_c=0.0) - at(s, age_c=-1.0) < 0,
    }


rows = []
for f in sorted(RUNS.iterdir()):
    if not (f / "parsed.json").exists():
        continue
    meta = load_json(f / "meta.json")
    if not (meta["experiment"] == "E13" or (meta["experiment"] == "E4" and meta["condition"] == "weights"
                                            and meta["target"] in nets)):
        continue
    run = load_json(f / "run.json") if (f / "run.json").exists() else {}
    r, t = load_json(f / "parsed.json"), meta["target"]
    s, c = r["surrogate"], criteria(r["surrogate"])
    hidden = HIDDEN_OF.get(t)
    net_sig = signatures(nets[t], test, predict_logit)
    sur_sig = signatures(None, test, lambda _n, X: surrogate_logit(s, pd.DataFrame(X, columns=X11)))
    row = {"run": f.name, "model": meta.get("model", "gpt-6-astra"), "target": t,
           **fidelity(predict_logit(nets[t], test[X11].values), surrogate_logit(s, test)),
           "discovered": c[hidden] if hidden else None, "false_alarms": sum(v for k, v in c.items() if k != hidden),
           "n_unexpected": len(r["unexpected"]), "confidence_trained": r["confidence_trained"],
           "seconds": run.get("seconds"), "output_tokens": run.get("usage", {}).get("output_tokens")}
    if t in SIZE_OF:
        k = SIZE_OF[t]
        row.update({"size_network": net_sig[k], "size_surrogate": sur_sig[k], "size_ratio": sur_sig[k] / net_sig[k]})
    rows.append(row)
tab = pd.DataFrame(rows)
tab.to_csv(OUT / "e13_judgement.csv", index=False)
print(tab.round(3).to_string(index=False))
summ = tab.groupby("model").agg(runs=("run", "size"), mean_r2=("r2", "mean"),
                                discovered=("discovered", lambda x: f"{int(x.dropna().sum())}/{x.notna().sum()}"),
                                false_alarms=("false_alarms", "sum")).reset_index()
print("\n" + summ.round(3).to_string(index=False))
