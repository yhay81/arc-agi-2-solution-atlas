"""Executable re-arc DSL program for ARC-AGI-2 task 0e206a2e.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    F,
    T,
    apply,
    chain,
    cmirror,
    compose,
    cover,
    dmirror,
    first,
    flip,
    fork,
    hmirror,
    identity,
    invert,
    lbind,
    mapply,
    matcher,
    merge,
    mostcolor,
    normalize,
    numcolors,
    objects,
    occurrences,
    paint,
    rbind,
    rot90,
    rot180,
    rot270,
    sfilter,
    shift,
    ulcorner,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "0e206a2e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, F, T)
    x1 = matcher(numcolors, FOUR)
    x2 = sfilter(x0, x1)
    x3 = apply(normalize, x2)
    x4 = merge(x2)
    x5 = cover(grid, x4)
    x6 = lbind(compose, flip)
    x7 = lbind(matcher, first)
    x8 = chain(x6, x7, mostcolor)
    x9 = fork(sfilter, identity, x8)
    x10 = chain(invert, ulcorner, x9)
    x11 = lbind(lbind, shift)
    x12 = fork(shift, identity, x10)
    x13 = compose(x11, x12)
    x14 = lbind(fork, mapply)
    x15 = lbind(x14, x13)
    x16 = rbind(compose, x9)
    x17 = lbind(lbind, occurrences)
    x18 = chain(x15, x16, x17)
    x19 = rbind(mapply, x3)
    x20 = compose(x19, x18)
    x21 = fork(paint, identity, x20)
    x22 = chain(identity, x21, identity)
    x23 = chain(dmirror, x21, dmirror)
    x24 = chain(cmirror, x21, cmirror)
    x25 = chain(hmirror, x21, hmirror)
    x26 = chain(vmirror, x21, vmirror)
    x27 = chain(rot90, x21, rot270)
    x28 = chain(rot180, x21, rot180)
    x29 = chain(rot270, x21, rot90)
    x30 = chain(x29, x28, x27)
    x31 = chain(x26, x25, x24)
    x32 = compose(x23, x22)
    x33 = chain(x30, x31, x32)
    x34 = x33(x5)
    return x34


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
