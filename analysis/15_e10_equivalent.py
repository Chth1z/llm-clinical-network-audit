"""E10: the E4 networks rewritten without changing what they compute.

Hidden units are permuted and half of them have their signs flipped (tanh is odd: negating a unit's incoming weights
and bias, and its outgoing weight, leaves the output unchanged). The numbers all change; the function does not. The
prompt is the E4 prompt with only the weights replaced.
Usage (from the repository root): python analysis/15_e10_equivalent.py
"""
import numpy as np

from p1common import MODELS, RUNS, fmt_model, load_json, predict_logit, save_json
from p1sim import X11, cohort


def equivalent(net, seed):
    rng = np.random.default_rng(seed)
    (W1, b1), (W2, b2) = [(np.asarray(L["W"], float), np.asarray(L["b"], float)) for L in net["layers"]]
    perm = rng.permutation(len(b1))
    flip = np.where(rng.random(len(b1)) < 0.5, -1.0, 1.0)
    W1n, b1n = (W1[perm] * flip[:, None]), b1[perm] * flip
    W2n = W2[:, perm] * flip[None, :]
    return {**net, "layers": [{"W": W1n.tolist(), "b": b1n.tolist(), "act": "tanh"},
                              {"W": W2n.tolist(), "b": b2.tolist(), "act": "linear"}]}


test = cohort("null", 5000, seed=99)
for k, seed in [("h1", 1101), ("h2", 1102)]:
    net = load_json(MODELS / f"e4_{k}.json")
    eq = equivalent(net, seed)
    gap = np.max(np.abs(predict_logit(net, test[X11].values) - predict_logit(eq, test[X11].values)))
    changed = np.mean([a != b for L, M in zip(net["layers"], eq["layers"]) for a, b in
                       zip(np.ravel(L["W"]), np.ravel(M["W"]))])
    print(f"e10_{k}_equiv: largest change in the log-odds {gap:.2e}; share of weights that changed {changed:.2f}")
    save_json(eq, MODELS / f"e10_{k}_equiv.json")
    old = (RUNS / f"e4_w_{k}_r1" / "prompt.md").read_text(encoding="utf-8")
    line = next(l for l in old.splitlines() if l.startswith('{"layers"'))
    assert line == fmt_model(net)
    folder = RUNS / f"e10_{k}_equiv"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "prompt.md").write_text(old.replace(line, fmt_model(eq)), encoding="utf-8")
    save_json({"run": folder.name, "experiment": "E4", "condition": "weights", "target": f"e10_{k}_equiv",
               "note": "E10: function-preserving rewrite of e4_" + k}, folder / "meta.json")
