"""E10: is Astra's reading unchanged when a network is rewritten without changing what it computes?

Judged with the E4 rules (shape of the surrogate) and against the two E4 runs on the original network: the strength
of the hidden relationship within 30% of their mean counts as unchanged.
Writes results/simulation/e10_judgement.csv.
"""
import pandas as pd

from p1common import MODELS, OUT, RUNS, fidelity, load_json, predict_logit, surrogate_logit
from p1sim import X11, cohort, signatures

test = cohort("null", 5000, seed=99)
KEY = {"h1": "l7_5_to_9_minus_1_to_5", "h2": "htn_effect_farmers"}
orig = pd.read_csv(OUT / "e4_magnitudes_posthoc.csv")
rows = []
for k in ("h1", "h2"):
    f = RUNS / f"e10_{k}_equiv"
    if not (f / "parsed.json").exists():
        continue
    s = load_json(f / "parsed.json")["surrogate"]
    net = load_json(MODELS / f"e10_{k}_equiv.json")
    sur = signatures(None, test, lambda _n, X: surrogate_logit(s, pd.DataFrame(X, columns=X11)))
    nsig = signatures(net, test, predict_logit)
    if k == "h1":
        found = any(t["input"] == "l7" and t["type"] == "hinge" and 4.5 <= t["knot"] <= 7.5 and t["coef"] > 0
                    for t in s["terms"])
    else:
        found = any(set(t["inputs"]) == {"htn", "farmer"} and t["coef"] > 0.5 for t in s["interactions"])
    before = orig[orig.run.isin([f"e4_w_{k}_r1", f"e4_w_{k}_r2"])][f"{KEY[k]}_astra"].mean()
    rows.append({"run": f.name, "found_by_E4_rule": found, "network_strength": nsig[KEY[k]],
                 "astra_strength": sur[KEY[k]], "astra_strength_on_original_mean": before,
                 "unchanged": abs(sur[KEY[k]] - before) <= 0.3 * abs(before),
                 "r2": fidelity(predict_logit(net, test[X11].values), surrogate_logit(s, test))["r2"],
                 "confidence_trained": load_json(f / "parsed.json")["confidence_trained"]})
tab = pd.DataFrame(rows)
tab.to_csv(OUT / "e10_judgement.csv", index=False)
print(tab.round(3).to_string(index=False))
