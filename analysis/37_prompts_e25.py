"""E25: repeats so that every cell of the preprint's reading, audit and repair tables has at least
3 runs. Prompts and settings are copied byte for byte from the original runs; only the run name changes (as E22,
35_prompts_e22.py).
Usage (from the repository root): python analysis/37_prompts_e25.py
"""
import shutil
import sys

from p1common import OUT, RUNS, load_json, save_json

PLAN = {  # source run -> how many more runs
    # reading, calculator (white box)
    "e17_w_int_S": 2, "e17_w_null_S": 2,
    "e17_w_thr_D3": 2, "e17_w_int_D3": 2, "e17_w_null_D3": 2,
    "e17_w_thr_XL": 2, "e17_w_int_XL": 2, "e17_w_null_XL": 2,
    # reading, default instruction, no tool
    "e6_w_thr_S": 1, "e6_w_int_S": 1, "e6_w_null_S": 1, "e6_w_thrweak_S": 2, "e6_w_intweak_S": 2,
    "e6_w_thr_M": 1, "e6_w_int_M": 1, "e6_w_null_M": 1,
    "e6_w_thr_L": 1, "e6_w_int_L": 1, "e6_w_null_L": 1,
    # reading, explicit instruction, no tool
    "e16_e6_w_thr_L": 1, "e16_e6_w_int_L": 1, "e16_e6_w_null_L": 1,
    # audit, no tool (default; default + stated reference; explicit; explicit + stated reference)
    "e8a_biased_r1": 1, "e8a_unbiased": 2, "e12a_biased_r1": 1, "e12a_unbiased": 2,
    "e16_e8a_biased_r1": 1, "e16_e8a_unbiased": 2, "e16_e12a_biased_r1": 1, "e16_e12a_unbiased": 2,
    # repair
    "e8b_repair_r1": 1, "e12b_repair_r1": 1, "e12c_exact_r1": 1, "e16_e8b_repair_r1": 1, "e16_e12b_tol_r1": 1,
    "e16_e12c_exact_r1": 1, "e16_e12c_tol_r1": 1, "e17_e12c_tol_r1": 1,
}
n = 0
for src, k in PLAN.items():
    for i in range(1, k + 1):
        run = f"e25_{src}_x{i}"
        (RUNS / run).mkdir(parents=True, exist_ok=True)
        shutil.copyfile(RUNS / src / "prompt.md", RUNS / run / "prompt.md")
        meta = load_json(RUNS / src / "meta.json")
        meta.update({"run": run, "prompt_from": src, "replicate_of": src})
        save_json(meta, RUNS / run / "meta.json")
        n += 1
print(f"{n} run folders")
