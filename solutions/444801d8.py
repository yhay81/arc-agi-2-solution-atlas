"""Executable re-arc DSL program for ARC-AGI-2 task 444801d8.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    ONE,
    UP,
    F,
    T,
    argmin,
    astuple,
    chain,
    combine,
    compose,
    connect,
    delta,
    difference,
    fork,
    lbind,
    leastcolor,
    llcorner,
    lrcorner,
    manhattan,
    mapply,
    objects,
    paint,
    rbind,
    recolor,
    shift,
    sizefilter,
    toobject,
    ulcorner,
    urcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "444801d8"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = sizefilter(x0, ONE)
    x2 = difference(x0, x1)
    x3 = rbind(toobject, grid)
    x4 = chain(leastcolor, x3, delta)
    x5 = rbind(shift, UP)
    x6 = fork(connect, ulcorner, urcorner)
    x7 = compose(x5, x6)
    x8 = rbind(shift, DOWN)
    x9 = fork(connect, llcorner, lrcorner)
    x10 = compose(x8, x9)
    x11 = fork(astuple, x7, x10)
    x12 = lbind(rbind, manhattan)
    x13 = compose(x12, delta)
    x14 = fork(argmin, x11, x13)
    x15 = fork(combine, delta, x14)
    x16 = fork(recolor, x4, x15)
    x17 = mapply(x16, x2)
    x18 = paint(grid, x17)
    return x18


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
