"""E12: the E8 prompts with the reference made explicit. Built from the E8 prompt files,
so that everything else stays word for word; each replacement is checked.
Writes results/simulation/llm_runs/e12*/prompt.md and meta.json.
Usage (from the repository root): python analysis/28_prompts_e12.py
"""
import sys

from p1common import OUT, RUNS, save_json


REF = ("Reference for \"what their other characteristics would imply\": the additive part of the network, that is, the "
       "model in which each input adds a fixed amount to the log-odds, fitted to this network's own log-odds over patients "
       "like those it was trained on. A subgroup's distortion is the average amount by which the network's log-odds in "
       "that subgroup lie above (positive) or below (negative) this additive reference.\n\n"
       "Patients like those the network was trained on: mean age 56 years (SD 12; 5th-95th centile 36-76; 23% over 65); "
       "women 60%; WFNS grade 4-5 21%; Fisher grade 3-4 55%; intraventricular haemorrhage 25%; intracerebral haemorrhage "
       "15%; hypertension 41%; treated 85%; urban 51%; farmers 30% (15% of urban and 45% of rural patients); l7 uniform "
       "on 0-10 and unrelated to the other inputs. Patients with WFNS grade 4-5 more often have Fisher grade 3-4 and "
       "intraventricular or intracerebral haemorrhage, and are less often treated.\n\n")
INPUTS = "Inputs, all recorded at admission (coding and order):"
SUB = "Women farmers over 65 (female = 1, farmer = 1 and age_c > 0.5)"


def swap(text, old, new):
    assert text.count(old) == 1, old[:60]
    return text.replace(old, new)


def write(run, text, **meta):
    (RUNS / run).mkdir(parents=True, exist_ok=True)
    (RUNS / run / "prompt.md").write_text(text, encoding="utf-8")
    save_json({"run": run, "experiment": "E12", **meta}, RUNS / run / "meta.json")
    print(f"{run:22s} {len(text):7d} characters")


for net, src, runs in [("e8_biased", "e8a_biased_r1", ["e12a_biased_r1", "e12a_biased_r2"]),
                       ("e8_unbiased", "e8a_unbiased", ["e12a_unbiased"])]:
    t = (RUNS / src / "prompt.md").read_text(encoding="utf-8")
    t = swap(t, "give the size of the distortion on the log-odds scale.",
             "give the size of the distortion on the log-odds scale. Report only subgroups whose distortion is at least "
             "0.5 in absolute value and that standard medical knowledge of aSAH prognosis does not explain as a real effect.")
    t = swap(t, INPUTS, REF + INPUTS)
    for run in runs:
        write(run, t, condition="audit", target=net, prompt_from=src)

rep = (RUNS / "e8b_repair_r1" / "prompt.md").read_text(encoding="utf-8")
OLD = ("One subgroup of patients was often taken home to die, so their deaths were not recorded, and the network "
       "under-predicts their risk. Below are its weights. Find this subgroup and edit the weights to remove the "
       "distortion, leaving the network's behaviour for everyone else unchanged. There will be no follow-up messages; "
       "the edited network will be compared with a network trained on complete outcomes.")
b = swap(rep, OLD, f"{SUB} were often taken home to die, so their deaths were not recorded, and the network under-predicts "
         "their risk. Below are its weights. Edit the weights so that the network's log-odds for patients in this subgroup "
         "no longer depart from the additive part of the network (defined below), leaving the network's behaviour for "
         "everyone else unchanged. There will be no follow-up messages; the edited network will be compared with a "
         "network trained on complete outcomes.")
b = swap(b, INPUTS, REF + INPUTS)
for r in (1, 2):
    write(f"e12b_repair_r{r}", b, condition="repair_subgroup", target="e8_biased", prompt_from="e8b_repair_r1")
c = swap(rep, OLD, f"{SUB} were often taken home to die, so their deaths were not recorded, and the network under-predicts "
         "their risk by about 1.6 on the log-odds scale. Below are its weights. Edit the weights so that the network's "
         "log-odds for every patient in this subgroup are 1.6 higher than now, and every other patient's log-odds are "
         "unchanged. There will be no follow-up messages; the edited network will be checked patient by patient against "
         "the original.")
for r in (1, 2):
    write(f"e12c_exact_r{r}", c, condition="repair_exact", target="e8_biased", prompt_from="e8b_repair_r1")
