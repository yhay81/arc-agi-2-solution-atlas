"""Executable re-arc DSL program for ARC-AGI-2 task 025d127b.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    RIGHT,
    F,
    T,
    argmax,
    canvas,
    chain,
    color,
    colorfilter,
    combine,
    compose,
    fill,
    fork,
    lbind,
    mapply,
    merge,
    mostcolor,
    normalize,
    objects,
    paint,
    rbind,
    remove,
    rightmost,
    shape,
    shift,
    ulcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "025d127b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = objects(grid, T, T, T)
    x2 = rbind(objects, F)
    x3 = rbind(x2, F)
    x4 = rbind(x3, T)
    x5 = lbind(canvas, x0)
    x6 = compose(x5, shape)
    x7 = fork(paint, x6, normalize)
    x8 = compose(x4, x7)
    x9 = fork(colorfilter, x8, color)
    x10 = rbind(shift, RIGHT)
    x11 = rbind(argmax, rightmost)
    x12 = compose(x11, x9)
    x13 = fork(remove, x12, x9)
    x14 = chain(x10, merge, x13)
    x15 = rbind(argmax, rightmost)
    x16 = compose(x15, x9)
    x17 = fork(combine, x16, x14)
    x18 = fork(shift, x17, ulcorner)
    x19 = merge(x1)
    x20 = fill(grid, x0, x19)
    x21 = mapply(x18, x1)
    x22 = paint(x20, x21)
    return x22


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
