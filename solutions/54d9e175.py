"""Executable re-arc DSL program for ARC-AGI-2 task 54d9e175.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FIVE,
    ZERO,
    F,
    T,
    canvas,
    chain,
    first,
    fork,
    frontiers,
    hconcat,
    increment,
    lbind,
    leastcolor,
    mapply,
    merge,
    objects,
    paint,
    palette,
    power,
    recolor,
    remove,
    shape,
    toindices,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "54d9e175"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = merge(x0)
    x2 = leastcolor(x1)
    x3 = shape(grid)
    x4 = canvas(x2, x3)
    x5 = hconcat(grid, x4)
    x6 = objects(x5, F, F, T)
    x7 = power(increment, FIVE)
    x8 = lbind(remove, FIVE)
    x9 = lbind(remove, ZERO)
    x10 = chain(x8, x9, palette)
    x11 = chain(x7, first, x10)
    x12 = fork(recolor, x11, toindices)
    x13 = mapply(x12, x6)
    x14 = paint(grid, x13)
    return x14


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
