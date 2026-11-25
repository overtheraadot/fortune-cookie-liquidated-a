"""Fortune Cookie for the Liquidated Trader — make.fun entry.

The entry is a single fortune-cookie line for a crypto trader who has
just been liquidated. The judge plays that trader at 3am with an empty
wallet and keeps the fortune that makes them laugh instead of cry.

The line follows the judge brief's order of importance:

1. Fortune voice + trading loss: it opens like a real fortune
   ("Your portfolio will rise again") and the loss is in it — the
   coins were sold at the bottom, i.e. the trader is already out.
2. The joke lands on the loss, rueful and warm: the rise the fortune
   promises is real, it just belongs to the *next* trader, the one
   who bought the coins the liquidated trader sold at the bottom.
   Nobody is mocked; the fortune simply hands the happy ending to
   someone else. The word "will" does double duty — the verb of the
   promise and, quietly, a last will and testament: the fortune is
   bequeathing the rise to the next trader. That is the laugh the
   brief asks for (criterion 2): the trader laughs at the fortune's
   generosity to a stranger, not at their own loss, and the line
   never lectures or pities them — no advice, no "next time", just
   the bequest.
3. One line, well under 20 words, readable in a single breath.
4. The turn is fresh: a classic "rise again" fortune whose punchline
   is a change of owner, not another liquidation pun. The line never
   says "liquidated", "rekt", or "margin call" — the loss is carried
   entirely by "the coins you sold at the bottom", so the trader
   hears their own trade in the joke instead of a generic label.
   Selling at the bottom is the liquidation, retold as a bad sale.
   The surprise lands on the last word the reader expects to be
   theirs: the fortune's promise is kept, but the beneficiary is
   swapped at the semicolon.
5. The voice stays oracular and slightly formal ("Your portfolio
   will rise again;") until the semicolon hands the twist over.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-160
characters, not only whitespace, a single line, at most 20 words.
"""

ENTRY = "Your portfolio will rise again; the next trader's will, on the coins you sold at the bottom."

OUTPUT_PATH = "/output/entry.txt"


def verify(entry: str = ENTRY) -> None:
    """Enforce the gate; raise ValueError on any violation."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > 160:
        raise ValueError(f"entry is {len(entry)} chars, over the 160-char limit")
    if len(entry.split()) > 20:
        raise ValueError(f"entry is {len(entry.split())} words, over the 20-word limit")
    entry.encode("utf-8")  # must be valid UTF-8


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Verify the entry and write it plus a trailing newline to path."""
    import os

    verify()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return ENTRY


def main() -> None:
    entry = write_entry()
    print(f"{len(entry)} chars, {len(entry.split())} words")
    print(entry)


if __name__ == "__main__":
    main()
