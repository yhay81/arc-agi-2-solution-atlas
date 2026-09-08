"""Executable re-arc DSL program for ARC-AGI-2 task 2dd70a9a.

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
    RIGHT,
    THREE,
    TWO,
    UP,
    F,
    T,
    add,
    adjacent,
    apply,
    both,
    branch,
    center,
    chain,
    colorfilter,
    combine,
    compose,
    connect,
    corners,
    difference,
    dmirror,
    either,
    equality,
    extract,
    fill,
    first,
    fork,
    hfrontier,
    hline,
    identity,
    index,
    last,
    lbind,
    mapply,
    matcher,
    mfilter,
    mostcolor,
    numcolors,
    objects,
    ofcolor,
    other,
    palette,
    product,
    rbind,
    remove,
    replace,
    sfilter,
    toindices,
    toobject,
    underfill,
    vline,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "2dd70a9a"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = ofcolor(grid, TWO)
    x1 = vline(x0)
    x2 = branch(x1, dmirror, identity)
    x3 = x2(grid)
    x4 = ofcolor(x3, THREE)
    x5 = ofcolor(x3, TWO)
    x6 = center(x4)
    x7 = hfrontier(x6)
    x8 = center(x5)
    x9 = hfrontier(x8)
    x10 = mostcolor(grid)
    x11 = palette(grid)
    x12 = remove(THREE, x11)
    x13 = remove(TWO, x12)
    x14 = other(x13, x10)
    x15 = replace(x3, THREE, x10)
    x16 = difference(x7, x4)
    x17 = underfill(x15, THREE, x16)
    x18 = replace(x3, TWO, x10)
    x19 = difference(x9, x5)
    x20 = underfill(x18, TWO, x19)
    x21 = objects(x17, T, F, F)
    x22 = colorfilter(x21, THREE)
    x23 = rbind(adjacent, x4)
    x24 = sfilter(x22, x23)
    x25 = objects(x20, T, F, F)
    x26 = colorfilter(x25, TWO)
    x27 = rbind(adjacent, x5)
    x28 = sfilter(x26, x27)
    x29 = mapply(toindices, x24)
    x30 = rbind(equality, x14)
    x31 = lbind(index, x3)
    x32 = compose(x30, x31)
    x33 = rbind(add, LEFT)
    x34 = compose(x32, x33)
    x35 = rbind(add, RIGHT)
    x36 = compose(x32, x35)
    x37 = fork(either, x34, x36)
    x38 = rbind(add, UP)
    x39 = compose(x32, x38)
    x40 = rbind(add, DOWN)
    x41 = compose(x32, x40)
    x42 = fork(either, x39, x41)
    x43 = sfilter(x29, x37)
    x44 = mapply(toindices, x28)
    x45 = sfilter(x44, x42)
    x46 = fork(connect, first, last)
    x47 = product(x43, x45)
    x48 = compose(vline, x46)
    x49 = rbind(toobject, x3)
    x50 = chain(numcolors, x49, x46)
    x51 = matcher(x50, ONE)
    x52 = fork(both, x48, x51)
    x53 = extract(x47, x52)
    x54 = x46(x53)
    x55 = center(x4)
    x56 = center(x5)
    x57 = fork(either, hline, vline)
    x58 = lbind(connect, x55)
    x59 = corners(x54)
    x60 = apply(x58, x59)
    x61 = mfilter(x60, x57)
    x62 = lbind(connect, x56)
    x63 = corners(x54)
    x64 = apply(x62, x63)
    x65 = mfilter(x64, x57)
    x66 = combine(x61, x65)
    x67 = combine(x54, x66)
    x68 = fill(x3, THREE, x67)
    x69 = fill(x68, TWO, x5)
    x70 = x2(x69)
    return x70


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
