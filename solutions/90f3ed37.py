"""Executable re-arc DSL program for ARC-AGI-2 task 90f3ed37.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ZERO,
    add,
    apply,
    argmax,
    asindices,
    astuple,
    center,
    chain,
    compose,
    contained,
    difference,
    double,
    fill,
    first,
    fork,
    greater,
    identity,
    increment,
    insert,
    intersection,
    interval,
    invert,
    lbind,
    leastcolor,
    leftmost,
    mapply,
    matcher,
    maximum,
    minimum,
    ofcolor,
    positive,
    rbind,
    remove,
    rightmost,
    sfilter,
    shift,
    size,
    toivec,
    tojvec,
    ulcorner,
    valmax,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "90f3ed37"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = ofcolor(grid, x0)
    x2 = apply(first, x1)
    x3 = asindices(grid)
    x4 = apply(first, x3)
    x5 = difference(x4, x2)
    x6 = ofcolor(grid, x0)
    x7 = rbind(interval, ONE)
    x8 = lbind(rbind, contained)
    x9 = lbind(sfilter, x5)
    x10 = rbind(matcher, ZERO)
    x11 = chain(size, x9, x8)
    x12 = lbind(sfilter, x6)
    x13 = lbind(compose, x11)
    x14 = chain(x12, x10, x13)
    x15 = lbind(fork, x7)
    x16 = compose(increment, minimum)
    x17 = lbind(lbind, astuple)
    x18 = lbind(chain, x16)
    x19 = rbind(x18, first)
    x20 = chain(x19, x17, first)
    x21 = lbind(chain, maximum)
    x22 = rbind(x21, first)
    x23 = chain(x22, x17, first)
    x24 = fork(x15, x20, x23)
    x25 = compose(x14, x24)
    x26 = apply(toivec, x2)
    x27 = apply(x25, x26)
    x28 = argmax(x27, width)
    x29 = remove(x28, x27)
    x30 = ulcorner(x28)
    x31 = invert(x30)
    x32 = shift(x28, x31)
    x33 = asindices(grid)
    x34 = center(x33)
    x35 = invert(x34)
    x36 = shift(x33, x35)
    x37 = width(grid)
    x38 = double(x37)
    x39 = tojvec(x38)
    x40 = rbind(apply, x36)
    x41 = lbind(rbind, add)
    x42 = chain(x40, x41, center)
    x43 = compose(positive, size)
    x44 = lbind(compose, size)
    x45 = lbind(shift, x32)
    x46 = rbind(compose, x45)
    x47 = lbind(rbind, intersection)
    x48 = compose(x46, x47)
    x49 = lbind(compose, x43)
    x50 = compose(x49, x48)
    x51 = fork(sfilter, x42, x50)
    x52 = compose(x44, x48)
    x53 = fork(valmax, x51, x52)
    x54 = compose(x44, x48)
    x55 = fork(matcher, x54, x53)
    x56 = fork(sfilter, x51, x55)
    x57 = lbind(shift, x32)
    x58 = lbind(insert, x39)
    x59 = lbind(rbind, greater)
    x60 = compose(x59, rightmost)
    x61 = compose(leftmost, x58)
    x62 = rbind(compose, x57)
    x63 = lbind(rbind, difference)
    x64 = compose(x62, x63)
    x65 = lbind(compose, x61)
    x66 = compose(x65, x64)
    x67 = fork(compose, x60, x66)
    x68 = fork(argmax, x56, x67)
    x69 = lbind(shift, x32)
    x70 = compose(x69, x68)
    x71 = fork(difference, x70, identity)
    x72 = mapply(x71, x29)
    x73 = fill(grid, ONE, x72)
    return x73


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
