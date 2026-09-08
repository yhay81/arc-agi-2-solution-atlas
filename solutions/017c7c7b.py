"""Executable re-arc DSL program for ARC-AGI-2 task 017c7c7b.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    ZERO,
    add,
    apply,
    asobject,
    astuple,
    canvas,
    fill,
    halve,
    height,
    increment,
    interval,
    lbind,
    mapply,
    ofcolor,
    other,
    palette,
    shift,
    toivec,
    vperiod,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "017c7c7b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = palette(grid)
    x1 = other(x0, ZERO)
    x2 = ofcolor(grid, x1)
    x3 = asobject(grid)
    x4 = vperiod(x3)
    x5 = height(grid)
    x6 = halve(x5)
    x7 = add(x5, x6)
    x8 = width(grid)
    x9 = astuple(x7, x8)
    x10 = canvas(ZERO, x9)
    x11 = increment(x7)
    x12 = interval(ZERO, x11, x4)
    x13 = lbind(shift, x2)
    x14 = apply(toivec, x12)
    x15 = mapply(x13, x14)
    x16 = fill(x10, TWO, x15)
    return x16


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
