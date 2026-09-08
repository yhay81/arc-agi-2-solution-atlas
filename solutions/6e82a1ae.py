"""Executable re-arc DSL program for ARC-AGI-2 task 6e82a1ae.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    ONE,
    THREE,
    TWO,
    F,
    T,
    fill,
    matcher,
    mfilter,
    objects,
    size,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "6e82a1ae"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = matcher(size, TWO)
    x2 = mfilter(x0, x1)
    x3 = matcher(size, THREE)
    x4 = mfilter(x0, x3)
    x5 = matcher(size, FOUR)
    x6 = mfilter(x0, x5)
    x7 = fill(grid, THREE, x2)
    x8 = fill(x7, TWO, x4)
    x9 = fill(x8, ONE, x6)
    return x9


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
