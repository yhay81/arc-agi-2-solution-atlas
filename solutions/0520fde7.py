"""Executable re-arc DSL program for ARC-AGI-2 task 0520fde7.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    TWO,
    ZERO,
    astuple,
    bottomhalf,
    branch,
    canvas,
    connect,
    decrement,
    equality,
    fill,
    halve,
    height,
    intersection,
    lefthalf,
    numcolors,
    ofcolor,
    other,
    palette,
    righthalf,
    shape,
    tojvec,
    toobject,
    tophalf,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "0520fde7"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = width(grid)
    x1 = halve(x0)
    x2 = tojvec(x1)
    x3 = height(grid)
    x4 = decrement(x3)
    x5 = astuple(x4, x1)
    x6 = connect(x2, x5)
    x7 = toobject(x6, grid)
    x8 = numcolors(x7)
    x9 = equality(x8, ONE)
    x10 = branch(x9, lefthalf, tophalf)
    x11 = branch(x9, righthalf, bottomhalf)
    x12 = x10(grid)
    x13 = x11(grid)
    x14 = palette(x12)
    x15 = other(x14, ZERO)
    x16 = palette(x13)
    x17 = other(x16, ZERO)
    x18 = shape(x12)
    x19 = canvas(ZERO, x18)
    x20 = ofcolor(x12, x15)
    x21 = ofcolor(x13, x17)
    x22 = intersection(x20, x21)
    x23 = fill(x19, TWO, x22)
    return x23


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
