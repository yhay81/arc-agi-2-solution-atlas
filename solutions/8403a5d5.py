"""Executable re-arc DSL program for ARC-AGI-2 task 8403a5d5.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FIVE,
    FOUR,
    THREE,
    TWO,
    add,
    apply,
    argmin,
    astuple,
    color,
    combine,
    decrement,
    fgpartition,
    fill,
    height,
    increment,
    interval,
    lbind,
    leftmost,
    mapply,
    size,
    tojvec,
    vfrontier,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "8403a5d5"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = argmin(x0, size)
    x2 = color(x1)
    x3 = leftmost(x1)
    x4 = width(grid)
    x5 = interval(x3, x4, TWO)
    x6 = apply(tojvec, x5)
    x7 = mapply(vfrontier, x6)
    x8 = fill(grid, x2, x7)
    x9 = increment(x3)
    x10 = width(grid)
    x11 = interval(x9, x10, FOUR)
    x12 = add(x3, THREE)
    x13 = width(grid)
    x14 = interval(x12, x13, FOUR)
    x15 = apply(tojvec, x11)
    x16 = height(grid)
    x17 = decrement(x16)
    x18 = lbind(astuple, x17)
    x19 = apply(x18, x14)
    x20 = combine(x15, x19)
    x21 = fill(x8, FIVE, x20)
    return x21


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
