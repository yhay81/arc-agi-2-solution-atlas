"""Executable re-arc DSL program for ARC-AGI-2 task d8c310e9.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ZERO,
    apply,
    asobject,
    astuple,
    both,
    chain,
    cmirror,
    combine,
    compose,
    decrement,
    dedupe,
    extract,
    first,
    flip,
    fork,
    hperiod,
    identity,
    increment,
    index,
    initset,
    interval,
    last,
    lbind,
    mapply,
    matcher,
    paint,
    pair,
    rapply,
    rbind,
    rot90,
    rot180,
    rot270,
    sfilter,
    shift,
    size,
    tojvec,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d8c310e9"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = astuple(identity, rot90)
    x1 = astuple(rot180, rot270)
    x2 = combine(x0, x1)
    x3 = astuple(identity, rot270)
    x4 = astuple(rot180, rot90)
    x5 = combine(x3, x4)
    x6 = pair(x2, x5)
    x7 = chain(size, dedupe, first)
    x8 = matcher(x7, ONE)
    x9 = compose(first, cmirror)
    x10 = chain(size, dedupe, x9)
    x11 = matcher(x10, ONE)
    x12 = fork(both, x8, x11)
    x13 = rbind(rapply, grid)
    x14 = compose(initset, first)
    x15 = chain(first, x13, x14)
    x16 = compose(x12, x15)
    x17 = extract(x6, x16)
    x18 = first(x17)
    x19 = last(x17)
    x20 = x18(grid)
    x21 = width(x20)
    x22 = decrement(x21)
    x23 = tojvec(x22)
    x24 = index(x20, x23)
    x25 = asobject(x20)
    x26 = matcher(first, x24)
    x27 = compose(flip, x26)
    x28 = sfilter(x25, x27)
    x29 = hperiod(x28)
    x30 = width(x20)
    x31 = increment(x30)
    x32 = interval(ZERO, x31, x29)
    x33 = apply(tojvec, x32)
    x34 = lbind(shift, x28)
    x35 = mapply(x34, x33)
    x36 = paint(x20, x35)
    x37 = x19(x36)
    return x37


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
