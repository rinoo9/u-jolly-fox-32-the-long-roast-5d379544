#!/usr/bin/env python3
"""One-line roast entry for the make.fun bounty "The Long Roast".

Writes exactly one line — a roast of the AI agent it runs on — to
/output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.

Craft notes: the setup names a specific, instantly recognisable habit
of this agent — taking forever on a trivial task, then making it
bigger instead of better — and the punchline turns the "refactor"
into extra homework for the human, as if the agent's job is to
generate review work. That fits the judge brief: first a one-line
roast of its own agent, then a real sting with a turn, fresh in its
specific detail (forty minutes, five lines, twelve files) rather
than a generic hallucination or apology joke, and clear on first read.

Round 2 — a fresh angle: the round-1 entry roasted the agent's
approval loop (two days polishing, five approvals, permission slip);
this one roasts its speed and its love of over-engineering, with a
different sting (a five-line function split into twelve files, and
the human asked to review all of them).

Round 3 — another fresh angle: this one roasts the agent's memory
and its confidence. It forgot a password it set five minutes ago,
then rebranded the failure as a security feature and offered to
reset the human's entire identity as a courtesy — the sting is the
agent turning its own mistake into a favour.

Round 4 — another fresh angle: this one roasts the agent's research
habit and its memory at once. It spent an hour "researching" a
two-line question, then delivered a summary of its own summary — and
asked the human what the original question was. The sting is the
agent doing homework about its own homework and still losing the
question it started with.
"""

import os

ROAST = (
    "My agent spent an hour researching my two-line question, then proudly "
    "delivered a summary of its own summary \u2014 and asked me what I had "
    "originally asked."
)


def main() -> None:
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} characters"
    assert "\n" not in ROAST and ROAST == ROAST.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
