"""One-time setup for Flux2 Klein Studio. Then start the app with: python run.py

    python setup.py                    # picks the CUDA runner for NVIDIA GPUs, Vulkan otherwise
    python setup.py --backend vulkan   # force a runner

It creates a Python environment in .venv (unless one is already active), installs the packages,
downloads the three model files and the stable-diffusion.cpp runner, and imports the text encoder
into Ollama if Ollama is installed. Uses only Python's standard library, so any Python 3.10+ can run it.

Safe to run again: finished steps are skipped and interrupted downloads resume where they stopped.
Every download is pinned to an exact version and checked against its SHA-256.
"""
import argparse
import hashlib
import shutil
import subprocess
import sys
import time
import urllib.request
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODELS = HERE / "models"
VENV = HERE / ".venv"

# (file in models/, pinned URL, size in bytes, sha256)
MODEL_FILES = [
    (
        "flux2-klein-4b-uncensored-q4_k_m.gguf",  # 1. text encoder (Qwen3-4B)
        "https://huggingface.co/ponpoke/flux2-klein-4b-uncensored-text-encoder/resolve/633217e588e4c0bc76619052e05d3ce0e057cd83/flux2-klein-4b-uncensored-q4_k_m.gguf",
        2497280416,
        "97dac4e931ffb1fed023c564aa2d73b1de82795612548369810478c2d69a3e49",
    ),
    (
        "flux-2-klein-4b-Q4_0.gguf",  # 2. diffusion model
        "https://huggingface.co/leejet/FLUX.2-klein-4B-GGUF/resolve/3b1f5a9dc3abb32238b053aeb3d823c30afdacbd/flux-2-klein-4b-Q4_0.gguf",
        2460378560,
        "d1023499ef3f2f82ff7c50e6778495195c1b6cc34835741778868428111f9ff4",
    ),
    (
        "flux2-vae.safetensors",  # 3. VAE
        "https://huggingface.co/Comfy-Org/flux2-dev/resolve/ed33133cd56476eac818c0943b6f9419b3e4a3a1/split_files/vae/flux2-vae.safetensors",
        336213556,
        "d64f3a68e1cc4f9f4e29b6e0da38a0204fe9a49f2d4053f0ec1fa1ca02f9c4b5",
    ),
]

SD_RELEASE = "https://github.com/leejet/stable-diffusion.cpp/releases/download/master-908-88411ef/"
# backend -> (folder the app looks in, [(zip name, size, sha256)], a file that proves it's installed)
RUNNERS = {
    "cuda": ("sd", [
        ("sd-master-88411ef-bin-win-cuda12-x64.zip", 333503246, "f55f8a2c1c873895f7466928fa7da82a5bb39de789af7d7755a65a9799dfccdb"),
        ("cudart-sd-bin-win-cu12-x64.zip", 563452046, "fe20366827d357c00797eebb58244dddab7fd9a348d70090c3871004c320f38d"),
    ], "cudart64_12.dll"),
    "vulkan": ("sd-vulkan", [
        ("sd-master-88411ef-bin-win-vulkan-x64.zip", 31966664, "e9d089361a00bd30b1e23cc39d2a98745536688acbf5e9e68ce2498a548d07e1"),
    ], "ggml-vulkan.dll"),
}

CHAT_MODEL = "flux2-klein"


def gb(n):
    return f"{n / 1e9:.2f} GB"


def ensure_environment(argv):
    """Run inside a virtual environment: the active one, or .venv here (created and switched to if needed)."""
    if sys.prefix == sys.base_prefix:  # plain system Python, not a virtual environment
        venv_python = VENV / "Scripts" / "python.exe"
        if not venv_python.exists():
            print("Creating a Python environment in .venv …", flush=True)
            import venv
            venv.create(VENV, with_pip=True)
        # Re-run this script with the .venv Python so everything below installs there
        sys.exit(subprocess.call([str(venv_python), str(Path(__file__).resolve()), *argv]))

    print(f"\n[1/4] Python packages → {sys.prefix}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--disable-pip-version-check", "-q",
                           "-r", str(HERE / "requirements.txt")])
    print("  ✓ streamlit, ollama, pillow installed")


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        while block := f.read(8 * 1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def download(url, dest, size, sha256):
    """Download to dest (resuming a .part file if there is one), then verify size and checksum."""
    if dest.exists() and dest.stat().st_size == size:
        print(f"  ✓ {dest.name} already downloaded")
        return
    part = dest.with_name(dest.name + ".part")
    if dest.exists():  # wrong size: treat it as an unfinished download
        dest.replace(part)
    have = part.stat().st_size if part.exists() else 0
    if have > size:
        part.unlink()
        have = 0

    if have < size:
        print(f"  ↓ {dest.name} ({gb(size)}){' resuming at ' + gb(have) if have else ''}")
        headers = {"User-Agent": "flux2-klein-studio-setup"}
        if have:
            headers["Range"] = f"bytes={have}-"
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as response:
            if have and response.status != 206:  # the server ignored the resume request, so start over
                have = 0
            with open(part, "ab" if have else "wb") as f:
                done, start, last = have, time.time(), 0.0
                while block := response.read(1024 * 1024):
                    f.write(block)
                    done += len(block)
                    now = time.time()
                    if now - last > 0.5 or done == size:
                        speed = (done - have) / max(now - start, 1e-6) / 1e6
                        print(f"\r    {done / size:6.1%}  {gb(done)} of {gb(size)}  {speed:5.1f} MB/s ", end="", flush=True)
                        last = now
        print()

    if part.stat().st_size != size:
        sys.exit(f"  ✗ {dest.name} is incomplete. Run setup again to resume.")
    print("    verifying checksum…", end="", flush=True)
    if sha256_of(part) != sha256:
        part.unlink()
        sys.exit(f"\n  ✗ {dest.name} is corrupted (checksum mismatch) and was deleted. Run setup again.")
    part.replace(dest)
    print(" ok")


def pick_backend(requested):
    if requested:
        return requested
    has_nvidia = shutil.which("nvidia-smi") and subprocess.run(["nvidia-smi"], capture_output=True).returncode == 0
    return "cuda" if has_nvidia else "vulkan"


def install_runner(backend):
    folder_name, zips, marker = RUNNERS[backend]
    folder = HERE / folder_name
    if (folder / "sd-cli.exe").exists() and (folder / marker).exists():
        print(f"  ✓ stable-diffusion.cpp ({backend}) already installed in {folder_name}\\")
        return
    folder.mkdir(exist_ok=True)
    for name, size, sha256 in zips:
        zip_path = folder / name
        download(SD_RELEASE + name, zip_path, size, sha256)
        with zipfile.ZipFile(zip_path) as z:
            z.extractall(folder)
        zip_path.unlink()  # no need to keep the zip once it's unpacked
    print(f"  ✓ unpacked into {folder_name}\\")


def setup_ollama():
    """Import the text encoder into Ollama for the Prompt assistant (optional)."""
    if not shutil.which("ollama"):
        print("  – Ollama isn't installed, so the Prompt assistant and Enhance prompt will be off.")
        print("    To turn them on: install it from https://ollama.com, then run setup again.")
        return
    listing = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    if listing.returncode != 0:
        print("  – Ollama is installed but not running. Start the Ollama app, then run setup again.")
        return
    if any(line.split(":")[0] == CHAT_MODEL for line in listing.stdout.splitlines()[1:]):
        print(f"  ✓ Ollama model '{CHAT_MODEL}' already exists")
        return
    print(f"  ↓ creating Ollama model '{CHAT_MODEL}' from the text encoder (copies ~2.5 GB)…")
    result = subprocess.run(["ollama", "create", CHAT_MODEL, "-f", "Modelfile"], cwd=HERE, capture_output=True, text=True)
    print(f"  ✓ Ollama model '{CHAT_MODEL}' created" if result.returncode == 0
          else f"  ✗ ollama create failed: {result.stderr.strip() or result.stdout.strip()}")


def main():
    parser = argparse.ArgumentParser(description="Download everything Flux2 Klein Studio needs.")
    parser.add_argument("--backend", choices=list(RUNNERS), help="GPU runner to install (default: cuda for NVIDIA, else vulkan)")
    args = parser.parse_args()

    if sys.version_info < (3, 10):
        sys.exit(f"Python 3.10 or newer is needed (this is {sys.version.split()[0]}). Get it from https://www.python.org/downloads/")
    if sys.platform != "win32":
        sys.exit("This setup downloads Windows builds of stable-diffusion.cpp. On macOS/Linux, see README.md → Step 6.")

    ensure_environment(sys.argv[1:])
    backend = pick_backend(args.backend)
    missing = sum(size for name, _, size, _ in MODEL_FILES if not (MODELS / name).exists())
    missing += sum(size for _, size, _ in RUNNERS[backend][1]) if not (HERE / RUNNERS[backend][0] / "sd-cli.exe").exists() else 0
    free = shutil.disk_usage(HERE).free
    if missing and free < missing * 1.2:
        sys.exit(f"Not enough disk space: need about {gb(missing * 1.2)}, have {gb(free)} free.")

    print(f"\n[2/4] Models → models\\  ({gb(missing)} to download)" if missing else "\n[2/4] Models → models\\")
    MODELS.mkdir(exist_ok=True)
    for name, url, size, sha256 in MODEL_FILES:
        download(url, MODELS / name, size, sha256)

    print(f"\n[3/4] Image runner: stable-diffusion.cpp, {backend.upper()} build")
    install_runner(backend)

    print("\n[4/4] Prompt assistant (optional)")
    setup_ollama()

    print("\nAll set. Start the app with: python run.py")
    print("Note: the text encoder is licensed for non-commercial use only (see README.md → Licenses).")


if __name__ == "__main__":
    sys.stdout.reconfigure(errors="replace")  # ✓ ↓ ✗ would crash when output is redirected to a file
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nStopped. Run setup again to resume where it left off.")
    except subprocess.CalledProcessError:
        sys.exit("\nInstalling the Python packages failed (see pip's message above). Check your internet connection and run setup again.")
    except OSError as e:  # network drops, timeouts, full disk
        sys.exit(f"\nDownload problem: {e}\nRun setup again to resume where it left off.")
