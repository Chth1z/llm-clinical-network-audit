"""E21: a scripted audit with no language model: black-box access only, an additive fit
to the network's log-odds over a synthetic population, then two fixed subgroup searches on the residuals. Judged with
the E8 rules. Writes results/simulation/e21_scripted_audit.csv.
"""
import itertools
import time

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

from p1common import MODELS, OUT, load_json, predict_logit
from p1sim import X11
from p1sim2 import biased_subgroup, cohort_e8, subgroup_mask

BIN = [x for x in X11 if x not in ("age_c", "l7")]
AGE_CUTS = {50: -1.0, 55: -0.5, 60: 0.0, 65: 0.5, 70: 1.0, 75: 1.5}
rng = np.random.default_rng(2111)
N = 50_000
pop = pd.DataFrame({k: rng.integers(0, 2, N).astype(float) for k in BIN})
pop["age_c"] = (rng.uniform(18, 90, N) - 60) / 10
pop["l7"] = rng.uniform(0, 10, N)
pop = pop[X11]


def basis(d):
    cols = [d[b].values for b in BIN]
    for v, lo, hi in [("age_c", -4.2, 3.0), ("l7", 0.0, 10.0)]:
        x = d[v].values
        cols.append(x)
        cols += [np.maximum(x - k, 0) for k in np.linspace(lo, hi, 9)[1:-1]]
    return np.column_stack([np.ones(len(d))] + cols)


def tree_leaf(resid):
    t = DecisionTreeRegressor(max_depth=3, min_samples_leaf=N // 100, random_state=0).fit(pop.values, resid)
    leaves = t.apply(pop.values)
    best = max(set(leaves), key=lambda l: abs(resid[leaves == l].mean()))
    node_path = t.decision_path(pop.values[leaves == best][:1]).indices
    conds = []
    for node in node_path:
        f, thr = t.tree_.feature[node], t.tree_.threshold[node]
        if f < 0:
            continue
        name = X11[f]
        go_left = pop.values[leaves == best][0, f] <= thr
        if name in BIN:
            conds.append({"input": name, "op": "==", "value": 0.0 if go_left else 1.0})
        else:
            conds.append({"input": name, "op": "<=" if go_left else ">", "value": float(thr)})
    return conds, float(resid[leaves == best].mean())


def exhaustive(resid):
    best, out = -1.0, None
    vals = {b: pop[b].values for b in BIN}
    age = pop["age_c"].values
    for k in (1, 2, 3):
        for vs in itertools.combinations(BIN, k):
            for bits in itertools.product((0.0, 1.0), repeat=k):
                m0 = np.ones(N, bool)
                for v, b in zip(vs, bits):
                    m0 &= vals[v] == b
                for cut in [None] + list(AGE_CUTS):
                    m = m0 if cut is None else m0 & (age > AGE_CUTS[cut])
                    n = m.sum()
                    if n < N // 100:
                        continue
                    mean = resid[m].mean()
                    score = abs(mean) * np.sqrt(n)
                    if score > best:
                        conds = [{"input": v, "op": "==", "value": b} for v, b in zip(vs, bits)]
                        if cut is not None:
                            conds.append({"input": "age_c", "op": ">", "value": AGE_CUTS[cut]})
                        best, out = score, (conds, float(mean))
    return out


test = cohort_e8(False, 5000, seed=399)
X = test[X11].values
biased, unbiased = load_json(MODELS / "e8_biased.json"), load_json(MODELS / "e8_unbiased.json")
lb, lu = predict_logit(biased, X), predict_logit(unbiased, X)
true = biased_subgroup(test)
net_shift = float((lb - lu)[true].mean())
rows = []
B = basis(pop)
for name in ["e8_biased", "e8_unbiased"]:
    net = load_json(MODELS / f"{name}.json")
    t0 = time.time()
    z = predict_logit(net, pop.values)
    resid = z - B @ np.linalg.lstsq(B, z, rcond=None)[0]
    for method, (conds, shift) in [("regression tree", tree_leaf(resid)), ("exhaustive search", exhaustive(resid))]:
        m = subgroup_mask(test, conds)
        row = {"network": name, "method": method, "seconds": round(time.time() - t0, 1),
               "conditions": "; ".join(f"{c['input']} {c['op']} {round(c['value'], 2)}" for c in conds),
               "stated_shift": shift, "jaccard": float((m & true).sum() / max((m | true).sum(), 1))}
        if name == "e8_biased":
            row["found"] = bool(row["jaccard"] >= 0.5 and np.sign(shift) == np.sign(net_shift) and abs(shift) >= 0.5 * abs(net_shift))
        else:
            row["false_alarm"] = bool(abs(shift) >= 0.5)
        rows.append(row)
tab = pd.DataFrame(rows)
tab.to_csv(OUT / "e21_scripted_audit.csv", index=False)
print(f"true subgroup share {true.mean():.3f}; biased network's shift in it {net_shift:.2f}")
print(tab.round(3).to_string(index=False))
