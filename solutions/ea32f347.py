"""Executable re-arc DSL program for ARC-AGI-2 task ea32f347.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    ONE,
    TWO,
    F,
    T,
    argmax,
    argmin,
    fill,
    merge,
    objects,
    size,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "ea32f347"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = merge(x0)
    x2 = fill(grid, FOUR, x1)
    x3 = argmin(x0, size)
    x4 = argmax(x0, size)
    x5 = fill(x2, ONE, x4)
    x6 = fill(x5, TWO, x3)
    return x6


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
