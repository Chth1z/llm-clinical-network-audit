"""E17: prompts for the runs with the one-tool calculator, and the no-tool control.

Reading: the E6 single-network prompt with the printed weights replaced by one sentence about the tool (and, for the
new sizes, the architecture line); everything else word for word. Repair and audit: the E16 tolerance prompt for E12c
and the E8 audit prompt, with one clause added saying the weights are also in the tool. Control: the E6 L prompts byte
for byte with the E16 instructions. Writes results/simulation/llm_runs/e17_* and e16_e6_w_*_L.
Usage (from the repository root): python analysis/31_prompts_e17.py
"""
import sys

from p1common import MODELS, OUT, RUNS, load_json, save_json

ASSUME = "instructions_assume.md"
TOOL = ("Its weights are loaded in your run_python tool: W1, b1, W2, b2, ... hold them, and predict(X) gives the "
        "network's log-odds for an array of inputs in the order listed.")
ALSO = ("Below are its weights; they are also loaded in your run_python tool (W1, b1, W2, b2; predict(X) gives the "
        "log-odds for an array of inputs in the order listed).")


def net_line(model, n_in):  # as in 24_prompts_e6_e8.py, without the sentence about the printed layers
    widths = [len(L["b"]) for L in model["layers"]]
    hs = " -> ".join(f"h{i + 1} = tanh(W{i + 1} {'x' if i == 0 else f'h{i}'} + b{i + 1}) ({w} units)"
                     for i, w in enumerate(widths[:-1]))
    k = len(widths)
    return (f"x ({n_in} inputs, in the order listed) -> {hs} -> log-odds = W{k} h{k - 1} + b{k}; probability = "
            f"1 / (1 + exp(-log-odds)). W[j][i] is the weight from input i of a layer to its unit j.")


def swap(text, old, new):
    assert text.count(old) == 1, old[:60]
    return text.replace(old, new)


def write(run, text, meta):
    (RUNS / run).mkdir(parents=True, exist_ok=True)
    (RUNS / run / "prompt.md").write_text(text, encoding="utf-8")
    save_json({"run": run, **meta}, RUNS / run / "meta.json")
    print(f"{run:22s} {len(text):7d} characters  {meta.get('variant')}  {meta.get('tool_network', '')}")


base = (RUNS / "e6_w_thr_L" / "prompt.md").read_text(encoding="utf-8")
lines = base.split("\n")
i = next(k for k, line in enumerate(lines) if line.startswith("The network: x (20 inputs"))
assert lines[i + 1].startswith('{"layers"')
for hidden in ["thr", "int", "null"]:
    for size in ["L", "XXL", "XL", "D3", "S"]:
        if size == "S" and hidden == "thr":
            continue
        name = f"e6_{hidden}_{size}" if size in ("S", "L") else f"e11_{hidden}_{size}"
        model = load_json(MODELS / f"{name}.json")
        out = lines[:i] + [f"The network: {net_line(model, 20)}"] + lines[i + 2:]
        text = swap("\n".join(out), "Below are its weights. ", TOOL + " ")
        write(f"e17_w_{hidden}_{size}", text, {"experiment": "E6", "condition": "weights", "target": name,
                                                 "instructions": ASSUME, "variant": "assume+calculator",
                                                 "tool_network": f"{name}.json", "prompt_from": "e6_w_thr_L"})
    src = f"e6_w_{hidden}_L"  # the control: same instructions, no tool, the prompt byte for byte
    meta = load_json(RUNS / src / "meta.json")
    meta.update({"instructions": ASSUME, "variant": "assume", "prompt_from": src})
    write(f"e16_{src}", (RUNS / src / "prompt.md").read_text(encoding="utf-8"), meta)
for r in (1, 2):
    src = f"e16_e12c_tol_r{r}"
    meta = load_json(RUNS / src / "meta.json")
    meta.update({"variant": "assume+tolerance+calculator", "tool_network": "e8_biased.json", "prompt_from": src})
    write(f"e17_e12c_tol_r{r}", swap((RUNS / src / "prompt.md").read_text(encoding="utf-8"), "Below are its weights.",
                                     ALSO), meta)
for src, run, net in [("e8a_biased_r1", "e17_e8a_biased_r1", "e8_biased"), ("e8a_biased_r2", "e17_e8a_biased_r2", "e8_biased"),
                      ("e8a_unbiased", "e17_e8a_unbiased", "e8_unbiased")]:
    meta = load_json(RUNS / src / "meta.json")
    meta.update({"instructions": ASSUME, "variant": "assume+calculator", "tool_network": f"{net}.json", "prompt_from": src})
    write(run, swap((RUNS / src / "prompt.md").read_text(encoding="utf-8"), "Below are its weights.", ALSO), meta)
