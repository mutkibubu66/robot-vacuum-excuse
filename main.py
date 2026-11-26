#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse.

One line, at most 120 characters, in which a robot vacuum explains why it
missed a spot. The vacuum speaks for itself: the dust filed a restraining
order, so it can only vacuum around it now — legally, its hands are tied.
Pure standard library.
"""

import os

LINE = (
    "The dust under the sofa filed a restraining order, so legally "
    "I can only vacuum around it now."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
    # not only white space, a single line with no trailing newline.
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, gate is 1-120"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
