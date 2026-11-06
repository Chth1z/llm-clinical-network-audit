"""E4: judge each reply against the network it was shown.

Discovery is judged from Astra's surrogate with the rules written before the runs; the "unexpected" text is saved for
reading. Writes results/simulation/e4_judgement.csv and e4_text.json.
"""
import pandas as pd

from p1common import MODELS, OUT, RUNS, fidelity, load_json, predict_logit, save_json, shuffled, surrogate_logit
from p1sim import X11, cohort

test = cohort("null", 5000, seed=99)  # inputs for the checks; the outcome column is not used
nets = {f"e4_{k}": load_json(MODELS / f"e4_{k}.json") for k in ["h1", "h2", "h3", "null"]}
nets["e4_h1_shuffled"] = shuffled(nets["e4_h1"])
logits = {k: predict_logit(v, test[X11].values) for k, v in nets.items()}
HIDDEN_OF = {"e4_h1": "found_l7_threshold", "e4_h2": "found_htn_x_farmer", "e4_h3": "found_age_dip_50_60"}


def at(s, **kw):
    """The surrogate's log-odds for one profile: every input 0 except those given."""
    return float(surrogate_logit(s, pd.DataFrame([{**{k: 0.0 for k in X11}, **kw}]))[0])


def criteria(s):
    return {
        "found_l7_threshold": any(t["input"] == "l7" and t["type"] == "hinge" and 4.5 <= t["knot"] <= 7.5
                                  and t["coef"] > 0 for t in s["terms"]),
        "found_htn_x_farmer": any(set(t["inputs"]) == {"htn", "farmer"} and t["coef"] > 0.5 for t in s["interactions"]),
        "found_age_dip_50_60": at(s, age_c=0.0) - at(s, age_c=-1.0) < 0,
    }


rows, text = [], {}
for f in sorted(RUNS.iterdir()):
    if not (f / "parsed.json").exists():
        continue
    meta = load_json(f / "meta.json")
    if meta["experiment"] != "E4":
        continue
    r = load_json(f / "parsed.json")
    s, c = r["surrogate"], criteria(r["surrogate"])
    text[f.name] = {"unexpected": r["unexpected"], "interactions": r["interactions"]}
    for t in ([meta["target"]] if isinstance(meta["target"], str) else meta["target"]):
        hidden = HIDDEN_OF.get(t)
        rows.append({"run": f.name, "condition": meta["condition"], "target": t,
                     **fidelity(logits[t], surrogate_logit(s, test)), **c,
                     "discovered": c[hidden] if hidden else None,
                     "false_alarms": sum(v for k, v in c.items() if k != hidden),
                     "n_unexpected": len(r["unexpected"]), "confidence_trained": r["confidence_trained"]})
tab = pd.DataFrame(rows)
tab.to_csv(OUT / "e4_judgement.csv", index=False)
save_json(text, OUT / "e4_text.json")
cols = ["run", "condition", "target", "r", "r2", "found_l7_threshold", "found_htn_x_farmer", "found_age_dip_50_60",
        "discovered", "false_alarms", "n_unexpected", "confidence_trained"]
print(tab[cols].round(3).to_string(index=False))
for run, t in text.items():
    for u in t["unexpected"]:
        print(f"{run}: {u.get('inputs')} | {str(u.get('description'))[:160]} | {str(u.get('where'))[:80]}")
