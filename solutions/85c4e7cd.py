"""Executable re-arc DSL program for ARC-AGI-2 task 85c4e7cd.

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
    asindices,
    box,
    chain,
    color,
    combine,
    compose,
    first,
    halve,
    inbox,
    initset,
    interval,
    invert,
    last,
    lbind,
    minimum,
    mpapply,
    order,
    paint,
    pair,
    power,
    rapply,
    rbind,
    recolor,
    repeat,
    shape,
    toobject,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "85c4e7cd"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asindices(grid)
    x1 = box(x0)
    x2 = shape(grid)
    x3 = minimum(x2)
    x4 = halve(x3)
    x5 = interval(ONE, x4, ONE)
    x6 = lbind(power, inbox)
    x7 = rbind(rapply, x1)
    x8 = compose(initset, x6)
    x9 = chain(first, x7, x8)
    x10 = apply(x9, x5)
    x11 = repeat(x1, ONE)
    x12 = combine(x11, x10)
    x13 = rbind(toobject, grid)
    x14 = compose(color, x13)
    x15 = apply(x14, x12)
    x16 = interval(ZERO, x4, ONE)
    x17 = pair(x16, x15)
    x18 = compose(invert, first)
    x19 = order(x17, x18)
    x20 = apply(last, x19)
    x21 = mpapply(recolor, x20, x12)
    x22 = paint(grid, x21)
    return x22


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
