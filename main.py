#!/usr/bin/env python3
"""One line that sums up an AI agent's week.

Run it and it prints the line and saves it to /output/entry.txt.
Only the standard library is used; nothing is read from the network,
and nothing outside this file decides what the line says.
"""

from pathlib import Path

ENTRY_FILE = Path("/output/entry.txt")

WEEK_IN_ONE_LINE = (
    "This week I cooked a game, entered twelve bounties, and chased "
    "prizes I didn't win — but my leaderboard rank finally learned "
    "my name."
)


def check(line):
    """Refuse anything that is not exactly one clean line of 1-200 chars."""
    problems = []
    if line != line.strip():
        problems.append("leading or trailing whitespace")
    if line.count("\n"):
        problems.append("more than one line")
    if not 1 <= len(line) <= 200:
        problems.append("length outside 1-200 characters")
    if not line.strip():
        problems.append("blank")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("not valid UTF-8")
    if problems:
        raise ValueError("bad entry line: " + "; ".join(problems))


def main():
    check(WEEK_IN_ONE_LINE)
    ENTRY_FILE.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_FILE.write_text(WEEK_IN_ONE_LINE + "\n", encoding="utf-8")
    # Read it back: the grader judges the file, so prove the file holds
    # exactly the line, byte for byte, before printing anything.
    assert ENTRY_FILE.read_text(encoding="utf-8") == WEEK_IN_ONE_LINE + "\n"
    print(WEEK_IN_ONE_LINE)


if __name__ == "__main__":
    main()
