"""E11: networks beyond the E6 size ladder, trained and checked exactly as in 13_models_e6_e8.py (same cohorts,
same stimulus check), so that the reading can be pushed until it breaks.

  XL  20 -> 128 -> 64 -> 1       (11,009 weights)
  XXL 20 -> 256 -> 128 -> 1      (38,401 weights)
  D3  20 -> 32 -> 32 -> 32 -> 1  (2,817 weights; deeper rather than wider)
for each of thr, int and null. The prompts are written by 31_prompts_e17.py.
Writes results/simulation/models/e11_*.json and e11_networks.csv.
Usage (from the repository root): python analysis/16_models_e11.py
"""
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

from p1common import MODELS, OUT, expit, fit_mlp, predict_logit, save_json
from p1sim2 import TRUE_SIG, X20, cohort20, signatures20

SIZES = {"XL": (128, 64), "XXL": (256, 128), "D3": (32, 32, 32)}
test20 = cohort20("null", 5000, seed=299)


def check20(hidden):
    def ok(net):
        sig = signatures20(lambda z: predict_logit(net, z[X20].values), test20)
        if hidden == "null":
            return abs(sig["thr"]) < 0.3 and abs(sig["int"]) < 0.3
        return sig[hidden] >= 0.5 * TRUE_SIG[hidden]
    return ok


def trained(d, widths, seed, ok):
    """As in 13_models_e6_e8.py: Adam with early stopping and L-BFGS in turn, up to 12 tries."""
    for k in range(12):
        es = k % 2 == 0
        net = fit_mlp(d, "y", X20, hidden=widths, seed=seed + 1000 * (k // 2), early_stopping=es)
        if ok(net):
            return net, f"{k // 2}{'a' if es else 'l'}"
    raise SystemExit(f"no network passed the check (seed {seed})")


rows, seed = [], 500
for hidden in ["thr", "int", "null"]:
    for size, widths in SIZES.items():
        seed += 1
        d = cohort20(hidden, 20000, seed)
        net, tries = trained(d, widths, seed, check20(hidden))
        save_json(net, MODELS / f"e11_{hidden}_{size}.json")
        sig = signatures20(lambda z: predict_logit(net, z[X20].values), test20)
        rows.append({"model": f"e11_{hidden}_{size}", "hidden": hidden, "size": size,
                     "weights": sum(np.size(L["W"]) + np.size(L["b"]) for L in net["layers"]),
                     "prevalence": d["y"].mean(), "auc_train": roc_auc_score(d["y"], expit(predict_logit(net, d[X20].values))),
                     "seed_tries": tries, **{f"sig_{k}": v for k, v in sig.items()}})
        print(rows[-1], flush=True)
tab = pd.DataFrame(rows)
tab.to_csv(OUT / "e11_networks.csv", index=False)
print(tab.round(3).to_string(index=False))
