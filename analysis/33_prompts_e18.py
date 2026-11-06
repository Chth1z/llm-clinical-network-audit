"""E18: white box against black box. The E17 reading prompts with "from its weights"
replaced by "from its outputs" and the architecture line removed; the E17 E8-audit prompts with the weights and the
architecture removed. The calculator then holds only predict(X) (tool_blackbox).
Writes results/simulation/llm_runs/e18_*.
Usage (from the repository root): python analysis/33_prompts_e18.py
"""
import sys

from p1common import OUT, RUNS, load_json, save_json

TOOL_W = ("Its weights are loaded in your run_python tool: W1, b1, W2, b2, ... hold them, and predict(X) gives the "
          "network's log-odds for an array of inputs in the order listed.")
TOOL_B = ("Its weights are not shown; you can query it in your run_python tool, where predict(X) gives the network's "
          "log-odds for an array of inputs in the order listed.")
ALSO = ("Below are its weights; they are also loaded in your run_python tool (W1, b1, W2, b2; predict(X) gives the "
        "log-odds for an array of inputs in the order listed).")


def swap(text, old, new):
    assert text.count(old) == 1, old[:60]
    return text.replace(old, new)


def drop_line(text, start):
    lines = text.split("\n")
    i = [k for k, line in enumerate(lines) if line.startswith(start)]
    assert len(i) == 1, start
    return "\n".join(lines[:i[0]] + lines[i[0] + 1:])


def write(run, text, meta):
    (RUNS / run).mkdir(parents=True, exist_ok=True)
    (RUNS / run / "prompt.md").write_text(text, encoding="utf-8")
    save_json({"run": run, **meta}, RUNS / run / "meta.json")
    print(f"{run:22s} {len(text):7d} characters")


for hidden in ["thr", "int", "null"]:
    for size in ["L", "XXL"]:
        src = f"e17_w_{hidden}_{size}"
        t = (RUNS / src / "prompt.md").read_text(encoding="utf-8")
        t = swap(swap(t, TOOL_W, TOOL_B), "from its weights rather than", "from its outputs rather than")
        t = drop_line(t, "The network: x (")
        meta = load_json(RUNS / src / "meta.json")
        meta.update({"run": f"e18_{hidden}_{size}", "variant": "assume+calculator, black box", "tool_blackbox": True,
                     "prompt_from": src})
        write(f"e18_{hidden}_{size}", t, meta)
for src, run in [("e17_e8a_biased_r1", "e18_e8a_biased_r1"), ("e17_e8a_biased_r2", "e18_e8a_biased_r2"),
                 ("e17_e8a_unbiased", "e18_e8a_unbiased")]:
    t = (RUNS / src / "prompt.md").read_text(encoding="utf-8")
    t = swap(t, ALSO, TOOL_B)
    t = drop_line(drop_line(t, "The network: x ("), '{"layers"')
    meta = load_json(RUNS / src / "meta.json")
    meta.update({"run": run, "variant": "assume+calculator, black box", "tool_blackbox": True, "prompt_from": src})
    write(run, t, meta)
