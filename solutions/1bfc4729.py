"""Executable re-arc DSL program for ARC-AGI-2 task 1bfc4729.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ORIGIN,
    astuple,
    bottomhalf,
    center,
    connect,
    decrement,
    fill,
    halve,
    height,
    hfrontier,
    leastcolor,
    ofcolor,
    toivec,
    tojvec,
    tophalf,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "1bfc4729"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = tophalf(grid)
    x1 = bottomhalf(grid)
    x2 = leastcolor(x0)
    x3 = leastcolor(x1)
    x4 = ofcolor(grid, x2)
    x5 = center(x4)
    x6 = ofcolor(grid, x3)
    x7 = center(x6)
    x8 = height(grid)
    x9 = width(grid)
    x10 = hfrontier(x5)
    x11 = fill(grid, x2, x10)
    x12 = hfrontier(x7)
    x13 = fill(x11, x3, x12)
    x14 = decrement(x9)
    x15 = decrement(x8)
    x16 = halve(x8)
    x17 = tojvec(x14)
    x18 = connect(ORIGIN, x17)
    x19 = fill(x13, x2, x18)
    x20 = toivec(x15)
    x21 = astuple(x15, x14)
    x22 = connect(x20, x21)
    x23 = fill(x19, x3, x22)
    x24 = decrement(x16)
    x25 = toivec(x24)
    x26 = connect(ORIGIN, x25)
    x27 = fill(x23, x2, x26)
    x28 = tojvec(x14)
    x29 = decrement(x16)
    x30 = astuple(x29, x14)
    x31 = connect(x28, x30)
    x32 = fill(x27, x2, x31)
    x33 = toivec(x16)
    x34 = toivec(x15)
    x35 = connect(x33, x34)
    x36 = fill(x32, x3, x35)
    x37 = astuple(x16, x14)
    x38 = astuple(x15, x14)
    x39 = connect(x37, x38)
    x40 = fill(x36, x3, x39)
    return x40


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
