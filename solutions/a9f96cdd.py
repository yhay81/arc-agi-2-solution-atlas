"""Executable re-arc DSL program for ARC-AGI-2 task a9f96cdd.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN_LEFT,
    EIGHT,
    NEG_UNITY,
    SEVEN,
    SIX,
    THREE,
    UNITY,
    UP_RIGHT,
    combine,
    fill,
    leastcolor,
    mostcolor,
    ofcolor,
    paint,
    recolor,
    shift,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "a9f96cdd"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = ofcolor(grid, x0)
    x2 = shift(x1, NEG_UNITY)
    x3 = recolor(THREE, x2)
    x4 = shift(x1, UNITY)
    x5 = recolor(SEVEN, x4)
    x6 = shift(x1, DOWN_LEFT)
    x7 = recolor(EIGHT, x6)
    x8 = shift(x1, UP_RIGHT)
    x9 = recolor(SIX, x8)
    x10 = mostcolor(grid)
    x11 = fill(grid, x10, x1)
    x12 = combine(x3, x5)
    x13 = combine(x7, x9)
    x14 = combine(x12, x13)
    x15 = paint(x11, x14)
    return x15


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
