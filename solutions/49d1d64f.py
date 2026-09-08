"""Executable re-arc DSL program for ARC-AGI-2 task 49d1d64f.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    LEFT,
    RIGHT,
    UNITY,
    UP,
    ZERO,
    asobject,
    canvas,
    increment,
    paint,
    shape,
    shift,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "49d1d64f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = shape(grid)
    x1 = increment(x0)
    x2 = increment(x1)
    x3 = canvas(ZERO, x2)
    x4 = asobject(grid)
    x5 = shift(x4, UNITY)
    x6 = shift(x5, LEFT)
    x7 = paint(x3, x6)
    x8 = shift(x5, RIGHT)
    x9 = paint(x7, x8)
    x10 = shift(x5, UP)
    x11 = paint(x9, x10)
    x12 = shift(x5, DOWN)
    x13 = paint(x11, x12)
    x14 = paint(x13, x5)
    return x14


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
