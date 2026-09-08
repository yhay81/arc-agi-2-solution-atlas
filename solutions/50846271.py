"""Executable re-arc DSL program for ARC-AGI-2 task 50846271.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    EIGHT,
    FIVE,
    FOUR,
    LEFT,
    ONE,
    RIGHT,
    TWO,
    UP,
    T,
    add,
    apply,
    both,
    center,
    chain,
    colorfilter,
    combine,
    compose,
    connect,
    contained,
    either,
    fill,
    first,
    fork,
    halve,
    hline,
    identity,
    initset,
    intersection,
    interval,
    invert,
    lbind,
    leastcolor,
    mapply,
    matcher,
    maximum,
    objects,
    ofcolor,
    paint,
    power,
    rapply,
    rbind,
    recolor,
    replace,
    sfilter,
    shape,
    shift,
    size,
    toivec,
    tojvec,
    vline,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "50846271"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = ofcolor(grid, x0)
    x2 = interval(TWO, FIVE, ONE)
    x3 = rbind(shift, RIGHT)
    x4 = rbind(shift, LEFT)
    x5 = rbind(shift, UP)
    x6 = rbind(shift, DOWN)
    x7 = lbind(fork, intersection)
    x8 = lbind(x7, identity)
    x9 = lbind(rbind, shift)
    x10 = compose(x8, x9)
    x11 = compose(x10, tojvec)
    x12 = chain(x10, tojvec, invert)
    x13 = compose(x10, toivec)
    x14 = chain(x10, toivec, invert)
    x15 = lbind(compose, initset)
    x16 = lbind(rbind, rapply)
    x17 = lbind(chain, first)
    x18 = lbind(compose, x4)
    x19 = x15(x11)
    x20 = rbind(x17, x19)
    x21 = chain(x18, x20, x16)
    x22 = lbind(compose, x3)
    x23 = x15(x12)
    x24 = rbind(x17, x23)
    x25 = chain(x22, x24, x16)
    x26 = lbind(compose, x5)
    x27 = x15(x13)
    x28 = rbind(x17, x27)
    x29 = chain(x26, x28, x16)
    x30 = lbind(compose, x6)
    x31 = x15(x14)
    x32 = rbind(x17, x31)
    x33 = chain(x30, x32, x16)
    x34 = rbind(ofcolor, x0)
    x35 = compose(x21, x34)
    x36 = compose(x25, x34)
    x37 = compose(x29, x34)
    x38 = compose(x33, x34)
    x39 = lbind(fork, combine)
    x40 = fork(x39, x35, x36)
    x41 = fork(x39, x37, x38)
    x42 = fork(x39, x40, x41)
    x43 = lbind(recolor, x0)
    x44 = rbind(mapply, x2)
    x45 = chain(x43, x44, x42)
    x46 = fork(paint, identity, x45)
    x47 = power(x46, FOUR)
    x48 = x47(grid)
    x49 = objects(x48, T, T, T)
    x50 = colorfilter(x49, x0)
    x51 = compose(maximum, shape)
    x52 = apply(x51, x50)
    x53 = maximum(x52)
    x54 = ofcolor(x48, x0)
    x55 = rbind(contained, x54)
    x56 = rbind(add, RIGHT)
    x57 = compose(x55, x56)
    x58 = rbind(add, LEFT)
    x59 = compose(x55, x58)
    x60 = fork(either, x57, x59)
    x61 = rbind(add, DOWN)
    x62 = compose(x55, x61)
    x63 = rbind(add, UP)
    x64 = compose(x55, x63)
    x65 = fork(either, x62, x64)
    x66 = fork(both, x60, x65)
    x67 = matcher(size, x53)
    x68 = fork(either, vline, hline)
    x69 = fork(both, x67, x68)
    x70 = sfilter(x50, x69)
    x71 = apply(center, x70)
    x72 = sfilter(x54, x66)
    x73 = combine(x72, x71)
    x74 = halve(x53)
    x75 = invert(x74)
    x76 = toivec(x75)
    x77 = rbind(add, x76)
    x78 = toivec(x74)
    x79 = rbind(add, x78)
    x80 = fork(connect, x77, x79)
    x81 = invert(x74)
    x82 = tojvec(x81)
    x83 = rbind(add, x82)
    x84 = tojvec(x74)
    x85 = rbind(add, x84)
    x86 = fork(connect, x83, x85)
    x87 = fork(combine, x80, x86)
    x88 = mapply(x87, x73)
    x89 = fill(x48, x0, x88)
    x90 = replace(x89, x0, EIGHT)
    x91 = fill(x90, x0, x1)
    return x91


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
