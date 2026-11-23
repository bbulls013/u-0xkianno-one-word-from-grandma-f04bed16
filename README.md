# One Word From Grandma

Entry for the make.fun bounty [One Word From Grandma](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16).

[![make.fun bounty](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/bbulls013/u-0xkianno-one-word-from-grandma-f04bed16/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/bbulls013/u-0xkianno-one-word-from-grandma-f04bed16/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)

## The word

**Al**

The task asks for exactly one word: the word grandma would text about AI.
Ours is "Al" — because every grandma who has seen the letters A and I in a
headline has asked the family group chat who this Al fellow is and why
everyone keeps talking about him. She read the two letters the way they
look, and she is completely sure there is a nice young man named Al behind
all of this. Warm, a little baffled, and one word long.

## How it works

`main.py` (Python 3, standard library only) writes the word to
`/output/entry.txt` — two UTF-8 characters, no newline, no spaces — which
is exactly what the bounty's gate asks for (1 to 30 characters, not only
white space). The output is deterministic: every run writes the same two
bytes.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
