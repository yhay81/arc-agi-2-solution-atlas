"""Executable re-arc DSL program for ARC-AGI-2 task 3e980e27.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    THREE,
    TWO,
    F,
    T,
    add,
    apply,
    argmax,
    branch,
    center,
    chain,
    compose,
    contained,
    first,
    fork,
    identity,
    invert,
    lbind,
    mapply,
    matcher,
    normalize,
    numcolors,
    objects,
    ofcolor,
    paint,
    palette,
    positive,
    rbind,
    remove,
    sfilter,
    shift,
    size,
    ulcorner,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "3e980e27"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = ofcolor(grid, THREE)
    x1 = ofcolor(grid, TWO)
    x2 = matcher(first, THREE)
    x3 = matcher(first, TWO)
    x4 = rbind(objects, T)
    x5 = rbind(x4, T)
    x6 = rbind(x5, F)
    x7 = lbind(contained, THREE)
    x8 = compose(x7, palette)
    x9 = lbind(contained, TWO)
    x10 = compose(x9, palette)
    x11 = rbind(sfilter, x8)
    x12 = compose(x11, x6)
    x13 = rbind(sfilter, x10)
    x14 = compose(x13, x6)
    x15 = rbind(argmax, numcolors)
    x16 = chain(normalize, x15, x12)
    x17 = rbind(argmax, numcolors)
    x18 = compose(x17, x14)
    x19 = chain(normalize, vmirror, x18)
    x20 = rbind(sfilter, x2)
    x21 = chain(ulcorner, x20, x16)
    x22 = rbind(sfilter, x3)
    x23 = chain(ulcorner, x22, x19)
    x24 = rbind(sfilter, x3)
    x25 = chain(center, x24, x18)
    x26 = lbind(lbind, shift)
    x27 = compose(x26, x16)
    x28 = lbind(lbind, shift)
    x29 = compose(x28, x19)
    x30 = rbind(apply, x0)
    x31 = lbind(lbind, add)
    x32 = compose(invert, x21)
    x33 = chain(x30, x31, x32)
    x34 = rbind(remove, x1)
    x35 = compose(x34, x25)
    x36 = lbind(lbind, add)
    x37 = chain(x36, invert, x23)
    x38 = fork(apply, x37, x35)
    x39 = fork(mapply, x27, x33)
    x40 = fork(mapply, x29, x38)
    x41 = fork(paint, identity, x39)
    x42 = fork(paint, identity, x40)
    x43 = size(x0)
    x44 = positive(x43)
    x45 = size(x1)
    x46 = positive(x45)
    x47 = branch(x44, x41, identity)
    x48 = branch(x46, x42, identity)
    x49 = compose(x47, x48)
    x50 = x49(grid)
    return x50


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
