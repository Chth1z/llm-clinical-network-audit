"""Numbers quoted in the preprint's text, computed from the evaluation outputs so that the text can be checked
against them. Prints the facts; writes nothing.
Usage (from the repository root): python manuscript/preprint/e25_facts.py
"""
import json
import math
import re
from pathlib import Path

import numpy as np
import pandas as pd

SIM = Path(__file__).resolve().parents[2] / "results" / "simulation"
RUNS = SIM / "llm_runs"


def meta(run):
    return json.loads((RUNS / run / "meta.json").read_text(encoding="utf-8"))


def wilson(k, n, z=1.96):
    p = k / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return f"{max(0, c - h):.2f}--{min(1, c + h):.2f}"


def base(run):
    return re.sub(r"^e2[25]_", "", re.sub(r"_x\d+$", "", run))


j = pd.read_csv(SIM / "e6_judgement.csv")
j["src"] = j.run.map(base)
j["calc"] = j.variant.astype(str).str.contains("calculator")
j["explicit"] = j.variant.astype(str).str.startswith("assume")
j["minutes"] = j.seconds / 60
default_w = j[(j.condition == "weights") & ~j.calc & ~j.explicit & j.model.eq("gpt-6-astra") & j.src.str.startswith("e6_w_")]
print("default, no tool, S/M/L run minutes:", round(default_w.minutes.min()), "to", round(default_w.minutes.max()))
for size in ("M", "L"):
    d = default_w[default_w["size"] == size]
    print(f"default {size}: thr ratios", sorted(round(x, 2) for x in (d.astra_thr / d.net_thr).dropna()),
          "| null r2", sorted(round(x, 2) for x in d[d.src.str.contains("null")].r2))
ex = j[(j.condition == "weights") & ~j.calc & j.explicit & j["size"].eq("L")]
print("explicit no tool L: runs", len(ex), "| r2 planted", sorted(round(x, 2) for x in ex[~ex.src.str.contains("null")].r2),
      "| r2 null", sorted(round(x, 2) for x in ex[ex.src.str.contains("null")].r2))
calc = j[j.calc & j.model.eq("gpt-6-astra") & j.condition.eq("weights")]
print("calculator reading runs:", len(calc), "| median minutes", round(calc.minutes.median(), 1),
      "| range", round(calc.minutes.min()), "to", round(calc.minutes.max()))
scan = pd.read_csv(SIM / "e6_scan.csv")
cs = scan[scan.variant.astype(str).str.contains("calculator")]
print("calculator runs: largest number of claims at zero locations per run:", int(cs.surrogate_flags_at_zero.max()))
print("Wilson: 39/39", wilson(39, 39), "| 0/21", wilson(0, 21), "| 17/21", wilson(17, 21), "| 0/24", wilson(0, 24))

a8 = pd.read_csv(SIM / "e8_audit.csv")
a8["src"] = a8.run.map(base)
u = a8[a8.network.eq("e8_unbiased") & a8.src.str.startswith("e16_e8a")]
print("explicit, weights, unbiased: runs", u.run.nunique(), "| largest |shift| per run",
      u.groupby("run").stated_shift.apply(lambda s: round(float(np.nanmax(np.abs(s))), 2) if s.notna().any() else None).to_dict())
a12 = pd.read_csv(SIM / "e12_audit.csv")
a12["src"] = a12.run.map(base)
u12 = a12[a12.network.eq("e8_unbiased") & a12.src.str.startswith("e16_e12a")]
fa = u12[u12.false_alarm == True]  # noqa: E712
print("explicit + reference, unbiased: false-alarm subgroups", len(fa), "in", fa.run.nunique(), "runs; conditions:")
for c in fa.conditions:
    print("   ", c)
r8 = pd.read_csv(SIM / "e8_repair.csv")
r8["src"] = r8.run.map(base)
print("E8 repair runs:\n" + r8[["run", "declined", "jaccard", "in_subgroup_vs_unbiased_after", "outside_change_vs_original"]].round(2).to_string(index=False))
for run in ("e16_e12c_tol_r2", "e25_e16_e12c_tol_r1_x1"):
    text = (RUNS / run / "reply.md").read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(.*?)```", text, flags=re.S)
    try:
        net = json.loads(blocks[-1])["mlp"]
        print(run, "hidden units in the edited network:", [len(L["b"]) for L in net["layers"]][:-1])
    except Exception as e:  # noqa: BLE001
        print(run, "could not read the edited network:", type(e).__name__)
