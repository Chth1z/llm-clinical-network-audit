"""A one-tool MCP server (stdio, JSON-RPC 2.0, no dependencies) for E17: `run_python` runs NumPy code with one
simulated network preloaded, and nothing else. It is the only tool the model gets; it has no file, network or shell
access.

Each call runs in a fresh subprocess (python -I, empty temporary folder, stripped environment, 60 s, output capped)
after an AST check: no imports; no name or attribute that starts with "_"; no NumPy file input/output or other
escape hatches (DENY); builtins limited to plain computation (SAFE_BUILTINS). This is a guard against a model that
wanders, not a security boundary against one that attacks.
With --blackbox (E18) only predict(X) is loaded: no weights and no layer information.
Usage (by Codex): python calc_server.py <network.json> [--blackbox]
"""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

NET = str(Path(sys.argv[1]).resolve())
BLACKBOX = "--blackbox" in sys.argv[2:]
DESCRIPTION = (
    "Run Python code (NumPy only) and return what it prints. Preloaded: np (NumPy); the network's layers as W1, b1, "
    "W2, b2, ... (NumPy arrays; W[j][i] is the weight from input i of a layer to its unit j); acts, the list of "
    "activations per layer; INPUTS, the input names in order; predict(X), the network's log-odds for an (n, inputs) "
    "array. Each call starts fresh: nothing is kept between calls. No imports, files, network or names beginning "
    "with an underscore; at most 60 seconds and 20,000 characters of output per call.")
if BLACKBOX:
    DESCRIPTION = ("Run Python code (NumPy only) and return what it prints. Preloaded: np (NumPy); INPUTS, the input "
                   "names in order; predict(X), the network's log-odds for an (n, inputs) array. The network's weights "
                   "are not available. Each call starts fresh: nothing is kept between calls. No imports, files, network "
                   "or names beginning with an underscore; at most 60 seconds and 20,000 characters of output per call.")
RUNNER = r'''
import ast, json, sys
import numpy as np
DENY = {"load", "loads", "save", "savez", "savez_compressed", "savetxt", "loadtxt", "genfromtxt", "fromfile", "tofile",
        "memmap", "fromregex", "DataSource", "lib", "ctypeslib", "testing", "f2py", "distutils", "os", "sys", "core",
        "dump", "dumps", "open", "system", "popen", "subprocess", "shutil", "pathlib", "builtins", "globals", "locals",
        "vars", "getattr", "setattr", "delattr", "eval", "exec", "compile", "importlib", "input", "breakpoint", "exit",
        "quit", "help", "memoryview", "frombuffer", "show_config", "show_runtime", "info", "source", "lookfor",
        "get_include", "ctypes", "char", "rec", "polynomial", "ma", "emath", "dtypes", "exceptions"}
SAFE_BUILTINS = {k: __builtins__[k] if isinstance(__builtins__, dict) else getattr(__builtins__, k) for k in [
    "abs", "all", "any", "bool", "dict", "divmod", "enumerate", "filter", "float", "format", "int", "isinstance", "len",
    "list", "map", "max", "min", "pow", "print", "range", "repr", "reversed", "round", "set", "slice", "sorted", "str",
    "sum", "tuple", "zip", "ValueError", "ZeroDivisionError", "Exception", "True", "False", "None"]
    if (k in __builtins__ if isinstance(__builtins__, dict) else hasattr(__builtins__, k))}
# NumPy's C code imports lazily through the caller's builtins; the code checked below cannot name it (no "_" names)
SAFE_BUILTINS["__import__"] = __import__
code = sys.stdin.read()
tree = ast.parse(code)
for node in ast.walk(tree):
    if isinstance(node, (ast.Import, ast.ImportFrom, ast.Global, ast.Nonlocal)):
        raise SystemExit("not allowed: import, global or nonlocal")
    name = node.id if isinstance(node, ast.Name) else node.attr if isinstance(node, ast.Attribute) else \
        node.name if isinstance(node, (ast.FunctionDef, ast.ClassDef)) else None
    if name is not None and (name.startswith("_") or name in DENY):
        raise SystemExit(f"not allowed: {name}")
net = json.loads(open(sys.argv[1], encoding="utf-8").read())
ns = {"__builtins__": SAFE_BUILTINS, "np": np, "INPUTS": list(net["inputs"])}
if sys.argv[2] == "white":
    ns["acts"] = [L["act"] for L in net["layers"]]
    for i, L in enumerate(net["layers"], 1):
        ns[f"W{i}"], ns[f"b{i}"] = np.array(L["W"], float), np.array(L["b"], float)
layers = [(np.array(L["W"], float), np.array(L["b"], float), L["act"]) for L in net["layers"]]
def predict(X):
    h = np.atleast_2d(np.asarray(X, float))
    for W, b, act in layers:
        h = h @ W.T + b
        h = np.tanh(h) if act == "tanh" else h
    return h[:, 0]
ns["predict"] = predict
exec(compile(tree, "<run_python>", "exec"), ns)
'''


def run_python(code: str) -> str:
    with tempfile.TemporaryDirectory(prefix="p1_calc_") as work:
        try:
            p = subprocess.run([sys.executable, "-I", "-c", RUNNER, NET, "black" if BLACKBOX else "white"], input=code, capture_output=True, text=True,
                               cwd=work, timeout=60, env={"SYSTEMROOT": os.environ.get("SYSTEMROOT", "")})
            failed = p.returncode != 0
            out = p.stdout + (("\n[error]\n" + p.stderr[-4000:]) if failed else "")
        except subprocess.TimeoutExpired:
            failed, out = True, "[error] more than 60 seconds"
    return failed, out[:20000] + ("\n[output cut at 20,000 characters]" if len(out) > 20000 else "")


def reply(id_, result=None, error=None):
    msg = {"jsonrpc": "2.0", "id": id_}
    msg.update({"error": error} if error else {"result": result})
    sys.stdout.write(json.dumps(msg) + "\n")
    sys.stdout.flush()


for line in sys.stdin:
    if not line.strip():
        continue
    req = json.loads(line)
    method, id_ = req.get("method"), req.get("id")
    if id_ is None:  # a notification (e.g. notifications/initialized)
        continue
    if method == "initialize":
        reply(id_, {"protocolVersion": req.get("params", {}).get("protocolVersion", "2025-06-18"),
                    "capabilities": {"tools": {}}, "serverInfo": {"name": "calc", "version": "1"}})
    elif method == "tools/list":
        reply(id_, {"tools": [{"name": "run_python", "description": DESCRIPTION,
                               "inputSchema": {"type": "object", "properties": {"code": {"type": "string"}},
                                               "required": ["code"]}}]})
    elif method == "tools/call":
        args = req.get("params", {}).get("arguments", {})
        failed, out = run_python(str(args.get("code", "")))
        reply(id_, {"content": [{"type": "text", "text": out}], "isError": failed})
    elif method == "ping":
        reply(id_, {})
    else:
        reply(id_, error={"code": -32601, "message": f"unknown method {method}"})
