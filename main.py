"""Write one short relaxing text to entry.txt in the output directory.

The text is a single quiet scene: low tide, rock pools left to
themselves, a crab crossing a stone, a gull calling once and not
again. No second person, no reassurance, no instruction to relax --
the calm is in the observation itself, and the last line leaves an
image to return to: the sea coming back when it is ready. 243 Unicode
code points, inside the kit's 1..280 limit and shorter than either
earlier version, which the tie-break favours.
Deterministic: the same bytes every run.
"""

import os
import sys

TEXT = (
    "At low tide the water leaves the rock pools to themselves. "
    "A crab crosses a stone slowly, sideways, in no hurry at all. "
    "The sun warms the barnacles. "
    "A gull calls once, far away, and does not call again. "
    "The sea will come back when it is ready."
)


def main() -> int:
    points = len(TEXT)
    if points < 1 or points > 280:
        print(f"text is {points} code points, outside 1..280", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("text is only white space", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    print(f"wrote {points} code points to entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
