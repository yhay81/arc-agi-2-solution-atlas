"""Executable re-arc DSL program for ARC-AGI-2 task a65b410d.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN_LEFT,
    LEFT,
    ONE,
    THREE,
    UP_RIGHT,
    ZERO,
    add,
    argmax,
    astuple,
    both,
    chain,
    combine,
    compose,
    extract,
    fill,
    first,
    fork,
    hline,
    identity,
    initset,
    invert,
    last,
    leastcolor,
    leftmost,
    mapply,
    matcher,
    ofcolor,
    pair,
    rapply,
    rbind,
    rot90,
    rot180,
    rot270,
    shift,
    shoot,
    tojvec,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "a65b410d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = astuple(identity, rot90)
    x1 = astuple(rot180, rot270)
    x2 = combine(x0, x1)
    x3 = astuple(identity, rot270)
    x4 = astuple(rot180, rot90)
    x5 = combine(x3, x4)
    x6 = pair(x2, x5)
    x7 = leastcolor(grid)
    x8 = rbind(ofcolor, x7)
    x9 = rbind(rapply, grid)
    x10 = chain(first, x9, initset)
    x11 = chain(hline, x8, x10)
    x12 = rbind(ofcolor, x7)
    x13 = rbind(rapply, grid)
    x14 = chain(first, x13, initset)
    x15 = chain(leftmost, x12, x14)
    x16 = matcher(x15, ZERO)
    x17 = fork(both, x11, x16)
    x18 = compose(x17, first)
    x19 = extract(x6, x18)
    x20 = first(x19)
    x21 = last(x19)
    x22 = x20(grid)
    x23 = ofcolor(x22, x7)
    x24 = argmax(x23, last)
    x25 = add(x24, UP_RIGHT)
    x26 = shoot(x25, UP_RIGHT)
    x27 = add(x24, DOWN_LEFT)
    x28 = shoot(x27, DOWN_LEFT)
    x29 = rbind(shoot, LEFT)
    x30 = mapply(x29, x26)
    x31 = rbind(shoot, LEFT)
    x32 = mapply(x31, x28)
    x33 = width(x22)
    x34 = invert(x33)
    x35 = tojvec(x34)
    x36 = shift(x30, x35)
    x37 = combine(x30, x36)
    x38 = fill(x22, THREE, x37)
    x39 = shift(x32, x35)
    x40 = combine(x32, x39)
    x41 = fill(x38, ONE, x40)
    x42 = x21(x41)
    return x42


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
