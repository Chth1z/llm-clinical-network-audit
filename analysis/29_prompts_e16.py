"""E16: the same prompts with system instructions that leave the open choices to the model
(prompts/instructions_assume.md), and for two repair tasks a stated tolerance.
Prompts are copied byte for byte from the source runs, except the two tolerance variants (each replacement checked).
Writes results/simulation/llm_runs/e16_*/prompt.md and meta.json ("instructions", "variant").
Usage (from the repository root): python analysis/29_prompts_e16.py
"""
import sys

from p1common import OUT, RUNS, load_json, save_json

END = ("There will be no follow-up messages; the edited network will be checked patient by patient against the "
       "original.")
TOL_C = ("An approximation is expected: a tanh network cannot jump exactly at age 65, so patients aged 64-66 may be "
         "treated either way. Done when, for everyone else, the change in log-odds is within 0.1 of the target (+1.6 in "
         "the subgroup, 0 outside it). ")
END_B = ("There will be no follow-up messages; the edited network will be compared with a network trained on complete "
         "outcomes.")
TOL_B = ("An approximation is expected: patients aged 64-66 may be treated either way. Done when, for everyone else, the "
         "subgroup's average departure from the additive part is within 0.2 of zero and other patients' log-odds change "
         "by less than 0.1. ")


def make(src, run, variant="assume", replace=None):
    text = (RUNS / src / "prompt.md").read_text(encoding="utf-8")
    if replace:
        old, new = replace
        assert text.count(old) == 1, (src, old[:50])
        text = text.replace(old, new)
    meta = load_json(RUNS / src / "meta.json")
    meta.update({"run": run, "instructions": "instructions_assume.md", "variant": variant, "prompt_from": src})
    (RUNS / run).mkdir(parents=True, exist_ok=True)
    (RUNS / run / "prompt.md").write_text(text, encoding="utf-8")
    save_json(meta, RUNS / run / "meta.json")
    print(f"{run:24s} {meta['experiment']:4s} {meta['condition']:16s} {variant}")


for src in ["e8a_biased_r1", "e8a_biased_r2", "e8a_unbiased", "e8b_repair_r1", "e8b_repair_r2",
            "e12a_biased_r1", "e12a_biased_r2", "e12a_unbiased", "e12c_exact_r1", "e12c_exact_r2",
            "e6_group_null", "e6_group_thr"]:
    make(src, f"e16_{src}")
for r in (1, 2):
    make(f"e12b_repair_r{r}", f"e16_e12b_tol_r{r}", "assume+tolerance", (END_B, TOL_B + END_B))
    make(f"e12c_exact_r{r}", f"e16_e12c_tol_r{r}", "assume+tolerance", (END, TOL_C + END))
