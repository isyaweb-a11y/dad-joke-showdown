"""Dad Joke Showdown entry.

Writes one dad joke to /output/entry.txt. The joke is a modern
dinner-table one: a father sets the family Wi-Fi password to the word
"incorrect", so the router itself delivers the punchline every time
one of his kids forgets it.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

JOKE = (
    "I set our Wi-Fi password to 'incorrect', so whenever my kids "
    "forget it, their phones remind them: 'Your password is incorrect.'"
)


def render() -> str:
    """Return the joke exactly as the judge should read it."""
    text = " ".join(JOKE.split())
    if not (1 <= len(text) <= 200):
        raise ValueError(f"joke must be 1..200 chars, got {len(text)}")
    if not text.rstrip("'\"").endswith("."):
        raise ValueError("a dad joke lands on its final beat; end with a period")
    return text


def main() -> None:
    text = render()
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
