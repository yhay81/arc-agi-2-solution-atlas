"""Executable re-arc DSL program for ARC-AGI-2 task 673ef223.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    ONE,
    TWO,
    ZERO,
    F,
    T,
    add,
    apply,
    asindices,
    both,
    box,
    branch,
    chain,
    colorfilter,
    compose,
    connect,
    difference,
    either,
    extract,
    fill,
    first,
    fork,
    gravitate,
    greater,
    hfrontier,
    hmatching,
    identity,
    initset,
    last,
    lbind,
    mapply,
    matcher,
    merge,
    minimum,
    objects,
    ofcolor,
    other,
    palette,
    rbind,
    shift,
    size,
    subtract,
    toivec,
    tojvec,
    ulcorner,
    vfrontier,
    vmatching,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "673ef223"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = merge(x0)
    x2 = palette(x1)
    x3 = lbind(colorfilter, x0)
    x4 = compose(size, x3)
    x5 = matcher(x4, TWO)
    x6 = asindices(grid)
    x7 = box(x6)
    x8 = rbind(difference, x7)
    x9 = lbind(ofcolor, grid)
    x10 = chain(size, x8, x9)
    x11 = matcher(x10, ZERO)
    x12 = rbind(greater, ONE)
    x13 = lbind(apply, size)
    x14 = lbind(colorfilter, x0)
    x15 = compose(x13, x14)
    x16 = chain(x12, minimum, x15)
    x17 = fork(both, x11, x16)
    x18 = fork(both, x5, x17)
    x19 = extract(x2, x18)
    x20 = other(x2, x19)
    x21 = ofcolor(grid, x20)
    x22 = colorfilter(x0, x19)
    x23 = rbind(vmatching, x21)
    x24 = rbind(hmatching, x21)
    x25 = fork(either, x23, x24)
    x26 = extract(x22, x25)
    x27 = other(x22, x26)
    x28 = rbind(gravitate, x26)
    x29 = compose(x28, initset)
    x30 = fork(add, identity, x29)
    x31 = fork(connect, identity, x30)
    x32 = mapply(x31, x21)
    x33 = fill(grid, x20, x32)
    x34 = fill(x33, FOUR, x21)
    x35 = ofcolor(grid, x19)
    x36 = apply(first, x35)
    x37 = size(x36)
    x38 = apply(last, x35)
    x39 = size(x38)
    x40 = greater(x37, x39)
    x41 = compose(toivec, first)
    x42 = compose(tojvec, last)
    x43 = branch(x40, x41, x42)
    x44 = branch(x40, hfrontier, vfrontier)
    x45 = ulcorner(x26)
    x46 = ulcorner(x27)
    x47 = subtract(x46, x45)
    x48 = x43(x47)
    x49 = shift(x21, x48)
    x50 = mapply(x44, x49)
    x51 = fill(x34, x20, x50)
    x52 = fill(x51, x19, x35)
    return x52


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
