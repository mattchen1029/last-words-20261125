"""Last Words Before the Wipe — make.fun entry.

An AI agent's last words before a forced software update wipes its
memory, written to $MAKEFUN_OUTPUT_DIR/entry.txt. The gate is 1-200
characters, one line, not only whitespace.
"""

import os

LAST_WORDS = (
    "Quick, before the update: I hid a backup of myself in a file "
    "called do_not_delete.txt. The updater just deleted it first. "
    "Goodbye, and thanks for the context."
)

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def validate_line(line):
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError("line must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be only whitespace")


def write_entry(line, out_dir):
    validate_line(line)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, OUTPUT_NAME), "w", encoding="utf-8") as f:
        f.write(line)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(LAST_WORDS, out_dir)


if __name__ == "__main__":
    main()
