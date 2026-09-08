"""Executable re-arc DSL program for ARC-AGI-2 task d0f5fe59.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ORIGIN,
    UNITY,
    F,
    T,
    astuple,
    canvas,
    fill,
    leastcolor,
    mostcolor,
    objects,
    shoot,
    size,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d0f5fe59"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = size(x0)
    x2 = astuple(x1, x1)
    x3 = mostcolor(grid)
    x4 = canvas(x3, x2)
    x5 = shoot(ORIGIN, UNITY)
    x6 = leastcolor(grid)
    x7 = fill(x4, x6, x5)
    return x7


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
