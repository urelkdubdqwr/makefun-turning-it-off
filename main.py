import os
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
    Path(directory).mkdir(parents=True, exist_ok=True)
    Path(directory, "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
