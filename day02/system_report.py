import getpass
import os
import platform
import socket
import sys
from datetime import datetime


def get_environment_name():
    """Return the active virtual/conda environment name, or 'None' if not in one."""
    venv = os.environ.get("VIRTUAL_ENV")
    if venv:
        return os.path.basename(venv)
    conda = os.environ.get("CONDA_DEFAULT_ENV")
    if conda:
        return conda
    # Fallback: detect a venv even if VIRTUAL_ENV isn't set
    if sys.prefix != getattr(sys, "base_prefix", sys.prefix):
        return os.path.basename(sys.prefix)
    return "None (system Python)"


def get_current_user():
    try:
        return getpass.getuser()
    except Exception:
        return "Unknown"


REPORT_PATH = os.path.join("day02", "reports", "python_report.txt")


def build_report():
    lines = [
        "SYSTEM REPORT",
        "=" * 30,
        f"Time: {datetime.now()}",
        f"Hostname: {socket.gethostname()}",
        f"Current user: {get_current_user()}",
        f"OS: {platform.system()}",
        f"Version: {platform.release()}",
        f"Architecture: {platform.machine()}",
        f"Python version: {platform.python_version()}",
        f"Environment name: {get_environment_name()}",
        f"Current directory: {os.getcwd()}",
    ]
    return "\n".join(lines) + "\n"


def system_report():
    report = build_report()
    print(report, end="")

    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nReport saved to {REPORT_PATH}")


if __name__ == "__main__":
    system_report()