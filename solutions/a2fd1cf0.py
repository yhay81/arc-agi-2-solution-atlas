"""Executable re-arc DSL program for ARC-AGI-2 task a2fd1cf0.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    THREE,
    TWO,
    astuple,
    combine,
    connect,
    leftmost,
    maximum,
    minimum,
    ofcolor,
    underfill,
    uppermost,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "a2fd1cf0"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = ofcolor(grid, TWO)
    x1 = ofcolor(grid, THREE)
    x2 = uppermost(x0)
    x3 = leftmost(x0)
    x4 = uppermost(x1)
    x5 = leftmost(x1)
    x6 = astuple(x2, x4)
    x7 = minimum(x6)
    x8 = maximum(x6)
    x9 = astuple(x7, x5)
    x10 = astuple(x8, x5)
    x11 = connect(x9, x10)
    x12 = astuple(x3, x5)
    x13 = minimum(x12)
    x14 = maximum(x12)
    x15 = astuple(x2, x13)
    x16 = astuple(x2, x14)
    x17 = connect(x15, x16)
    x18 = combine(x11, x17)
    x19 = underfill(grid, EIGHT, x18)
    return x19


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
