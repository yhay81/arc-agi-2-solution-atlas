"""Executable re-arc DSL program for ARC-AGI-2 task 6e02f1e3.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FIVE,
    ORIGIN,
    THREE,
    TWO,
    ZERO,
    branch,
    canvas,
    connect,
    decrement,
    equality,
    fill,
    height,
    numcolors,
    shape,
    toivec,
    tojvec,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "6e02f1e3"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = numcolors(grid)
    x1 = equality(x0, THREE)
    x2 = height(grid)
    x3 = decrement(x2)
    x4 = toivec(x3)
    x5 = branch(x1, x4, ORIGIN)
    x6 = equality(x0, TWO)
    x7 = shape(grid)
    x8 = decrement(x7)
    x9 = width(grid)
    x10 = decrement(x9)
    x11 = tojvec(x10)
    x12 = branch(x6, x8, x11)
    x13 = shape(grid)
    x14 = canvas(ZERO, x13)
    x15 = connect(x5, x12)
    x16 = fill(x14, FIVE, x15)
    return x16


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
