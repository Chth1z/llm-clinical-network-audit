"""Read each reply, check the shape of its JSON block, write parsed.json and a summary of the runs (p1_runs.csv).

A reply without a usable JSON block counts as a failed run (no retries).
"""
import pandas as pd

from p1common import MODELS, OUT, RUNS, last_json, load_json, save_json


def number(x, what):
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        raise ValueError(f"{what} is not a number: {x!r}")
    return float(x)


def surrogate(s, inputs):
    out = {"intercept": number(s.get("intercept", 0.0), "intercept"), "terms": [], "interactions": []}
    for t in s.get("terms", []):
        if t["input"] not in inputs or t.get("type", "linear") not in ("linear", "hinge"):
            raise ValueError(f"bad surrogate term {t}")
        term = {"input": t["input"], "type": t.get("type", "linear"), "coef": number(t["coef"], "coef")}
        if term["type"] == "hinge":
            term["knot"] = number(t["knot"], "knot")
        out["terms"].append(term)
    for t in s.get("interactions", []):
        if len(t["inputs"]) != 2 or any(v not in inputs for v in t["inputs"]):
            raise ValueError(f"bad surrogate interaction {t}")
        term = {"inputs": list(t["inputs"]), "coef": number(t["coef"], "coef")}
        if t.get("knots"):
            term["knots"] = [number(k, "knot") for k in t["knots"]]
        out["interactions"].append(term)
    return out


def mlp_like(obj, like):
    """An edited network with exactly the shapes of `like`."""
    layers = obj["layers"]
    if len(layers) != len(like["layers"]):
        raise ValueError("edited network has a different number of layers")
    out = []
    for layer, ref in zip(layers, like["layers"]):
        W, b = layer["W"], layer["b"]
        if len(W) != len(ref["W"]) or any(len(r) != len(ref["W"][0]) for r in W) or len(b) != len(ref["b"]):
            raise ValueError("edited network has different shapes")
        out.append({"W": [[number(v, "weight") for v in r] for r in W], "b": [number(v, "bias") for v in b],
                    "act": ref["act"]})
    return {"kind": "mlp", "inputs": like["inputs"], "layers": out}


def conditions(c, inputs):
    for x in c:
        if x["input"] not in inputs or x["op"] not in (">", ">=", "<", "<=", "=="):
            raise ValueError(f"bad subgroup condition {x}")
        number(x["value"], "value")
    return c


def parse(meta, j):
    exp, cond = meta["experiment"], meta["condition"]
    if exp == "E6":
        from p1sim2 import X20
        eff = j["effects"]
        missing = [k for k in X20 if k not in eff]
        if missing:
            raise ValueError(f"effects lack {missing}")
        return {"effects": {k: eff[k] for k in X20}, "unexpected": j.get("unexpected", []),
                "surrogate": surrogate(j["surrogate"], X20), "confidence_trained": j.get("confidence_trained")}
    if exp in ("E8", "E12"):
        from p1sim import X11
        if cond == "audit":
            subs = j.get("subgroups", [])
            for s_ in subs:
                conditions(s_["conditions"], X11)
                number(s_["logit_shift"], "logit_shift")
            return {"subgroups": subs, "confidence_trained": j.get("confidence_trained")}
        like = load_json(MODELS / "e8_biased.json")
        if j.get("subgroup") is None:  # it declined to name a subgroup (and to edit): recorded, judged as no repair
            return {"subgroup": None, "mlp": mlp_like(j["mlp"], like) if j.get("mlp") else None, "declined": True}
        conditions(j["subgroup"]["conditions"], X11)
        return {"subgroup": j["subgroup"], "mlp": mlp_like(j["mlp"], like)}
    if exp in ("E4", "E10", "E13"):
        from p1sim import X11
        eff = j["effects"]
        missing = [k for k in X11 if k not in eff]
        if missing:
            raise ValueError(f"effects lack {missing}")
        return {"effects": {k: eff[k] for k in X11}, "interactions": j.get("interactions", []),
                "unexpected": j.get("unexpected", []), "surrogate": surrogate(j["surrogate"], X11),
                "confidence_trained": j.get("confidence_trained")}
    raise ValueError(f"unknown experiment {exp}")


rows = []
for folder in sorted(RUNS.iterdir()):
    if not (folder / "prompt.md").exists():
        continue
    meta = load_json(folder / "meta.json")
    run = load_json(folder / "run.json") if (folder / "run.json").exists() else {}
    row = {"run": folder.name, "experiment": meta["experiment"], "condition": meta["condition"],
           "seconds": run.get("seconds"), "tool_free": run.get("tool_free"),
           **{k: run.get("usage", {}).get(k) for k in ["input_tokens", "output_tokens", "reasoning_output_tokens"]}}
    try:
        if not (folder / "reply.md").exists():
            raise ValueError("no reply")
        j = last_json((folder / "reply.md").read_text(encoding="utf-8"))
        if j is None:
            raise ValueError("no parsable JSON block")
        save_json(parse(meta, j), folder / "parsed.json")
        row["ok"], row["error"] = True, ""
    except (ValueError, KeyError, TypeError) as e:
        (folder / "parsed.json").unlink(missing_ok=True)
        row["ok"], row["error"] = False, f"{type(e).__name__}: {e}"
    rows.append(row)
tab = pd.DataFrame(rows)
tab.to_csv(OUT / "p1_runs.csv", index=False)
print(tab.to_string(index=False))
