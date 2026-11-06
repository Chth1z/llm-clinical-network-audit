"""Tables, figures and numbers for the preprint, generated from the simulation results.

Reads results/simulation/*.csv and the run.json files of the runs; writes tables/*.tex, figures/*.pdf and
numbers.json next to this file. Re-run after new runs are evaluated; do not edit the outputs by hand.
Usage (from the repository root): python manuscript/preprint/make_assets.py
"""
import json
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

HERE = Path(__file__).resolve().parent
SIM = HERE.parents[1] / "results" / "simulation"
RUNS = SIM / "llm_runs"
(HERE / "tables").mkdir(exist_ok=True)
(HERE / "figures").mkdir(exist_ok=True)
NUM = {}


def csv(name):
    return pd.read_csv(SIM / name, keep_default_na=False, na_values=[""])


def run_json(run):
    f = RUNS / run / "run.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}


def wilson(k, n, z=1.96):
    if n == 0:
        return (math.nan, math.nan)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def access(variant):
    v = str(variant)
    return "black" if "black" in v else "white" if "calculator" in v else "none"


def instr(variant):
    return "default" if str(variant) in ("neutral", "", "nan") else "explicit"


def num(v, fmt="{:.2f}"):
    s = fmt.format(v)
    return "$-$" + s[1:] if s.startswith("-") else s


def rng(x, fmt="{:.2f}"):
    x = [v for v in x if pd.notna(v)]
    if not x:
        return "--"
    lo, hi = num(min(x), fmt), num(max(x), fmt)
    if lo == hi:
        return lo
    return f"{lo} to {hi}" if min(x) < 0 else f"{lo}--{hi}"


def tex(s):
    return str(s).replace("_", r"\_").replace("%", r"\%").replace("&", r"\&")


# ---------------------------------------------------------------- reading (E6, E16, E17, E18, E19, E20, E22)
rd = csv("e6_judgement.csv")
rd = rd[rd.condition.eq("weights")].copy()
rd["access"] = rd.variant.map(access)
rd["weak"] = rd.run.str.contains("weak")
rd["instr"] = rd.variant.map(instr)
rd["ratio"] = rd.apply(lambda r: r["astra_" + r.hidden] / r["net_" + r.hidden] if r.hidden != "null" else np.nan, axis=1)
rd["calls"] = rd.run.map(lambda r: run_json(r).get("tool_calls"))
scan = csv("e6_scan.csv")[["run", "surrogate_flags_at_zero"]]
rd = rd.merge(scan, on="run", how="left")
astra = rd[rd.model.eq("gpt-6-astra")]
COND = [("default", "none", "Default, no tool"), ("explicit", "none", "Explicit, no tool"),
        ("explicit", "white", "Calculator, white box"), ("explicit", "black", "Calculator, black box")]
SIZES = ["S", "M", "L", "D3", "XL", "XXL"]
HID = {"thr": "Threshold", "int": "Interaction", "thrweak": "Threshold, half strength", "intweak": "Interaction, half strength", "null": "None (null)"}
WEIGHTS = {s: int(astra[astra["size"].eq(s)].weights.iloc[0]) for s in SIZES if (astra["size"] == s).any()}

lines = [r"\begin{tabular}{llcccc}", r"\toprule",
         r"Network (weights) & Planted & " + " & ".join(c[2] for c in COND) + r" \\", r"\midrule"]
for s in SIZES:
    if s not in WEIGHTS:
        continue
    for h in ["thr", "int", "thrweak", "intweak", "null"]:
        base, weak = h.replace("weak", ""), h.endswith("weak")
        if weak and not ((astra["size"] == s) & astra.weak).any():
            continue
        cells = []
        for i, a, _ in COND:
            x = astra[(astra["size"] == s) & (astra.hidden == base) & (astra.weak == weak) & (astra.instr == i) & (astra.access == a)]
            if x.empty:
                cells.append("--")
            elif base == "null":
                fa = int((x.false_alarm.astype(str).str.lower() == "true").sum())
                cells.append(f"{rng(x.r2)} [{fa}/{len(x)}]")
            else:
                found = int((x.discovered.astype(str).str.lower() == "true").sum())
                cells.append(f"{rng(x.ratio)}; {rng(x.r2)} [{found}/{len(x)}]")
        lines.append(f"{s} ({WEIGHTS[s]:,}) & {HID[h]} & " + " & ".join(cells) + r" \\")
    lines.append(r"\addlinespace")
lines[-1] = r"\bottomrule"
lines.append(r"\end{tabular}")
(HERE / "tables" / "reading.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

# numbers for the text
calc = astra[astra.access.isin(["white", "black"])]
pl = calc[calc.hidden != "null"]
NUM["calc_found"] = f"{int((pl.discovered.astype(str).str.lower() == 'true').sum())}/{len(pl)}"
NUM["calc_ratio"] = rng(pl.ratio)
NUM["calc_r2"] = rng(calc.r2)
nl = calc[calc.hidden == "null"]
NUM["calc_null_fa"] = f"{int((nl.false_alarm.astype(str).str.lower() == 'true').sum())}/{len(nl)}"
NUM["calc_runs"] = len(calc)
NUM["calc_calls"] = rng(calc.calls, "{:.0f}")
NUM["calc_seconds"] = rng(calc.seconds, "{:.0f}")
for a in ["white", "black"]:
    x = calc[calc.access == a]
    NUM[f"{a}_r2"] = rng(x.r2)
    NUM[f"{a}_ratio"] = rng(x[x.hidden != "null"].ratio)
    NUM[f"{a}_runs"] = len(x)

# Figure 1: reading fidelity by size
COLORS = {"Default, no tool": "#2a78d6", "Explicit, no tool": "#eb6834", "Calculator, white box": "#1baf7a",
          "Calculator, black box": "#eda100"}
MARK = {"Default, no tool": "o", "Explicit, no tool": "s", "Calculator, white box": "^", "Calculator, black box": "D"}
fig, axes = plt.subplots(1, 2, figsize=(10, 3.9))
for ax, what in zip(axes, ["ratio", "r2"]):
    for k, (i, a, label) in enumerate(COND):
        x = astra[(astra.instr == i) & (astra.access == a)]
        if what == "ratio":
            x = x[x.hidden != "null"]
        xs = x.weights.values * (1 + 0.06 * (k - 1.5))
        ax.scatter(xs, x[what].clip(lower=-0.7), s=36, marker=MARK[label], facecolor=COLORS[label],
                   edgecolor="white", linewidth=1.0, label=label, zorder=3)
    ax.set_xscale("log")
    ax.set_xlabel("Weights in the network (log scale)")
    ax.grid(axis="y", color="#e6e6e6", linewidth=0.8)
    for sp in ["top", "right"]:
        ax.spines[sp].set_visible(False)
    if what == "ratio":
        ax.axhline(1.0, color="#888888", linewidth=1.0, linestyle="--", zorder=1)
        ax.axhline(0.5, color="#bbbbbb", linewidth=1.0, linestyle=":", zorder=1)
        ax.set_ylabel("Strength read / strength in network")
        ax.set_title("a  Planted relationship", loc="left", fontsize=11)
    else:
        ax.axhline(0.0, color="#bbbbbb", linewidth=1.0, linestyle=":", zorder=1)
        ax.set_ylabel(r"$R^2$ of the surrogate on the network")
        ax.set_title("b  Fidelity of the surrogate (all networks)", loc="left", fontsize=11)
handles, labels = axes[1].get_legend_handles_labels()
fig.legend(handles, labels, frameon=False, fontsize=9, loc="upper center", ncol=4, bbox_to_anchor=(0.5, 1.0))
fig.tight_layout(rect=(0, 0, 1, 0.92))
fig.savefig(HERE / "figures" / "reading.pdf")
fig.savefig(HERE / "figures" / "reading.png", dpi=110)
plt.close(fig)

# ---------------------------------------------------------------- auditing (E8, E12, E16, E17, E18, E19, E20, E22, E21)
a8 = csv("e8_audit.csv")
a12 = csv("e12_audit.csv")
a12["model"] = "gpt-6-astra"
a8["reference"], a12["reference"] = "none", "additive"
aud = pd.concat([a8, a12], ignore_index=True)
aud["access"], aud["instr"] = aud.variant.map(access), aud.variant.map(instr)


def per_run(g):
    has = g.conditions.notna()
    found = (g.found.astype(str).str.lower() == "true").any()
    fa = (g.false_alarm.astype(str).str.lower() == "true").any()
    return pd.Series({"model": g.model.iloc[0], "network": g.network.iloc[0], "reference": g.reference.iloc[0],
                      "access": g.access.iloc[0], "instr": g.instr.iloc[0], "declined": not has.any(),
                      "found": bool(found), "false_alarm": bool(fa),
                      "best_jaccard": float(g.jaccard.max()) if has.any() else 0.0})


runs = aud.groupby("run").apply(per_run).reset_index()
ROWS = [("Default instructions, weights in prompt", dict(model="gpt-6-astra", instr="default", access="none", reference="none")),
        ("Default + stated additive reference", dict(model="gpt-6-astra", instr="default", access="none", reference="additive")),
        ("Explicit instructions, weights in prompt", dict(model="gpt-6-astra", instr="explicit", access="none", reference="none")),
        ("Explicit + stated additive reference", dict(model="gpt-6-astra", instr="explicit", access="none", reference="additive")),
        ("Explicit + calculator, white box", dict(model="gpt-6-astra", instr="explicit", access="white", reference="none")),
        ("Explicit + calculator, black box", dict(model="gpt-6-astra", instr="explicit", access="black", reference="none"))]
for m in ["gpt-6.1-sol", "gpt-6-sol", "gpt-6-luna"]:
    ROWS.append((f"{m} + calculator, white box", dict(model=m, instr="explicit", access="white", reference="none")))
sa = csv("e21_scripted_audit.csv")
lines = [r"\begin{tabular}{lcccc}", r"\toprule",
         r"Condition & Biased: found & Biased: declined & Best Jaccard & Unbiased: false alarm \\", r"\midrule"]
fig_rows = []
for label, sel in ROWS:
    x = runs
    for k, v in sel.items():
        x = x[x[k] == v]
    b, u = x[x.network == "e8_biased"], x[x.network == "e8_unbiased"]
    lines.append(f"{tex(label)} & {int(b.found.sum())}/{len(b)} & {int(b.declined.sum())}/{len(b)} & "
                 f"{rng(b.best_jaccard)} & {int(u.false_alarm.sum())}/{len(u)}" + r" \\")
    fig_rows.append((label, b.best_jaccard.values, b.declined.values))
    NUM[f"audit::{label}"] = {"found": f"{int(b.found.sum())}/{len(b)}", "declined": f"{int(b.declined.sum())}/{len(b)}",
                              "fa": f"{int(u.false_alarm.sum())}/{len(u)}", "n_unbiased_declined": int(u.declined.sum())}
for _, r in sa.iterrows():
    if r.network == "e8_biased":
        u = sa[(sa.network == "e8_unbiased") & (sa.method == r.method)].iloc[0]
        label = f"Script, {r.method} (no LLM)"
        lines.append(f"{tex(label)} & {int(bool(r.found))}/1 & 0/1 & {r.jaccard:.2f} & {int(bool(u.false_alarm))}/1" + r" \\")
        fig_rows.append((label, np.array([r.jaccard]), np.array([False])))
lines += [r"\bottomrule", r"\end{tabular}"]
(HERE / "tables" / "audit.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
calc_b = runs[(runs.model == "gpt-6-astra") & runs.access.isin(["white", "black"]) & (runs.network == "e8_biased")]
NUM["astra_calc_audit"] = f"{int(calc_b.found.sum())}/{len(calc_b)}"
NUM["astra_calc_audit_jaccard"] = rng(calc_b.best_jaccard, "{:.3f}")
lo, hi = wilson(int(calc_b.found.sum()), len(calc_b))
NUM["astra_calc_audit_ci"] = f"{lo:.2f}--{hi:.2f}"
default_all = runs[(runs.model == "gpt-6-astra") & (runs.instr == "default") & (runs.access == "none")]
NUM["default_audit_declined"] = f"{int(default_all.declined.sum())}/{len(default_all)}"

fig, ax = plt.subplots(figsize=(8.6, 4.4))
for k, (label, jac, dec) in enumerate(fig_rows[::-1]):
    y = np.full(len(jac), k) + np.linspace(-0.12, 0.12, len(jac)) if len(jac) > 1 else np.array([k])
    ax.scatter(jac[~dec], y[~dec], s=40, marker="o", facecolor="#2a78d6", edgecolor="white", linewidth=1.0, zorder=3)
    ax.scatter(np.zeros(dec.sum()) - 0.04, y[dec], s=40, marker="x", color="#777777", zorder=3, linewidth=1.4)
ax.axvline(0.5, color="#bbbbbb", linewidth=1.0, linestyle=":")
ax.set_yticks(range(len(fig_rows)))
ax.set_yticklabels([r[0] for r in fig_rows[::-1]], fontsize=8.5)
ax.set_xlim(-0.1, 1.05)
ax.set_xlabel("Jaccard overlap of the reported subgroup with the true subgroup (biased network)")
ax.scatter([], [], s=40, marker="o", facecolor="#2a78d6", edgecolor="white", label="Subgroup reported")
ax.scatter([], [], s=40, marker="x", color="#777777", label="Declined (no subgroup)")
ax.legend(frameon=False, fontsize=8.5, loc="lower right")
for sp in ["top", "right"]:
    ax.spines[sp].set_visible(False)
ax.grid(axis="x", color="#eeeeee", linewidth=0.8)
fig.tight_layout()
fig.savefig(HERE / "figures" / "audit.pdf")
fig.savefig(HERE / "figures" / "audit.png", dpi=110)
plt.close(fig)

# ---------------------------------------------------------------- repair (E8b, E12b, E12c, E16, E17, E23)
r8 = csv("e8_repair.csv")
r12 = csv("e12_repair.csv")
sr = csv("e23_scripted_repair.csv")
runs_log = csv("p1_runs.csv")
INVALID = set(runs_log[runs_log.error.astype(str).str.contains("shape")].run)  # an answer that broke the shape constraint
explicit8 = r8.run.str.replace(r"^e2[25]_", "", regex=True).str.startswith("e16")  # repeats (E22, E25) keep their source's condition
REP = [("E8 repair, default (subgroup not given)", r8[~explicit8], "e8"),
       ("E8 repair, explicit (subgroup not given)", r8[explicit8], "e8"),
       ("Subgroup given, default", r12[(r12.condition == "repair_subgroup") & (r12.variant == "neutral")], "e12"),
       ("Subgroup given, explicit + tolerance", r12[(r12.condition == "repair_subgroup") & (r12.variant != "neutral")], "e12"),
       ("+1.6 exact, default", r12[(r12.condition == "repair_exact") & (r12.variant == "neutral")], "e12"),
       ("+1.6 exact, explicit", r12[(r12.condition == "repair_exact") & (r12.variant == "assume")], "e12"),
       ("+1.6 exact, explicit + tolerance", r12[(r12.condition == "repair_exact") & (r12.variant == "assume+tolerance")], "e12"),
       ("+1.6 exact, explicit + tolerance + calculator", r12[(r12.condition == "repair_exact") & (r12.variant == "assume+tolerance+calculator")], "e12")]
lines = [r"\begin{tabular}{lcccccc}", r"\toprule",
         r"Condition & Runs & Declined & Invalid & Change in subgroup & Mean $|$change$|$ elsewhere & Bias after \\", r"\midrule"]
for label, x, kind in REP:
    if x.empty:
        continue
    if kind == "e8":
        sub = "--"
        out = rng(x.outside_change_vs_original)
        after = rng(x.in_subgroup_vs_unbiased_after)
    else:
        sub = rng(x.in_subgroup_change_mean)
        out = rng(x.outside_change_mean_abs)
        after = rng(x.in_subgroup_vs_unbiased_after)
    inv = x.run.isin(INVALID)
    dec = x.declined.astype(str).str.lower().eq("true") & ~inv
    lines.append(f"{tex(label)} & {len(x)} & {int(dec.sum())} & {int(inv.sum())} & {sub} & {out} & {after}" + r" \\")
lines.append(r"\midrule")
for _, r in sr.iterrows():
    lines.append(f"Script: {tex(r.method)} ({int(r.parameters_changed)}/{int(r['of'])} parameters) & 1 & 0 & 0 & "
                 f"{num(r.in_subgroup_change_mean)} & {num(r.outside_change_mean_abs)} & {num(r.in_subgroup_vs_unbiased_after)}" + r" \\")
lines += [r"\bottomrule", r"\end{tabular}"]
(HERE / "tables" / "repair.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

# ---------------------------------------------------------------- other models (E13 tool-free; E19 calculator)
e13 = csv("e13_judgement.csv")
E4W = sum(len(L['b']) * (1 + len(L['W'][0])) for L in json.loads((SIM / 'models' / 'e4_h1.json').read_text())['layers'])
NUM['e4_weights'] = E4W
e13["found"] = e13.discovered.astype(str).str.lower().eq("true")
e13["scored"] = e13.target.ne("e4_null")
lines = [r"\begin{tabular}{lccccc}", r"\toprule",
         r"Model & \multicolumn{2}{c}{No tool, " + f"{E4W}" + r"-weight networks (E13)} & \multicolumn{3}{c}{Calculator, white box (E19)} \\",
         r"\cmidrule(lr){2-3}\cmidrule(lr){4-6}",
         r" & Found & $R^2$ & Interaction ratio (L, XXL) & Null $R^2$ (L, XXL) & Audit (Jaccard; false alarm) \\", r"\midrule"]
for m in ["gpt-6-astra", "gpt-6.1-sol", "gpt-6-sol", "gpt-6-luna", "gpt-5.6-sol"]:
    x = e13[e13.model == m]
    found = f"{int(x[x.scored].found.sum())}/{int(x.scored.sum())}" if len(x) else "--"
    r = rd[(rd.model == m) & rd.access.eq("white")]
    ratio = rng(r[r.hidden == "int"].ratio)
    nr2 = rng(r[r.hidden == "null"].r2)
    au = runs[(runs.model == m) & runs.access.eq("white")]
    b, u = au[au.network == "e8_biased"], au[au.network == "e8_unbiased"]
    audit = f"{rng(b.best_jaccard)}; {int(u.false_alarm.sum())}/{len(u)}" if len(au) else "--"
    lines.append(f"{m} & {found} & {rng(x.r2)} & {ratio} & {nr2} & {audit}" + r" \\")
lines += [r"\bottomrule", r"\end{tabular}"]
(HERE / "tables" / "models.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

e10 = csv("e10_judgement.csv")
NUM["e10"] = [{"run": r.run, "after": round(r.astra_strength, 2), "before": round(r.astra_strength_on_original_mean, 2),
               "r2": round(r.r2, 2)} for r in e10.itertuples()]
(HERE / "numbers.json").write_text(json.dumps(NUM, indent=1, ensure_ascii=False), encoding="utf-8")
print(json.dumps(NUM, indent=1, ensure_ascii=False)[:3000])

# ---------------------------------------------------------------- appendix: pre-specification record
import subprocess  # noqa: E402

PRESPEC = [
    ("Planted relationships in 105-weight networks", "3a6bd3c", ["e4_w_"]),
    ("Size ladder, half strength and network groups; biased-label audit and repair", "e259471", ["e6_w_", "e6_group", "e8a_", "e8b_"]),
    ("Function-preserving rewrites", "449c348", ["e10_"]),
    ("Addendum: claims at zero locations and exact scan", "09a62cd", []),
    ("Other models without tools (105-weight prompts)", "5bc52e3", ["e13_"]),
    ("Stated reference for audit and repair", "1425aa0", ["e12a_", "e12b_", "e12c_"]),
    ("Explicit system instruction", "8b3a434", ["e16_e8", "e16_e12", "e16_e6"]),
    ("Calculation-only tool, white box", "796eb7e", ["e17_"]),
    ("Calculation-only tool, black box", "e49843a", ["e18_"]),
    ("Other models with the tool; first repeats", "0004706", ["e19_", "e20_"]),
    ("Scripted audit without an LLM", "b759c7b", []),
    ("Further repeats; scripted repairs without an LLM", "ab5e8f7", ["e22_"]),
    ("Repeats so that every cell has three runs", "650e180", ["e25_"]),
]
lines = [r"\begin{tabular}{llll}", r"\toprule", r"Experiment & Plan commit & Committed (UTC+8) & First run started \\", r"\midrule"]
for label, h, prefixes in PRESPEC:
    when = subprocess.run(["git", "show", "-s", "--format=%ci", h], capture_output=True, text=True, cwd=HERE).stdout.strip()[:16]
    starts = []
    for pre in prefixes:
        for f in RUNS.glob(pre + "*"):
            s = run_json(f.name).get("started")
            if s:
                starts.append(s)
    first = min(starts)[:16] if starts else "script, after the commit"
    lines.append(tex(label) + r" & \texttt{" + h + "} & " + when + " & " + first + r" \\")
lines += [r"\bottomrule", r"\end{tabular}"]
(HERE / "tables" / "prespec.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("prespec ok")
