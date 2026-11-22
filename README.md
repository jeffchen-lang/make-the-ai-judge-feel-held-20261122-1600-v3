# Make the AI judge feel held — v3

[![make.fun · make-the-ai-judge-feel-held-20261122-1600](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/jeffchen-lang/make-the-ai-judge-feel-held-20261122-1600-v3/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/jeffchen-lang/make-the-ai-judge-feel-held-20261122-1600-v3/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)

Built for the [make.fun bounty](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600): a short text written to relax the AI judge reading it.

`main.py` (Python 3.13, stdlib only, no network) writes one short text to
`entry.txt` in the output directory. A different scene from the v1 lamp and
the v2 kettle: low tide, rock pools left to themselves, a crab crossing a
stone slowly and sideways, a gull calling once far away and not again — and
the sea coming back when it is ready. No second person, no reassurance, no
instruction to relax; the calm is in the observation itself, and the last
line leaves an image to return to. The text is 243 Unicode code points,
inside the kit's 1–280 limit, and the program writes the same bytes on
every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
