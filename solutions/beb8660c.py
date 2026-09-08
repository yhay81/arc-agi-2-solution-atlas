"""Executable re-arc DSL program for ARC-AGI-2 task beb8660c.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    ONE,
    ZERO,
    apply,
    argmax,
    astuple,
    canvas,
    chain,
    color,
    combine,
    compose,
    extract,
    first,
    flip,
    identity,
    initset,
    interval,
    invert,
    last,
    lbind,
    lowermost,
    matcher,
    mpapply,
    normalize,
    ofcolor,
    order,
    paint,
    pair,
    palette,
    partition,
    rapply,
    rbind,
    rot90,
    rot180,
    rot270,
    sfilter,
    shape,
    shift,
    size,
    toivec,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "beb8660c"
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
    x7 = rbind(rapply, grid)
    x8 = compose(initset, first)
    x9 = chain(first, x7, x8)
    x10 = rbind(ofcolor, EIGHT)
    x11 = chain(lowermost, x10, x9)
    x12 = matcher(x11, ZERO)
    x13 = extract(x6, x12)
    x14 = first(x13)
    x15 = last(x13)
    x16 = x14(grid)
    x17 = rot180(x16)
    x18 = shape(x17)
    x19 = lbind(apply, first)
    x20 = lbind(ofcolor, x17)
    x21 = chain(size, x19, x20)
    x22 = palette(grid)
    x23 = argmax(x22, x21)
    x24 = partition(x17)
    x25 = matcher(color, x23)
    x26 = compose(flip, x25)
    x27 = sfilter(x24, x26)
    x28 = compose(invert, size)
    x29 = order(x27, x28)
    x30 = apply(normalize, x29)
    x31 = size(x30)
    x32 = interval(ZERO, x31, ONE)
    x33 = apply(toivec, x32)
    x34 = mpapply(shift, x30, x33)
    x35 = canvas(x23, x18)
    x36 = paint(x35, x34)
    x37 = x15(x36)
    return x37


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
