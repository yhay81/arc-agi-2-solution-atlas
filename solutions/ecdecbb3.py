"""Executable re-arc DSL program for ARC-AGI-2 task ecdecbb3.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NEG_ONE,
    F,
    T,
    add,
    argmin,
    astuple,
    backdrop,
    branch,
    colorfilter,
    compose,
    connect,
    contained,
    crement,
    extract,
    fill,
    first,
    fork,
    frontiers,
    gravitate,
    height,
    hfrontier,
    hline,
    identity,
    initset,
    insert,
    intersection,
    lbind,
    leastcolor,
    manhattan,
    mapply,
    merge,
    neighbors,
    objects,
    ofcolor,
    other,
    palette,
    positive,
    rapply,
    rbind,
    remove,
    sfilter,
    size,
    toivec,
    tojvec,
    vfrontier,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "ecdecbb3"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = objects(grid, T, F, T)
    x2 = merge(x1)
    x3 = palette(x2)
    x4 = other(x3, x0)
    x5 = ofcolor(grid, x0)
    x6 = frontiers(grid)
    x7 = colorfilter(x6, x4)
    x8 = sfilter(x7, hline)
    x9 = size(x8)
    x10 = positive(x9)
    x11 = height(grid)
    x12 = toivec(x11)
    x13 = hfrontier(x12)
    x14 = toivec(NEG_ONE)
    x15 = hfrontier(x14)
    x16 = insert(x15, x7)
    x17 = insert(x13, x16)
    x18 = width(grid)
    x19 = tojvec(x18)
    x20 = vfrontier(x19)
    x21 = tojvec(NEG_ONE)
    x22 = vfrontier(x21)
    x23 = insert(x22, x7)
    x24 = insert(x20, x23)
    x25 = branch(x10, x17, x24)
    x26 = lbind(argmin, x25)
    x27 = lbind(rbind, manhattan)
    x28 = compose(x27, initset)
    x29 = compose(x26, x28)
    x30 = rbind(remove, x25)
    x31 = compose(x30, x29)
    x32 = fork(argmin, x31, x28)
    x33 = fork(gravitate, initset, x29)
    x34 = compose(crement, x33)
    x35 = fork(add, identity, x34)
    x36 = fork(gravitate, initset, x32)
    x37 = compose(crement, x36)
    x38 = fork(add, identity, x37)
    x39 = ofcolor(grid, x4)
    x40 = backdrop(x39)
    x41 = fork(connect, x35, x38)
    x42 = rbind(contained, x40)
    x43 = rbind(extract, x42)
    x44 = fork(astuple, x35, x38)
    x45 = compose(x43, x44)
    x46 = fork(connect, identity, x45)
    x47 = rbind(branch, x46)
    x48 = rbind(x47, x41)
    x49 = rbind(contained, x40)
    x50 = compose(x48, x49)
    x51 = compose(initset, x50)
    x52 = fork(rapply, x51, identity)
    x53 = compose(first, x52)
    x54 = mapply(x53, x5)
    x55 = fill(grid, x0, x54)
    x56 = intersection(x39, x54)
    x57 = mapply(neighbors, x56)
    x58 = fill(x55, x4, x57)
    return x58


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
