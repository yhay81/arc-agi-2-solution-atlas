"""Executable re-arc DSL program for ARC-AGI-2 task e8593010.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    THREE,
    TWO,
    F,
    T,
    fill,
    merge,
    objects,
    sizefilter,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "e8593010"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = sizefilter(x0, ONE)
    x2 = sizefilter(x0, TWO)
    x3 = sizefilter(x0, THREE)
    x4 = merge(x1)
    x5 = fill(grid, THREE, x4)
    x6 = merge(x2)
    x7 = fill(x5, TWO, x6)
    x8 = merge(x3)
    x9 = fill(x7, ONE, x8)
    return x9


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
