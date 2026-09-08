"""Executable re-arc DSL program for ARC-AGI-2 task 6d58a25d.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    ONE,
    SIX,
    THREE,
    TWO,
    TWO_BY_TWO,
    UP,
    apply,
    argmin,
    astuple,
    chain,
    colorcount,
    combine,
    compose,
    connect,
    contained,
    decrement,
    extract,
    fill,
    first,
    fork,
    height,
    identity,
    increment,
    initset,
    insert,
    intersection,
    last,
    lbind,
    mapply,
    matcher,
    normalize,
    ofcolor,
    palette,
    partition,
    positive,
    rapply,
    rbind,
    remove,
    rot90,
    rot180,
    rot270,
    sfilter,
    shoot,
    size,
    toindices,
    toivec,
    tojvec,
    valmax,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "6d58a25d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = astuple(ONE, THREE)
    x1 = astuple(TWO, FOUR)
    x2 = initset(x1)
    x3 = insert(TWO_BY_TWO, x2)
    x4 = insert(x0, x3)
    x5 = tojvec(THREE)
    x6 = toivec(THREE)
    x7 = connect(x5, x6)
    x8 = astuple(THREE, SIX)
    x9 = connect(x5, x8)
    x10 = combine(x7, x9)
    x11 = combine(x4, x10)
    x12 = lbind(contained, x11)
    x13 = compose(normalize, toindices)
    x14 = lbind(apply, x13)
    x15 = chain(x12, x14, partition)
    x16 = astuple(identity, identity)
    x17 = astuple(rot90, rot270)
    x18 = astuple(x16, x17)
    x19 = astuple(rot180, rot180)
    x20 = astuple(rot270, rot90)
    x21 = astuple(x19, x20)
    x22 = combine(x18, x21)
    x23 = rbind(rapply, grid)
    x24 = compose(initset, first)
    x25 = chain(first, x23, x24)
    x26 = compose(x15, x25)
    x27 = extract(x22, x26)
    x28 = first(x27)
    x29 = last(x27)
    x30 = x28(grid)
    x31 = palette(grid)
    x32 = lbind(ofcolor, x30)
    x33 = compose(normalize, x32)
    x34 = matcher(x33, x11)
    x35 = extract(x31, x34)
    x36 = remove(x35, x31)
    x37 = lbind(colorcount, x30)
    x38 = argmin(x36, x37)
    x39 = ofcolor(x30, x38)
    x40 = ofcolor(x30, x35)
    x41 = compose(positive, size)
    x42 = rbind(intersection, x40)
    x43 = rbind(shoot, UP)
    x44 = chain(x41, x42, x43)
    x45 = sfilter(x39, x44)
    x46 = height(x30)
    x47 = rbind(valmax, first)
    x48 = lbind(sfilter, x40)
    x49 = lbind(matcher, last)
    x50 = chain(x48, x49, last)
    x51 = chain(increment, x47, x50)
    x52 = fork(astuple, x51, last)
    x53 = decrement(x46)
    x54 = lbind(astuple, x53)
    x55 = compose(x54, last)
    x56 = fork(connect, x52, x55)
    x57 = mapply(x56, x45)
    x58 = fill(x30, x38, x57)
    x59 = x29(x58)
    return x59


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
