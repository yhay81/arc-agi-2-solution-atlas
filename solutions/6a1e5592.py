"""Executable re-arc DSL program for ARC-AGI-2 task 6a1e5592.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    ONE,
    ORIGIN,
    ZERO,
    T,
    add,
    argmax,
    argmin,
    asobject,
    astuple,
    both,
    chain,
    cmirror,
    color,
    colorfilter,
    combine,
    compose,
    cover,
    decrement,
    difference,
    dmirror,
    dneighbors,
    fill,
    first,
    flip,
    fork,
    greater,
    height,
    hmirror,
    identity,
    initset,
    intersection,
    lbind,
    lowermost,
    mapply,
    matcher,
    merge,
    mostcolor,
    neighbors,
    normalize,
    numcolors,
    objects,
    ofcolor,
    other,
    palette,
    rapply,
    rbind,
    remove,
    sfilter,
    shift,
    size,
    toindices,
    vsplit,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "6a1e5592"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = astuple(identity, dmirror)
    x1 = astuple(cmirror, hmirror)
    x2 = combine(x0, x1)
    x3 = fork(vsplit, identity, height)
    x4 = chain(asobject, first, x3)
    x5 = mostcolor(grid)
    x6 = lbind(chain, numcolors)
    x7 = lbind(x6, x4)
    x8 = lbind(chain, color)
    x9 = lbind(x8, x4)
    x10 = rbind(rapply, grid)
    x11 = compose(initset, x7)
    x12 = chain(first, x10, x11)
    x13 = rbind(rapply, grid)
    x14 = compose(initset, x9)
    x15 = chain(first, x13, x14)
    x16 = matcher(x12, ONE)
    x17 = matcher(x15, x5)
    x18 = compose(flip, x17)
    x19 = fork(both, x16, x18)
    x20 = argmax(x2, x19)
    x21 = x20(grid)
    x22 = x4(x21)
    x23 = color(x22)
    x24 = palette(x21)
    x25 = remove(x23, x24)
    x26 = other(x25, x5)
    x27 = objects(x21, T, T, T)
    x28 = colorfilter(x27, x26)
    x29 = ofcolor(x21, x23)
    x30 = ofcolor(x21, x5)
    x31 = mapply(neighbors, x30)
    x32 = mapply(neighbors, x31)
    x33 = lowermost(x29)
    x34 = dneighbors(ORIGIN)
    x35 = remove(DOWN, x34)
    x36 = rbind(mapply, x35)
    x37 = lbind(chain, x36)
    x38 = lbind(lbind, add)
    x39 = rbind(x37, x38)
    x40 = lbind(lbind, compose)
    x41 = lbind(lbind, shift)
    x42 = chain(x39, x40, x41)
    x43 = lbind(chain, size)
    x44 = rbind(intersection, x29)
    x45 = lbind(x43, x44)
    x46 = rbind(matcher, ZERO)
    x47 = lbind(lbind, shift)
    x48 = chain(x46, x45, x47)
    x49 = rbind(chain, first)
    x50 = rbind(x49, decrement)
    x51 = lbind(greater, x33)
    x52 = x50(x51)
    x53 = rbind(sfilter, x52)
    x54 = lbind(compose, x53)
    x55 = lbind(chain, size)
    x56 = rbind(difference, x30)
    x57 = lbind(x55, x56)
    x58 = rbind(matcher, ZERO)
    x59 = lbind(lbind, shift)
    x60 = chain(x58, x57, x59)
    x61 = lbind(chain, size)
    x62 = rbind(intersection, x30)
    x63 = lbind(x61, x62)
    x64 = lbind(fork, difference)
    x65 = compose(x54, x42)
    x66 = lbind(lbind, shift)
    x67 = fork(x64, x65, x66)
    x68 = compose(x63, x67)
    x69 = rbind(matcher, ZERO)
    x70 = compose(x69, x68)
    x71 = lbind(fork, both)
    x72 = fork(x71, x70, x60)
    x73 = lbind(fork, both)
    x74 = fork(x73, x48, x72)
    x75 = compose(normalize, toindices)
    x76 = lbind(sfilter, x32)
    x77 = chain(x76, x74, x75)
    x78 = rbind(argmin, first)
    x79 = compose(x78, x77)
    x80 = fork(shift, x75, x79)
    x81 = mapply(x80, x28)
    x82 = merge(x28)
    x83 = cover(x21, x82)
    x84 = fill(x83, ONE, x81)
    x85 = x20(x84)
    return x85


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
