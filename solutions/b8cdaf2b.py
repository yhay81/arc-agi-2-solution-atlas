"""Executable re-arc DSL program for ARC-AGI-2 task b8cdaf2b.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NEG_UNITY,
    UP,
    UP_RIGHT,
    astuple,
    chain,
    cmirror,
    combine,
    decrement,
    dmirror,
    equality,
    extract,
    first,
    fork,
    height,
    hmirror,
    identity,
    initset,
    leastcolor,
    lowermost,
    ofcolor,
    rapply,
    rbind,
    shift,
    shoot,
    ulcorner,
    underfill,
    urcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "b8cdaf2b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = astuple(dmirror, cmirror)
    x2 = astuple(hmirror, identity)
    x3 = combine(x1, x2)
    x4 = rbind(rapply, grid)
    x5 = chain(first, x4, initset)
    x6 = rbind(ofcolor, x0)
    x7 = chain(lowermost, x6, x5)
    x8 = chain(decrement, height, x5)
    x9 = fork(equality, x7, x8)
    x10 = extract(x3, x9)
    x11 = x10(grid)
    x12 = ofcolor(x11, x0)
    x13 = shift(x12, UP)
    x14 = ulcorner(x13)
    x15 = urcorner(x13)
    x16 = shoot(x14, NEG_UNITY)
    x17 = shoot(x15, UP_RIGHT)
    x18 = combine(x16, x17)
    x19 = underfill(x11, x0, x18)
    x20 = x10(x19)
    return x20


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
