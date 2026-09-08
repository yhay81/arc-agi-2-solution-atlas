"""Executable re-arc DSL program for ARC-AGI-2 task 234bbc79.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ORIGIN,
    RIGHT,
    TWO,
    F,
    T,
    argmin,
    astuple,
    branch,
    chain,
    colorcount,
    combine,
    compose,
    contained,
    cover,
    crop,
    decrement,
    dneighbors,
    extract,
    first,
    flip,
    fork,
    height,
    identity,
    initset,
    insert,
    last,
    lbind,
    leftmost,
    manhattan,
    mapply,
    matcher,
    merge,
    mostcolor,
    objects,
    ofcolor,
    order,
    paint,
    palette,
    power,
    rbind,
    recolor,
    remove,
    sfilter,
    shift,
    size,
    subtract,
    toobject,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "234bbc79"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, F, T)
    x1 = order(x0, leftmost)
    x2 = astuple(ONE, TWO)
    x3 = rbind(contained, x2)
    x4 = lbind(compose, x3)
    x5 = lbind(rbind, colorcount)
    x6 = compose(x4, x5)
    x7 = lbind(sfilter, x0)
    x8 = chain(size, x7, x6)
    x9 = size(x0)
    x10 = matcher(x8, x9)
    x11 = palette(grid)
    x12 = sfilter(x11, x10)
    x13 = lbind(colorcount, grid)
    x14 = argmin(x12, x13)
    x15 = matcher(first, x14)
    x16 = rbind(extract, x15)
    x17 = compose(x16, first)
    x18 = fork(remove, x17, first)
    x19 = rbind(compose, initset)
    x20 = lbind(rbind, manhattan)
    x21 = compose(initset, x17)
    x22 = chain(x19, x20, x21)
    x23 = fork(argmin, x18, x22)
    x24 = compose(last, x17)
    x25 = compose(first, x23)
    x26 = fork(astuple, x25, x24)
    x27 = fork(insert, x26, x18)
    x28 = compose(last, last)
    x29 = rbind(argmin, x28)
    x30 = rbind(sfilter, x15)
    x31 = compose(first, last)
    x32 = chain(x29, x30, x31)
    x33 = compose(flip, x15)
    x34 = rbind(sfilter, x33)
    x35 = compose(first, last)
    x36 = fork(remove, x32, x35)
    x37 = compose(x34, x36)
    x38 = rbind(compose, initset)
    x39 = lbind(rbind, manhattan)
    x40 = compose(initset, x32)
    x41 = chain(x38, x39, x40)
    x42 = fork(argmin, x37, x41)
    x43 = compose(first, x42)
    x44 = compose(last, x32)
    x45 = fork(astuple, x43, x44)
    x46 = compose(first, last)
    x47 = fork(remove, x32, x46)
    x48 = fork(insert, x45, x47)
    x49 = rbind(shift, RIGHT)
    x50 = compose(last, x32)
    x51 = fork(subtract, x24, x50)
    x52 = fork(shift, x48, x51)
    x53 = compose(x49, x52)
    x54 = fork(combine, x27, x53)
    x55 = compose(first, last)
    x56 = fork(remove, x55, last)
    x57 = fork(astuple, x54, x56)
    x58 = size(x0)
    x59 = decrement(x58)
    x60 = power(x57, x59)
    x61 = first(x1)
    x62 = remove(x61, x1)
    x63 = astuple(x61, x62)
    x64 = x60(x63)
    x65 = first(x64)
    x66 = merge(x0)
    x67 = cover(grid, x66)
    x68 = paint(x67, x65)
    x69 = height(grid)
    x70 = width(x65)
    x71 = astuple(x69, x70)
    x72 = crop(x68, ORIGIN, x71)
    x73 = ofcolor(x72, x14)
    x74 = mostcolor(grid)
    x75 = palette(x72)
    x76 = contained(x14, x75)
    x77 = matcher(first, x74)
    x78 = compose(flip, x77)
    x79 = rbind(sfilter, x78)
    x80 = mapply(dneighbors, x73)
    x81 = lbind(toobject, x80)
    x82 = compose(x79, x81)
    x83 = rbind(recolor, x73)
    x84 = chain(x83, mostcolor, x82)
    x85 = fork(paint, identity, x84)
    x86 = branch(x76, x85, identity)
    x87 = x86(x72)
    return x87


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
