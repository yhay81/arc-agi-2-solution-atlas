"""Executable re-arc DSL program for ARC-AGI-2 task 67385a82.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    ONE,
    ZERO,
    F,
    T,
    colorfilter,
    difference,
    fill,
    merge,
    objects,
    other,
    palette,
    sizefilter,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "67385a82"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = palette(grid)
    x2 = other(x1, ZERO)
    x3 = colorfilter(x0, x2)
    x4 = sizefilter(x3, ONE)
    x5 = difference(x3, x4)
    x6 = merge(x5)
    x7 = fill(grid, EIGHT, x6)
    return x7


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
