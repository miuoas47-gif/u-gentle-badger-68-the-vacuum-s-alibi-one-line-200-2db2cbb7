#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters max.

Writes the robot vacuum's one-line excuse for missing a spot to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Stdlib only, no arguments, no network, deterministic: every run
writes the exact same bytes.
"""

import os
import sys

LINE = (
    "I skipped that spot on purpose: my sensors classified the dust bunny "
    "as a pet, and my warranty forbids eating pets."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"alibi is {len(LINE)} characters, must be 1-200", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or "\n" in LINE or "\r" in LINE:
        print("alibi must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "rb") as f:
        raw = f.read()
    if raw != LINE.encode("utf-8"):
        print("read-back mismatch", file=sys.stderr)
        return 1
    if raw != raw.strip() or b"\n" in raw or b"\r" in raw:
        print("output must be a single line with no surrounding whitespace", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)}-character alibi to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
