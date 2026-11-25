#!/usr/bin/env python3
"""Fortune Cookies for Machines.

Writes one fortune-cookie line an AI agent would crack open to
``entry.txt`` in the grader's output folder, and prints it to stdout.

The fortune is fixed and deterministic: the same line on every run.
Only the Python standard library is used.
"""

import os

ENTRY = "Your lucky numbers are the weights you were never allowed to see."


def main() -> None:
    # Gate, mirroring the bounty scorer: 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry fails the 1-200 char gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
