"""Executable re-arc DSL program for ARC-AGI-2 task 05269061.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    NEG_UNITY,
    ONE,
    RIGHT,
    UP_RIGHT,
    ZERO,
    apply,
    astuple,
    branch,
    chain,
    combine,
    compose,
    decrement,
    divide,
    double,
    first,
    flip,
    fork,
    greater,
    identity,
    increment,
    interval,
    last,
    lbind,
    mapply,
    matcher,
    maximum,
    mostcolor,
    multiply,
    numcolors,
    paint,
    pair,
    rbind,
    recolor,
    sfilter,
    shape,
    shoot,
    size,
    subtract,
    toivec,
    tojvec,
    toobject,
    valmax,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "05269061"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = shape(grid)
    x1 = maximum(x0)
    x2 = interval(ZERO, x1, ONE)
    x3 = interval(ONE, x1, ONE)
    x4 = rbind(toobject, grid)
    x5 = rbind(shoot, RIGHT)
    x6 = chain(x4, x5, toivec)
    x7 = rbind(shoot, DOWN)
    x8 = chain(x4, x7, tojvec)
    x9 = apply(x6, x2)
    x10 = apply(x8, x2)
    x11 = rbind(shoot, UP_RIGHT)
    x12 = chain(x4, x11, toivec)
    x13 = rbind(shoot, UP_RIGHT)
    x14 = decrement(x1)
    x15 = lbind(astuple, x14)
    x16 = chain(x4, x13, x15)
    x17 = apply(x12, x2)
    x18 = apply(x16, x3)
    x19 = combine(x17, x18)
    x20 = rbind(shoot, NEG_UNITY)
    x21 = decrement(x1)
    x22 = lbind(astuple, x21)
    x23 = chain(x4, x20, x22)
    x24 = rbind(shoot, NEG_UNITY)
    x25 = decrement(x1)
    x26 = rbind(astuple, x25)
    x27 = lbind(subtract, x25)
    x28 = compose(x26, x27)
    x29 = chain(x4, x24, x28)
    x30 = apply(x23, x2)
    x31 = apply(x29, x3)
    x32 = combine(x30, x31)
    x33 = rbind(valmax, numcolors)
    x34 = matcher(x33, ONE)
    x35 = x34(x9)
    x36 = x34(x10)
    x37 = x34(x19)
    x38 = branch(x37, x19, x32)
    x39 = branch(x36, x10, x38)
    x40 = branch(x35, x9, x39)
    x41 = apply(mostcolor, x40)
    x42 = matcher(identity, ZERO)
    x43 = compose(flip, x42)
    x44 = sfilter(x41, x43)
    x45 = size(x44)
    x46 = double(x1)
    x47 = divide(x46, x45)
    x48 = increment(x47)
    x49 = interval(ZERO, x48, ONE)
    x50 = matcher(first, ZERO)
    x51 = compose(flip, x50)
    x52 = fork(recolor, first, last)
    x53 = size(x40)
    x54 = interval(ZERO, x53, ONE)
    x55 = rbind(compose, first)
    x56 = lbind(rbind, greater)
    x57 = chain(x55, x56, decrement)
    x58 = lbind(apply, last)
    x59 = lbind(chain, x58)
    x60 = rbind(x59, x57)
    x61 = lbind(lbind, sfilter)
    x62 = lbind(pair, x54)
    x63 = chain(x60, x61, x62)
    x64 = x63(x40)
    x65 = x63(x41)
    x66 = rbind(multiply, x45)
    x67 = compose(x64, x66)
    x68 = rbind(multiply, x45)
    x69 = compose(x65, x68)
    x70 = lbind(mapply, x52)
    x71 = rbind(sfilter, x51)
    x72 = lbind(pair, x41)
    x73 = compose(x72, x67)
    x74 = chain(x70, x71, x73)
    x75 = lbind(mapply, x52)
    x76 = rbind(sfilter, x51)
    x77 = rbind(pair, x40)
    x78 = compose(x77, x69)
    x79 = chain(x75, x76, x78)
    x80 = fork(combine, x74, x79)
    x81 = mapply(x80, x49)
    x82 = paint(grid, x81)
    return x82


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
