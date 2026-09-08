"""Executable re-arc DSL program for ARC-AGI-2 task e21d9049.

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
    branch,
    combine,
    compose,
    divide,
    equality,
    fgpartition,
    first,
    height,
    hline,
    increment,
    interval,
    invert,
    last,
    lbind,
    mapply,
    matcher,
    merge,
    mfilter,
    mostcommon,
    multiply,
    objects,
    paint,
    sfilter,
    shift,
    size,
    toivec,
    tojvec,
    totuple,
    vline,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "e21d9049"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = merge(x0)
    x2 = compose(first, last)
    x3 = totuple(x1)
    x4 = apply(x2, x3)
    x5 = mostcommon(x4)
    x6 = compose(last, last)
    x7 = totuple(x1)
    x8 = apply(x6, x7)
    x9 = mostcommon(x8)
    x10 = compose(first, last)
    x11 = matcher(x10, x5)
    x12 = sfilter(x1, x11)
    x13 = compose(last, last)
    x14 = matcher(x13, x9)
    x15 = sfilter(x1, x14)
    x16 = objects(grid, F, T, T)
    x17 = size(x16)
    x18 = equality(x17, TWO)
    x19 = mfilter(x16, hline)
    x20 = mfilter(x16, vline)
    x21 = branch(x18, x19, x12)
    x22 = branch(x18, x20, x15)
    x23 = width(x21)
    x24 = lbind(multiply, x23)
    x25 = width(grid)
    x26 = divide(x25, x23)
    x27 = increment(x26)
    x28 = interval(ZERO, x27, ONE)
    x29 = apply(x24, x28)
    x30 = apply(invert, x29)
    x31 = combine(x29, x30)
    x32 = apply(tojvec, x31)
    x33 = lbind(shift, x21)
    x34 = mapply(x33, x32)
    x35 = height(x22)
    x36 = lbind(multiply, x35)
    x37 = height(grid)
    x38 = height(x21)
    x39 = divide(x37, x38)
    x40 = increment(x39)
    x41 = interval(ZERO, x40, ONE)
    x42 = apply(x36, x41)
    x43 = apply(invert, x42)
    x44 = combine(x42, x43)
    x45 = apply(toivec, x44)
    x46 = lbind(shift, x22)
    x47 = mapply(x46, x45)
    x48 = combine(x34, x47)
    x49 = paint(grid, x48)
    return x49


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
