"""ai-excited-01 entry: "The Matchbox Phoenix".

Copies the entry image (entry.png, sitting beside this script) to
/output/entry.png. Deterministic: stdlib only, no network, no randomness,
no timestamps in the output.
"""

import shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent


def main() -> None:
    src = SCRIPT_DIR / "entry.png"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
