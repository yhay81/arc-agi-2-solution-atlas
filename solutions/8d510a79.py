"""Executable re-arc DSL program for ARC-AGI-2 task 8d510a79.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    TWO,
    add,
    apply,
    branch,
    chain,
    color,
    colorfilter,
    compose,
    connect,
    dmirror,
    fill,
    fork,
    frontiers,
    gravitate,
    identity,
    initset,
    lbind,
    leastcommon,
    mapply,
    maximum,
    multiply,
    ofcolor,
    positive,
    rbind,
    shape,
    sign,
    size,
    totuple,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "8d510a79"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = totuple(x0)
    x2 = apply(color, x1)
    x3 = leastcommon(x2)
    x4 = frontiers(grid)
    x5 = colorfilter(x4, x3)
    x6 = size(x5)
    x7 = positive(x6)
    branch(x7, dmirror, identity)
    x9 = ofcolor(grid, x3)
    x10 = ofcolor(grid, TWO)
    x11 = ofcolor(grid, ONE)
    x12 = rbind(gravitate, x9)
    x13 = compose(x12, initset)
    x14 = fork(add, identity, x13)
    x15 = fork(connect, identity, x14)
    x16 = shape(grid)
    x17 = maximum(x16)
    x18 = lbind(multiply, x17)
    x19 = lbind(gravitate, x9)
    x20 = chain(x18, sign, x19)
    x21 = compose(x20, initset)
    x22 = fork(add, identity, x21)
    x23 = fork(connect, identity, x22)
    x24 = mapply(x15, x10)
    x25 = mapply(x23, x11)
    x26 = fill(grid, TWO, x24)
    x27 = fill(x26, ONE, x25)
    return x27


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
