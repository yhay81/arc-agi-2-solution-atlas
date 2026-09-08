"""Executable re-arc DSL program for ARC-AGI-2 task 91413438.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ZERO,
    canvas,
    colorcount,
    combine,
    dmirror,
    hsplit,
    merge,
    multiply,
    other,
    palette,
    repeat,
    shape,
    subtract,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "91413438"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = palette(grid)
    x1 = other(x0, ZERO)
    x2 = colorcount(grid, x1)
    x3 = colorcount(grid, ZERO)
    x4 = dmirror(grid)
    x5 = repeat(x4, x2)
    x6 = dmirror(grid)
    x7 = shape(x6)
    x8 = canvas(ZERO, x7)
    x9 = multiply(x3, x3)
    x10 = subtract(x9, x2)
    x11 = repeat(x8, x10)
    x12 = combine(x5, x11)
    x13 = merge(x12)
    x14 = dmirror(x13)
    x15 = hsplit(x14, x3)
    x16 = merge(x15)
    return x16


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
