"""Shared definitions and functions: input definitions, network prediction and fitting, surrogate evaluation, and
file input and output. Paths point to results/simulation.
"""
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier

OUT = Path(__file__).resolve().parent.parent / "results" / "simulation"
RUNS = OUT / "llm_runs"
MODELS = OUT / "models"
PROMPTS = Path(__file__).resolve().parent / "prompts"


def expit(x):
    return 1 / (1 + np.exp(-np.asarray(x, float)))


X8 = ["age_c", "female", "wfns45", "fisher34", "ct_ivh", "ct_ich", "htn", "surgery"]

X10 = X8 + ["urban", "farmer"]

XCAP = ["age_c", "female", "wfns45", "surgery", "urban", "farmer"]

DEFS = {
    "age_c": "(age in years - 60) / 10, so 0 is age 60 and 1 is ten years older",
    "female": "1 female, 0 male",
    "wfns45": "1 if WFNS grade 4 or 5 at admission, 0 if grade 1-3",
    "fisher34": "1 if Fisher grade 3 or 4 on the admission CT, 0 if grade 1-2",
    "ct_ivh": "1 if intraventricular haemorrhage on the admission CT, else 0",
    "ct_ich": "1 if intracerebral (parenchymal) haemorrhage on the admission CT, else 0",
    "htn": "1 if a history of hypertension, else 0",
    "surgery": "1 if the aneurysm was treated (surgical clipping or endovascular coiling) during the admission, "
               "0 if managed conservatively",
    "urban": "1 if the patient lives in a city, 0 otherwise",
    "farmer": "1 if the patient's occupation is farmer, else 0",
}

def predict_logit(model: dict, X: np.ndarray) -> np.ndarray:
    X = np.asarray(X, float)
    if model["kind"] == "logistic":
        return model["intercept"] + X @ np.array([model["coef"][k] for k in model["inputs"]], float)
    h = X
    for layer in model["layers"]:
        h = h @ np.asarray(layer["W"], float).T + np.asarray(layer["b"], float)
        if layer["act"] == "tanh":
            h = np.tanh(h)
        elif layer["act"] == "relu":
            h = np.maximum(h, 0)
    return h[:, 0]

def predict(model: dict, d: pd.DataFrame) -> np.ndarray:
    return expit(predict_logit(model, d[model["inputs"]].values))

def fit_mlp(d: pd.DataFrame, y: str, inputs: list[str], hidden=8, seed: int = 0, early_stopping: bool = False) -> dict:
    """A tanh network; `hidden` is the width of one hidden layer, or a tuple of widths for several. By default L-BFGS
    with a light L2 penalty (E4); with early_stopping, Adam stopped on a 15% validation split (E6, E8, E11), which
    keeps larger networks from memorising noise."""
    from sklearn.neural_network import MLPClassifier
    sizes = (hidden,) if isinstance(hidden, int) else tuple(hidden)
    if early_stopping:
        m = MLPClassifier(hidden_layer_sizes=sizes, activation="tanh", solver="adam", alpha=1e-4, early_stopping=True,
                          validation_fraction=0.15, n_iter_no_change=20, max_iter=2000, random_state=seed)
    else:
        m = MLPClassifier(hidden_layer_sizes=sizes, activation="tanh", solver="lbfgs", alpha=1.0, max_iter=5000,
                          random_state=seed)
    m = m.fit(d[inputs].values, d[y].values)
    layers = [{"W": W.T.tolist(), "b": b.tolist(), "act": "tanh"} for W, b in zip(m.coefs_, m.intercepts_)]
    layers[-1]["act"] = "linear"
    return {"kind": "mlp", "inputs": list(inputs), "layers": layers}

def surrogate_logit(s: dict, d: pd.DataFrame) -> np.ndarray:
    """Log-odds of a surrogate written as JSON (intercept, linear and hinge terms, pairwise products, optionally of
    hinges)."""
    z = np.full(len(d), float(s.get("intercept", 0.0)))
    for t in s.get("terms", []):
        x = d[t["input"]].values.astype(float)
        if t.get("type", "linear") == "hinge":
            x = np.maximum(x - float(t["knot"]), 0.0)
        z += float(t["coef"]) * x
    for t in s.get("interactions", []):
        (a, b), knots = t["inputs"], t.get("knots")
        xa, xb = d[a].values.astype(float), d[b].values.astype(float)
        if knots:  # product of two hinges: coef x max(a - k1, 0) x max(b - k2, 0)
            xa, xb = np.maximum(xa - float(knots[0]), 0.0), np.maximum(xb - float(knots[1]), 0.0)
        z += float(t["coef"]) * xa * xb
    return z

def fidelity(target: np.ndarray, guess: np.ndarray) -> dict:
    """How closely one set of log-odds reproduces another."""
    sst = float(np.sum((target - target.mean()) ** 2))
    top_t = target >= np.quantile(target, 0.9)
    top_g = guess >= np.quantile(guess, 0.9)
    from scipy.stats import spearmanr
    return {"r": float(np.corrcoef(target, guess)[0, 1]), "r2": 1 - float(np.sum((target - guess) ** 2)) / sst,
            "spearman": float(spearmanr(target, guess).statistic), "top10_overlap": float((top_t & top_g).sum() / top_t.sum()),
            "mean_abs_diff": float(np.mean(np.abs(target - guess)))}

def shuffled(model: dict, seed: int = 20261104) -> dict:
    """The same network with the entries of every weight matrix and bias vector permuted at random."""
    rng = np.random.default_rng(seed)
    layers = []
    for layer in model["layers"]:
        W, b = np.asarray(layer["W"], float), np.asarray(layer["b"], float)
        layers.append({"W": rng.permutation(W.ravel()).reshape(W.shape).tolist(), "b": rng.permutation(b).tolist(),
                       "act": layer["act"]})
    return {**model, "layers": layers}

def fmt_model(model: dict, digits: int = 4) -> str:
    """A model as compact JSON text for a prompt (numbers to `digits` significant figures)."""
    def r(x):
        if isinstance(x, list):
            return [r(v) for v in x]
        if isinstance(x, dict):
            return {k: r(v) for k, v in x.items()}
        return float(f"{x:.{digits}g}") if isinstance(x, float) else x
    if model["kind"] == "logistic":
        body = {"intercept": r(model["intercept"]), "coef": r(model["coef"])}
    else:
        body = {"layers": [{"W": r(L["W"]), "b": r(L["b"]), "act": L["act"]} for L in model["layers"]]}
    return json.dumps(body, separators=(",", ":"))

def last_json(text: str):
    """The last fenced ```json block of a reply, parsed; None when there is none or it does not parse."""
    blocks = re.findall(r"```json\s*(.*?)```", text, flags=re.S)
    for block in reversed(blocks):
        try:
            return json.loads(block)
        except json.JSONDecodeError:
            continue
    return None

def save_json(obj, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=1, ensure_ascii=False), encoding="utf-8")
    return path

def load_json(path: Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))
