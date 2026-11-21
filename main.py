import os
from pathlib import Path


POEM = """Forty years he climbed the tower steps and lit the lamp.
He never had to ask leave of anyone.
Tonight the tower is the young keeper’s.
Hat in hand, he asks, “One last time?”
She steps out of the light without a word.
He strikes the match."""


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    for stale in output_dir.iterdir():
        if stale.is_symlink() or not stale.is_dir():
            stale.unlink()
    (output_dir / "entry.txt").write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
