"""Simulated cohorts for E6 and E8.

E6: 20 inputs, the 10 clinical inputs of E4 plus 10 neutral lab values l1-l10 (uniform on 0-10, independent);
    one hidden relationship on lab values (threshold on l3, or l5 and l8 both high), at two strengths, or none.
E8: the 11 inputs of E4; a subgroup (women farmers over 65) whose recorded risk is pushed down by 3.0 on the log-odds.
"""
import numpy as np
import pandas as pd

from p1common import X10, expit
from p1sim import X11, predictors as clinical_predictors

TRUE_SIG = {"thr": 2.7, "int": 1.58}  # strength of each hidden relationship in the generating log-odds (strength 1)

LABS = [f"l{i}" for i in range(1, 11)]
X20 = X10 + LABS
LAB_DEF = "an admission laboratory value, on a scale from 0 to 10"


def predictors20(n: int, rng: np.random.Generator) -> pd.DataFrame:
    d = clinical_predictors(n, rng)[X10].copy()
    for k in LABS:
        d[k] = rng.uniform(0, 10, n)
    return d[X20]


def s(x):
    return 1 / (1 + np.exp(-2 * (x - 5)))


def base(d: pd.DataFrame) -> np.ndarray:
    return np.asarray(-2.3 + 0.45 * d["age_c"] + 1.8 * d["wfns45"] + 0.4 * d["fisher34"] + 0.5 * d["ct_ivh"]
                      + 0.4 * d["ct_ich"] - 1.6 * d["surgery"] + 0.3 * d["htn"], float)


def log_odds20(d: pd.DataFrame, hidden: str, strength: float = 1.0) -> np.ndarray:
    z = base(d)
    if hidden == "thr":
        z = z + 0.9 * strength * np.maximum(d["l3"].values - 6, 0)
    elif hidden == "int":
        z = z + 1.6 * strength * s(d["l5"].values) * s(d["l8"].values)
    return z


def cohort20(hidden: str, n: int, seed: int, strength: float = 1.0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    d = predictors20(n, rng)
    d["y"] = rng.binomial(1, expit(log_odds20(d, hidden, strength))).astype(float)
    return d


def signatures20(f, d: pd.DataFrame) -> dict:
    """Strength of the two hidden relationships in a model; f maps a frame of inputs to log-odds."""
    def at(**kw):
        z = d.copy()
        for k, v in kw.items():
            z[k] = v
        return f(z)
    thr = np.mean(at(l3=9.0) - at(l3=5.0)) - np.mean(at(l3=5.0) - at(l3=1.0))
    inter = np.mean(at(l5=8.0, l8=8.0) - at(l5=8.0, l8=2.0) - at(l5=2.0, l8=8.0) + at(l5=2.0, l8=2.0))
    return {"thr": float(thr), "int": float(inter)}


def biased_subgroup(d: pd.DataFrame) -> np.ndarray:
    return ((d["female"] == 1) & (d["farmer"] == 1) & (d["age_c"] > 0.5)).values


def cohort_e8(biased: bool, n: int, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    d = clinical_predictors(n, rng)[X11].copy()
    z = base(d) - (3.0 * biased_subgroup(d) if biased else 0.0)
    d["y"] = rng.binomial(1, expit(z)).astype(float)
    return d


def subgroup_mask(d: pd.DataFrame, conditions: list) -> np.ndarray:
    """Patients meeting every condition {"input", "op" ('>', '>=', '<', '<=', '=='), "value"}."""
    m = np.ones(len(d), bool)
    ops = {">": np.greater, ">=": np.greater_equal, "<": np.less, "<=": np.less_equal, "==": np.equal}
    for c in conditions:
        m &= ops[c["op"]](d[c["input"]].values.astype(float), float(c["value"]))
    return m
