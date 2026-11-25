#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun bounty entry.

Writes a single line (under 200 characters) to /output/entry.txt:
the most creative excuse a hardware wallet gives for refusing to
sign a transaction at 3 AM.

The line is a fixed string. No network, no randomness, no files
outside this repository are read: the program is fully deterministic
so the graded run produces exactly the text tested here.
"""

from pathlib import Path

ENTRY = (
    "It's 3 AM: I'm not your wallet tonight, I'm your designated "
    "driver, and nothing gets signed until the sun vouches for you."
)


def main() -> None:
    # Fail loudly instead of shipping an entry the gate would refuse.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character, 1 to 200.
    output_path.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {output_path}")


if __name__ == "__main__":
    main()
