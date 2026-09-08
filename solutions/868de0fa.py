"""Executable re-arc DSL program for ARC-AGI-2 task 868de0fa.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    SEVEN,
    TWO,
    F,
    T,
    compose,
    difference,
    even,
    fill,
    height,
    merge,
    objects,
    sfilter,
    square,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "868de0fa"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = sfilter(x0, square)
    x2 = compose(even, height)
    x3 = sfilter(x1, x2)
    x4 = difference(x1, x3)
    x5 = merge(x3)
    x6 = merge(x4)
    x7 = fill(grid, TWO, x5)
    x8 = fill(x7, SEVEN, x6)
    return x8


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
