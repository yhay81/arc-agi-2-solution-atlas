"""Executable re-arc DSL program for ARC-AGI-2 task d364b489.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    EIGHT,
    LEFT,
    RIGHT,
    SEVEN,
    SIX,
    TWO,
    UP,
    fgpartition,
    fill,
    merge,
    shift,
    toindices,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d364b489"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = merge(x0)
    x2 = toindices(x1)
    x3 = shift(x2, DOWN)
    x4 = fill(grid, EIGHT, x3)
    x5 = shift(x2, UP)
    x6 = fill(x4, TWO, x5)
    x7 = shift(x2, RIGHT)
    x8 = fill(x6, SIX, x7)
    x9 = shift(x2, LEFT)
    x10 = fill(x8, SEVEN, x9)
    return x10


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
