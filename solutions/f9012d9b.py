"""Executable re-arc DSL program for ARC-AGI-2 task f9012d9b.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ZERO,
    apply,
    asobject,
    astuple,
    compose,
    contained,
    divide,
    dmirror,
    first,
    flip,
    height,
    hperiod,
    increment,
    interval,
    invert,
    lbind,
    mapply,
    matcher,
    maximum,
    multiply,
    ofcolor,
    paint,
    product,
    sfilter,
    shift,
    subgrid,
    vsplit,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "f9012d9b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = lbind(contained, ZERO)
    x1 = compose(flip, x0)
    x2 = sfilter(grid, x1)
    x3 = dmirror(grid)
    x4 = lbind(contained, ZERO)
    x5 = compose(flip, x4)
    x6 = sfilter(x3, x5)
    x7 = compose(hperiod, asobject)
    x8 = height(x2)
    x9 = vsplit(x2, x8)
    x10 = apply(x7, x9)
    x11 = maximum(x10)
    x12 = compose(hperiod, asobject)
    x13 = height(x6)
    x14 = vsplit(x6, x13)
    x15 = apply(x12, x14)
    x16 = maximum(x15)
    x17 = ofcolor(grid, ZERO)
    x18 = asobject(grid)
    x19 = matcher(first, ZERO)
    x20 = compose(flip, x19)
    x21 = sfilter(x18, x20)
    x22 = lbind(shift, x21)
    x23 = height(grid)
    x24 = divide(x23, x16)
    x25 = increment(x24)
    x26 = width(grid)
    x27 = divide(x26, x11)
    x28 = increment(x27)
    x29 = invert(x25)
    x30 = increment(x25)
    x31 = interval(x29, x30, ONE)
    x32 = invert(x28)
    x33 = increment(x28)
    x34 = interval(x32, x33, ONE)
    x35 = product(x31, x34)
    x36 = astuple(x16, x11)
    x37 = lbind(multiply, x36)
    x38 = apply(x37, x35)
    x39 = mapply(x22, x38)
    x40 = paint(grid, x39)
    x41 = subgrid(x17, x40)
    return x41


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
