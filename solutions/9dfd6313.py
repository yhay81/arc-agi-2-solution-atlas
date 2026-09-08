"""Executable re-arc DSL program for ARC-AGI-2 task 9dfd6313.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ORIGIN,
    astuple,
    both,
    chain,
    cmirror,
    color,
    colorcount,
    combine,
    compose,
    connect,
    decrement,
    dmirror,
    equality,
    extract,
    first,
    fork,
    halve,
    height,
    hmirror,
    last,
    lbind,
    matcher,
    numcolors,
    rbind,
    shape,
    size,
    toivec,
    tojvec,
    toobject,
    vmirror,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "9dfd6313"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = shape(grid)
    x1 = decrement(x0)
    x2 = connect(ORIGIN, x1)
    x3 = height(grid)
    x4 = decrement(x3)
    x5 = toivec(x4)
    x6 = width(grid)
    x7 = decrement(x6)
    x8 = tojvec(x7)
    x9 = connect(x5, x8)
    x10 = height(grid)
    x11 = halve(x10)
    x12 = toivec(x11)
    x13 = width(grid)
    x14 = decrement(x13)
    x15 = astuple(x11, x14)
    x16 = connect(x12, x15)
    x17 = width(grid)
    x18 = halve(x17)
    x19 = tojvec(x18)
    x20 = height(grid)
    x21 = decrement(x20)
    x22 = astuple(x21, x18)
    x23 = connect(x19, x22)
    x24 = astuple(x2, dmirror)
    x25 = astuple(x9, cmirror)
    x26 = astuple(x24, x25)
    x27 = astuple(x23, vmirror)
    x28 = astuple(x16, hmirror)
    x29 = astuple(x27, x28)
    x30 = combine(x26, x29)
    x31 = lbind(colorcount, grid)
    x32 = rbind(toobject, grid)
    x33 = compose(x32, first)
    x34 = chain(x31, color, x33)
    x35 = compose(size, first)
    x36 = fork(equality, x34, x35)
    x37 = rbind(toobject, grid)
    x38 = chain(numcolors, x37, first)
    x39 = matcher(x38, ONE)
    x40 = fork(both, x39, x36)
    x41 = extract(x30, x40)
    x42 = last(x41)
    x43 = x42(grid)
    return x43


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
