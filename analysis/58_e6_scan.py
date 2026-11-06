"""Addendum to the E6 scoring: an exact scan of every lab input and every pair of lab inputs, on
each E6 network and on Astra's surrogate of it.

On the same 5,000 test inputs as 54_eval_e6.py: for each lab input the range effect f(9) - f(1) and the curvature
[f(9) - f(5)] - [f(5) - f(1)]; for each pair of lab inputs the interaction contrast at 2 and 8 (65 locations). A
location is flagged when |statistic| >= 0.5. The scan of the network is what a script reading the network exactly would
report (it needs only the network and the inputs' codings); the scan of the surrogate is what Astra reported. Locations
of the planted relationship are left out; every other location is zero in the generating model.
Writes results/simulation/e6_scan.csv (one row per run) and e6_scan_locations.csv (one row per run and location).
"""
import itertools

import numpy as np
import pandas as pd

from p1common import MODELS, OUT, RUNS, load_json, predict_logit, surrogate_logit
from p1sim2 import LABS, X20, cohort20

test = cohort20("null", 5000, seed=299)
FLAG = 0.5
PLANTED = {"null": set(), "thr": {"range l3", "curve l3"},
           "int": {"range l5", "range l8", "curve l5", "curve l8", "pair l5*l8"}}
PLANTED_LABS = {"null": set(), "thr": {"l3"}, "int": {"l5", "l8"}}


def at(f, **kw):
    z = test.copy()
    for k, v in kw.items():
        z[k] = v
    return np.mean(f(z))


def scan(f):
    out = {}
    for k in LABS:
        f1, f5, f9 = (at(f, **{k: v}) for v in (1.0, 5.0, 9.0))
        out[f"range {k}"], out[f"curve {k}"] = f9 - f1, (f9 - f5) - (f5 - f1)
    for a, b in itertools.combinations(LABS, 2):
        out[f"pair {a}*{b}"] = (at(f, **{a: 8.0, b: 8.0}) - at(f, **{a: 8.0, b: 2.0})
                                - at(f, **{a: 2.0, b: 8.0}) + at(f, **{a: 2.0, b: 2.0}))
    return out


def net_f(n):
    return lambda z: predict_logit(n, z[X20].values)


rows, locs = [], []
for f in sorted(RUNS.iterdir()):
    if not (f / "parsed.json").exists() or load_json(f / "meta.json")["experiment"] != "E6":
        continue
    meta, r = load_json(f / "meta.json"), load_json(f / "parsed.json")
    targets = [meta["target"]] if isinstance(meta["target"], str) else meta["target"]
    hidden = "null" if "_null" in f.name else "thr" if "_thr" in f.name else "int"
    nets = [scan(net_f(load_json(MODELS / f"{t}.json"))) for t in targets]
    sur = scan(lambda z: surrogate_logit(r["surrogate"], z))
    net = {k: float(np.mean([n[k] for n in nets])) for k in sur}
    shared = {k for k in sur if all(abs(n[k]) >= FLAG for n in nets) and len({np.sign(n[k]) for n in nets}) == 1}
    zero = [k for k in sur if k not in PLANTED[hidden]]
    s_flag = {k for k in zero if abs(sur[k]) >= FLAG}
    n_flag = {k for k in zero if abs(net[k]) >= FLAG}
    faithful = {k for k in s_flag & n_flag if np.sign(sur[k]) == np.sign(net[k])}
    planted = PLANTED_LABS[hidden]
    spurious_unexp = [u for u in r["unexpected"]
                      if any(i in LABS for i in u.get("inputs", [])) and not planted & set(u.get("inputs", []))]
    rows.append({"run": f.name, "variant": meta.get("variant", "neutral"), "condition": meta["condition"], "hidden": hidden,
                 "network_flags_at_zero": len(n_flag), "surrogate_flags_at_zero": len(s_flag),
                 "faithful_noise": len(faithful), "invented": len(s_flag - n_flag),
                 "noise_left_out": len(n_flag - s_flag), "shared_by_all_networks_at_zero": len(shared & set(zero)),
                 "unexpected_on_null_labs": len(spurious_unexp),
                 "largest_network_at_zero": max(abs(net[k]) for k in zero),
                 "largest_surrogate_at_zero": max(abs(sur[k]) for k in zero),
                 "flags_surrogate": "; ".join(sorted(s_flag)), "flags_network": "; ".join(sorted(n_flag))})
    locs += [{"run": f.name, "location": k, "planted": k in PLANTED[hidden], "network": net[k],
              "surrogate": sur[k], **{f"network_{i + 1}": n[k] for i, n in enumerate(nets) if len(nets) > 1}}
             for k in sur]
if not rows:
    raise SystemExit("no parsed E6 replies yet")
tab = pd.DataFrame(rows)
tab.to_csv(OUT / "e6_scan.csv", index=False)
pd.DataFrame(locs).to_csv(OUT / "e6_scan_locations.csv", index=False)
print(tab.drop(columns=["flags_surrogate", "flags_network"]).round(2).to_string(index=False))
for _, x in tab.iterrows():
    print(f"{x.run}: surrogate flags {x.flags_surrogate or '-'} | network flags {x.flags_network or '-'}")
