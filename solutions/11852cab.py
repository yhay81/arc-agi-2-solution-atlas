"""Executable re-arc DSL program for ARC-AGI-2 task 11852cab.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FIVE,
    FOUR,
    ONE,
    SEVEN,
    THREE,
    UNITY,
    ZERO,
    add,
    asindices,
    backdrop,
    both,
    box,
    canvas,
    center,
    chain,
    cmirror,
    combine,
    compose,
    crop,
    decrement,
    dmirror,
    even,
    fgpartition,
    first,
    flip,
    fork,
    height,
    hmirror,
    identity,
    inbox,
    initset,
    insert,
    interval,
    last,
    lbind,
    mapply,
    matcher,
    merge,
    minimum,
    mostcolor,
    multiply,
    paint,
    palette,
    positive,
    product,
    rbind,
    remove,
    sfilter,
    shape,
    size,
    subtract,
    toobject,
    trim,
    vmirror,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "11852cab"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = lbind(remove, x0)
    x2 = chain(positive, size, x1)
    x3 = compose(x2, palette)
    x4 = multiply(FIVE, UNITY)
    x5 = canvas(ZERO, x4)
    x6 = asindices(x5)
    x7 = fork(add, first, last)
    x8 = chain(flip, even, x7)
    x9 = sfilter(x6, x8)
    x10 = initset(x0)
    x11 = box(x6)
    x12 = inbox(x6)
    x13 = center(x6)
    x14 = initset(x13)
    x15 = lbind(toobject, x11)
    x16 = compose(x3, x15)
    x17 = lbind(toobject, x12)
    x18 = compose(x3, x17)
    x19 = lbind(toobject, x14)
    x20 = compose(x3, x19)
    x21 = fork(both, x18, x20)
    x22 = fork(both, x16, x21)
    x23 = compose(x22, trim)
    x24 = compose(box, asindices)
    x25 = fork(toobject, x24, identity)
    x26 = compose(palette, x25)
    x27 = matcher(x26, x10)
    x28 = lbind(toobject, x9)
    x29 = chain(palette, x28, trim)
    x30 = matcher(x29, x10)
    x31 = compose(minimum, shape)
    x32 = chain(x31, merge, fgpartition)
    x33 = matcher(x32, FIVE)
    x34 = fork(both, x23, x27)
    x35 = fork(both, x30, x33)
    x36 = fork(both, x34, x35)
    x37 = height(grid)
    x38 = subtract(x37, THREE)
    x39 = interval(ONE, x38, ONE)
    x40 = width(grid)
    x41 = subtract(x40, THREE)
    x42 = interval(ONE, x41, ONE)
    x43 = multiply(SEVEN, UNITY)
    x44 = lbind(crop, grid)
    x45 = rbind(x44, x43)
    x46 = chain(x36, x45, decrement)
    x47 = product(x39, x42)
    x48 = sfilter(x47, x46)
    x49 = matcher(first, x0)
    x50 = compose(flip, x49)
    x51 = rbind(sfilter, x50)
    x52 = compose(x51, dmirror)
    x53 = fork(combine, x51, x52)
    x54 = compose(x51, cmirror)
    x55 = compose(x51, hmirror)
    x56 = compose(x51, vmirror)
    x57 = fork(combine, x55, x56)
    x58 = fork(combine, x54, x57)
    x59 = fork(combine, x53, x58)
    x60 = multiply(FOUR, UNITY)
    x61 = rbind(add, x60)
    x62 = fork(insert, x61, initset)
    x63 = compose(backdrop, x62)
    x64 = rbind(toobject, grid)
    x65 = chain(x59, x64, x63)
    x66 = mapply(x65, x48)
    x67 = paint(grid, x66)
    return x67


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
