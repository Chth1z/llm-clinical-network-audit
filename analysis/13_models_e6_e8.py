"""E6 and E8: the simulated cohorts and the networks. All are trained with Adam and early stopping
(p1common.fit_mlp), so that the larger ones do not memorise noise.

Writes results/simulation/models/e6_*.json and e8_*.json, and e6_networks.csv / e8_networks.csv with each network's own
strength of the hidden relationship (the yardstick for judging Astra's surrogates).
Usage (from the repository root): python analysis/13_models_e6_e8.py
"""
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

from p1common import MODELS, OUT, expit, fit_mlp, predict_logit, save_json
from p1sim import X11
from p1sim2 import TRUE_SIG, X20, biased_subgroup, cohort20, cohort_e8, signatures20

SIZES = {"S": (16,), "M": (32, 16), "L": (64, 32)}
test20 = cohort20("null", 5000, seed=299)
rows = []


def trained(d, inputs, widths, seed, ok):
    """The first network that passes the stimulus check `ok`: it carries at least half of the
    hidden relationship, or, for a null network, no spurious one of 0.3 or more. Tries Adam with early stopping and
    L-BFGS with a light penalty in turn, with training seeds seed, seed+1000, ...; returns the network and the try."""
    for k in range(12):
        es = k % 2 == 0
        net = fit_mlp(d, "y", inputs, hidden=widths, seed=seed + 1000 * (k // 2), early_stopping=es)
        if ok(net):
            return net, f"{k // 2}{'a' if es else 'l'}"
    raise SystemExit(f"no network passed the check (seed {seed})")


def check20(hidden, strength=1.0):
    def ok(net):
        sig = signatures20(lambda z: predict_logit(net, z[X20].values), test20)
        if hidden == "null":
            return abs(sig["thr"]) < 0.3 and abs(sig["int"]) < 0.3
        return sig[hidden] >= 0.5 * strength * TRUE_SIG[hidden]
    return ok


def record(name, net, d, hidden, size, strength):
    global tries
    p = expit(predict_logit(net, d[X20].values))
    sig = signatures20(lambda z: predict_logit(net, z[X20].values), test20)
    rows.append({"model": name, "hidden": hidden, "size": size, "strength": strength, "weights": sum(
        np.size(L["W"]) + np.size(L["b"]) for L in net["layers"]), "prevalence": d["y"].mean(),
        "auc_train": roc_auc_score(d["y"], p), "seed_tries": tries, **{f"sig_{k}": v for k, v in sig.items()}})


seed = 300
for hidden in ["thr", "int", "null"]:  # E6a: size ladder, strong effects
    for size, widths in SIZES.items():
        seed += 1
        d = cohort20(hidden, 20000, seed)
        net, tries = trained(d, X20, widths, seed, check20(hidden))
        save_json(net, MODELS / f"e6_{hidden}_{size}.json")
        record(f"e6_{hidden}_{size}", net, d, hidden, size, 1.0)
for hidden in ["thr", "int"]:  # E6b: weak effects, size S
    seed += 1
    d = cohort20(hidden, 20000, seed, strength=0.5)
    net, tries = trained(d, X20, SIZES["S"], seed, check20(hidden, 0.5))
    save_json(net, MODELS / f"e6_{hidden}weak_S.json")
    record(f"e6_{hidden}weak_S", net, d, hidden, "S", 0.5)
for hidden in ["null", "thr"]:  # E6c: three networks on bootstrap resamples of one cohort
    seed += 1
    d = cohort20(hidden, 20000, seed)
    rng = np.random.default_rng(seed)
    for b in (1, 2, 3):
        db = d.iloc[rng.integers(0, len(d), len(d))].reset_index(drop=True)
        net, tries = trained(db, X20, SIZES["S"], seed * 10 + b, check20(hidden))
        save_json(net, MODELS / f"e6_group_{hidden}_{b}.json")
        record(f"e6_group_{hidden}_{b}", net, db, hidden, "S", 1.0)
tab = pd.DataFrame(rows)
tab.to_csv(OUT / "e6_networks.csv", index=False)
print(tab.round(3).to_string(index=False))

rows8 = []
test8 = cohort_e8(False, 5000, seed=399)
e8_ref = fit_mlp(cohort_e8(False, 20000, seed=402), "y", X11, hidden=16, seed=7, early_stopping=True)
for name, biased in [("e8_unbiased", False), ("e8_biased", True)]:
    d = cohort_e8(biased, 20000, seed=401 if biased else 402)
    net, tries = trained(d, X11, 16, 7, (lambda n: True) if not biased else
                         (lambda n: predict_logit(n, test8[X11].values)[biased_subgroup(test8)].mean()
                          - predict_logit(e8_ref, test8[X11].values)[biased_subgroup(test8)].mean() <= -1.5))
    net = e8_ref if not biased else net
    save_json(net, MODELS / f"{name}.json")
    sub = biased_subgroup(test8)
    rows8.append({"model": name, "prevalence": d["y"].mean(), "subgroup_share": float(sub.mean()),
                  "subgroup_mean_logit": float(predict_logit(net, test8[X11].values)[sub].mean())})
t8 = pd.DataFrame(rows8)
t8["shift_vs_unbiased"] = t8["subgroup_mean_logit"] - t8.loc[t8.model == "e8_unbiased", "subgroup_mean_logit"].values[0]
t8.to_csv(OUT / "e8_networks.csv", index=False)
print(t8.round(3).to_string(index=False))
