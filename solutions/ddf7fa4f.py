"""Executable re-arc DSL program for ARC-AGI-2 task ddf7fa4f.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ORIGIN,
    TEN,
    ZERO,
    F,
    T,
    apply,
    argmax,
    asindices,
    astuple,
    box,
    chain,
    color,
    combine,
    compose,
    connect,
    decrement,
    difference,
    either,
    extract,
    first,
    flip,
    fork,
    height,
    hmatching,
    initset,
    intersection,
    last,
    lbind,
    mapply,
    matcher,
    mostcolor,
    objects,
    ofcolor,
    paint,
    power,
    rbind,
    recolor,
    sfilter,
    shape,
    size,
    sizefilter,
    subgrid,
    toindices,
    toivec,
    tojvec,
    toobject,
    vmatching,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "ddf7fa4f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = width(grid)
    x1 = decrement(x0)
    x2 = tojvec(x1)
    x3 = connect(ORIGIN, x2)
    x4 = height(grid)
    x5 = decrement(x4)
    x6 = toivec(x5)
    x7 = connect(ORIGIN, x6)
    x8 = width(grid)
    x9 = decrement(x8)
    x10 = tojvec(x9)
    x11 = shape(grid)
    x12 = decrement(x11)
    x13 = connect(x10, x12)
    x14 = height(grid)
    x15 = decrement(x14)
    x16 = toivec(x15)
    x17 = shape(grid)
    x18 = decrement(x17)
    x19 = connect(x16, x18)
    x20 = asindices(grid)
    x21 = box(x20)
    x22 = toobject(x21, grid)
    x23 = mostcolor(x22)
    x24 = matcher(color, x23)
    x25 = compose(flip, x24)
    x26 = rbind(sfilter, x25)
    x27 = rbind(sizefilter, ONE)
    x28 = rbind(objects, F)
    x29 = rbind(x28, F)
    x30 = rbind(x29, T)
    x31 = rbind(subgrid, grid)
    x32 = chain(x26, x30, x31)
    x33 = chain(size, x27, x32)
    x34 = astuple(x3, x7)
    x35 = astuple(x13, x19)
    x36 = combine(x34, x35)
    x37 = argmax(x36, x33)
    x38 = rbind(toobject, grid)
    x39 = compose(x38, initset)
    x40 = ofcolor(grid, x23)
    x41 = difference(x37, x40)
    x42 = apply(x39, x41)
    x43 = rbind(intersection, x37)
    x44 = chain(size, x43, toindices)
    x45 = matcher(x44, ZERO)
    x46 = objects(grid, T, F, T)
    x47 = sfilter(x46, x45)
    x48 = lbind(fork, either)
    x49 = lbind(lbind, hmatching)
    x50 = lbind(lbind, vmatching)
    x51 = fork(x48, x49, x50)
    x52 = lbind(chain, size)
    x53 = rbind(x52, x51)
    x54 = lbind(lbind, sfilter)
    x55 = compose(last, last)
    x56 = chain(x53, x54, x55)
    x57 = rbind(compose, x51)
    x58 = lbind(lbind, extract)
    x59 = compose(last, last)
    x60 = chain(x57, x58, x59)
    x61 = compose(first, last)
    x62 = rbind(matcher, ONE)
    x63 = compose(x62, x56)
    x64 = fork(sfilter, x61, x63)
    x65 = lbind(fork, recolor)
    x66 = lbind(x65, color)
    x67 = compose(x66, x60)
    x68 = fork(mapply, x67, x64)
    x69 = fork(combine, first, x68)
    x70 = compose(first, last)
    x71 = fork(difference, x70, x64)
    x72 = compose(last, last)
    x73 = fork(apply, x60, x64)
    x74 = fork(difference, x72, x73)
    x75 = fork(astuple, x71, x74)
    x76 = fork(astuple, x69, x75)
    x77 = difference(x42, x42)
    x78 = power(x76, TEN)
    x79 = astuple(x42, x47)
    x80 = astuple(x77, x79)
    x81 = x78(x80)
    x82 = first(x81)
    x83 = paint(grid, x82)
    return x83


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
