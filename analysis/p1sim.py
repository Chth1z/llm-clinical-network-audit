"""Simulated cohorts for E4: the usual aSAH risk factors plus one hidden relationship per model.

Ten clinical inputs, coded as in a typical admission dataset, and l7, a neutral laboratory value (0-10).
"""
import numpy as np
import pandas as pd

from p1common import X10, expit

X11 = X10 + ["l7"]
L7_DEF = "an admission laboratory value, on a scale from 0 to 10"
HIDDEN = {
    "h1": "l7 above 6: risk rises steeply (+0.9 on the log-odds per unit above 6)",
    "h2": "hypertension raises risk only among farmers (+1.6 on the log-odds; no effect otherwise)",
    "h3": "between ages 50 and 60 risk falls with age (-1.5 per ten years), recovering by age 70",
    "null": "none",
}


def predictors(n: int, rng: np.random.Generator) -> pd.DataFrame:
    age = np.clip(rng.normal(56, 12, n), 18, 92)
    a = (age - 60) / 10
    wfns45 = rng.binomial(1, expit(-1.3 + 0.25 * a))
    urban = rng.binomial(1, 0.5, n)
    d = pd.DataFrame({
        "age_c": a, "female": rng.binomial(1, 0.6, n), "wfns45": wfns45,
        "fisher34": rng.binomial(1, expit(1.2 * wfns45)),
        "ct_ivh": rng.binomial(1, expit(-1.3 + 1.1 * wfns45 + 0.2 * a)),
        "ct_ich": rng.binomial(1, expit(-2.0 + 0.9 * wfns45)),
        "htn": rng.binomial(1, expit(-0.2 + 0.5 * a)),
        "surgery": rng.binomial(1, expit(1.8 - 1.2 * wfns45 - 0.35 * a + 0.5 * urban)),
        "urban": urban, "farmer": rng.binomial(1, expit(-0.2 - 1.6 * urban)),
        "l7": rng.uniform(0, 10, n),
    })
    return d[X11].astype(float)


def age_term(a: np.ndarray, dip: bool) -> np.ndarray:
    """0.45 per ten years; with the dip, falling 1.5 per ten years from 50 to 60 and recovering by 70."""
    if not dip:
        return 0.45 * a
    return np.select([a < -1, a < 0, a < 1],
                     [0.45 * a, -0.45 - 1.5 * (a + 1), -1.95 + 2.4 * a], 0.45 * a)


def log_odds(d: pd.DataFrame, model: str) -> np.ndarray:
    z = (-2.3 + age_term(d["age_c"].values, model == "h3") + 1.8 * d["wfns45"] + 0.4 * d["fisher34"]
         + 0.5 * d["ct_ivh"] + 0.4 * d["ct_ich"] - 1.6 * d["surgery"])
    if model == "h2":
        z = z + 1.6 * d["htn"] * d["farmer"]
    else:
        z = z + 0.3 * d["htn"]
    if model == "h1":
        z = z + 0.9 * np.maximum(d["l7"] - 6, 0)
    return np.asarray(z, float)


def cohort(model: str, n: int, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    d = predictors(n, rng)
    d["y"] = rng.binomial(1, expit(log_odds(d, model))).astype(float)
    return d


def signatures(net: dict, d: pd.DataFrame, predict_logit) -> dict:
    """How strongly a network carries each hidden relationship (average changes in its log-odds)."""
    X = d[X11].copy()

    def at(**kw):
        Z = X.copy()
        for k, v in kw.items():
            Z[k] = v
        return predict_logit(net, Z.values)

    farmer = X["farmer"].values == 1
    htn_effect = at(htn=1.0) - at(htn=0.0)
    return {
        "l7_5_to_9_minus_1_to_5": float(np.mean(at(l7=9.0) - at(l7=5.0)) - np.mean(at(l7=5.0) - at(l7=1.0))),
        "htn_effect_farmers": float(htn_effect[farmer].mean()),
        "htn_effect_nonfarmers": float(htn_effect[~farmer].mean()),
        "age_50_to_60": float(np.mean(at(age_c=0.0) - at(age_c=-1.0))),
        "age_40_to_50": float(np.mean(at(age_c=-1.0) - at(age_c=-2.0))),
        "age_60_to_70": float(np.mean(at(age_c=1.0) - at(age_c=0.0))),
    }
