"""Executable re-arc DSL program for ARC-AGI-2 task 6e19193c.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN_LEFT,
    NEG_UNITY,
    UNITY,
    UP_RIGHT,
    F,
    T,
    add,
    chain,
    color,
    combine,
    equality,
    fork,
    llcorner,
    lrcorner,
    mapply,
    objects,
    paint,
    rbind,
    recolor,
    remove,
    sfilter,
    shoot,
    toindices,
    ulcorner,
    urcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "6e19193c"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = rbind(shoot, UNITY)
    x2 = rbind(add, UNITY)
    x3 = chain(x1, x2, lrcorner)
    x4 = fork(recolor, color, x3)
    x5 = rbind(shoot, UP_RIGHT)
    x6 = rbind(add, UP_RIGHT)
    x7 = chain(x5, x6, urcorner)
    x8 = fork(recolor, color, x7)
    x9 = rbind(shoot, NEG_UNITY)
    x10 = rbind(add, NEG_UNITY)
    x11 = chain(x9, x10, ulcorner)
    x12 = fork(recolor, color, x11)
    x13 = rbind(shoot, DOWN_LEFT)
    x14 = rbind(add, DOWN_LEFT)
    x15 = chain(x13, x14, llcorner)
    x16 = fork(recolor, color, x15)
    x17 = fork(remove, lrcorner, toindices)
    x18 = fork(equality, toindices, x17)
    x19 = sfilter(x0, x18)
    x20 = fork(remove, urcorner, toindices)
    x21 = fork(equality, toindices, x20)
    x22 = sfilter(x0, x21)
    x23 = fork(remove, ulcorner, toindices)
    x24 = fork(equality, toindices, x23)
    x25 = sfilter(x0, x24)
    x26 = fork(remove, llcorner, toindices)
    x27 = fork(equality, toindices, x26)
    x28 = sfilter(x0, x27)
    x29 = mapply(x4, x19)
    x30 = mapply(x8, x22)
    x31 = combine(x29, x30)
    x32 = mapply(x12, x25)
    x33 = mapply(x16, x28)
    x34 = combine(x32, x33)
    x35 = combine(x31, x34)
    x36 = paint(grid, x35)
    return x36


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
