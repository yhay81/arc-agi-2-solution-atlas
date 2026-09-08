"""Executable re-arc DSL program for ARC-AGI-2 task 6ecd11f4.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ZERO,
    F,
    T,
    apply,
    argmax,
    argmin,
    canvas,
    chain,
    color,
    compose,
    contained,
    divide,
    equality,
    first,
    fork,
    height,
    identity,
    interval,
    last,
    lbind,
    mostcolor,
    multiply,
    normalize,
    numcolors,
    objects,
    ofcolor,
    paint,
    pair,
    rbind,
    sfilter,
    shape,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "6ecd11f4"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, T, T)
    x1 = argmax(x0, numcolors)
    x2 = argmin(x0, numcolors)
    x3 = mostcolor(grid)
    x4 = shape(x2)
    x5 = canvas(x3, x4)
    x6 = normalize(x2)
    x7 = paint(x5, x6)
    x8 = height(x1)
    x9 = width(x1)
    x10 = height(x2)
    x11 = width(x2)
    x12 = normalize(x1)
    x13 = divide(x10, x8)
    x14 = divide(x11, x9)
    x15 = width(x7)
    x16 = interval(ZERO, x15, ONE)
    x17 = height(x7)
    x18 = interval(ZERO, x17, ONE)
    x19 = rbind(multiply, x14)
    x20 = rbind(divide, x14)
    x21 = compose(x19, x20)
    x22 = fork(equality, identity, x21)
    x23 = rbind(multiply, x13)
    x24 = rbind(divide, x13)
    x25 = compose(x23, x24)
    x26 = fork(equality, identity, x25)
    x27 = lbind(apply, last)
    x28 = compose(x22, first)
    x29 = rbind(sfilter, x28)
    x30 = lbind(pair, x16)
    x31 = chain(x27, x29, x30)
    x32 = compose(x31, last)
    x33 = pair(x18, x7)
    x34 = compose(x26, first)
    x35 = sfilter(x33, x34)
    x36 = apply(x32, x35)
    x37 = color(x2)
    x38 = ofcolor(x36, x37)
    x39 = rbind(contained, x38)
    x40 = compose(x39, last)
    x41 = sfilter(x12, x40)
    x42 = paint(x36, x41)
    return x42


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
