"""Executable re-arc DSL program for ARC-AGI-2 task 3ac3eb23.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    TWO,
    ZERO,
    F,
    T,
    apply,
    astuple,
    center,
    chain,
    cmirror,
    color,
    combine,
    compose,
    decrement,
    dmirror,
    extract,
    fgpartition,
    first,
    fork,
    height,
    hmirror,
    identity,
    increment,
    initset,
    interval,
    last,
    lbind,
    lowermost,
    mapply,
    matcher,
    merge,
    objects,
    paint,
    rapply,
    rbind,
    recolor,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "3ac3eb23"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = astuple(identity, dmirror)
    x1 = astuple(cmirror, hmirror)
    x2 = combine(x0, x1)
    x3 = chain(lowermost, merge, fgpartition)
    x4 = rbind(rapply, grid)
    x5 = lbind(compose, x3)
    x6 = compose(initset, x5)
    x7 = chain(first, x4, x6)
    x8 = matcher(x7, ZERO)
    x9 = extract(x2, x8)
    x10 = x9(grid)
    x11 = objects(x10, T, F, T)
    x12 = height(x10)
    x13 = interval(ZERO, x12, TWO)
    x14 = height(x10)
    x15 = interval(ONE, x14, TWO)
    x16 = rbind(apply, x13)
    x17 = lbind(rbind, astuple)
    x18 = chain(x16, x17, last)
    x19 = rbind(apply, x15)
    x20 = lbind(rbind, astuple)
    x21 = compose(increment, last)
    x22 = chain(x19, x20, x21)
    x23 = rbind(apply, x15)
    x24 = lbind(rbind, astuple)
    x25 = compose(decrement, last)
    x26 = chain(x23, x24, x25)
    x27 = fork(combine, x18, x22)
    x28 = fork(combine, x27, x26)
    x29 = compose(x28, center)
    x30 = fork(recolor, color, x29)
    x31 = mapply(x30, x11)
    x32 = paint(x10, x31)
    x33 = x9(x32)
    return x33


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
