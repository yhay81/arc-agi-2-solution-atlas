"""Executable re-arc DSL program for ARC-AGI-2 task cf98881b.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ORIGIN,
    THREE,
    TWO,
    add,
    astuple,
    canvas,
    crop,
    decrement,
    divide,
    double,
    fill,
    first,
    height,
    increment,
    intersection,
    ofcolor,
    other,
    palette,
    tojvec,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "cf98881b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = width(grid)
    x1 = increment(x0)
    x2 = divide(x1, THREE)
    x3 = decrement(x2)
    x4 = height(grid)
    x5 = astuple(x4, x3)
    x6 = crop(grid, ORIGIN, x5)
    x7 = add(x3, ONE)
    x8 = tojvec(x7)
    x9 = crop(grid, x8, x5)
    x10 = double(x3)
    x11 = add(x10, TWO)
    x12 = tojvec(x11)
    x13 = crop(grid, x12, x5)
    x14 = palette(x6)
    x15 = palette(x9)
    x16 = palette(x13)
    x17 = intersection(x14, x15)
    x18 = intersection(x17, x16)
    x19 = first(x18)
    x20 = other(x14, x19)
    x21 = other(x15, x19)
    x22 = other(x16, x19)
    x23 = canvas(x19, x5)
    x24 = ofcolor(x6, x20)
    x25 = ofcolor(x9, x21)
    x26 = ofcolor(x13, x22)
    x27 = fill(x23, x22, x26)
    x28 = fill(x27, x21, x25)
    x29 = fill(x28, x20, x24)
    return x29


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
