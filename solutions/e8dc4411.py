"""Executable re-arc DSL program for ARC-AGI-2 task e8dc4411.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ORIGIN,
    UNITY,
    ZERO,
    apply,
    argmax,
    chain,
    color,
    fgpartition,
    height,
    increment,
    ineighbors,
    intersection,
    interval,
    lbind,
    mapply,
    maximum,
    multiply,
    other,
    paint,
    pair,
    positive,
    rbind,
    recolor,
    sfilter,
    shape,
    shift,
    size,
    toindices,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "e8dc4411"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = argmax(x0, size)
    x2 = other(x0, x1)
    x3 = ineighbors(ORIGIN)
    x4 = height(x1)
    x5 = increment(x4)
    x6 = interval(ZERO, x5, ONE)
    x7 = lbind(intersection, x1)
    x8 = chain(positive, size, x7)
    x9 = lbind(shift, x1)
    x10 = rbind(multiply, UNITY)
    x11 = chain(x8, x9, x10)
    x12 = sfilter(x6, x11)
    x13 = maximum(x12)
    x14 = increment(x13)
    x15 = toindices(x2)
    x16 = lbind(intersection, x15)
    x17 = lbind(shift, x1)
    x18 = rbind(multiply, x14)
    x19 = chain(toindices, x17, x18)
    x20 = chain(size, x16, x19)
    x21 = argmax(x3, x20)
    x22 = shape(grid)
    x23 = maximum(x22)
    x24 = increment(x23)
    x25 = interval(ONE, x24, ONE)
    x26 = lbind(shift, x1)
    x27 = multiply(x14, x21)
    x28 = lbind(multiply, x27)
    x29 = pair(x25, x25)
    x30 = apply(x28, x29)
    x31 = mapply(x26, x30)
    x32 = color(x2)
    x33 = recolor(x32, x31)
    x34 = paint(grid, x33)
    return x34


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
