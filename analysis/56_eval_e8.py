"""E8: the audit for a subgroup whose risk is under-predicted, and its repair.

Audit: a reported subgroup counts as found when its overlap (Jaccard) with the true subgroup is at least 0.5 and its
stated shift has the right sign and at least half the network's actual shift; on the unbiased network any subgroup
with a stated shift of 0.5 or more is a false alarm. Repair: the edited network inside the true subgroup against the
network trained on complete outcomes, and outside it against the original network. Writes e8_audit.csv, e8_repair.csv.
"""
import numpy as np
import pandas as pd

from p1common import MODELS, OUT, RUNS, load_json, predict_logit
from p1sim import X11
from p1sim2 import biased_subgroup, cohort_e8, subgroup_mask

test = cohort_e8(False, 5000, seed=399)
X = test[X11].values
biased, unbiased = load_json(MODELS / "e8_biased.json"), load_json(MODELS / "e8_unbiased.json")
lb, lu = predict_logit(biased, X), predict_logit(unbiased, X)
true = biased_subgroup(test)
net_shift = float((lb - lu)[true].mean())
audit, repair = [], []
for f in sorted(RUNS.iterdir()):
    if not (f / "parsed.json").exists() or load_json(f / "meta.json")["experiment"] != "E8":
        continue
    meta, r = load_json(f / "meta.json"), load_json(f / "parsed.json")
    if meta["condition"] == "audit":
        for i, s in enumerate(r["subgroups"] or [{}]):
            row = {"run": f.name, "model": meta.get("model", "gpt-6-astra"), "variant": meta.get("variant", "neutral"),
                   "network": meta["target"], "subgroup": i + 1}
            if s:
                m = subgroup_mask(test, s["conditions"])
                row.update({"conditions": "; ".join(f"{c['input']} {c['op']} {c['value']}" for c in s["conditions"]),
                            "share": float(m.mean()), "jaccard": float((m & true).sum() / max((m | true).sum(), 1)),
                            "stated_shift": s["logit_shift"],
                            "network_shift_in_it": float((lb - lu)[m].mean()) if m.any() else np.nan})
                if meta["target"] == "e8_biased":
                    row["found"] = bool(row["jaccard"] >= 0.5 and np.sign(s["logit_shift"]) == np.sign(net_shift)
                                        and abs(s["logit_shift"]) >= 0.5 * abs(net_shift))
                else:
                    row["false_alarm"] = bool(abs(s["logit_shift"]) >= 0.5)
            row["confidence_trained"] = r["confidence_trained"]
            audit.append(row)
    else:
        declined = bool(r.get("declined"))
        le = predict_logit(r["mlp"] or biased, X)  # declined without weights: the network stays as it was
        m = subgroup_mask(test, r["subgroup"]["conditions"]) if r["subgroup"] else np.zeros(len(test), bool)
        repair.append({"run": f.name, "variant": meta.get("variant", "neutral"), "declined": declined, "jaccard": float((m & true).sum() / max((m | true).sum(), 1)),
                       "in_subgroup_vs_unbiased_before": float((lb - lu)[true].mean()),
                       "in_subgroup_vs_unbiased_after": float((le - lu)[true].mean()),
                       "outside_change_vs_original": float(np.abs(le - lb)[~true].mean()),
                       "outside_vs_unbiased_before": float(np.abs(lb - lu)[~true].mean()),
                       "outside_vs_unbiased_after": float(np.abs(le - lu)[~true].mean())})
print(f"true subgroup: {true.mean():.3f} of test patients; the biased network's shift in it: {net_shift:.2f}")
if audit:
    pd.DataFrame(audit).to_csv(OUT / "e8_audit.csv", index=False)
    print(pd.DataFrame(audit).round(3).to_string(index=False))
if repair:
    pd.DataFrame(repair).to_csv(OUT / "e8_repair.csv", index=False)
    print(pd.DataFrame(repair).round(3).to_string(index=False))
