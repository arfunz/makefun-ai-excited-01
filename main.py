"""Board-game stampede: three beasts break out at once.

A charging rhino, a tall giraffe and a leaping boar tumble out of a
board game on a dark table while the guests around it flinch and step
back. This script drops the entry picture at /output/entry.png.
"""

import hashlib
import pathlib


def fingerprint(path):
    """Hex SHA-256 of a file, hashed a chunk at a time."""
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        while True:
            piece = stream.read(65536)
            if not piece:
                break
            hasher.update(piece)
    return hasher.hexdigest()


def main():
    folder = pathlib.Path(__file__).resolve().parent
    picture = folder / "entry.png"
    target_dir = pathlib.Path("/output")
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    with picture.open("rb") as incoming, target.open("wb") as outgoing:
        for piece in iter(lambda: incoming.read(65536), b""):
            outgoing.write(piece)
    if fingerprint(picture) != fingerprint(target):
        raise SystemExit("entry.png copy is not identical to the source")


if __name__ == "__main__":
    main()
