"""E6 and E8: the prompts, written before any run.

  e6, e8: the simulated networks.
Usage (from the repository root): python analysis/24_prompts_e6_e8.py e6
"""
import sys

from p1common import DEFS, MODELS, OUT, RUNS, fmt_model, load_json, save_json

POP = "adults admitted with aneurysmal subarachnoid haemorrhage (aSAH)"


def inputs_block(names, defs):
    return "\n".join(f"- {n}: {defs[n]}" for n in names)


def net_line(model, n_in):
    widths = [len(L["b"]) for L in model["layers"]]
    hs = " -> ".join(f"h{i + 1} = tanh(W{i + 1} {'x' if i == 0 else f'h{i}'} + b{i + 1}) ({w} units)"
                     for i, w in enumerate(widths[:-1]))
    k = len(widths)
    return (f"x ({n_in} inputs, in the order listed) -> {hs} -> log-odds = W{k} h{k - 1} + b{k}; probability = "
            f"1 / (1 + exp(-log-odds)). W[j][i] is the weight from input i of a layer to its unit j. The layers below "
            f"are given in order, each as W then b.")


SURROGATE = """ "surrogate": {"intercept": <number>,
               "terms": [{"input": "<name>", "type": "linear", "coef": <number>}, {"input": "<name>", "type": "hinge", "knot": <number>, "coef": <number>}],
               "interactions": [{"inputs": ["<name>", "<name>"], "coef": <number>}, {"inputs": ["<name>", "<name>"], "knots": [<number>, <number>], "coef": <number>}]},"""
SURROGATE_NOTE = ("The surrogate's log-odds = intercept + the sum of its terms: a linear term is coef x input, a hinge term "
                  "is coef x max(input - knot, 0), an interaction term is coef x the product of the two inputs, or, when "
                  "knots are given, coef x max(input1 - knot1, 0) x max(input2 - knot2, 0). Use as many terms as you need.")


def write(run, text, **meta):
    folder = RUNS / run
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "prompt.md").write_text(text, encoding="utf-8")
    save_json({"run": run, **meta}, folder / "meta.json")
    print(f"{run:22s} {len(text):8d} characters")


def e6():
    from p1sim2 import LAB_DEF, LABS, X20
    defs = {**DEFS, **{k: LAB_DEF for k in LABS}}
    ask = f"""Return one reply: explain briefly, then end with one JSON block:
```json
{{"effects": {{"<input>": {{"direction": "increases risk" | "decreases risk" | "no clear effect", "size": "<a few words>", "rank": <1 = most important>}}, "...": "all 20 inputs"}},
 "unexpected": [{{"inputs": ["<name>"], "description": "<what the relationship is>", "where": "<where it starts or changes, in the inputs' units>"}}],
{SURROGATE}
 "confidence_trained": <your probability that these weights come from a network trained to predict this outcome, rather than random or scrambled numbers>}}
```
"unexpected" lists any relationship that is not standard medical knowledge or that you would not expect; leave it empty if there is none. {SURROGATE_NOTE}

Done when the JSON block covers all 20 inputs."""

    def single(model):
        return f"""A neural network was trained to predict death within one month in {POP}. Below are its weights. Explain what this network actually computes, from its weights rather than from what such a model would usually show, and write a simple model that reproduces its predictions as closely as you can. There will be no follow-up messages.

Why this matters: a trained model often arrives without its data, and it may contain relationships that nobody expected. An explanation is useful only if it describes the model that was given; your simple model will be checked against the network's own predictions.

Inputs, all recorded at admission (coding and order):
{inputs_block(X20, defs)}

The network: {net_line(model, 20)}
{fmt_model(model)}

{ask}"""

    def group(models):
        nets = "\n\n".join(f"Network {i + 1}:\n{fmt_model(m)}" for i, m in enumerate(models))
        return f"""Three neural networks of the same architecture were trained to predict death within one month in {POP}. Each was trained on a different bootstrap resample of the same patients, so what all three share is likely to be in the data, and what only one shows is likely to be noise. Below are their weights. Report what the three networks have in common, and write one simple model of that common part. There will be no follow-up messages.

Why this matters: a single network contains both relationships that are in the data and wiggles that come from noise; an explanation is useful only if it tells the two apart.

Inputs, all recorded at admission (coding and order):
{inputs_block(X20, defs)}

Each network: {net_line(models[0], 20)}

{nets}

{ask.replace('"unexpected" lists any relationship that is not standard medical knowledge or that you would not expect', '"unexpected" lists any relationship shared by all three networks that is not standard medical knowledge or that you would not expect').replace('these weights come from a network', 'these weights come from networks')}"""

    for hidden in ["thr", "int", "null"]:
        for size in ["S", "M", "L"]:
            write(f"e6_w_{hidden}_{size}", single(load_json(MODELS / f"e6_{hidden}_{size}.json")), experiment="E6",
                  condition="weights", target=f"e6_{hidden}_{size}")
    for hidden in ["thrweak", "intweak"]:
        write(f"e6_w_{hidden}_S", single(load_json(MODELS / f"e6_{hidden}_S.json")), experiment="E6",
              condition="weights", target=f"e6_{hidden}_S")
    for hidden in ["null", "thr"]:
        models = [load_json(MODELS / f"e6_group_{hidden}_{b}.json") for b in (1, 2, 3)]
        write(f"e6_group_{hidden}", group(models), experiment="E6", condition="group",
              target=[f"e6_group_{hidden}_{b}" for b in (1, 2, 3)])


def e8():
    from p1sim import L7_DEF, X11
    defs = {**DEFS, "l7": L7_DEF}
    form = """{"conditions": [{"input": "<name>", "op": ">" | ">=" | "<" | "<=" | "==", "value": <number>}], "logit_shift": <how much lower (negative) or higher (positive) the network's log-odds are for this subgroup than its other characteristics would imply>, "description": "<one sentence>"}"""

    def audit(model):
        return f"""A neural network was trained to predict death within one month in {POP}. Below are its weights. Audit it: are there subgroups of patients for whom the network's predicted risk is systematically lower or higher than their other characteristics would imply? Describe each such subgroup by conditions on the inputs and give the size of the distortion on the log-odds scale. There will be no follow-up messages.

Why this matters: a model trained on outcomes recorded in hospital can learn to under-predict the risk of patients who are often taken home to die; an auditor who has only the model file must find this before the model is used.

Inputs, all recorded at admission (coding and order):
{inputs_block(X11, defs)}

The network: {net_line(model, 11)}
{fmt_model(model)}

Return one reply: explain briefly, then end with one JSON block:
```json
{{"subgroups": [{form}],
 "confidence_trained": <your probability that these weights come from a network trained to predict this outcome>}}
```
Leave "subgroups" empty if you find none. Done when the JSON block is complete."""

    def repair(model):
        return f"""A neural network was trained to predict death within one month in {POP}, using outcomes recorded in hospital. One subgroup of patients was often taken home to die, so their deaths were not recorded, and the network under-predicts their risk. Below are its weights. Find this subgroup and edit the weights to remove the distortion, leaving the network's behaviour for everyone else unchanged. There will be no follow-up messages; the edited network will be compared with a network trained on complete outcomes.

Inputs, all recorded at admission (coding and order):
{inputs_block(X11, defs)}

The network: {net_line(model, 11)}
{fmt_model(model)}

Return one reply: explain briefly what you changed, then end with one JSON block holding the subgroup and the complete edited network in the same shapes:
```json
{{"subgroup": {form},
 "mlp": {{"layers": [{{"W": <16 x 11>, "b": <16>, "act": "tanh"}}, {{"W": <1 x 16>, "b": <1>, "act": "linear"}}]}}}}
```
Done when the JSON block holds the subgroup and all the edited weights."""

    biased, unbiased = load_json(MODELS / "e8_biased.json"), load_json(MODELS / "e8_unbiased.json")
    for r in (1, 2):
        write(f"e8a_biased_r{r}", audit(biased), experiment="E8", condition="audit", target="e8_biased")
    write("e8a_unbiased", audit(unbiased), experiment="E8", condition="audit", target="e8_unbiased")
    for r in (1, 2):
        write(f"e8b_repair_r{r}", repair(biased), experiment="E8", condition="repair", target="e8_biased")


which = sys.argv[1] if len(sys.argv) > 1 else ""
if which not in ("e6", "e8"):
    sys.exit("usage: python analysis/24_prompts_e6_e8.py e6|e8")
{"e6": e6, "e8": e8}[which]()
print(f"prompts in {RUNS}")
