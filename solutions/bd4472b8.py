"""Executable re-arc DSL program for ARC-AGI-2 task bd4472b8.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    TWO_BY_ZERO,
    ZERO,
    apply,
    asobject,
    astuple,
    both,
    chain,
    combine,
    compose,
    dedupe,
    dmirror,
    extract,
    first,
    fork,
    frontiers,
    greater,
    height,
    hline,
    hupscale,
    identity,
    initset,
    interval,
    last,
    lbind,
    mapply,
    paint,
    pair,
    positive,
    rapply,
    rbind,
    repeat,
    rot90,
    rot180,
    rot270,
    sfilter,
    shift,
    size,
    toivec,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "bd4472b8"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = compose(positive, size)
    x1 = rbind(sfilter, hline)
    x2 = chain(x0, x1, frontiers)
    x3 = chain(size, dedupe, first)
    x4 = chain(size, dedupe, last)
    x5 = fork(greater, x3, x4)
    x6 = fork(both, x2, x5)
    x7 = astuple(identity, rot90)
    x8 = astuple(rot180, rot270)
    x9 = combine(x7, x8)
    x10 = astuple(identity, rot270)
    x11 = astuple(rot180, rot90)
    x12 = combine(x10, x11)
    x13 = pair(x9, x12)
    x14 = rbind(rapply, grid)
    x15 = compose(initset, first)
    x16 = chain(first, x14, x15)
    x17 = compose(x6, x16)
    x18 = extract(x13, x17)
    x19 = first(x18)
    x20 = last(x18)
    x21 = x19(grid)
    x22 = first(x21)
    x23 = repeat(x22, ONE)
    x24 = dmirror(x23)
    x25 = width(x21)
    x26 = hupscale(x24, x25)
    x27 = asobject(x26)
    x28 = height(x21)
    x29 = height(x27)
    x30 = interval(ZERO, x28, x29)
    x31 = lbind(shift, x27)
    x32 = apply(toivec, x30)
    x33 = mapply(x31, x32)
    x34 = shift(x33, TWO_BY_ZERO)
    x35 = paint(x21, x34)
    x36 = x20(x35)
    return x36


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
