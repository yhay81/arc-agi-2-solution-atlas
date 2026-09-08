"""Executable re-arc DSL program for ARC-AGI-2 task d06dbe63.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    FIVE,
    NEG_TWO,
    ONE,
    ORIGIN,
    TEN,
    TWO,
    TWO_BY_ZERO,
    ZERO,
    ZERO_BY_TWO,
    apply,
    astuple,
    canvas,
    center,
    chain,
    combine,
    compose,
    connect,
    double,
    fill,
    fork,
    identity,
    initset,
    interval,
    lbind,
    leastcolor,
    mapply,
    mostcolor,
    multiply,
    ofcolor,
    paint,
    rbind,
    recolor,
    rot180,
    shape,
    shift,
    subtract,
    toivec,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d06dbe63"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = double(TEN)
    x1 = interval(ZERO, x0, ONE)
    x2 = connect(ORIGIN, DOWN)
    x3 = connect(ORIGIN, ZERO_BY_TWO)
    x4 = combine(x2, x3)
    x5 = astuple(NEG_TWO, TWO)
    x6 = lbind(multiply, x5)
    x7 = toivec(NEG_TWO)
    x8 = apply(x6, x1)
    x9 = rbind(subtract, TWO_BY_ZERO)
    x10 = fork(ofcolor, identity, leastcolor)
    x11 = chain(x9, center, x10)
    x12 = rbind(mapply, x8)
    x13 = lbind(lbind, shift)
    x14 = lbind(shift, x4)
    x15 = compose(x14, x11)
    x16 = chain(x12, x13, x15)
    x17 = lbind(recolor, FIVE)
    x18 = compose(x17, x16)
    x19 = fork(paint, identity, x18)
    x20 = compose(rot180, x19)
    x21 = fork(ofcolor, x20, leastcolor)
    x22 = compose(center, x21)
    x23 = fork(subtract, x22, x11)
    x24 = fork(shift, x16, x23)
    x25 = lbind(recolor, FIVE)
    x26 = rbind(shift, x7)
    x27 = chain(x25, x26, x24)
    x28 = fork(paint, x20, x27)
    x29 = compose(rot180, x28)
    x30 = rbind(ofcolor, FIVE)
    x31 = compose(x30, x29)
    x32 = leastcolor(grid)
    x33 = ofcolor(grid, x32)
    x34 = mostcolor(grid)
    x35 = shape(grid)
    x36 = canvas(x34, x35)
    x37 = lbind(paint, x36)
    x38 = lbind(recolor, x32)
    x39 = chain(x37, x38, initset)
    x40 = compose(x31, x39)
    x41 = mapply(x40, x33)
    x42 = fill(grid, FIVE, x41)
    x43 = fill(x42, x32, x33)
    return x43


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
