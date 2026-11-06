"""E22: repeats so that the key cells have 3 runs. Prompts and settings are copied
byte for byte from the original runs; only the run name changes.
Usage (from the repository root): python analysis/35_prompts_e22.py
"""
import shutil
import sys

from p1common import OUT, RUNS, load_json, save_json

PLAN = {  # source run -> how many more runs
    "e17_w_int_L": 1, "e17_w_null_L": 1, "e17_w_int_XXL": 1, "e17_w_null_XXL": 2, "e17_w_thr_L": 2, "e17_w_thr_XXL": 2,
    "e18_int_L": 1, "e18_null_L": 1, "e18_int_XXL": 1, "e18_null_XXL": 2, "e18_thr_L": 2, "e18_thr_XXL": 2,
    "e17_e8a_unbiased": 2, "e18_e8a_unbiased": 2,
    "e6_w_thr_S": 1, "e6_w_int_S": 1, "e6_w_null_S": 1, "e6_w_thr_M": 1, "e6_w_int_M": 1, "e6_w_null_M": 1,
    "e6_w_thr_L": 1, "e6_w_int_L": 1, "e6_w_null_L": 1,
    "e16_e6_w_thr_L": 1, "e16_e6_w_int_L": 1, "e16_e6_w_null_L": 1,
}
for src, k in PLAN.items():
    for i in range(1, k + 1):
        run = f"e22_{src}_x{i}"
        (RUNS / run).mkdir(parents=True, exist_ok=True)
        shutil.copyfile(RUNS / src / "prompt.md", RUNS / run / "prompt.md")
        meta = load_json(RUNS / src / "meta.json")
        meta.update({"run": run, "prompt_from": src, "replicate_of": src})
        save_json(meta, RUNS / run / "meta.json")
        print(run)
