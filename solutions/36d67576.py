"""Executable re-arc DSL program for ARC-AGI-2 task 36d67576.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ZERO,
    F,
    T,
    apply,
    argmax,
    astuple,
    branch,
    chain,
    cmirror,
    combine,
    compose,
    contained,
    dmirror,
    equality,
    first,
    fork,
    hmirror,
    identity,
    initset,
    invert,
    last,
    lbind,
    mapply,
    merge,
    objects,
    occurrences,
    paint,
    palette,
    product,
    rapply,
    rbind,
    remove,
    repeat,
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

TASK_ID = "36d67576"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, T, T)
    x1 = argmax(x0, size)
    x2 = remove(x1, x0)
    x3 = merge(x2)
    x4 = palette(x3)
    x5 = repeat(identity, ONE)
    x6 = astuple(cmirror, dmirror)
    x7 = astuple(vmirror, hmirror)
    x8 = combine(x6, x7)
    x9 = combine(x5, x8)
    x10 = fork(compose, first, last)
    x11 = product(x9, x9)
    x12 = apply(x10, x11)
    x13 = rbind(contained, x4)
    x14 = compose(x13, first)
    x15 = rbind(sfilter, x14)
    x16 = lbind(chain, ulcorner)
    x17 = lbind(x16, x15)
    x18 = lbind(fork, shift)
    x19 = lbind(lbind, shift)
    x20 = lbind(occurrences, grid)
    x21 = rbind(rapply, x1)
    x22 = chain(first, x21, initset)
    x23 = lbind(compose, invert)
    x24 = compose(x23, x17)
    x25 = lbind(compose, x15)
    x26 = fork(x18, x25, x24)
    x27 = compose(x22, x26)
    x28 = rbind(rapply, x1)
    x29 = chain(first, x28, initset)
    x30 = rbind(rapply, x1)
    x31 = compose(initset, x17)
    x32 = chain(first, x30, x31)
    x33 = compose(invert, x32)
    x34 = fork(shift, x29, x33)
    x35 = compose(x19, x34)
    x36 = compose(x20, x27)
    x37 = fork(mapply, x35, x36)
    x38 = rbind(astuple, x37)
    x39 = compose(last, x38)
    x40 = rbind(astuple, x12)
    x41 = compose(last, x40)
    x42 = fork(mapply, x39, x41)
    x43 = fork(paint, identity, x42)
    x44 = rbind(contained, x4)
    x45 = compose(x44, first)
    x46 = sfilter(x1, x45)
    x47 = size(x46)
    x48 = equality(x47, ZERO)
    x49 = branch(x48, identity, x43)
    x50 = x49(grid)
    return x50


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
