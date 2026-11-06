"""E23: scripted repairs with no language model. Target as in E12c: +1.6 on the log-odds
of women farmers over 65, everyone else unchanged; same 16-unit shape. (a) gradient fine-tuning of all parameters
(Adam, learning rate 1e-3, 2,000 full-batch steps, mean squared error on the target log-odds); (b) a scripted gate: the
unit whose removal costs least becomes a steep gate for the subgroup, and the output layer is refitted by least squares.
Both on the balanced synthetic population of E21; judged on the E8 test inputs with the E12c measures.
Writes results/simulation/e23_scripted_repair.csv.
"""
import time

import numpy as np
import pandas as pd

from p1common import MODELS, OUT, load_json, predict_logit
from p1sim import X11
from p1sim2 import biased_subgroup, cohort_e8

BIN = [x for x in X11 if x not in ("age_c", "l7")]
rng = np.random.default_rng(2111)
N = 50_000
pop = pd.DataFrame({k: rng.integers(0, 2, N).astype(float) for k in BIN})
pop["age_c"] = (rng.uniform(18, 90, N) - 60) / 10
pop["l7"] = rng.uniform(0, 10, N)
Xp = pop[X11].values
net = load_json(MODELS / "e8_biased.json")
W1, b1 = np.array(net["layers"][0]["W"]), np.array(net["layers"][0]["b"])
W2, b2 = np.array(net["layers"][1]["W"]), np.array(net["layers"][1]["b"])
S_pop = biased_subgroup(pop)
target = predict_logit(net, Xp) + 1.6 * S_pop


def as_net(W1, b1, W2, b2):
    return {"kind": "mlp", "inputs": list(X11), "layers": [
        {"W": W1.tolist(), "b": b1.tolist(), "act": "tanh"}, {"W": W2.tolist(), "b": b2.tolist(), "act": "linear"}]}


def finetune(steps=2000, lr=1e-3):
    p = [W1.copy(), b1.copy(), W2.copy(), b2.copy()]
    m = [np.zeros_like(x) for x in p]
    v = [np.zeros_like(x) for x in p]
    for t in range(1, steps + 1):
        h = np.tanh(Xp @ p[0].T + p[1])
        z = h @ p[2].T + p[3]
        dz = 2 * (z[:, 0] - target)[:, None] / N
        g2, gb2 = dz.T @ h, dz.sum(0)
        dpre = (dz @ p[2]) * (1 - h ** 2)
        grads = [dpre.T @ Xp, dpre.sum(0), g2, gb2]
        for i, g in enumerate(grads):
            m[i] = 0.9 * m[i] + 0.1 * g
            v[i] = 0.999 * v[i] + 0.001 * g ** 2
            p[i] -= lr * (m[i] / (1 - 0.9 ** t)) / (np.sqrt(v[i] / (1 - 0.999 ** t)) + 1e-8)
    return as_net(*p)


def gate():
    H = np.tanh(Xp @ W1.T + b1)
    f = H @ W2[0] + b2[0]

    def refit(Hs, y):
        A = np.column_stack([Hs, np.ones(N)])
        c = np.linalg.lstsq(A, y, rcond=None)[0]
        return c, float(np.mean((A @ c - y) ** 2))
    costs = [refit(np.delete(H, j, axis=1), f)[1] for j in range(16)]
    j = int(np.argmin(costs))
    w = np.zeros(len(X11))
    w[X11.index("female")], w[X11.index("farmer")], w[X11.index("age_c")] = 40.0, 40.0, 10.0
    nW1, nb1 = W1.copy(), b1.copy()
    nW1[j], nb1[j] = w, -80.0 - 10.0 * 0.5  # off unless female = farmer = 1; then a step at age_c = 0.5 (65 years)
    Hn = np.tanh(Xp @ nW1.T + nb1)
    c, _ = refit(Hn, target)
    return as_net(nW1, nb1, c[:16][None, :], c[16:17]), j


test = cohort_e8(False, 5000, seed=399)
X = test[X11].values
lb, lu = predict_logit(net, X), predict_logit(load_json(MODELS / "e8_unbiased.json"), X)
true = biased_subgroup(test)
band = ((test["female"] == 1) & (test["farmer"] == 1) & test["age_c"].between(0.4, 0.6)).values
flat = np.concatenate([W1.ravel(), b1, W2.ravel(), b2])
rows = []
for method, fn in [("gradient fine-tuning", finetune), ("scripted gate + least squares", gate)]:
    t0 = time.time()
    out = fn()
    new, unit = (out if isinstance(out, tuple) else (out, None))
    secs = time.time() - t0
    L = new["layers"]
    nflat = np.concatenate([np.ravel(L[0]["W"]), L[0]["b"], np.ravel(L[1]["W"]), L[1]["b"]])
    ch = predict_logit(new, X) - lb
    rows.append({"method": method, "seconds": round(secs, 1), "unit_replaced": unit,
                 "parameters_changed": int((np.abs(nflat - flat) > 1e-4).sum()), "of": len(flat),
                 "in_subgroup_change_mean": float(ch[true].mean()),
                 "in_subgroup_within_0.3_of_1.6": float((np.abs(ch[true] - 1.6) <= 0.3).mean()),
                 "outside_change_mean_abs": float(np.abs(ch[~true]).mean()),
                 "outside_within_0.1": float((np.abs(ch[~true]) <= 0.1).mean()),
                 "done_share_subgroup": float((np.abs(ch - 1.6) <= 0.1)[true & ~band].mean()),
                 "done_share_others": float((np.abs(ch) <= 0.1)[~true & ~band].mean()),
                 "in_subgroup_vs_unbiased_after": float((lb + ch - lu)[true].mean())})
tab = pd.DataFrame(rows)
tab.to_csv(OUT / "e23_scripted_repair.csv", index=False)
print(tab.round(3).T.to_string())
