"""Executable re-arc DSL program for ARC-AGI-2 task c0f76784.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    FOUR,
    NINE,
    ONE,
    SEVEN,
    SIX,
    F,
    T,
    colorfilter,
    fill,
    merge,
    mostcolor,
    objects,
    sizefilter,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "c0f76784"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = mostcolor(grid)
    x2 = colorfilter(x0, x1)
    x3 = sizefilter(x2, ONE)
    x4 = merge(x3)
    x5 = sizefilter(x2, FOUR)
    x6 = merge(x5)
    x7 = sizefilter(x2, NINE)
    x8 = merge(x7)
    x9 = fill(grid, SIX, x4)
    x10 = fill(x9, SEVEN, x6)
    x11 = fill(x10, EIGHT, x8)
    return x11


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
