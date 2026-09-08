"""Executable re-arc DSL program for ARC-AGI-2 task 5614dbcf.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FIVE,
    ONE,
    THREE,
    THREE_BY_THREE,
    ZERO,
    apply,
    asindices,
    canvas,
    chain,
    color,
    compose,
    divide,
    downscale,
    first,
    flip,
    fork,
    interval,
    last,
    lbind,
    mapply,
    matcher,
    multiply,
    paint,
    product,
    rbind,
    recolor,
    sfilter,
    shape,
    shift,
    toobject,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "5614dbcf"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = canvas(ZERO, THREE_BY_THREE)
    x1 = asindices(x0)
    x2 = shape(grid)
    x3 = divide(x2, THREE)
    x4 = first(x3)
    x5 = last(x3)
    x6 = interval(ZERO, x4, ONE)
    x7 = interval(ZERO, x5, ONE)
    x8 = product(x6, x7)
    x9 = rbind(multiply, THREE)
    x10 = apply(x9, x8)
    x11 = matcher(first, FIVE)
    x12 = compose(flip, x11)
    x13 = rbind(sfilter, x12)
    x14 = rbind(toobject, grid)
    x15 = lbind(shift, x1)
    x16 = chain(x13, x14, x15)
    x17 = compose(color, x16)
    x18 = lbind(shift, x1)
    x19 = fork(recolor, x17, x18)
    x20 = mapply(x19, x10)
    x21 = paint(grid, x20)
    x22 = downscale(x21, THREE)
    return x22


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
