"""Executable re-arc DSL program for ARC-AGI-2 task d22278a0.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NEG_ONE,
    ONE,
    TEN,
    TWO,
    F,
    T,
    add,
    apply,
    asindices,
    astuple,
    center,
    chain,
    color,
    combine,
    compose,
    first,
    fork,
    greater,
    halve,
    identity,
    initset,
    intersection,
    interval,
    last,
    lbind,
    manhattan,
    mapply,
    maximum,
    merge,
    minimum,
    multiply,
    objects,
    outbox,
    paint,
    pair,
    power,
    rapply,
    rbind,
    recolor,
    remove,
    repeat,
    sfilter,
    shape,
    totuple,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d22278a0"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = totuple(x0)
    x2 = apply(color, x1)
    x3 = repeat(NEG_ONE, ONE)
    x4 = combine(x2, x3)
    x5 = multiply(TEN, TEN)
    x6 = apply(center, x1)
    x7 = astuple(x5, x5)
    x8 = repeat(x7, ONE)
    x9 = combine(x6, x8)
    x10 = identity(grid)
    x11 = asindices(grid)
    x12 = shape(grid)
    x13 = maximum(x12)
    x14 = halve(x13)
    x15 = add(TWO, x14)
    x16 = interval(ONE, x15, ONE)
    x17 = compose(outbox, outbox)
    x18 = lbind(power, x17)
    x19 = apply(x18, x16)
    x20 = lbind(rapply, x19)
    x21 = chain(merge, x20, initset)
    x22 = fork(combine, initset, x21)
    x23 = lbind(rbind, manhattan)
    x24 = rbind(chain, initset)
    x25 = rbind(x24, x23)
    x26 = lbind(rbind, apply)
    x27 = lbind(apply, initset)
    x28 = rbind(remove, x9)
    x29 = chain(x25, x26, x27)
    x30 = chain(x29, x28, last)
    x31 = lbind(sfilter, x11)
    x32 = rbind(compose, initset)
    x33 = lbind(compose, minimum)
    x34 = lbind(fork, greater)
    x35 = compose(x33, x30)
    x36 = compose(initset, last)
    x37 = chain(x32, x23, x36)
    x38 = fork(x34, x35, x37)
    x39 = compose(x31, x38)
    x40 = compose(x22, last)
    x41 = fork(intersection, x39, x40)
    x42 = fork(recolor, first, x41)
    x43 = pair(x4, x9)
    x44 = mapply(x42, x43)
    x45 = paint(x10, x44)
    return x45


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
