"""Executable re-arc DSL program for ARC-AGI-2 task 28e73c20.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    LEFT,
    ONE,
    ORIGIN,
    RIGHT,
    TEN,
    THREE,
    UP,
    ZERO,
    F,
    add,
    astuple,
    branch,
    canvas,
    chain,
    combine,
    compose,
    connect,
    crop,
    decrement,
    dmirror,
    extract,
    fill,
    first,
    flip,
    fork,
    hconcat,
    height,
    identity,
    initset,
    last,
    lbind,
    matcher,
    multiply,
    paint,
    positive,
    power,
    rapply,
    rbind,
    recolor,
    shape,
    tojvec,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "28e73c20"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = astuple(RIGHT, DOWN)
    x1 = astuple(DOWN, LEFT)
    x2 = astuple(x0, x1)
    x3 = astuple(LEFT, UP)
    x4 = astuple(UP, RIGHT)
    x5 = astuple(x3, x4)
    x6 = combine(x2, x5)
    x7 = height(grid)
    x8 = astuple(x7, ONE)
    x9 = canvas(THREE, x8)
    x10 = hconcat(x9, grid)
    x11 = height(x10)
    x12 = width(x10)
    x13 = decrement(x12)
    x14 = tojvec(x13)
    x15 = identity(DOWN)
    x16 = connect(ORIGIN, x14)
    x17 = fill(x10, THREE, x16)
    x18 = identity(x12)
    x19 = identity(x11)
    x20 = identity(x11)
    x21 = identity(F)
    x22 = identity(ZERO)
    x23 = compose(first, first)
    x24 = chain(first, last, x23)
    x25 = compose(first, first)
    x26 = chain(last, last, x25)
    x27 = chain(first, first, first)
    x28 = chain(first, last, last)
    x29 = chain(first, first, last)
    x30 = chain(last, first, last)
    x31 = compose(decrement, x24)
    x32 = compose(decrement, x26)
    x33 = fork(astuple, x31, x32)
    x34 = compose(decrement, x26)
    x35 = fork(multiply, x29, x34)
    x36 = fork(add, x28, x35)
    x37 = compose(decrement, x27)
    x38 = fork(multiply, x29, x37)
    x39 = fork(add, x28, x38)
    x40 = fork(astuple, x39, x36)
    x41 = lbind(extract, x6)
    x42 = lbind(matcher, first)
    x43 = compose(x42, x29)
    x44 = chain(last, x41, x43)
    x45 = compose(last, first)
    x46 = lbind(recolor, THREE)
    x47 = compose(decrement, x27)
    x48 = fork(multiply, x29, x47)
    x49 = fork(add, x28, x48)
    x50 = fork(connect, x28, x49)
    x51 = compose(x46, x50)
    x52 = fork(paint, x45, x51)
    x53 = compose(decrement, x26)
    x54 = fork(multiply, x30, x53)
    x55 = compose(flip, x30)
    x56 = compose(decrement, x24)
    x57 = fork(multiply, x55, x56)
    x58 = fork(add, x54, x57)
    x59 = power(first, THREE)
    x60 = chain(flip, positive, x59)
    x61 = fork(astuple, x58, x33)
    x62 = compose(flip, x30)
    x63 = fork(astuple, x44, x62)
    x64 = fork(astuple, x61, x52)
    x65 = fork(astuple, x63, x40)
    x66 = fork(astuple, x64, x65)
    x67 = rbind(branch, x66)
    x68 = rbind(x67, identity)
    x69 = chain(initset, x68, x60)
    x70 = fork(rapply, x69, identity)
    x71 = compose(first, x70)
    x72 = multiply(TEN, THREE)
    x73 = power(x71, x72)
    x74 = astuple(x18, x19)
    x75 = astuple(x15, x21)
    x76 = astuple(x14, x22)
    x77 = astuple(x20, x74)
    x78 = astuple(x75, x76)
    x79 = astuple(x77, x17)
    x80 = astuple(x79, x78)
    x81 = x73(x80)
    x82 = first(x81)
    x83 = last(x82)
    x84 = dmirror(x83)
    x85 = shape(x84)
    x86 = add(x85, UP)
    x87 = crop(x84, DOWN, x86)
    x88 = dmirror(x87)
    return x88


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
