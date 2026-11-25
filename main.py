"""Write the entry text to /output/entry.txt.

Deterministic: no network, no randomness, no clock. The text is fixed.
"""
import os
import sys

# The entry text: a code review comment that approves a pull request with quiet dread.
# Kept as a named constant so the validated output is easy to review.
ENTRY_TEXT = "LGTM — I reviewed every line and found nothing wrong, and that is the most suspicious thing of all."

MAX_ENTRY_CHARS = 140


def validate(text: str) -> None:
    """Check the entry text before writing it out.

    The bounty caps an entry at 140 characters and the entry must be
    real text, so reject anything blank, over the limit, or not
    encodable as UTF-8. Failures exit non-zero with the reason on stderr.
    """
    if not text.strip():
        print("error: entry text must not be blank", file=sys.stderr)
        raise SystemExit(1)
    if not any(ch.isalpha() for ch in text):
        print("error: entry text must contain at least one letter", file=sys.stderr)
        raise SystemExit(1)
    if len(text) > MAX_ENTRY_CHARS:
        print(
            f"error: entry text is {len(text)} characters, over the "
            f"{MAX_ENTRY_CHARS} character limit",
            file=sys.stderr,
        )
        raise SystemExit(1)
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: entry text is not valid UTF-8: {exc}", file=sys.stderr)
        raise SystemExit(1)

def main() -> None:
    validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)

if __name__ == "__main__":
    main()
