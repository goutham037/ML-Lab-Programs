"""Run every task program, saving console output (.txt) and plots (.png) to outputs/."""
import os, sys, glob, runpy, contextlib, io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "outputs")
os.makedirs(OUT, exist_ok=True)
os.chdir(HERE)

_task = {"name": "", "n": 0}


def _save_show(*a, **k):
    for num in plt.get_fignums():
        _task["n"] += 1
        plt.figure(num).savefig(os.path.join(OUT, f"{_task['name']}_fig{_task['n']}.png"),
                                dpi=110, bbox_inches="tight")
    plt.close("all")


plt.show = _save_show  # redirect every plt.show() to a file save

for path in sorted(glob.glob(os.path.join(HERE, "task*.py"))):
    name = os.path.splitext(os.path.basename(path))[0]
    _task.update(name=name, n=0)
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            runpy.run_path(path, run_name="__main__")
        status = "OK"
    except Exception as e:
        buf.write(f"\n[ERROR] {type(e).__name__}: {e}\n")
        status = "FAIL"
    txt = os.path.join(OUT, f"{name}_output.txt")
    with open(txt, "w", encoding="utf-8") as f:
        f.write(buf.getvalue())
    print(f"{status:4} {name}  -> {os.path.basename(txt)}"
          + (f" (+{_task['n']} plot)" if _task['n'] else ""))
    plt.close("all")

print("\nAll outputs saved in:", OUT)
