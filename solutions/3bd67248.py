"""Executable re-arc DSL program for ARC-AGI-2 task 3bd67248.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    FOUR,
    ONE,
    TWO,
    ZERO,
    apply,
    asindices,
    astuple,
    canvas,
    chain,
    combine,
    compose,
    dedupe,
    extract,
    fill,
    first,
    height,
    identity,
    initset,
    interval,
    last,
    lbind,
    leastcolor,
    mapply,
    matcher,
    maximum,
    ofcolor,
    pair,
    rapply,
    rbind,
    repeat,
    rot90,
    rot180,
    rot270,
    shape,
    shift,
    shoot,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "3bd67248"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = astuple(identity, identity)
    x1 = astuple(rot90, rot270)
    x2 = astuple(x0, x1)
    x3 = astuple(rot180, rot180)
    x4 = astuple(rot270, rot90)
    x5 = astuple(x3, x4)
    x6 = combine(x2, x5)
    x7 = leastcolor(grid)
    x8 = repeat(x7, ONE)
    x9 = rbind(rapply, grid)
    x10 = chain(x9, initset, first)
    x11 = compose(first, x10)
    x12 = chain(dedupe, first, x11)
    x13 = matcher(x12, x8)
    x14 = extract(x6, x13)
    x15 = first(x14)
    x16 = last(x14)
    x17 = x15(grid)
    x18 = ofcolor(x17, x7)
    x19 = height(x18)
    x20 = interval(ZERO, x19, ONE)
    x21 = lbind(astuple, x19)
    x22 = apply(x21, x20)
    x23 = rbind(shoot, DOWN)
    x24 = mapply(x23, x22)
    x25 = fill(x17, FOUR, x24)
    x26 = astuple(x19, x19)
    x27 = canvas(ZERO, x26)
    x28 = asindices(x27)
    x29 = shift(x28, x26)
    x30 = shape(grid)
    x31 = maximum(x30)
    x32 = lbind(shift, x29)
    x33 = interval(ZERO, x31, x19)
    x34 = pair(x33, x33)
    x35 = mapply(x32, x34)
    x36 = fill(x25, TWO, x35)
    x37 = x16(x36)
    return x37


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
