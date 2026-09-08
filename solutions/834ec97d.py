"""Executable re-arc DSL program for ARC-AGI-2 task 834ec97d.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    FOUR,
    NEG_ONE,
    NEG_TWO,
    TWO,
    UP,
    apply,
    argmin,
    astuple,
    combine,
    cover,
    fill,
    interval,
    lbind,
    leftmost,
    mapply,
    paint,
    partition,
    rbind,
    shift,
    shoot,
    size,
    uppermost,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "834ec97d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = argmin(x0, size)
    x2 = cover(grid, x1)
    x3 = shift(x1, DOWN)
    x4 = paint(x2, x3)
    x5 = leftmost(x1)
    x6 = width(grid)
    x7 = interval(x5, x6, TWO)
    x8 = leftmost(x1)
    x9 = interval(x8, NEG_ONE, NEG_TWO)
    x10 = combine(x7, x9)
    x11 = rbind(shoot, UP)
    x12 = uppermost(x1)
    x13 = lbind(astuple, x12)
    x14 = apply(x13, x10)
    x15 = mapply(x11, x14)
    x16 = fill(x4, FOUR, x15)
    return x16


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
