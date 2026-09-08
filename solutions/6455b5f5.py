"""Executable re-arc DSL program for ARC-AGI-2 task 6455b5f5.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    ONE,
    F,
    T,
    asindices,
    colorfilter,
    corners,
    fill,
    merge,
    mostcolor,
    objects,
    size,
    sizefilter,
    toobject,
    valmax,
    valmin,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "6455b5f5"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = asindices(grid)
    x2 = corners(x1)
    x3 = toobject(x2, grid)
    x4 = mostcolor(x3)
    x5 = colorfilter(x0, x4)
    x6 = valmax(x5, size)
    x7 = valmin(x5, size)
    x8 = sizefilter(x5, x6)
    x9 = sizefilter(x5, x7)
    x10 = merge(x8)
    x11 = fill(grid, ONE, x10)
    x12 = merge(x9)
    x13 = fill(x11, EIGHT, x12)
    return x13


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
