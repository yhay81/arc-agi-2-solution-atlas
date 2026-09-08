"""Executable re-arc DSL program for ARC-AGI-2 task 36fdfd69.

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
    apply,
    astuple,
    backdrop,
    chain,
    compose,
    fill,
    first,
    fork,
    greater,
    identity,
    last,
    lbind,
    leastcolor,
    mapply,
    maximum,
    multiply,
    ofcolor,
    power,
    rbind,
    sfilter,
    sign,
    subtract,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "36fdfd69"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = ofcolor(grid, x0)
    x2 = fork(subtract, first, last)
    x3 = fork(multiply, sign, identity)
    x4 = compose(x3, x2)
    x5 = lbind(greater, THREE)
    x6 = chain(x5, maximum, x4)
    x7 = lbind(lbind, astuple)
    x8 = rbind(chain, x7)
    x9 = lbind(compose, x6)
    x10 = rbind(x8, x9)
    x11 = lbind(lbind, sfilter)
    x12 = compose(x10, x11)
    x13 = lbind(mapply, backdrop)
    x14 = fork(apply, x12, identity)
    x15 = compose(x13, x14)
    x16 = power(x15, TWO)
    x17 = x16(x1)
    x18 = fill(grid, FOUR, x17)
    x19 = fill(x18, x0, x1)
    return x19


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
