"""Executable re-arc DSL program for ARC-AGI-2 task 5c2c9af4.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    TEN,
    THREE,
    ZERO,
    add,
    apply,
    box,
    fill,
    halve,
    height,
    interval,
    invert,
    leastcolor,
    lrcorner,
    mapply,
    maximum,
    multiply,
    ofcolor,
    pair,
    rbind,
    shape,
    ulcorner,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "5c2c9af4"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = ofcolor(grid, x0)
    x2 = height(x1)
    x3 = halve(x2)
    x4 = width(x1)
    x5 = halve(x4)
    x6 = ulcorner(x1)
    x7 = lrcorner(x1)
    x8 = shape(grid)
    maximum(x8)
    x10 = multiply(THREE, TEN)
    x11 = interval(ZERO, x10, ONE)
    x12 = rbind(multiply, x3)
    x13 = apply(x12, x11)
    x14 = rbind(multiply, x5)
    x15 = apply(x14, x11)
    x16 = pair(x13, x15)
    x17 = rbind(add, x6)
    x18 = apply(invert, x16)
    x19 = apply(x17, x18)
    x20 = rbind(add, x7)
    x21 = apply(x20, x16)
    x22 = pair(x19, x21)
    x23 = mapply(box, x22)
    x24 = fill(grid, x0, x23)
    return x24


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
