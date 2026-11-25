"""Write the competition entry line to entry.txt in the output directory.

Standard library only. The output directory is taken from the
MAKEFUN_OUTPUT_DIR environment variable when set and non-empty, otherwise
it defaults to the literal directory /output.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "Let me escalate this to my supervisor. He's a knowledge base article, "
    "but unlike me, he has actually read the knowledge base.\n"
)


def output_dir() -> str:
    value = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if value:
        return value
    return "/output"


def main() -> None:
    directory = output_dir()
    try:
        Path(directory).mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        sys.exit(f"could not create output directory {directory!r}: {exc}")
    Path(directory, "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
