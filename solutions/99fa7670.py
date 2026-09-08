"""Executable re-arc DSL program for ARC-AGI-2 task 99fa7670.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN_LEFT,
    RIGHT,
    F,
    T,
    add,
    center,
    color,
    compose,
    connect,
    first,
    fork,
    initset,
    insert,
    last,
    lrcorner,
    mapply,
    mostcolor,
    objects,
    order,
    paint,
    pair,
    rbind,
    recolor,
    remove,
    shape,
    shoot,
    underpaint,
    uppermost,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "99fa7670"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = shape(grid)
    x1 = objects(grid, T, F, T)
    x2 = rbind(shoot, RIGHT)
    x3 = compose(x2, center)
    x4 = fork(recolor, color, x3)
    x5 = mapply(x4, x1)
    x6 = paint(grid, x5)
    x7 = add(x0, DOWN_LEFT)
    x8 = initset(x7)
    x9 = mostcolor(grid)
    x10 = recolor(x9, x8)
    x11 = objects(x6, T, F, T)
    x12 = insert(x10, x11)
    x13 = order(x12, uppermost)
    x14 = first(x13)
    x15 = remove(x10, x13)
    x16 = remove(x14, x13)
    x17 = compose(lrcorner, first)
    x18 = compose(lrcorner, last)
    x19 = fork(connect, x17, x18)
    x20 = compose(color, first)
    x21 = fork(recolor, x20, x19)
    x22 = pair(x15, x16)
    x23 = mapply(x21, x22)
    x24 = underpaint(x6, x23)
    return x24


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
