# Computation, not weight access: large language models as auditors of clinical prediction networks — artefacts

This repository holds everything behind the experiments of the preprint *Computation, not weight access: large language models as auditors of clinical prediction networks* ([arXiv:2611.07847](https://arxiv.org/abs/2611.07847)): the simulated networks, every prompt and reply, the event logs, the scoring code and the tables. All networks were trained on simulated data.

## Layout

| Path | What it holds |
|---|---|
| `results/simulation/models/` | The simulated networks (JSON: layers with `W`, `b`, activation) |
| `results/simulation/llm_runs/<run>/` | One folder per run: `prompt.md` (the prompt), `meta.json` (experiment, condition, target network, model, system instruction, tool), `reply.md`, `parsed.json`, `run.json` (start time, seconds, exit code, token usage, tool-use audit), `events.jsonl` (the event stream), `stderr.log`; files named `*_busy_*`, `*_killed_*` or `failed_service_*` are attempts that failed or were stopped and were repeated |
| `results/simulation/*.csv` | Scoring tables produced by the evaluation scripts |
| `analysis/` | Code: simulation and training (`p1sim*.py`, `11_`, `13_`, `15_`, `16_`), prompt writers (`22_`–`37_`), runner and queue (`21_astra.py`, `22_queue.py`), parser (`30_parse.py`), scoring (`41_`–`63_`) |
| `analysis/tools/calc_server.py` | The calculation-only tool (a one-tool MCP server) |
| `analysis/prompts/` | The two system instructions (default and explicit) |
| `manuscript/preprint/` | LaTeX source of the preprint; `make_assets.py` regenerates its tables and figures from `results/simulation` |

## Experiments

| Label | Question | Networks | Runs |
|---|---|---|---|
| E4 | Read planted relationships in 105-weight networks | `e4_*` | `e4_w_*` |
| E6 | Size ladder (S, M, L), half strength, bootstrap groups | `e6_*` | `e6_w_*`, `e6_group_*` |
| E8 | Audit and repair a network trained on biased labels | `e8_biased`, `e8_unbiased` | `e8a_*`, `e8b_*` |
| E10 | Function-preserving rewrites (permuted, sign-flipped units) | `e10_*` | `e10_*` |
| E11 | Larger and deeper networks (XL, XXL, D3) | `e11_*` | via E17 |
| E12 | Audit and repair with a stated reference | as E8 | `e12a_*`, `e12b_*`, `e12c_*` |
| E13 | Other models without tools | as E4 | `e13_*` |
| E16 | Explicit system instruction, prompts unchanged | as above | `e16_*` |
| E17 | Calculation-only tool, white box | `e6_*`, `e11_*`, `e8_*` | `e17_*` |
| E18 | Calculation-only tool, black box (predictions only) | as E17 | `e18_*` |
| E19 | Other models with the tool | as E17 | `e19_*` |
| E20, E22 | Repeats of key cells | as above | `e20_*`, `e22_*` |
| E25 | Repeats so that every cell of the reading, audit and repair tables has three runs | as above | `e25_*` |
| E21 | Scripted audit without an LLM | `e8_*` | `analysis/62_e21_scripted_audit.py` |
| E23 | Scripted repairs without an LLM | `e8_biased` | `analysis/63_e23_scripted_repair.py` |

## Re-scoring

With Python 3.11+ and `numpy`, `pandas`, `scikit-learn`, `statsmodels`, `matplotlib`:

```
cd analysis
python 30_parse.py          # replies -> parsed.json
python 54_eval_e6.py        # reading (E6, E16-E22, E25)
python 58_e6_scan.py        # claims at zero locations
python 56_eval_e8.py        # audit and repair (E8, E16-E20, E22, E25)
python 60_eval_e12.py       # E12 and its E16/E17 variants (with E25)
python 59_eval_e13.py       # other models (E13)
python 57_eval_e10.py       # rewrites (E10)
python 62_e21_scripted_audit.py
python 63_e23_scripted_repair.py
cd .. && python manuscript/preprint/make_assets.py
python manuscript/preprint/e25_facts.py   # numbers quoted in the text
```

The commit times in the pre-specification table (`tables/prespec.tex`) are read from the repository in which the plans were committed, so `make_assets.py` leaves them empty elsewhere; the released table carries them.

## Re-running the models

Runs used the Codex command-line interface (0.166.0) with an OpenAI account: `codex exec` in a new empty folder, the user's configuration ignored, a read-only sandbox, web search off and every built-in tool disabled (`analysis/21_astra.py` gives the exact command). Each run's `meta.json` names the model and the system instruction. For E17–E19 and their repeats the runner adds the calculation-only tool as an MCP server; the tool refuses imports, names beginning with an underscore and NumPy's file functions, runs each call in a fresh subprocess in an empty folder with a 60-second limit, and accepts only the networks in `results/simulation/models`. This guards against a model that wanders; it is not a security boundary against one that attacks. `analysis/22_queue.py` limits the number of concurrent runs.

## Licence

Code: MIT (`LICENSE`). Networks, prompts, replies, logs and tables: CC BY 4.0.

## Citation

Liu Z, Yang X. Computation, not weight access: large language models as auditors of clinical prediction networks. arXiv:2611.07847 [cs.LG], 2026. https://arxiv.org/abs/2611.07847

```bibtex
@misc{liu2026computation,
  title         = {Computation, not weight access: large language models as auditors of clinical prediction networks},
  author        = {Liu, Zhiyu and Yang, Xinyu},
  year          = {2026},
  eprint        = {2611.07847},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url           = {https://arxiv.org/abs/2611.07847}
}
```
