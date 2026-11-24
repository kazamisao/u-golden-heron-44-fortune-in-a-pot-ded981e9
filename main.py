"""Fortune in a Pot (make.fun).

Writes one kind, funny fortune for a houseplant to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, stdlib only, no network:
the same single line on every run.
"""

import os
from pathlib import Path

FORTUNE = (
    "Your next leaf arrives like a promotion, and I have already booked "
    "a photographer for its debut."
)


def main() -> None:
    # The gate refuses anything outside 1-120 characters; fail loudly
    # here rather than shipping an invalid entry.
    if not 1 <= len(FORTUNE) <= 120 or not FORTUNE.strip():
        raise ValueError(f"fortune is {len(FORTUNE)} characters, must be 1-120")
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
