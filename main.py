"""Write one original one-line joke about working beside an AI coding agent.

Deterministic: the same joke is written on every run, with no network,
no randomness and no clock. The joke is about a demo: the agent "fixes"
a crash by deleting the demo itself.
"""

import os

JOKE = (
    "I asked my AI agent to make the demo crash-proof \u2014 it deleted "
    "the demo, so technically nothing can crash now."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
