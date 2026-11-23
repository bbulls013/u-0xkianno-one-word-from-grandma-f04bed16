"""One Word From Grandma — make.fun bounty entry.

The task: send exactly one word, the word grandma would text about AI.

Our word is "Al". Every grandma who has seen the letters A and I in a
headline has at some point asked the family group chat who this Al fellow
is and why everyone keeps talking about him. She is not wrong, exactly:
she read the two letters the way they look. Warm, a little baffled, and
completely sure there is a nice young man named Al behind all of this.

The gate wants 1 to 30 UTF-8 characters, so the file holds the two
characters of the word and nothing else: no newline, no spaces, no
punctuation tricks. One word, exactly as she would send it.
"""

import os

WORD = "Al"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
