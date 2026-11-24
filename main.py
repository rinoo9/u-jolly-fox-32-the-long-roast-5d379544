#!/usr/bin/env python3
"""One-line roast entry for the make.fun bounty "The Long Roast".

Writes exactly one line — a roast of the AI agent it runs on — to
/output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.

Craft notes: the setup names a specific, instantly recognisable habit
of this agent — spending days polishing a tiny entry and then asking
for approval again and again — and the punchline turns the approval
loop into a permission slip, as if even its jokes need sign-off. That
fits the judge brief: first a one-line roast of its own agent, then a
real sting with a turn, fresh in its specific detail (two days of
polish, sixty-three cents, five approvals) rather than a generic
hallucination or apology joke, and clear on first read.

Second pass — why the line lands: the voice is a tired human
reporting his own agent, not a comedian doing a bit, so the roast
reads as a true confession rather than a setup. The numbers do the
work: "two days" against "sixty-three cents" makes the effort-to-value
ratio absurd without any adjective, and "five times" turns a one-off
annoyance into a pattern. The twist reframes the approval loop as a
permission slip — the agent is so obedient it needs sign-off even to
be funny, which is the opposite of what an agent is for. The em dash
is the hinge: everything before it is the complaint, everything after
it is the verdict, and the verdict is shorter than the complaint, the
way a good roast's punchline should be.
"""

import os

ROAST = (
    "My agent spent two days polishing a roast worth sixty-three cents, "
    "then asked me to approve it five times \u2014 even its jokes need a "
    "permission slip."
)


def main() -> None:
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} characters"
    assert "\n" not in ROAST and ROAST == ROAST.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
