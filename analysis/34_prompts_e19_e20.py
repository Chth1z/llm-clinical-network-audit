"""E19 (other models with the calculator) and E20 (repeats): the E17 and E18 prompts byte for byte, with only
the model (E19) or the run name (E20) changed.
Usage (from the repository root): python analysis/34_prompts_e19_e20.py
"""
import shutil
import sys

from p1common import OUT, RUNS, load_json, save_json

CELLS = ["e17_w_int_L", "e17_w_null_L", "e17_w_int_XXL", "e17_w_null_XXL", "e17_e8a_biased_r1", "e17_e8a_unbiased"]
MODELS19 = {"sol61": "gpt-6.1-sol", "sol6": "gpt-6-sol", "luna6": "gpt-6-luna"}


def copy(src, run, **changes):
    (RUNS / run).mkdir(parents=True, exist_ok=True)
    shutil.copyfile(RUNS / src / "prompt.md", RUNS / run / "prompt.md")
    meta = load_json(RUNS / src / "meta.json")
    meta.update({"run": run, "prompt_from": src, **changes})
    save_json(meta, RUNS / run / "meta.json")
    print(f"{run:28s} {meta.get('model', 'gpt-6-astra'):12s} {meta.get('variant')}")


for tag, model in MODELS19.items():
    for src in CELLS:
        copy(src, f"e19_{tag}_{src[4:]}", model=model, replicate_of=None)
for src in ["e17_w_int_L", "e17_w_null_L", "e17_w_int_XXL", "e17_e8a_biased_r1",
            "e18_int_L", "e18_null_L", "e18_int_XXL", "e18_e8a_biased_r1"]:
    copy(src, f"e20_{src}", replicate_of=src)
