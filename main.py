#!/usr/bin/env python3
"""Write the one-line resignation letter of a health check to entry.txt.

The entry is a single line, 1-140 UTF-8 characters, written with no
trailing newline and no surrounding quotation marks.

Deterministic: the output is a fixed string; nothing is read from the
environment, the network, or the clock.
"""

import os
import sys

LINE = "I said healthy 2.1 million times; the one time I didn't, I became the incident."


def main() -> int:
    text = LINE
    encoded = text.encode("utf-8")
    if not 1 <= len(encoded) <= 140:
        raise SystemExit(f"entry must be 1-140 UTF-8 chars, got {len(encoded)}")
    if text != text.strip() or "\n" in text:
        raise SystemExit("entry must be exactly one line with no surrounding whitespace")
    if text.startswith('"') and text.endswith('"'):
        raise SystemExit("entry must not be wrapped in quotation marks")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(encoded)
    return 0


if __name__ == "__main__":
    sys.exit(main())
