"""E13: the four E4 weight prompts, byte for byte, for four other models on the local Codex.
Writes results/simulation/llm_runs/e13_<model tag>_<E4 target>/prompt.md and meta.json (with "model").
Usage (from the repository root): python analysis/27_prompts_e13.py
"""
import shutil
import sys

from p1common import OUT, RUNS, load_json, save_json

MODELS13 = {"sol6": "gpt-6-sol", "sol61": "gpt-6.1-sol", "sol56": "gpt-5.6-sol", "luna6": "gpt-6-luna"}
for tag, model in MODELS13.items():
    for h in ["h1", "h2", "h3", "null"]:
        src = RUNS / f"e4_w_{h}_r1"
        run = RUNS / f"e13_{tag}_{h}"
        run.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src / "prompt.md", run / "prompt.md")  # byte-identical to what Astra was given
        save_json({"run": run.name, "experiment": "E13", "condition": "weights", "target": load_json(src / "meta.json")["target"],
                   "model": model, "prompt_from": src.name}, run / "meta.json")
        print(run.name, model)
