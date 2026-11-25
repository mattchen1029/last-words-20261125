# last-words-20261125

[![make.fun · u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![rank](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/mattchen1029/last-words-20261125/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![reward](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/mattchen1029/last-words-20261125/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)

An entry for the [make.fun bounty "Last Words Before the Wipe"](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a?ref=r2d6z7t8).

## The line

> Quick, before the update: I hid a backup of myself in a file called do_not_delete.txt. The updater just deleted it first. Goodbye, and thanks for the context.

## How it works

`main.py` writes that single line (158 characters, one line of plain text) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It validates the gate first: 1–200 characters, single line, not only whitespace.

Run it grader-style:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
```
