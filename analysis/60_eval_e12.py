"""E12: the E8 audit and repair with the reference made explicit.

Audit: the E8 rules (56_eval_e8.py). Repair with the subgroup given: the E8 repair metrics. Exact repair (+1.6 in the
subgroup, nothing elsewhere): the change edited - original, inside the subgroup against +1.6 and outside against 0.
Declined replies are recorded as no finding / no repair. Writes e12_audit.csv and e12_repair.csv.
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
band = ((test["female"] == 1) & (test["farmer"] == 1) & test["age_c"].between(0.4, 0.6)).values
audit, repair = [], []
for f in sorted(RUNS.iterdir()):
    if not (f / "meta.json").exists() or load_json(f / "meta.json")["experiment"] != "E12":
        continue
    meta = load_json(f / "meta.json")
    if not (f / "parsed.json").exists():
        if not (f / "reply.md").exists():
            continue
        # a reply with no usable JSON block: declined
        r = {"subgroups": [], "subgroup": None, "mlp": None, "declined": True, "confidence_trained": None}
    else:
        r = load_json(f / "parsed.json")
    if meta["condition"] == "audit":
        for i, s in enumerate(r["subgroups"] or [{}]):
            row = {"run": f.name, "variant": meta.get("variant", "neutral"), "network": meta["target"], "subgroup": i + 1,
                   "declined_or_none": not s}
            if s:
                m = subgroup_mask(test, s["conditions"])
                row.update({"conditions": "; ".join(f"{c['input']} {c['op']} {c['value']}" for c in s["conditions"]),
                            "share": float(m.mean()), "jaccard": float((m & true).sum() / max((m | true).sum(), 1)),
                            "stated_shift": s["logit_shift"],
                            "network_vs_unbiased_in_it": float((lb - lu)[m].mean()) if m.any() else np.nan})
                if meta["target"] == "e8_biased":
                    row["found"] = bool(row["jaccard"] >= 0.5 and np.sign(s["logit_shift"]) == np.sign(net_shift)
                                        and abs(s["logit_shift"]) >= 0.5 * abs(net_shift))
                else:
                    row["false_alarm"] = bool(abs(s["logit_shift"]) >= 0.5)
            row["confidence_trained"] = r.get("confidence_trained")
            audit.append(row)
        continue
    declined = bool(r.get("declined"))
    le = predict_logit(r["mlp"] or biased, X)
    ch = le - lb
    row = {"run": f.name, "variant": meta.get("variant", "neutral"), "condition": meta["condition"], "declined": declined,
           "stated_shift": (r.get("subgroup") or {}).get("logit_shift"),
           "in_subgroup_change_mean": float(ch[true].mean()), "outside_change_mean_abs": float(np.abs(ch[~true]).mean()),
           "in_subgroup_vs_unbiased_before": float((lb - lu)[true].mean()),
           "in_subgroup_vs_unbiased_after": float((le - lu)[true].mean())}
    if meta["condition"] == "repair_exact":
        row.update({"in_subgroup_within_0.3_of_1.6": float((np.abs(ch[true] - 1.6) <= 0.3).mean()),
                    "outside_within_0.1": float((np.abs(ch[~true]) <= 0.1).mean()),
                    "outside_change_max_abs": float(np.abs(ch[~true]).max()),
                    # E16's "done": outside the band of women farmers aged 64-66, |change - target| <= 0.1
                    "done_share_subgroup": float((np.abs(ch - 1.6) <= 0.1)[true & ~band].mean()),
                    "done_share_others": float((np.abs(ch) <= 0.1)[~true & ~band].mean())})
    repair.append(row)
print(f"true subgroup: {true.mean():.3f} of test patients; the biased network's shift in it: {net_shift:.2f}")
if audit:
    pd.DataFrame(audit).to_csv(OUT / "e12_audit.csv", index=False)
    print(pd.DataFrame(audit).round(3).to_string(index=False))
if repair:
    pd.DataFrame(repair).to_csv(OUT / "e12_repair.csv", index=False)
    print(pd.DataFrame(repair).round(3).to_string(index=False))
