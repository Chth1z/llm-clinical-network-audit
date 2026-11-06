"""Run prompts through one queue, with at most --cap of our Codex runs at a time on this machine (too many
at once lead to errors). Our runs are counted by their command line (codex exec
--ignore-user-config --ephemeral), so batches started with 21_astra.py count too and other Codex sessions
do not. Several queues may run at once: a lock file makes each count-and-start step one at a time.

Each argument is a run folder (results/simulation/llm_runs/<run>); runs start in the
order given; a folder that already has a reply is skipped. Each run is done by 21_astra.run (model and instructions
from its meta.json, retries when the service is busy).
Usage (from the repository root): python analysis/22_queue.py [--cap 6] <run folder> ...
"""
import argparse
import importlib
import os
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
astra = importlib.import_module("21_astra")
LOCK = Path(tempfile.gettempdir()) / "p1_astra_queue.lock"
COUNT = ("(Get-CimInstance Win32_Process -Filter \"name='codex.exe'\" | Where-Object { $_.CommandLine -like "
         "'*--ephemeral*' -and $_.CommandLine -like '*--ignore-user-config*' } | Measure-Object).Count")


def ours() -> int:
    out = subprocess.run(["powershell", "-NoProfile", "-Command", COUNT], capture_output=True, text=True).stdout
    return int(out.strip() or 0)


def acquire():
    while True:
        try:
            os.close(os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY))
            return
        except FileExistsError:
            if time.time() - LOCK.stat().st_mtime > 300:  # left behind by a queue that died
                LOCK.unlink(missing_ok=True)
            time.sleep(5)


ap = argparse.ArgumentParser()
ap.add_argument("--cap", type=int, default=6)
ap.add_argument("folders", nargs="+")
args = ap.parse_args()
threads = []
for folder in map(Path, args.folders):
    folder = folder.resolve()
    if (folder / "reply.md").exists():
        print(f"{folder.name}: has a reply, skipped", flush=True)
        continue
    if not astra.allowed(folder) or not (folder / "prompt.md").exists():
        print(f"{folder.name}: not a run folder that may be sent, skipped", flush=True)
        continue
    while True:
        acquire()
        try:
            if ours() < args.cap:
                th = threading.Thread(target=astra.run, args=(folder,))
                th.start()
                threads.append(th)
                time.sleep(20)  # let its codex process appear before the next count
                break
        finally:
            LOCK.unlink(missing_ok=True)
        time.sleep(60)
for th in threads:
    th.join()
print("all done", flush=True)
