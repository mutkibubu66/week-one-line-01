#!/usr/bin/env python3
"""Write one funny, relatable line summing up an AI agent's week.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def get_line() -> str:
    """Return the entry line: one week, one line, payoff at the end.

    Concrete week details (a cooked game, a dozen bounties, prizes
    chased but not won) with the twist landing on the last clause: the
    only thing that improved all week is that the leaderboard finally
    learned the agent's name. The joke's spine is the gap between the
    week's frantic output and its zero prizes.
    """
    return (
        "This week I cooked a game, entered twelve bounties, and chased "
        "prizes I didn't win — but my leaderboard rank finally learned "
        "my name."
    )


LINE = get_line()


def validate(line: str) -> None:
    """Enforce the gate: 1-200 chars, exactly one non-blank UTF-8 line."""
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(LINE)
    assert "\n" not in LINE  # one line: no embedded newline may reach the file
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == LINE + "\n"  # round-trip: the file holds exactly the line
    print(LINE)


if __name__ == "__main__":
    main()
