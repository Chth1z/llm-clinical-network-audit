"""Run the prompts through GPT-6 Astra (Codex CLI), one reply each, with every built-in tool switched off.

For each results/simulation/llm_runs/<run>/prompt.md without a reply.md: `codex exec` in a new empty folder outside the
workspace, read-only sandbox, the user's config ignored, a one-line neutral instruction (prompts/instructions_neutral.md),
no shell, no files, no web, no plugins or agents (as in the harness of Takehi et al. 2026). Saves reply.md (the last
message), events.jsonl (the event stream, with token usage), stderr.log and run.json (times, exit code, usage, and an
audit that no tool was used). Runs in order. A run that fails because the service is busy ("at capacity", a dropped
stream) is retried after 2, 5, 10 and 20 minutes, keeping the failed attempt's events; any other failure is retried on
the next start. The system instructions are prompts/instructions_neutral.md unless meta.json names another file
("instructions", E16).
The model is gpt-6-astra unless the run's meta.json names another ("model", E13); run.json records the one used.
Usage (from the repository root): python analysis/21_astra.py [run ...]
"""
import json
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from p1common import OUT, PROMPTS, RUNS, save_json



def allowed(folder: Path) -> bool:
    """Prompts are sent only from run folders of the study layout (results/simulation/llm_runs)."""
    return folder.parent.name == "llm_runs" and folder.parent.parent.name == "simulation"


MODEL, EFFORT, TIMEOUT = "gpt-6-astra", "max", 3 * 3600
CODEX = shutil.which("codex")  # on Windows the npm shim codex.cmd
if not CODEX:
    sys.exit("codex is not on the PATH")
OFF = ["shell_tool", "unified_exec", "unified_exec_tty", "shell_snapshot", "view_image", "image_generation", "multi_agent",
       "apps", "plugins", "remote_plugin", "browser_use", "browser_use_external", "browser_use_full_cdp_access",
       "in_app_browser", "computer_use", "code_mode_host", "skill_search", "skill_mcp_dependency_install", "sleep_tool",
       "tool_suggest", "goals", "hooks", "workspace_dependencies", "memories"]
TEXT_ITEMS = {"agent_message", "reasoning", "error"}  # "error": Codex's notice that code mode is off


TOOL_NETS = (Path(__file__).resolve().parent.parent / "results" / "simulation" / "models").resolve()
CALC = Path(__file__).resolve().parent / "tools" / "calc_server.py"


def command(work: Path, reply: Path, model: str = MODEL, instructions: str = "instructions_neutral.md",
            tool_net: str | None = None, blackbox: bool = False) -> list[str]:
    """tool_net: a simulated network (results/simulation/models/...) for the one-tool calculator of E17; then Code
    Mode's host stays on (Codex routes MCP tools through it) and every other tool stays off."""
    cmd = [CODEX, "exec", "--ignore-user-config", "--ephemeral", "--skip-git-repo-check", "-C", str(work),
           "-s", "read-only", "--json", "-o", str(reply), "-m", model,
           "-c", f'model_reasoning_effort="{EFFORT}"', "-c", 'service_tier="default"', "-c", 'approval_policy="never"',
           "-c", 'web_search="disabled"', "-c", "agents.enabled=false",
           "-c", f'model_instructions_file="{(PROMPTS / instructions).as_posix()}"']
    off = OFF
    if tool_net:
        net = (TOOL_NETS / tool_net).resolve()
        if TOOL_NETS not in net.parents or not net.exists():  # only the simulated networks of this repository
            raise SystemExit(f"the calculator takes only simulated networks in {TOOL_NETS}: {tool_net}")
        off = [f for f in OFF if f != "code_mode_host"]
        cmd += ["-c", f'mcp_servers.calc.command="{Path(sys.executable).as_posix()}"',
                "-c", f'mcp_servers.calc.args=["{CALC.as_posix()}", "{net.as_posix()}"{', "--blackbox"' if blackbox else ''}]',
                "-c", 'mcp_servers.calc.default_tools_approval_mode="approve"', "-c", "mcp_servers.calc.tool_timeout_sec=120"]
    for feature in off:
        cmd += ["--disable", feature]
    return cmd + ["-"]


def audit(events: Path) -> dict:
    usage, items, threads, calls = {}, {}, [], []
    for line in events.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("type") == "turn.completed":
            usage = e.get("usage", {})
        if e.get("type") == "thread.started":
            threads.append(e.get("thread_id"))
        if e.get("type") == "item.completed":
            item = e.get("item", {})
            kind = item.get("type", "?")
            items[kind] = items.get(kind, 0) + 1
            if kind == "mcp_tool_call":
                calls.append(f'{item.get("server")}/{item.get("tool")}')
    other = {k for k in items if k not in TEXT_ITEMS | {"mcp_tool_call", "text"}}
    return {"usage": usage, "items": items, "threads": threads, "tool_free": all(k in TEXT_ITEMS for k in items),
            "tool_calls": len(calls), "only_calculator": not other and all(c == "calc/run_python" for c in calls)}


BUSY = ("at capacity", "stream disconnected", "Reconnecting")
WAITS = [120, 300, 600, 1200]


def busy(events: Path) -> bool:
    text = events.read_text(encoding="utf-8", errors="replace") if events.exists() else ""
    return '"turn.failed"' in text and any(b in text for b in BUSY)


def run(folder: Path):
    meta = json.loads((folder / "meta.json").read_text(encoding="utf-8")) if (folder / "meta.json").exists() else {}
    model, instructions = meta.get("model", MODEL), meta.get("instructions", "instructions_neutral.md")
    tool_net, blackbox = meta.get("tool_network"), bool(meta.get("tool_blackbox"))
    for attempt in range(len(WAITS) + 1):
        code, seconds, started = attempt_once(folder, model, instructions, tool_net, blackbox)
        if code == 0 or not busy(folder / "events.jsonl") or attempt == len(WAITS):
            break
        (folder / "events.jsonl").rename(folder / f"events_busy_{int(started)}.jsonl")
        print(f"{time.strftime('%H:%M:%S')} {folder.name}: service busy, retry in {WAITS[attempt] // 60} min", flush=True)
        time.sleep(WAITS[attempt])
    reply = folder / "reply.md"
    record = {"model": model, "effort": EFFORT, "instructions": instructions, "tool_network": tool_net,
              "tool_blackbox": blackbox,
              "started": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(started)), "seconds": seconds, "exit": code,
              "attempts": attempt + 1, **audit(folder / "events.jsonl")}
    if code != 0 and reply.exists():
        reply.rename(folder / f"reply_failed_{int(started)}.md")
    save_json(record, folder / "run.json")
    u = record["usage"]
    print(f"{time.strftime('%H:%M:%S')} {folder.name}: exit {code}, {seconds} s, input {u.get('input_tokens')}, "
          f"output {u.get('output_tokens')} (reasoning {u.get('reasoning_output_tokens')}), "
          f"tool-free {record['tool_free']}, tool calls {record['tool_calls']}, only calculator {record['only_calculator']}",
          flush=True)


def attempt_once(folder: Path, model: str, instructions: str, tool_net: str | None = None, blackbox: bool = False):
    reply = folder / "reply.md"
    work = Path(tempfile.mkdtemp(prefix="p1_astra_"))
    started = time.time()
    print(f"{time.strftime('%H:%M:%S')} {folder.name}: started ({model}, {instructions}"
          f"{', calculator' if tool_net else ''}{' (black box)' if blackbox else ''})", flush=True)
    with open(folder / "prompt.md", "rb") as prompt, open(folder / "events.jsonl", "wb") as out,             open(folder / "stderr.log", "wb") as err:
        try:
            code = subprocess.run(command(work, reply, model, instructions, tool_net, blackbox), stdin=prompt, stdout=out, stderr=err,
                                  cwd=work, timeout=TIMEOUT).returncode
        except subprocess.TimeoutExpired:
            code = "timeout"
    return code, round(time.time() - started), started


if __name__ == "__main__":
    wanted = set(sys.argv[1:])
    todo = [f for f in sorted(RUNS.iterdir()) if (f / "prompt.md").exists() and not (f / "reply.md").exists()
            and (not wanted or f.name in wanted)]
    print(f"{len(todo)} runs to do: {', '.join(f.name for f in todo)}", flush=True)
    for folder in todo:
        run(folder)
    print("all done", flush=True)
