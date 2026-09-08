"""Executable re-arc DSL program for ARC-AGI-2 task 963e52fc.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ORIGIN,
    asobject,
    astuple,
    crop,
    divide,
    double,
    height,
    hperiod,
    increment,
    merge,
    repeat,
    rot90,
    rot270,
    ulcorner,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "963e52fc"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = width(grid)
    x1 = asobject(grid)
    x2 = hperiod(x1)
    x3 = height(x1)
    x4 = astuple(x3, x2)
    x5 = ulcorner(x1)
    x6 = crop(grid, x5, x4)
    x7 = rot90(x6)
    x8 = double(x0)
    x9 = divide(x8, x2)
    x10 = increment(x9)
    x11 = repeat(x7, x10)
    x12 = merge(x11)
    x13 = rot270(x12)
    x14 = astuple(x3, x8)
    x15 = crop(x13, ORIGIN, x14)
    return x15


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
