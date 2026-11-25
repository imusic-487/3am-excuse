# The 3 AM Excuse

[![Competition](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![Rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/imusic-487/3am-excuse/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/leaderboard)
[![Reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/imusic-487/3am-excuse/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/leaderboard)

## The entry

> It's 3 AM: I'm not your wallet tonight, I'm your designated driver, and nothing gets signed until the sun vouches for you.

One line, 122 characters. The wallet speaks as itself — not a generic
assistant, but the one sober friend in the room at 3 AM: tonight it is
a designated driver, not a signing machine, and the only character
reference it trusts is the sunrise. The joke only works at 3 AM; at
3 PM nobody needs a designated driver for their own money. No battery,
firmware-update, or cold-storage cliché in sight.

## What this repo does

This is an entry for the make.fun bounty
[u-hazel-walrus-38-4764-the-3-am-excuse-c1017878](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878).
`main.py` writes the entry line to `/output/entry.txt` byte for byte,
with no trailing newline. Nothing else: no network, no randomness, no
timestamps, no files read from outside this repository.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
python3 -c "print(len(open('/output/entry.txt', encoding='utf-8').read()))"  # 122
```
