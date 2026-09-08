"""Executable re-arc DSL program for ARC-AGI-2 task a78176bb.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    DOWN_LEFT,
    NEG_UNITY,
    RIGHT,
    UNITY,
    UP_RIGHT,
    F,
    T,
    add,
    branch,
    chain,
    combine,
    compose,
    connect,
    contained,
    cover,
    equality,
    first,
    flip,
    fork,
    hmirror,
    identity,
    index,
    initset,
    lbind,
    llcorner,
    lrcorner,
    mapply,
    merge,
    mostcolor,
    objects,
    paint,
    positive,
    rapply,
    rbind,
    recolor,
    sfilter,
    shoot,
    size,
    toindices,
    ulcorner,
    urcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "a78176bb"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    mostcolor(grid)
    x1 = objects(grid, T, T, F)
    x2 = fork(connect, ulcorner, lrcorner)
    x3 = fork(equality, toindices, x2)
    x4 = sfilter(x1, x3)
    x5 = size(x4)
    x6 = positive(x5)
    x7 = branch(x6, identity, hmirror)
    x8 = x7(grid)
    x9 = objects(x8, T, F, T)
    x10 = compose(flip, x3)
    x11 = sfilter(x9, x10)
    x12 = rbind(shoot, UNITY)
    x13 = rbind(shoot, NEG_UNITY)
    x14 = fork(combine, x12, x13)
    x15 = rbind(branch, llcorner)
    x16 = rbind(x15, urcorner)
    x17 = rbind(branch, DOWN_LEFT)
    x18 = rbind(x17, UP_RIGHT)
    x19 = rbind(branch, RIGHT)
    x20 = rbind(x19, DOWN)
    x21 = fork(contained, urcorner, toindices)
    x22 = lbind(index, x8)
    x23 = compose(x20, x21)
    x24 = fork(add, ulcorner, x23)
    x25 = compose(x22, x24)
    x26 = chain(initset, x16, x21)
    x27 = fork(rapply, x26, identity)
    x28 = compose(first, x27)
    x29 = compose(x18, x21)
    x30 = fork(add, x28, x29)
    x31 = compose(x14, x30)
    x32 = fork(recolor, x25, x31)
    x33 = mapply(x32, x11)
    x34 = merge(x11)
    x35 = cover(x8, x34)
    x36 = paint(x35, x33)
    x37 = x7(x36)
    return x37


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
