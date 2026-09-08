"""Executable re-arc DSL program for ARC-AGI-2 task 3eda0437.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NEG_ONE,
    ONE,
    SIX,
    TWO,
    ZERO,
    apply,
    argmax,
    asindices,
    branch,
    canvas,
    chain,
    compose,
    difference,
    dmirror,
    first,
    fork,
    identity,
    increment,
    interval,
    last,
    lbind,
    mapply,
    matcher,
    maximum,
    multiply,
    occurrences,
    paint,
    positive,
    product,
    rbind,
    recolor,
    sfilter,
    shift,
    size,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "3eda0437"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = matcher(identity, ZERO)
    x1 = rbind(sfilter, x0)
    x2 = compose(size, x1)
    x3 = apply(x2, grid)
    x4 = maximum(x3)
    x5 = dmirror(grid)
    x6 = apply(x2, x5)
    x7 = maximum(x6)
    x8 = increment(x7)
    x9 = interval(TWO, x8, ONE)
    x10 = increment(x4)
    x11 = interval(TWO, x10, ONE)
    x12 = product(x9, x11)
    x13 = fork(multiply, first, last)
    x14 = apply(x13, x12)
    x15 = lbind(sfilter, x12)
    x16 = lbind(matcher, x13)
    x17 = compose(x15, x16)
    x18 = apply(x17, x14)
    x19 = lbind(occurrences, grid)
    x20 = lbind(recolor, ZERO)
    x21 = lbind(canvas, NEG_ONE)
    x22 = compose(asindices, x21)
    x23 = chain(x19, x20, x22)
    x24 = lbind(mapply, x23)
    x25 = chain(positive, size, x24)
    x26 = sfilter(x18, x25)
    x27 = compose(x13, first)
    x28 = rbind(argmax, x27)
    x29 = lbind(recolor, ZERO)
    x30 = lbind(canvas, NEG_ONE)
    x31 = chain(x29, asindices, x30)
    x32 = lbind(lbind, shift)
    x33 = lbind(occurrences, grid)
    x34 = fork(mapply, x32, x33)
    x35 = compose(x34, x31)
    x36 = size(x26)
    x37 = positive(x36)
    x38 = lbind(recolor, SIX)
    x39 = lbind(mapply, x35)
    x40 = chain(x38, x39, x28)
    x41 = fork(difference, identity, identity)
    x42 = branch(x37, x40, x41)
    x43 = x42(x26)
    x44 = paint(grid, x43)
    return x44


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
