"""Write the entry for Funniest One-Line Out-of-Office Reply.

One line, 1 to 160 characters: the funniest out-of-office email auto-reply
a colleague will read all week. The program writes the line to
/output/entry.txt and checks it against the gate before writing.
"""

import os

ENTRY = (
    "I'm out of office until Monday. If it's urgent, wait until "
    "Monday, when it will be older, slightly less urgent, and "
    "entirely my problem again."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
MAX_CHARS = 160


def validate_entry(text):
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "\t" in text:
        raise ValueError("entry must not contain tabs")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is over %d characters" % MAX_CHARS)
    return text


def main():
    text = validate_entry(ENTRY)
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == text, "read-back mismatch"
    print("Wrote %d chars to %s" % (len(text), OUTPUT_PATH))
    print(text)


if __name__ == "__main__":
    main()
