"""Executable re-arc DSL program for ARC-AGI-2 task d89b689b.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    F,
    T,
    apply,
    argmax,
    argmin,
    color,
    compose,
    cover,
    fork,
    initset,
    lbind,
    manhattan,
    mapply,
    merge,
    objects,
    paint,
    rbind,
    recolor,
    sfilter,
    size,
    sizefilter,
    square,
    toindices,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d89b689b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = sfilter(x0, square)
    x2 = argmax(x1, size)
    x3 = toindices(x2)
    x4 = sizefilter(x1, ONE)
    x5 = apply(initset, x3)
    x6 = lbind(argmin, x5)
    x7 = lbind(rbind, manhattan)
    x8 = compose(x6, x7)
    x9 = fork(recolor, color, x8)
    x10 = mapply(x9, x4)
    x11 = merge(x4)
    x12 = cover(grid, x11)
    x13 = paint(x12, x10)
    return x13


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
