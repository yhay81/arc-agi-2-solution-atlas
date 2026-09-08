"""Executable re-arc DSL program for ARC-AGI-2 task 2013d3e2.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    ONE,
    TEN,
    THREE,
    ZERO,
    apply,
    branch,
    chain,
    compose,
    dedupe,
    equality,
    first,
    fork,
    identity,
    initset,
    interval,
    last,
    lbind,
    lefthalf,
    multiply,
    pair,
    positive,
    power,
    rapply,
    rbind,
    rot90,
    sfilter,
    size,
    tophalf,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "2013d3e2"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = lbind(apply, last)
    x1 = compose(positive, first)
    x2 = lbind(interval, ZERO)
    x3 = rbind(x2, ONE)
    x4 = rbind(sfilter, x1)
    x5 = compose(x3, size)
    x6 = fork(pair, x5, identity)
    x7 = chain(x0, x4, x6)
    x8 = rbind(branch, identity)
    x9 = rbind(x8, x7)
    x10 = chain(size, dedupe, first)
    x11 = lbind(equality, ONE)
    x12 = chain(x9, x11, x10)
    x13 = compose(initset, x12)
    x14 = fork(rapply, x13, identity)
    x15 = compose(first, x14)
    x16 = rbind(branch, identity)
    x17 = rbind(x16, x15)
    x18 = chain(x17, positive, size)
    x19 = compose(initset, x18)
    x20 = fork(rapply, x19, identity)
    x21 = compose(first, x20)
    x22 = multiply(TEN, THREE)
    x23 = power(x21, x22)
    x24 = compose(rot90, x23)
    x25 = power(x24, FOUR)
    x26 = x25(grid)
    x27 = lefthalf(x26)
    x28 = tophalf(x27)
    return x28


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
