#!/usr/bin/env python3
"""Write one out-of-office reply to /output/entry.txt.

The reply is assembled from a plain word list: the words carry their
own punctuation, and joining them with single spaces gives the line.
No network, standard library only.
"""

import os

WORDS = [
    "I'm", "out", "until", "Monday.",
    "Dave", "from", "accounting", "is", "covering", "for", "me.",
    "He", "quit", "in", "March.",
]

AWAY_DAY = "Monday"
COVER_NAME = "Dave"
COVER_TEAM = "accounting"
QUIT_MONTH = "March"


def build_reply(words):
    """Join the word list into the single reply line."""
    return " ".join(words)


def main():
    line = build_reply(WORDS)
    if not 1 <= len(line) <= 160 or "\n" in line:
        raise ValueError("reply must be one line of 1-160 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
