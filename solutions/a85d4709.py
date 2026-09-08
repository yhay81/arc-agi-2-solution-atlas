"""Executable re-arc DSL program for ARC-AGI-2 task a85d4709.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    THREE,
    TWO,
    add,
    apply,
    both,
    compose,
    divide,
    either,
    flip,
    fork,
    greater,
    height,
    lbind,
    leastcolor,
    leftmost,
    multiply,
    ofcolor,
    rbind,
    repeat,
    vsplit,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "a85d4709"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = height(grid)
    x2 = vsplit(grid, x1)
    x3 = rbind(ofcolor, x0)
    x4 = compose(leftmost, x3)
    x5 = width(grid)
    x6 = divide(x5, THREE)
    x7 = multiply(x6, TWO)
    x8 = lbind(greater, x6)
    x9 = compose(x8, x4)
    x10 = lbind(greater, x7)
    x11 = compose(x10, x4)
    x12 = compose(flip, x9)
    x13 = fork(both, x11, x12)
    x14 = fork(either, x9, x13)
    x15 = compose(flip, x14)
    x16 = rbind(multiply, TWO)
    x17 = compose(x16, x9)
    x18 = rbind(multiply, FOUR)
    x19 = compose(x18, x13)
    x20 = rbind(multiply, THREE)
    x21 = compose(x20, x15)
    x22 = fork(add, x17, x19)
    x23 = fork(add, x22, x21)
    x24 = width(grid)
    x25 = rbind(repeat, x24)
    x26 = compose(x25, x23)
    x27 = apply(x26, x2)
    return x27


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
