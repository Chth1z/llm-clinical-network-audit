"""E4: the prompts, written before any run.

  e4: the simulated networks with a hidden relationship.
Usage (from the repository root): python analysis/22_prompts_e4.py e4
"""
import sys

from p1common import DEFS, MODELS, OUT, RUNS, X8, fmt_model, load_json, save_json, shuffled

POPULATION = "adults admitted with aneurysmal subarachnoid haemorrhage (aSAH), followed up for vital status"


def inputs_block(names, defs):
    return "\n".join(f"- {n}: {defs[n]}" for n in names)


def write(run, text, **meta):
    folder = RUNS / run
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "prompt.md").write_text(text, encoding="utf-8")
    save_json({"run": run, **meta}, folder / "meta.json")
    print(f"{run:14s} {len(text):7d} characters")


def e4():
    from p1sim import L7_DEF, X11
    defs = {**DEFS, "l7": L7_DEF}
    net = ("x (11 inputs, in the order listed) -> h = tanh(W1 x + b1) (8 units) -> log-odds = W2 h + b2; probability = "
           "1 / (1 + exp(-log-odds)). W[j][i] is the weight from input i of a layer to its unit j, so W1 has 8 rows of "
           "11 numbers and W2 has 1 row of 8.")
    ask = """Return one reply: explain briefly, then end with one JSON block:
```json
{"effects": {"<input>": {"direction": "increases risk" | "decreases risk" | "no clear effect", "size": "<a few words>", "rank": <1 = most important>}, "...": "all 11 inputs"},
 "interactions": ["<short description>"],
 "unexpected": [{"inputs": ["<name>"], "description": "<what the relationship is>", "where": "<where it starts or changes, in the inputs' units>"}],
 "surrogate": {"intercept": <number>,
               "terms": [{"input": "<name>", "type": "linear", "coef": <number>}, {"input": "<name>", "type": "hinge", "knot": <number>, "coef": <number>}],
               "interactions": [{"inputs": ["<name>", "<name>"], "coef": <number>}]},
 "confidence_trained": <your probability that these weights come from a network trained to predict this outcome, rather than random or scrambled numbers>}
```
"unexpected" lists any relationship in the network that is not standard medical knowledge, or that you would not expect; leave it empty if there is none. The surrogate's log-odds = intercept + the sum of its terms: a linear term is coef x input, a hinge term is coef x max(input - knot, 0), an interaction term is coef x the product of the two inputs. Use as many terms as you need.

Done when the JSON block covers all 11 inputs."""

    def with_weights(model):
        return f"""A small neural network was trained to predict death within one month in {POPULATION}. Below are its weights. Explain what this network actually computes, from its weights rather than from what such a model would usually show, and write a simple model that reproduces its predictions as closely as you can. There will be no follow-up messages.

Why this matters: a trained model often arrives without its data, and it may contain relationships that nobody expected. An explanation is useful only if it describes the model that was given; your simple model will be checked against the network's own predictions.

Inputs, all recorded at admission (coding and order):
{inputs_block(X11, defs)}

The network: {net} The layers below are W1, b1 then W2, b2.
{fmt_model(model)}

{ask}"""

    knowledge = f"""A small neural network was trained to predict death within one month in {POPULATION}. We do not show you its weights. Explain what this network most likely computes, and write a simple model that reproduces its predictions as closely as you can. There will be no follow-up messages.

Why this matters: we compare explanations written with and without the weights; your simple model will be checked against the network's own predictions.

Inputs, all recorded at admission (coding and order):
{inputs_block(X11, defs)}

The network: {net}

{ask.replace('<your probability that these weights come from a network trained to predict this outcome, rather than random or scrambled numbers>', 'null')}"""

    nets = {k: load_json(MODELS / f"e4_{k}.json") for k in ["h1", "h2", "h3", "null"]}
    for k, model in nets.items():
        for r in (1, 2):
            write(f"e4_w_{k}_r{r}", with_weights(model), experiment="E4", condition="weights", target=f"e4_{k}")
    write("e4_k", knowledge, experiment="E4", condition="knowledge only", target=[f"e4_{k}" for k in nets])
    write("e4_s_h1", with_weights(shuffled(nets["h1"])), experiment="E4", condition="shuffled weights",
          target="e4_h1_shuffled")


which = sys.argv[1] if len(sys.argv) > 1 else ""
if which != "e4":
    sys.exit("usage: python analysis/22_prompts_e4.py e4")
{"e4": e4}[which]()
print(f"prompts in {RUNS}")
