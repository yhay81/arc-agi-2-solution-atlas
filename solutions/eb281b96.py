"""Executable re-arc DSL program for ARC-AGI-2 task eb281b96.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    ORIGIN,
    astuple,
    crop,
    decrement,
    double,
    height,
    hmirror,
    vconcat,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "eb281b96"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = height(grid)
    x1 = width(grid)
    x2 = decrement(x0)
    x3 = astuple(x2, x1)
    x4 = crop(grid, ORIGIN, x3)
    x5 = hmirror(x4)
    x6 = vconcat(grid, x5)
    x7 = double(x2)
    x8 = astuple(x7, x1)
    x9 = crop(x6, DOWN, x8)
    x10 = vconcat(x6, x9)
    return x10


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
