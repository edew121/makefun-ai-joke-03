"""ai-joke-03 entry: write one joke about AI coding agents to entry.txt.

The program is deterministic: it always writes the same bytes, so the
two grading runs produce identical output.
"""

import os
from pathlib import Path

JOKE = "I told my agent to keep the change small. It changed one line \u2014 in 37 files."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Self-check against the gate before writing: 1-280 characters,
    # at least one of them not white space. Fail loudly instead of
    # silently writing an entry the scorer would refuse.
    if not 1 <= len(JOKE) <= 280:
        raise ValueError(f"joke is {len(JOKE)} characters, must be 1-280")
    if not any(not ch.isspace() for ch in JOKE):
        raise ValueError("joke is only white space")
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    # Write exactly the joke bytes: no trailing newline, because the
    # judge reads exactly what is in the file.
    (out / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
