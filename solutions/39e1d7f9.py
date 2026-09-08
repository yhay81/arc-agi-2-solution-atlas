"""Executable re-arc DSL program for ARC-AGI-2 task 39e1d7f9.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ORIGIN,
    ZERO,
    F,
    T,
    apply,
    argmax,
    astuple,
    branch,
    chain,
    color,
    colorfilter,
    compose,
    compress,
    crop,
    divide,
    equality,
    first,
    fork,
    frontiers,
    height,
    hline,
    hupscale,
    identity,
    increment,
    initset,
    interval,
    invert,
    last,
    lbind,
    leastcolor,
    mapply,
    matcher,
    merge,
    multiply,
    normalize,
    numcolors,
    objects,
    paint,
    pair,
    positive,
    rapply,
    rbind,
    remove,
    sfilter,
    shape,
    shift,
    size,
    ulcorner,
    vline,
    vupscale,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "39e1d7f9"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = compress(grid)
    x1 = objects(x0, F, F, T)
    x2 = argmax(x1, numcolors)
    x3 = remove(x2, x1)
    x4 = merge(x3)
    x5 = size(x4)
    x6 = positive(x5)
    x7 = astuple(color, x4)
    x8 = astuple(leastcolor, x2)
    x9 = branch(x6, x7, x8)
    x10 = compose(initset, first)
    x11 = fork(rapply, x10, last)
    x12 = compose(first, x11)
    x13 = x12(x9)
    x14 = normalize(x2)
    x15 = matcher(first, x13)
    x16 = sfilter(x14, x15)
    x17 = ulcorner(x16)
    x18 = invert(x17)
    x19 = shift(x14, x18)
    x20 = lbind(shift, x19)
    x21 = objects(x0, T, F, T)
    x22 = colorfilter(x21, x13)
    x23 = apply(ulcorner, x22)
    x24 = mapply(x20, x23)
    x25 = paint(x0, x24)
    x26 = height(x0)
    x27 = frontiers(grid)
    x28 = sfilter(x27, hline)
    x29 = size(x28)
    x30 = increment(x29)
    x31 = divide(x26, x30)
    x32 = width(x0)
    x33 = frontiers(grid)
    x34 = sfilter(x33, vline)
    x35 = size(x34)
    x36 = increment(x35)
    x37 = divide(x32, x36)
    x38 = rbind(multiply, x37)
    x39 = rbind(divide, x37)
    x40 = compose(x38, x39)
    x41 = fork(equality, x40, identity)
    x42 = compose(x41, first)
    x43 = rbind(multiply, x31)
    x44 = rbind(divide, x31)
    x45 = compose(x43, x44)
    x46 = fork(equality, x45, identity)
    x47 = compose(x46, first)
    x48 = lbind(interval, ZERO)
    x49 = rbind(x48, ONE)
    x50 = compose(x49, size)
    x51 = fork(pair, x50, identity)
    x52 = lbind(apply, last)
    x53 = rbind(sfilter, x42)
    x54 = chain(x52, x53, x51)
    x55 = compose(x54, last)
    x56 = height(x25)
    x57 = interval(ZERO, x56, ONE)
    x58 = pair(x57, x25)
    x59 = sfilter(x58, x47)
    x60 = apply(x55, x59)
    x61 = increment(x37)
    x62 = hupscale(x60, x61)
    x63 = increment(x31)
    x64 = vupscale(x62, x63)
    x65 = frontiers(grid)
    x66 = merge(x65)
    x67 = paint(x64, x66)
    x68 = shape(grid)
    x69 = crop(x67, ORIGIN, x68)
    return x69


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
