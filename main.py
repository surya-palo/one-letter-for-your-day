#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

Writes exactly one letter, A-Z, to /output/entry.txt and nothing else.
The letter is the whole entry: behind it sits the word that describes
the day. See BUILD_LOG.md for the choice and the reasoning.
"""

import os

LETTER = "C"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
