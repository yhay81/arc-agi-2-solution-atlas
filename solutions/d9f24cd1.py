"""Executable re-arc DSL program for ARC-AGI-2 task d9f24cd1.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    TWO,
    UNITY,
    UP,
    F,
    T,
    apply,
    asindices,
    astuple,
    box,
    chain,
    colorfilter,
    combine,
    compose,
    connect,
    dedupe,
    difference,
    extract,
    fill,
    first,
    greater,
    identity,
    initset,
    last,
    mapply,
    matcher,
    mfilter,
    mostcolor,
    numcolors,
    objects,
    ofcolor,
    other,
    palette,
    prapply,
    rapply,
    rbind,
    rot90,
    rot180,
    rot270,
    sfilter,
    shift,
    shoot,
    size,
    toindices,
    toobject,
    trim,
    underfill,
    urcorner,
    vfrontier,
    vline,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d9f24cd1"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = astuple(identity, identity)
    x1 = astuple(rot90, rot270)
    x2 = astuple(x0, x1)
    x3 = astuple(rot180, rot180)
    x4 = astuple(rot270, rot90)
    x5 = astuple(x3, x4)
    x6 = combine(x2, x5)
    x7 = rbind(greater, ONE)
    x8 = chain(size, dedupe, last)
    x9 = compose(x7, x8)
    x10 = rbind(rapply, grid)
    x11 = compose(initset, first)
    x12 = chain(first, x10, x11)
    x13 = compose(x9, x12)
    x14 = extract(x6, x13)
    x15 = first(x14)
    x16 = last(x14)
    x17 = x15(grid)
    x18 = mostcolor(grid)
    x19 = trim(grid)
    x20 = palette(x19)
    x21 = other(x20, x18)
    x22 = asindices(grid)
    x23 = box(x22)
    x24 = toobject(x23, grid)
    x25 = palette(x24)
    x26 = other(x25, x18)
    x27 = ofcolor(x17, x26)
    x28 = ofcolor(x17, x21)
    x29 = prapply(connect, x27, x28)
    x30 = mfilter(x29, vline)
    x31 = underfill(x17, x26, x30)
    x32 = matcher(numcolors, TWO)
    x33 = objects(x31, F, F, T)
    x34 = sfilter(x33, x32)
    x35 = difference(x33, x34)
    x36 = colorfilter(x35, x26)
    x37 = mapply(toindices, x36)
    x38 = apply(urcorner, x34)
    x39 = shift(x38, UNITY)
    x40 = rbind(shoot, UP)
    x41 = mapply(x40, x39)
    x42 = fill(x31, x26, x41)
    x43 = mapply(vfrontier, x37)
    x44 = fill(x42, x26, x43)
    x45 = x16(x44)
    return x45


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
