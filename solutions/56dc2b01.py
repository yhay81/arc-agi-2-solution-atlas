"""Executable re-arc DSL program for ARC-AGI-2 task 56dc2b01.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    TWO,
    branch,
    color,
    compose,
    cover,
    decrement,
    dmirror,
    extract,
    fgpartition,
    fill,
    flip,
    greater,
    hline,
    identity,
    increment,
    invert,
    leftmost,
    manhattan,
    matcher,
    ofcolor,
    paint,
    rightmost,
    shift,
    tojvec,
    vfrontier,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "56dc2b01"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = ofcolor(grid, TWO)
    x1 = hline(x0)
    x2 = branch(x1, dmirror, identity)
    x3 = x2(grid)
    x4 = fgpartition(x3)
    x5 = matcher(color, TWO)
    x6 = compose(flip, x5)
    x7 = extract(x4, x6)
    x8 = ofcolor(x3, TWO)
    x9 = leftmost(x8)
    x10 = leftmost(x7)
    x11 = greater(x9, x10)
    x12 = manhattan(x7, x8)
    x13 = decrement(x12)
    x14 = branch(x11, identity, invert)
    x15 = branch(x11, decrement, increment)
    x16 = branch(x11, leftmost, rightmost)
    x17 = x14(x13)
    x18 = tojvec(x17)
    x19 = shift(x7, x18)
    x20 = x16(x19)
    x21 = x15(x20)
    x22 = tojvec(x21)
    x23 = vfrontier(x22)
    x24 = cover(x3, x7)
    x25 = paint(x24, x19)
    x26 = fill(x25, EIGHT, x23)
    x27 = x2(x26)
    return x27


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
