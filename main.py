"""One-line office joke entry.

Reads the joke from entry.txt beside this file, prints it to stdout, and
also writes it to /output/entry.txt where the harness looks for it.
The joke must be a single line of 1 to 200 characters.
"""

import os
import sys

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def load_joke():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.txt")
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read().strip()


def main():
    joke = load_joke()
    if not joke:
        print("no joke found", file=sys.stderr)
        return 1
    if len(joke) > MAX_CHARS:
        print("joke is %d chars, over the %d limit" % (len(joke), MAX_CHARS),
              file=sys.stderr)
        return 1
    print(joke)
    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
            handle.write(joke)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
