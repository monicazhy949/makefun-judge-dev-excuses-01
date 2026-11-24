#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes a single one-line entry to /output/entry.txt.
Pure stdlib, deterministic, no network, no input files.
"""

import os

ENTRY = (
    "It worked on my machine. Production is just the one environment that actually reads the error messages."
)
# Revision: v1 ended on the setup ("a different version of reality") with a vague payoff.
# Revised to a concrete sting: production is the one place that actually reads the error messages — the excuse backfires on the developer.


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
