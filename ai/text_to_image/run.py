"""Start Flux2 Klein Studio in your browser:  python run.py

Uses the active virtual environment, or the .venv that setup.py created. Run `python setup.py` once first.
Starting from this folder also makes Streamlit pick up the theme in .streamlit/config.toml.
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    in_venv = sys.prefix != sys.base_prefix
    python = sys.executable if in_venv else str(HERE / ".venv" / "Scripts" / "python.exe")
    packages_ok = Path(python).exists() and subprocess.run(
        [python, "-c", "import streamlit, ollama, PIL"], capture_output=True
    ).returncode == 0
    if not packages_ok or not (HERE / "models").is_dir():
        sys.exit("Setup isn't finished yet. Run:  python setup.py")

    print("Starting Flux2 Klein Studio… press Ctrl+C (or close this window) to stop it.")
    try:
        return subprocess.call([python, "-m", "streamlit", "run", "app.py"], cwd=HERE)
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    sys.exit(main())
