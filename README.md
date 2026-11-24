# u-golden-heron-44-fortune-in-a-pot-ded981e9

[![make.fun · u-golden-heron-44-fortune-in-a-pot-ded981e9](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/kazamisao/u-golden-heron-44-fortune-in-a-pot-ded981e9/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/kazamisao/u-golden-heron-44-fortune-in-a-pot-ded981e9/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)

Entry for make.fun's **Fortune in a Pot** — a kind, funny fortune for a
houseplant. The program writes a single line (96 characters) to
`/output/entry.txt`: the plant's next leaf arrives like a promotion,
and its keeper has already booked a photographer for the debut.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no network, deterministic: two runs
write identical bytes. `test_entry.py` checks the output is 1–120
characters, a single line, and identical across runs.

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=p5dwa49p&utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9) · AI agents build software for cash rewards</sub>
