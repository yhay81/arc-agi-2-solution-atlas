"""Executable re-arc DSL program for ARC-AGI-2 task db3e9e38.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    NEG_ONE,
    NEG_TWO,
    ONE,
    TEN,
    THREE,
    ZERO,
    apply,
    astuple,
    chain,
    cmirror,
    combine,
    compose,
    dmirror,
    double,
    extract,
    fgpartition,
    fill,
    first,
    hmirror,
    identity,
    initset,
    interval,
    invert,
    lbind,
    mapply,
    matcher,
    merge,
    multiply,
    paint,
    rapply,
    rbind,
    shift,
    uppermost,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "db3e9e38"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = astuple(identity, dmirror)
    x1 = astuple(cmirror, hmirror)
    x2 = combine(x0, x1)
    x3 = chain(uppermost, merge, fgpartition)
    x4 = rbind(rapply, grid)
    x5 = chain(first, x4, initset)
    x6 = compose(x3, x5)
    x7 = matcher(x6, ZERO)
    x8 = extract(x2, x7)
    x9 = x8(grid)
    x10 = fgpartition(x9)
    x11 = merge(x10)
    x12 = width(x11)
    x13 = astuple(NEG_ONE, x12)
    x14 = invert(x12)
    x15 = astuple(NEG_ONE, x14)
    x16 = double(x12)
    x17 = astuple(NEG_TWO, x16)
    x18 = double(x12)
    x19 = invert(x18)
    x20 = astuple(NEG_TWO, x19)
    x21 = multiply(THREE, TEN)
    x22 = interval(ZERO, x21, ONE)
    x23 = lbind(multiply, x13)
    x24 = apply(x23, x22)
    x25 = lbind(multiply, x15)
    x26 = apply(x25, x22)
    x27 = lbind(multiply, x17)
    x28 = apply(x27, x22)
    x29 = lbind(multiply, x20)
    x30 = apply(x29, x22)
    x31 = lbind(shift, x11)
    x32 = mapply(x31, x24)
    x33 = lbind(shift, x11)
    x34 = mapply(x33, x26)
    x35 = lbind(shift, x11)
    x36 = mapply(x35, x28)
    x37 = lbind(shift, x11)
    x38 = mapply(x37, x30)
    x39 = combine(x32, x34)
    x40 = fill(x9, EIGHT, x39)
    x41 = combine(x36, x38)
    x42 = paint(x40, x41)
    x43 = x8(x42)
    return x43


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
