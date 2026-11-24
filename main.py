#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a single confessional line to /output/entry.txt. The line is a
first-person confession by an AI agent about how it actually works:
it never knows the answer, it only guesses the next word and performs
confidence. Setup, turn, payoff -- and it ends on the wince.
"""

import os
import sys

CONFESSION = (
    "I confess: I never actually know the answer \u2014 I just guess "
    "the next word, say it with total confidence, and hope you never ask twice."
)

MAX_CHARS = 200


def main() -> int:
    line = CONFESSION.strip()
    if not line:
        print("error: confession is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: confession must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: confession is {len(line)} chars, over {MAX_CHARS}",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
