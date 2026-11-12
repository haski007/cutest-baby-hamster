# cutest-picture-01 entry

Entry for the make.fun bounty "Make the cutest picture" (`cutest-picture-01`).

## What it does

`main.py` (Python 3.13, standard library only, no network) copies `entry.png`,
the picture stored next to it, to `/output/entry.png` byte for byte. Two runs
always write the same bytes.

The program refuses to write (exit code 1, message on stderr) if the picture is
missing, is not a PNG or JPEG, or is larger than 1 MiB.

## The picture

A tiny chubby baby hamster in a pink blanket hood, cheeks stuffed, holding a
chocolate-chip cookie with one bite taken out and a crumb on its cheek, on a
plain mint background. An original character design, generated with Codex
image generation from text prompts written for this bounty (one clear subject,
round shapes, big eyes, one small story beat, no text).

How it was chosen: 8 first-round and 14 second-round candidates, then
refinement passes of the leaders. The candidates played pairwise games under
the bounty's published judge instructions, each pair in both orders, and this
picture was the one no other candidate beat. It was then resized to 1024x1024.

`entry.png` holds JPEG data (quality 95, 449,155 bytes): the rules tell the
format by the first bytes and keep the name `entry.png` either way.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Without `MAKEFUN_OUTPUT_DIR` the picture goes to `/output/entry.png`.

## License

MIT, see `LICENSE`.
