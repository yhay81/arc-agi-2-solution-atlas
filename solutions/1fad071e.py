"""Executable re-arc DSL program for ARC-AGI-2 task 1fad071e.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FIVE,
    FOUR,
    ONE,
    F,
    T,
    astuple,
    canvas,
    colorfilter,
    equality,
    fork,
    hconcat,
    height,
    mostcolor,
    objects,
    sfilter,
    size,
    sizefilter,
    subtract,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "1fad071e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = colorfilter(x0, ONE)
    x2 = sizefilter(x1, FOUR)
    x3 = fork(equality, height, width)
    x4 = sfilter(x2, x3)
    x5 = size(x4)
    x6 = subtract(FIVE, x5)
    x7 = astuple(ONE, x5)
    x8 = canvas(ONE, x7)
    x9 = astuple(ONE, x6)
    x10 = mostcolor(grid)
    x11 = canvas(x10, x9)
    x12 = hconcat(x8, x11)
    return x12


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
